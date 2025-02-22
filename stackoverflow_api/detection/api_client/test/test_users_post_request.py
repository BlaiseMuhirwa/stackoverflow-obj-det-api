# coding: utf-8

"""
    Stack Overflow Object Detection API

    API that fetches the top 10 users from the Stack Overflow Users API, reads their profile images, and uses an open-source object detection model to detect specified objects in those images.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.users_post_request import UsersPostRequest

class TestUsersPostRequest(unittest.TestCase):
    """UsersPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersPostRequest:
        """Test UsersPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersPostRequest`
        """
        model = UsersPostRequest()
        if include_optional:
            return UsersPostRequest(
                query = 'face'
            )
        else:
            return UsersPostRequest(
        )
        """

    def testUsersPostRequest(self):
        """Test UsersPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
