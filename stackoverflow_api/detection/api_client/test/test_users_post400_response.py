# coding: utf-8

"""
    Stack Overflow Object Detection API

    API that fetches the top 10 users from the Stack Overflow Users API, reads their profile images, and uses an open-source object detection model to detect specified objects in those images.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.users_post400_response import UsersPost400Response

class TestUsersPost400Response(unittest.TestCase):
    """UsersPost400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersPost400Response:
        """Test UsersPost400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersPost400Response`
        """
        model = UsersPost400Response()
        if include_optional:
            return UsersPost400Response(
                error = 'Query parameter 'query' is required'
            )
        else:
            return UsersPost400Response(
        )
        """

    def testUsersPost400Response(self):
        """Test UsersPost400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
