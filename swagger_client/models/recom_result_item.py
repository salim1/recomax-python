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


class RecomResultItem(object):
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
        'item': 'Item',
        'rank': 'float',
        'recommendation_id': 'str'
    }

    attribute_map = {
        'item': 'item',
        'rank': 'rank',
        'recommendation_id': 'recommendationId'
    }

    def __init__(self, item=None, rank=None, recommendation_id=None, _configuration=None):  # noqa: E501
        """RecomResultItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._item = None
        self._rank = None
        self._recommendation_id = None
        self.discriminator = None

        self.item = item
        self.rank = rank
        self.recommendation_id = recommendation_id

    @property
    def item(self):
        """Gets the item of this RecomResultItem.  # noqa: E501

        item  # noqa: E501

        :return: The item of this RecomResultItem.  # noqa: E501
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this RecomResultItem.

        item  # noqa: E501

        :param item: The item of this RecomResultItem.  # noqa: E501
        :type: Item
        """
        if self._configuration.client_side_validation and item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501

        self._item = item

    @property
    def rank(self):
        """Gets the rank of this RecomResultItem.  # noqa: E501

        rank  # noqa: E501

        :return: The rank of this RecomResultItem.  # noqa: E501
        :rtype: float
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this RecomResultItem.

        rank  # noqa: E501

        :param rank: The rank of this RecomResultItem.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and rank is None:
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    @property
    def recommendation_id(self):
        """Gets the recommendation_id of this RecomResultItem.  # noqa: E501

        recommendationId  # noqa: E501

        :return: The recommendation_id of this RecomResultItem.  # noqa: E501
        :rtype: str
        """
        return self._recommendation_id

    @recommendation_id.setter
    def recommendation_id(self, recommendation_id):
        """Sets the recommendation_id of this RecomResultItem.

        recommendationId  # noqa: E501

        :param recommendation_id: The recommendation_id of this RecomResultItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and recommendation_id is None:
            raise ValueError("Invalid value for `recommendation_id`, must not be `None`")  # noqa: E501

        self._recommendation_id = recommendation_id

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
        if issubclass(RecomResultItem, dict):
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
        if not isinstance(other, RecomResultItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecomResultItem):
            return True

        return self.to_dict() != other.to_dict()