# coding: utf-8

"""
    Recomax REST API

    Recomax REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@recomax.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class RecomResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'count': 'int',
        'recom_virtual_category_list': 'list[RecomVirtualCategory]',
        'search_result_item_list': 'list[RecomResultItem]'
    }

    attribute_map = {
        'count': 'count',
        'recom_virtual_category_list': 'recomVirtualCategoryList',
        'search_result_item_list': 'searchResultItemList'
    }

    def __init__(self, count=None, recom_virtual_category_list=None, search_result_item_list=None, _configuration=None):  # noqa: E501
        """RecomResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._recom_virtual_category_list = None
        self._search_result_item_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if recom_virtual_category_list is not None:
            self.recom_virtual_category_list = recom_virtual_category_list
        if search_result_item_list is not None:
            self.search_result_item_list = search_result_item_list

    @property
    def count(self):
        """Gets the count of this RecomResult.  # noqa: E501


        :return: The count of this RecomResult.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RecomResult.


        :param count: The count of this RecomResult.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def recom_virtual_category_list(self):
        """Gets the recom_virtual_category_list of this RecomResult.  # noqa: E501


        :return: The recom_virtual_category_list of this RecomResult.  # noqa: E501
        :rtype: list[RecomVirtualCategory]
        """
        return self._recom_virtual_category_list

    @recom_virtual_category_list.setter
    def recom_virtual_category_list(self, recom_virtual_category_list):
        """Sets the recom_virtual_category_list of this RecomResult.


        :param recom_virtual_category_list: The recom_virtual_category_list of this RecomResult.  # noqa: E501
        :type: list[RecomVirtualCategory]
        """

        self._recom_virtual_category_list = recom_virtual_category_list

    @property
    def search_result_item_list(self):
        """Gets the search_result_item_list of this RecomResult.  # noqa: E501


        :return: The search_result_item_list of this RecomResult.  # noqa: E501
        :rtype: list[RecomResultItem]
        """
        return self._search_result_item_list

    @search_result_item_list.setter
    def search_result_item_list(self, search_result_item_list):
        """Sets the search_result_item_list of this RecomResult.


        :param search_result_item_list: The search_result_item_list of this RecomResult.  # noqa: E501
        :type: list[RecomResultItem]
        """

        self._search_result_item_list = search_result_item_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RecomResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecomResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecomResult):
            return True

        return self.to_dict() != other.to_dict()
