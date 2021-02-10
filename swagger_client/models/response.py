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


class Response(object):
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
        'allowed_methods': 'list[str]',
        'cookies': 'dict(str, NewCookie)',
        'date': 'datetime',
        'entity': 'object',
        'entity_tag': 'EntityTag',
        'headers': 'dict(str, list[object])',
        'language': 'Locale',
        'last_modified': 'datetime',
        'length': 'int',
        'links': 'list[Link]',
        'location': 'URI',
        'media_type': 'MediaType',
        'metadata': 'dict(str, list[object])',
        'status': 'int',
        'status_info': 'StatusType',
        'string_headers': 'dict(str, list[str])'
    }

    attribute_map = {
        'allowed_methods': 'allowedMethods',
        'cookies': 'cookies',
        'date': 'date',
        'entity': 'entity',
        'entity_tag': 'entityTag',
        'headers': 'headers',
        'language': 'language',
        'last_modified': 'lastModified',
        'length': 'length',
        'links': 'links',
        'location': 'location',
        'media_type': 'mediaType',
        'metadata': 'metadata',
        'status': 'status',
        'status_info': 'statusInfo',
        'string_headers': 'stringHeaders'
    }

    def __init__(self, allowed_methods=None, cookies=None, date=None, entity=None, entity_tag=None, headers=None, language=None, last_modified=None, length=None, links=None, location=None, media_type=None, metadata=None, status=None, status_info=None, string_headers=None, _configuration=None):  # noqa: E501
        """Response - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allowed_methods = None
        self._cookies = None
        self._date = None
        self._entity = None
        self._entity_tag = None
        self._headers = None
        self._language = None
        self._last_modified = None
        self._length = None
        self._links = None
        self._location = None
        self._media_type = None
        self._metadata = None
        self._status = None
        self._status_info = None
        self._string_headers = None
        self.discriminator = None

        if allowed_methods is not None:
            self.allowed_methods = allowed_methods
        if cookies is not None:
            self.cookies = cookies
        if date is not None:
            self.date = date
        if entity is not None:
            self.entity = entity
        if entity_tag is not None:
            self.entity_tag = entity_tag
        if headers is not None:
            self.headers = headers
        if language is not None:
            self.language = language
        if last_modified is not None:
            self.last_modified = last_modified
        if length is not None:
            self.length = length
        if links is not None:
            self.links = links
        if location is not None:
            self.location = location
        if media_type is not None:
            self.media_type = media_type
        if metadata is not None:
            self.metadata = metadata
        if status is not None:
            self.status = status
        if status_info is not None:
            self.status_info = status_info
        if string_headers is not None:
            self.string_headers = string_headers

    @property
    def allowed_methods(self):
        """Gets the allowed_methods of this Response.  # noqa: E501


        :return: The allowed_methods of this Response.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_methods

    @allowed_methods.setter
    def allowed_methods(self, allowed_methods):
        """Sets the allowed_methods of this Response.


        :param allowed_methods: The allowed_methods of this Response.  # noqa: E501
        :type: list[str]
        """

        self._allowed_methods = allowed_methods

    @property
    def cookies(self):
        """Gets the cookies of this Response.  # noqa: E501


        :return: The cookies of this Response.  # noqa: E501
        :rtype: dict(str, NewCookie)
        """
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        """Sets the cookies of this Response.


        :param cookies: The cookies of this Response.  # noqa: E501
        :type: dict(str, NewCookie)
        """

        self._cookies = cookies

    @property
    def date(self):
        """Gets the date of this Response.  # noqa: E501


        :return: The date of this Response.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Response.


        :param date: The date of this Response.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def entity(self):
        """Gets the entity of this Response.  # noqa: E501


        :return: The entity of this Response.  # noqa: E501
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Response.


        :param entity: The entity of this Response.  # noqa: E501
        :type: object
        """

        self._entity = entity

    @property
    def entity_tag(self):
        """Gets the entity_tag of this Response.  # noqa: E501


        :return: The entity_tag of this Response.  # noqa: E501
        :rtype: EntityTag
        """
        return self._entity_tag

    @entity_tag.setter
    def entity_tag(self, entity_tag):
        """Sets the entity_tag of this Response.


        :param entity_tag: The entity_tag of this Response.  # noqa: E501
        :type: EntityTag
        """

        self._entity_tag = entity_tag

    @property
    def headers(self):
        """Gets the headers of this Response.  # noqa: E501


        :return: The headers of this Response.  # noqa: E501
        :rtype: dict(str, list[object])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Response.


        :param headers: The headers of this Response.  # noqa: E501
        :type: dict(str, list[object])
        """

        self._headers = headers

    @property
    def language(self):
        """Gets the language of this Response.  # noqa: E501


        :return: The language of this Response.  # noqa: E501
        :rtype: Locale
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Response.


        :param language: The language of this Response.  # noqa: E501
        :type: Locale
        """

        self._language = language

    @property
    def last_modified(self):
        """Gets the last_modified of this Response.  # noqa: E501


        :return: The last_modified of this Response.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Response.


        :param last_modified: The last_modified of this Response.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def length(self):
        """Gets the length of this Response.  # noqa: E501


        :return: The length of this Response.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Response.


        :param length: The length of this Response.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def links(self):
        """Gets the links of this Response.  # noqa: E501


        :return: The links of this Response.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Response.


        :param links: The links of this Response.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def location(self):
        """Gets the location of this Response.  # noqa: E501


        :return: The location of this Response.  # noqa: E501
        :rtype: URI
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Response.


        :param location: The location of this Response.  # noqa: E501
        :type: URI
        """

        self._location = location

    @property
    def media_type(self):
        """Gets the media_type of this Response.  # noqa: E501


        :return: The media_type of this Response.  # noqa: E501
        :rtype: MediaType
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Response.


        :param media_type: The media_type of this Response.  # noqa: E501
        :type: MediaType
        """

        self._media_type = media_type

    @property
    def metadata(self):
        """Gets the metadata of this Response.  # noqa: E501


        :return: The metadata of this Response.  # noqa: E501
        :rtype: dict(str, list[object])
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Response.


        :param metadata: The metadata of this Response.  # noqa: E501
        :type: dict(str, list[object])
        """

        self._metadata = metadata

    @property
    def status(self):
        """Gets the status of this Response.  # noqa: E501


        :return: The status of this Response.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Response.


        :param status: The status of this Response.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def status_info(self):
        """Gets the status_info of this Response.  # noqa: E501


        :return: The status_info of this Response.  # noqa: E501
        :rtype: StatusType
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """Sets the status_info of this Response.


        :param status_info: The status_info of this Response.  # noqa: E501
        :type: StatusType
        """

        self._status_info = status_info

    @property
    def string_headers(self):
        """Gets the string_headers of this Response.  # noqa: E501


        :return: The string_headers of this Response.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._string_headers

    @string_headers.setter
    def string_headers(self, string_headers):
        """Sets the string_headers of this Response.


        :param string_headers: The string_headers of this Response.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._string_headers = string_headers

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
        if issubclass(Response, dict):
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
        if not isinstance(other, Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Response):
            return True

        return self.to_dict() != other.to_dict()