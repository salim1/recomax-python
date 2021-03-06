# coding: utf-8

"""
    Recomax REST API

    Recomax REST API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@recomax.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_user_using_post(self, api_key, attribute_list, **kwargs):  # noqa: E501
        """Add User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_using_post(api_key, attribute_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param list[Attribute] attribute_list: attributeList (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_user_using_post_with_http_info(api_key, attribute_list, **kwargs)  # noqa: E501
        else:
            (data) = self.add_user_using_post_with_http_info(api_key, attribute_list, **kwargs)  # noqa: E501
            return data

    def add_user_using_post_with_http_info(self, api_key, attribute_list, **kwargs):  # noqa: E501
        """Add User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_using_post_with_http_info(api_key, attribute_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param list[Attribute] attribute_list: attributeList (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'attribute_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `add_user_using_post`")  # noqa: E501
        # verify the required parameter 'attribute_list' is set
        if self.api_client.client_side_validation and ('attribute_list' not in params or
                                                       params['attribute_list'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `attribute_list` when calling `add_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_key' in params:
            path_params['apiKey'] = params['api_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'attribute_list' in params:
            body_params = params['attribute_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{apiKey}/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_user_using_put(self, api_key, id, attribute_list, **kwargs):  # noqa: E501
        """Add User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_using_put(api_key, id, attribute_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :param list[Attribute] attribute_list: attributeList (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_user_using_put_with_http_info(api_key, id, attribute_list, **kwargs)  # noqa: E501
        else:
            (data) = self.add_user_using_put_with_http_info(api_key, id, attribute_list, **kwargs)  # noqa: E501
            return data

    def add_user_using_put_with_http_info(self, api_key, id, attribute_list, **kwargs):  # noqa: E501
        """Add User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_user_using_put_with_http_info(api_key, id, attribute_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :param list[Attribute] attribute_list: attributeList (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'id', 'attribute_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `add_user_using_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `add_user_using_put`")  # noqa: E501
        # verify the required parameter 'attribute_list' is set
        if self.api_client.client_side_validation and ('attribute_list' not in params or
                                                       params['attribute_list'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `attribute_list` when calling `add_user_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_key' in params:
            path_params['apiKey'] = params['api_key']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'attribute_list' in params:
            body_params = params['attribute_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{apiKey}/users/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user_using_delete(self, api_key, id, **kwargs):  # noqa: E501
        """Delete User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_using_delete(api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_using_delete_with_http_info(api_key, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_using_delete_with_http_info(api_key, id, **kwargs)  # noqa: E501
            return data

    def delete_user_using_delete_with_http_info(self, api_key, id, **kwargs):  # noqa: E501
        """Delete User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_using_delete_with_http_info(api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `delete_user_using_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_user_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_key' in params:
            path_params['apiKey'] = params['api_key']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{apiKey}/users/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_segments_using_get(self, api_key, id, **kwargs):  # noqa: E501
        """Get User List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segments_using_get(api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_segments_using_get_with_http_info(api_key, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_segments_using_get_with_http_info(api_key, id, **kwargs)  # noqa: E501
            return data

    def get_segments_using_get_with_http_info(self, api_key, id, **kwargs):  # noqa: E501
        """Get User List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segments_using_get_with_http_info(api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_segments_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `get_segments_using_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_segments_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_key' in params:
            path_params['apiKey'] = params['api_key']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{apiKey}/uses/{id}/segments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_using_get(self, api_key, id, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_using_get(api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_using_get_with_http_info(api_key, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_using_get_with_http_info(api_key, id, **kwargs)  # noqa: E501
            return data

    def get_user_using_get_with_http_info(self, api_key, id, **kwargs):  # noqa: E501
        """Get User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_using_get_with_http_info(api_key, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `get_user_using_get`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_user_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_key' in params:
            path_params['apiKey'] = params['api_key']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{apiKey}/users/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_users_using_get(self, api_key, **kwargs):  # noqa: E501
        """List Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_using_get(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param int offset: offsel of the items list
        :param int limit: limit of the items list
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_users_using_get_with_http_info(api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.list_users_using_get_with_http_info(api_key, **kwargs)  # noqa: E501
            return data

    def list_users_using_get_with_http_info(self, api_key, **kwargs):  # noqa: E501
        """List Users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_using_get_with_http_info(api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param int offset: offsel of the items list
        :param int limit: limit of the items list
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_users_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `list_users_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_key' in params:
            path_params['apiKey'] = params['api_key']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{apiKey}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[User]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user_using_post(self, api_key, id, attribute_list, **kwargs):  # noqa: E501
        """User item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_using_post(api_key, id, attribute_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :param list[Attribute] attribute_list: attributeList (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_using_post_with_http_info(api_key, id, attribute_list, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_using_post_with_http_info(api_key, id, attribute_list, **kwargs)  # noqa: E501
            return data

    def update_user_using_post_with_http_info(self, api_key, id, attribute_list, **kwargs):  # noqa: E501
        """User item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_using_post_with_http_info(api_key, id, attribute_list, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_key: apiKey (required)
        :param str id: id (required)
        :param list[Attribute] attribute_list: attributeList (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'id', 'attribute_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if self.api_client.client_side_validation and ('api_key' not in params or
                                                       params['api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `api_key` when calling `update_user_using_post`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `update_user_using_post`")  # noqa: E501
        # verify the required parameter 'attribute_list' is set
        if self.api_client.client_side_validation and ('attribute_list' not in params or
                                                       params['attribute_list'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `attribute_list` when calling `update_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'api_key' in params:
            path_params['apiKey'] = params['api_key']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'attribute_list' in params:
            body_params = params['attribute_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{apiKey}/users/{id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
