# coding: utf-8

"""
    Stack Overflow Object Detection API

    API that fetches the top 10 users from the Stack Overflow Users API, reads their profile images, and uses an open-source object detection model to detect specified objects in those images.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.users_post200_response_inner import UsersPost200ResponseInner

class TestUsersPost200ResponseInner(unittest.TestCase):
    """UsersPost200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersPost200ResponseInner:
        """Test UsersPost200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersPost200ResponseInner`
        """
        model = UsersPost200ResponseInner()
        if include_optional:
            return UsersPost200ResponseInner(
                user_id = 1,
                display_name = 'User Name',
                profile_image = 'http://example.com/image.jpg',
                object_detected = True,
                bounding_boxes = [
                    openapi_client.models._users_post_200_response_inner_bounding_boxes_inner._users_post_200_response_inner_bounding_boxes_inner(
                        x = 100, 
                        y = 150, 
                        width = 50, 
                        height = 50, )
                    ],
                detection_time_ms = 123.45
            )
        else:
            return UsersPost200ResponseInner(
        )
        """

    def testUsersPost200ResponseInner(self):
        """Test UsersPost200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
