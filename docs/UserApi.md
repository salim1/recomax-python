# swagger_client.UserApi

All URIs are relative to *https://convertein.com:8083/convertein/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_using_post**](UserApi.md#add_user_using_post) | **POST** /{apiKey}/users | Add User
[**add_user_using_put**](UserApi.md#add_user_using_put) | **PUT** /{apiKey}/users/{id} | Add User
[**delete_user_using_delete**](UserApi.md#delete_user_using_delete) | **DELETE** /{apiKey}/users/{id} | Delete User
[**get_segments_using_get**](UserApi.md#get_segments_using_get) | **GET** /{apiKey}/uses/{id}/segments | Get User List
[**get_user_using_get**](UserApi.md#get_user_using_get) | **GET** /{apiKey}/users/{id} | Get User
[**list_users_using_get**](UserApi.md#list_users_using_get) | **GET** /{apiKey}/users | List Users
[**update_user_using_post**](UserApi.md#update_user_using_post) | **POST** /{apiKey}/users/{id} | User item


# **add_user_using_post**
> Response add_user_using_post(api_key, attribute_list)

Add User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | apiKey
attribute_list = [swagger_client.Attribute()] # list[Attribute] | attributeList

try:
    # Add User
    api_response = api_instance.add_user_using_post(api_key, attribute_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **attribute_list** | [**list[Attribute]**](Attribute.md)| attributeList | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_using_put**
> User add_user_using_put(api_key, id, attribute_list)

Add User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id
attribute_list = [swagger_client.Attribute()] # list[Attribute] | attributeList

try:
    # Add User
    api_response = api_instance.add_user_using_put(api_key, id, attribute_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 
 **attribute_list** | [**list[Attribute]**](Attribute.md)| attributeList | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_using_delete**
> User delete_user_using_delete(api_key, id)

Delete User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id

try:
    # Delete User
    api_response = api_instance.delete_user_using_delete(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segments_using_get**
> list[str] get_segments_using_get(api_key, id)

Get User List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id

try:
    # Get User List
    api_response = api_instance.get_segments_using_get(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_segments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> User get_user_using_get(api_key, id)

Get User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id

try:
    # Get User
    api_response = api_instance.get_user_using_get(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_using_get**
> list[User] list_users_using_get(api_key, offset=offset, limit=limit)

List Users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | apiKey
offset = 56 # int | offsel of the items list (optional)
limit = 56 # int | limit of the items list (optional)

try:
    # List Users
    api_response = api_instance.list_users_using_get(api_key, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **offset** | **int**| offsel of the items list | [optional] 
 **limit** | **int**| limit of the items list | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_using_post**
> Response update_user_using_post(api_key, id, attribute_list)

User item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id
attribute_list = [swagger_client.Attribute()] # list[Attribute] | attributeList

try:
    # User item
    api_response = api_instance.update_user_using_post(api_key, id, attribute_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 
 **attribute_list** | [**list[Attribute]**](Attribute.md)| attributeList | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

