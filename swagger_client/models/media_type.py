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


class MediaType(object):
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
        'parameters': 'dict(str, str)',
        'subtype': 'str',
        'type': 'str',
        'wildcard_subtype': 'bool',
        'wildcard_type': 'bool'
    }

    attribute_map = {
        'parameters': 'parameters',
        'subtype': 'subtype',
        'type': 'type',
        'wildcard_subtype': 'wildcardSubtype',
        'wildcard_type': 'wildcardType'
    }

    def __init__(self, parameters=None, subtype=None, type=None, wildcard_subtype=None, wildcard_type=None, _configuration=None):  # noqa: E501
        """MediaType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parameters = None
        self._subtype = None
        self._type = None
        self._wildcard_subtype = None
        self._wildcard_type = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if subtype is not None:
            self.subtype = subtype
        if type is not None:
            self.type = type
        if wildcard_subtype is not None:
            self.wildcard_subtype = wildcard_subtype
        if wildcard_type is not None:
            self.wildcard_type = wildcard_type

    @property
    def parameters(self):
        """Gets the parameters of this MediaType.  # noqa: E501


        :return: The parameters of this MediaType.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MediaType.


        :param parameters: The parameters of this MediaType.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def subtype(self):
        """Gets the subtype of this MediaType.  # noqa: E501


        :return: The subtype of this MediaType.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this MediaType.


        :param subtype: The subtype of this MediaType.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

    @property
    def type(self):
        """Gets the type of this MediaType.  # noqa: E501


        :return: The type of this MediaType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MediaType.


        :param type: The type of this MediaType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def wildcard_subtype(self):
        """Gets the wildcard_subtype of this MediaType.  # noqa: E501


        :return: The wildcard_subtype of this MediaType.  # noqa: E501
        :rtype: bool
        """
        return self._wildcard_subtype

    @wildcard_subtype.setter
    def wildcard_subtype(self, wildcard_subtype):
        """Sets the wildcard_subtype of this MediaType.


        :param wildcard_subtype: The wildcard_subtype of this MediaType.  # noqa: E501
        :type: bool
        """

        self._wildcard_subtype = wildcard_subtype

    @property
    def wildcard_type(self):
        """Gets the wildcard_type of this MediaType.  # noqa: E501


        :return: The wildcard_type of this MediaType.  # noqa: E501
        :rtype: bool
        """
        return self._wildcard_type

    @wildcard_type.setter
    def wildcard_type(self, wildcard_type):
        """Sets the wildcard_type of this MediaType.


        :param wildcard_type: The wildcard_type of this MediaType.  # noqa: E501
        :type: bool
        """

        self._wildcard_type = wildcard_type

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
        if issubclass(MediaType, dict):
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
        if not isinstance(other, MediaType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaType):
            return True

        return self.to_dict() != other.to_dict()