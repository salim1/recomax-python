# swagger_client.EventApi

All URIs are relative to *https://convertein.com:8083/convertein/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_test_using_post**](EventApi.md#create_event_test_using_post) | **POST** /{apiKey}/events | Get Event List
[**create_event_using_put**](EventApi.md#create_event_using_put) | **PUT** /{apiKey}/event/{id} | Create event


# **create_event_test_using_post**
> ResponseEntity create_event_test_using_post(api_key, item_id, user_id, name)

Get Event List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventApi()
api_key = 'api_key_example' # str | apiKey
item_id = 'item_id_example' # str | itemId
user_id = 'user_id_example' # str | userId
name = 'name_example' # str | name

try:
    # Get Event List
    api_response = api_instance.create_event_test_using_post(api_key, item_id, user_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->create_event_test_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **item_id** | **str**| itemId | 
 **user_id** | **str**| userId | 
 **name** | **str**| name | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_using_put**
> ResponseEntity create_event_using_put(api_key, id, item_id=item_id, user_id=user_id, name=name)

Create event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id
item_id = 'item_id_example' # str | itemId (optional)
user_id = 'user_id_example' # str | userId (optional)
name = 'VIEW' # str | name (optional) (default to VIEW)

try:
    # Create event
    api_response = api_instance.create_event_using_put(api_key, id, item_id=item_id, user_id=user_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->create_event_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 
 **item_id** | **str**| itemId | [optional] 
 **user_id** | **str**| userId | [optional] 
 **name** | **str**| name | [optional] [default to VIEW]

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

