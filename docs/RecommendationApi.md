# swagger_client.RecommendationApi

All URIs are relative to *https://convertein.com:8083/convertein/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_item_using_get**](RecommendationApi.md#query_item_using_get) | **GET** /{apiKey}/recommendations/items/{id} | Get Recommendations for items
[**recommend_for_user_using_get**](RecommendationApi.md#recommend_for_user_using_get) | **GET** /{apiKey}/recommendations/users/{id} | Get Recommendations for user


# **query_item_using_get**
> RecomResult query_item_using_get(api_key, id, start=start, page_size=page_size, sort_field=sort_field, sort_type=sort_type, token=token, did=did, user=user, fq=fq, event=event, sb=sb, callback=callback, uid_cookie=uid_cookie)

Get Recommendations for items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RecommendationApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id
start = 0 # int | start (optional) (default to 0)
page_size = 10 # int | pageSize (optional) (default to 10)
sort_field = 'sort_field_example' # str | sortField (optional)
sort_type = 'asc' # str | sortType (optional) (default to asc)
token = 'token_example' # str | token (optional)
did = 'did_example' # str | did (optional)
user = 'user_example' # str | user (optional)
fq = ['fq_example'] # list[str] | fq (optional)
event = 'ON_QUERY' # str | event (optional) (default to ON_QUERY)
sb = 'false' # str | sb (optional) (default to false)
callback = 'callback_example' # str | callback (optional)
uid_cookie = 'uid_cookie_example' # str | uidCookie (optional)

try:
    # Get Recommendations for items
    api_response = api_instance.query_item_using_get(api_key, id, start=start, page_size=page_size, sort_field=sort_field, sort_type=sort_type, token=token, did=did, user=user, fq=fq, event=event, sb=sb, callback=callback, uid_cookie=uid_cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendationApi->query_item_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 
 **start** | **int**| start | [optional] [default to 0]
 **page_size** | **int**| pageSize | [optional] [default to 10]
 **sort_field** | **str**| sortField | [optional] 
 **sort_type** | **str**| sortType | [optional] [default to asc]
 **token** | **str**| token | [optional] 
 **did** | **str**| did | [optional] 
 **user** | **str**| user | [optional] 
 **fq** | [**list[str]**](str.md)| fq | [optional] 
 **event** | **str**| event | [optional] [default to ON_QUERY]
 **sb** | **str**| sb | [optional] [default to false]
 **callback** | **str**| callback | [optional] 
 **uid_cookie** | **str**| uidCookie | [optional] 

### Return type

[**RecomResult**](RecomResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommend_for_user_using_get**
> RecomResult recommend_for_user_using_get(api_key, id)

Get Recommendations for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RecommendationApi()
api_key = 'api_key_example' # str | apiKey
id = 'id_example' # str | id

try:
    # Get Recommendations for user
    api_response = api_instance.recommend_for_user_using_get(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendationApi->recommend_for_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| apiKey | 
 **id** | **str**| id | 

### Return type

[**RecomResult**](RecomResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

