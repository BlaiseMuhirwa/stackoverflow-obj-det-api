# coding: utf-8

# flake8: noqa

"""
    Stack Overflow Object Detection API

    API that fetches the top 10 users from the Stack Overflow Users API, reads their profile images, and uses an open-source object detection model to detect specified objects in those images.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.default_api import DefaultApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.users_post200_response_inner import UsersPost200ResponseInner
from openapi_client.models.users_post200_response_inner_bounding_boxes_inner import UsersPost200ResponseInnerBoundingBoxesInner
from openapi_client.models.users_post400_response import UsersPost400Response
from openapi_client.models.users_post422_response import UsersPost422Response
from openapi_client.models.users_post500_response import UsersPost500Response
from openapi_client.models.users_post_request import UsersPostRequest
