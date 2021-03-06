# coding: utf-8

"""
    Recomax REST API

    Recomax REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@recomax.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from .item_api import ItemApi  # noqa: E501
from swagger_client.rest import ApiException


class TestItemApi(unittest.TestCase):
    """ItemApi unit test stubs"""

    def setUp(self):
        self.api = .item_api.ItemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_at_using_put(self):
        """Test case for add_item_at_using_put

        Add item  # noqa: E501
        """
        pass

    def test_add_item_using_post(self):
        """Test case for add_item_using_post

        Add item  # noqa: E501
        """
        pass

    def test_delete_item_using_delete(self):
        """Test case for delete_item_using_delete

        Delete item  # noqa: E501
        """
        pass

    def test_gettem_using_get(self):
        """Test case for gettem_using_get

        Get item  # noqa: E501
        """
        pass

    def test_listtem_using_get(self):
        """Test case for listtem_using_get

        List items  # noqa: E501
        """
        pass

    def test_update_item_using_post(self):
        """Test case for update_item_using_post

        Update item  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
