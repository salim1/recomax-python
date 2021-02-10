# coding: utf-8

# flake8: noqa

"""
    Recomax REST API

    Recomax REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@recomax.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client/apis.event_api import EventApi
from swagger_client/apis.item_api import ItemApi
from swagger_client/apis.recommendation_api import RecommendationApi
from swagger_client/apis.user_api import UserApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client/models.attribute import Attribute
from swagger_client/models.character import Character
from swagger_client/models.entity_tag import EntityTag
from swagger_client/models.item import Item
from swagger_client/models.link import Link
from swagger_client/models.locale import Locale
from swagger_client/models.media_type import MediaType
from swagger_client/models.new_cookie import NewCookie
from swagger_client/models.recom_result import RecomResult
from swagger_client/models.recom_result_item import RecomResultItem
from swagger_client/models.recom_virtual_category import RecomVirtualCategory
from swagger_client/models.response import Response
from swagger_client/models.response_entity import ResponseEntity
from swagger_client/models.status_type import StatusType
from swagger_client/models.uri import URI
from swagger_client/models.uri_builder import UriBuilder
from swagger_client/models.user import User
