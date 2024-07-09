from django.shortcuts import render
import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from torchvision import models, transforms
from PIL import Image
import torch

# Import the generated api client
from openapi_client.api.default_api import DefaultApi
from openapi_client.api_client import ApiClient
from openapi_client.models.users_post_request import UsersPostRequest

import logging


logger = logging.getLogger(__name__)

# Hard-code the Stack Overflow API URL
# TODO: This is not ideal. Should I have enough time, I should refactor this to use the generated API client
STACK_OVERFLOW_URL = "https://api.stackexchange.com/2.2/users?order=desc&sort=reputation&site=stackoverflow"


# Object detection confidence threshold
# TODO: It would be nice to refactor this so that it's configurable. For instance, we can
# have this be part of the request itself.
DETECTION_CONFIDENCE_THRESHOLD = 0.5


class StackOverflowObjDetectionView(APIView):

    def post(self, request):
        query = request.data.get("query", None)
        if not query:
            return Response(
                {"error": "Query parameter 'query' is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        logger.info(f"Received query: {query}")

        try:
            # Fetch top 10 Stack Overflow users
            response = requests.get(STACK_OVERFLOW_URL)
            response.raise_for_status()
            users = response.json().get("items", [])[:10]
            logger.debug(f"Fetched users: {users}")
        except requests.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Load a pre-trained Faster R-CNN model for object detection
        # https://pytorch.org/vision/main/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html#torchvision.models.detection.FasterRCNN_ResNet50_FPN_Weights
        weights = models.detection.FasterRCNN_ResNet50_FPN_Weights.COCO_V1
        model = models.detection.fasterrcnn_resnet50_fpn(weights=weights)
        model.eval()

        transform = transforms.Compose([transforms.ToTensor()])

        results = []
        for user in users:
            profile_image_url = user.get("profile_image")
            if not profile_image_url:
                continue

            logger.debug(f"Processing image for user: {user.get('display_name')}")

            # Load and process image
            image_response = requests.get(profile_image_url, stream=True)
            if image_response.status_code == 200:
                image = Image.open(image_response.raw).convert("RGB")
                image_tensor = transform(image)
                image_tensor = image_tensor.unsqueeze(0)

                # Perform object detection
                start_time = time.time()
                with torch.no_grad():
                    predictions = model(image_tensor)[0]
                detection_time = time.time() - start_time

                # Process predictions to find the specified object
                detected = False
                bounding_boxes = []
                for i, (label, score) in enumerate(
                    zip(predictions["labels"], predictions["scores"])
                ):  
                    # TODO: Don't hard-code the label. This should be configurable.
                    if label == 1 and score > DETECTION_CONFIDENCE_THRESHOLD:
                        detected = True
                        bbox = predictions["boxes"][i].tolist()
                        bounding_boxes.append(
                            {
                                "x": bbox[0],
                                "y": bbox[1],
                                "width": bbox[2] - bbox[0],
                                "height": bbox[3] - bbox[1],
                            }
                        )

                results.append(
                    {
                        "user_id": user.get("user_id"),
                        "display_name": user.get("display_name"),
                        "profile_image": profile_image_url,
                        "object_detected": detected,
                        "bounding_boxes": bounding_boxes,
                        "detection_time_ms": detection_time * 1000,
                    }
                )

        logger.info(f"Detection results: {results}")
        return Response(
            UserSerializer(results, many=True).data, status=status.HTTP_200_OK
        )
