# swagger_client.ItemApi

All URIs are relative to *https://convertein.com:8083/convertein/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_at_using_put**](ItemApi.md#add_item_at_using_put) | **PUT** /{apiKey}/items/{id} | Add item
[**add_item_using_post**](ItemApi.md#add_item_using_post) | **POST** /{apiKey}/items | Add item
[**delete_item_using_delete**](ItemApi.md#delete_item_using_delete) | **DELETE** /{apiKey}/items/{id} | Delete item
[**gettem_using_get**](ItemApi.md#gettem_using_get) | **GET** /{apiKey}/items/{id} | Get item
[**listtem_using_get**](ItemApi.md#listtem_using_get) | **GET** /{apiKey}/items | List items
[**update_item_using_post**](ItemApi.md#update_item_using_post) | **POST** /{apiKey}/items/{id} | Update item


# **add_item_at_using_put**
> Item add_item_at_using_put(api_key, id, attribute_list)

Add item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id
attribute_list = [swagger_client.Attribute()] # list[Attribute] | attributeList

try:
    # Add item
    api_response = api_instance.add_item_at_using_put(api_key, id, attribute_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->add_item_at_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 
 **attribute_list** | [**list[Attribute]**](Attribute.md)| attributeList | 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_using_post**
> Response add_item_using_post(api_key, attribute_list)

Add item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemApi()
api_key = 'api_key_example' # str | apiKey
attribute_list = [swagger_client.Attribute()] # list[Attribute] | attributeList

try:
    # Add item
    api_response = api_instance.add_item_using_post(api_key, attribute_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->add_item_using_post: %s\n" % e)
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

# **delete_item_using_delete**
> Item delete_item_using_delete(api_key, id)

Delete item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id

try:
    # Delete item
    api_response = api_instance.delete_item_using_delete(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->delete_item_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gettem_using_get**
> Item gettem_using_get(api_key, id)

Get item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id

try:
    # Get item
    api_response = api_instance.gettem_using_get(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->gettem_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 

### Return type

[**Item**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listtem_using_get**
> list[Item] listtem_using_get(api_key, offset=offset, limit=limit)

List items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemApi()
api_key = 'api_key_example' # str | apiKey
offset = 56 # int | offsel of the items list (optional)
limit = 56 # int | limit of the items list (optional)

try:
    # List items
    api_response = api_instance.listtem_using_get(api_key, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->listtem_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **offset** | **int**| offsel of the items list | [optional] 
 **limit** | **int**| limit of the items list | [optional] 

### Return type

[**list[Item]**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_using_post**
> Response update_item_using_post(api_key, id, attribute_list)

Update item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id
attribute_list = [swagger_client.Attribute()] # list[Attribute] | attributeList

try:
    # Update item
    api_response = api_instance.update_item_using_post(api_key, id, attribute_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->update_item_using_post: %s\n" % e)
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

