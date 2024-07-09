from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import requests_mock
import json


class StackOverflowObjectDetectionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.stack_overflow_api_url = "https://api.stackexchange.com/2.2/users?order=desc&sort=reputation&site=stackoverflow"

    @requests_mock.Mocker()
    def test_object_detection(self, mocker):
        # Mock Stack Overflow API response
        mock_stack_overflow_response = {
            "items": [
                {
                    "badge_counts": {"bronze": 9277, "silver": 9232, "gold": 881},
                    "account_id": 11683,
                    "is_employee": False,
                    "last_modified_date": 1720126213,
                    "last_access_date": 1720475661,
                    "reputation_change_year": 30913,
                    "reputation_change_quarter": 1333,
                    "reputation_change_month": 1333,
                    "reputation_change_week": 300,
                    "reputation_change_day": 0,
                    "reputation": 1472601,
                    "creation_date": 1222430705,
                    "user_type": "registered",
                    "user_id": 22656,
                    "accept_rate": 86,
                    "location": "Reading, United Kingdom",
                    "website_url": "http://csharpindepth.com",
                    "link": "https://stackoverflow.com/users/22656/jon-skeet",
                    "profile_image": "https://www.gravatar.com/avatar/6d8ebb117e8d83d74ea95fbdd0f87e13?s=256&d=identicon&r=PG",
                    "display_name": "Jon Skeet",
                },
                {
                    "badge_counts": {"bronze": 5475, "silver": 4625, "gold": 547},
                    "account_id": 4243,
                    "is_employee": False,
                    "last_modified_date": 1720444201,
                    "last_access_date": 1720472633,
                    "reputation_change_year": -30239,
                    "reputation_change_quarter": 1223,
                    "reputation_change_month": 1223,
                    "reputation_change_week": 175,
                    "reputation_change_day": 0,
                    "reputation": 1287098,
                    "creation_date": 1221344553,
                    "user_type": "registered",
                    "user_id": 6309,
                    "accept_rate": 100,
                    "location": "France",
                    "website_url": "https://devstory.fyi/vonc",
                    "link": "https://stackoverflow.com/users/6309/vonc",
                    "profile_image": "https://i.sstatic.net/I4fiW.jpg?s=256",
                    "display_name": "VonC",
                },
            ]
        }

        # Mock the API request to Stack Overflow
        mocker.get(self.stack_overflow_api_url, json=mock_stack_overflow_response)

        url = "/api/v1/users"
        data = {"query": "face"}
        response = self.client.post(
            url, data=json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()

        # Check that the response data has the expected structure and content
        self.assertIsInstance(response_data, list)
        self.assertGreaterEqual(len(response_data), 1)
        for user in response_data:
            self.assertIn("user_id", user)
            self.assertIn("display_name", user)
            self.assertIn("profile_image", user)
            self.assertIn("object_detected", user)
            self.assertIn("bounding_boxes", user)
            self.assertIn("detection_time_ms", user)

        print(response.json())
