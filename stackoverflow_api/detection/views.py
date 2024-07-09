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


class StackOverflowObjDetectionView(APIView):
    def post(self, request):
        query = request.data.get("query", None)
        if not query:
            return Response(
                {"error": "Query parameter 'query' is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Initialize the generated client
        client = ApiClient()
        api_instance = DefaultApi(client)
        users_post_request = UsersPostRequest(query=query)

        try:
            # Fetch top 10 Stack Overflow users
            users = api_instance.users_post(users_post_request)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Load object detection model (e.g., pre-trained model from torchvision)
        model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
        model.eval()

        transform = transforms.Compose([transforms.ToTensor()])

        results = []
        for user in users[:10]:
            profile_image_url = user.profile_image
            if not profile_image_url:
                continue

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
                for i, label in enumerate(predictions["labels"]):
                    if (
                        label == query
                    ):  # Simplified; in practice, you'd map query to COCO labels
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
                        "user_id": user.user_id,
                        "display_name": user.display_name,
                        "profile_image": profile_image_url,
                        "object_detected": detected,
                        "bounding_boxes": bounding_boxes,
                        "detection_time_ms": detection_time * 1000,
                    }
                )

        return Response(
            UserSerializer(results, many=True).data, status=status.HTTP_200_OK
        )
