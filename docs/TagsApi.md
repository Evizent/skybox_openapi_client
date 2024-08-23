# skybox_openapi_client.TagsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_bulk**](TagsApi.md#tags_bulk) | **PUT** /tags/bulk | 
[**tags_delete**](TagsApi.md#tags_delete) | **POST** /tags/actions/delete | 
[**tags_get_filtered_tags**](TagsApi.md#tags_get_filtered_tags) | **GET** /tags/filtered | 
[**tags_list**](TagsApi.md#tags_list) | **GET** /tags | 
[**tags_tags_summary**](TagsApi.md#tags_tags_summary) | **GET** /tags/summary | 
[**tags_update_color**](TagsApi.md#tags_update_color) | **PUT** /tags/color | 


# **tags_bulk**
> List[TagSummary] tags_bulk(bulk_tag_request)



Bulk add/remove tags

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.bulk_tag_request import BulkTagRequest
from skybox_openapi_client.models.tag_summary import TagSummary
from skybox_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://skybox.vividseats.com/services
# See configuration.py for a list of all supported configuration parameters.
configuration = skybox_openapi_client.Configuration(
    host = "https://skybox.vividseats.com/services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Account
configuration.api_key['Account'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Account'] = 'Bearer'

# Configure API key authorization: Authorization_Token
configuration.api_key['Authorization_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization_Token'] = 'Bearer'

# Configure API key authorization: Application_Token
configuration.api_key['Application_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Application_Token'] = 'Bearer'

# Enter a context with an instance of the API client
with skybox_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = skybox_openapi_client.TagsApi(api_client)
    bulk_tag_request = skybox_openapi_client.BulkTagRequest() # BulkTagRequest | Update payload

    try:
        api_response = api_instance.tags_bulk(bulk_tag_request)
        print("The response of TagsApi->tags_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_tag_request** | [**BulkTagRequest**](BulkTagRequest.md)| Update payload | 

### Return type

[**List[TagSummary]**](TagSummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tag deleted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_delete**
> tags_delete(tag_request)



Deletes tags for an account

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.tag_request import TagRequest
from skybox_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://skybox.vividseats.com/services
# See configuration.py for a list of all supported configuration parameters.
configuration = skybox_openapi_client.Configuration(
    host = "https://skybox.vividseats.com/services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Account
configuration.api_key['Account'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Account'] = 'Bearer'

# Configure API key authorization: Authorization_Token
configuration.api_key['Authorization_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization_Token'] = 'Bearer'

# Configure API key authorization: Application_Token
configuration.api_key['Application_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Application_Token'] = 'Bearer'

# Enter a context with an instance of the API client
with skybox_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = skybox_openapi_client.TagsApi(api_client)
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to remove

    try:
        api_instance.tags_delete(tag_request)
    except Exception as e:
        print("Exception when calling TagsApi->tags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_request** | [**List[TagRequest]**](TagRequest.md)| Tags to remove | 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tags deleted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get_filtered_tags**
> List[str] tags_get_filtered_tags(tag)



Retrieves a list of tags for an account

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://skybox.vividseats.com/services
# See configuration.py for a list of all supported configuration parameters.
configuration = skybox_openapi_client.Configuration(
    host = "https://skybox.vividseats.com/services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Account
configuration.api_key['Account'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Account'] = 'Bearer'

# Configure API key authorization: Authorization_Token
configuration.api_key['Authorization_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization_Token'] = 'Bearer'

# Configure API key authorization: Application_Token
configuration.api_key['Application_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Application_Token'] = 'Bearer'

# Enter a context with an instance of the API client
with skybox_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = skybox_openapi_client.TagsApi(api_client)
    tag = 'tag_example' # str | Key value to search

    try:
        api_response = api_instance.tags_get_filtered_tags(tag)
        print("The response of TagsApi->tags_get_filtered_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_get_filtered_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Key value to search | 

### Return type

**List[str]**

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_list**
> List[str] tags_list()



Retrieves a list of tags for an account

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://skybox.vividseats.com/services
# See configuration.py for a list of all supported configuration parameters.
configuration = skybox_openapi_client.Configuration(
    host = "https://skybox.vividseats.com/services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Account
configuration.api_key['Account'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Account'] = 'Bearer'

# Configure API key authorization: Authorization_Token
configuration.api_key['Authorization_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization_Token'] = 'Bearer'

# Configure API key authorization: Application_Token
configuration.api_key['Application_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Application_Token'] = 'Bearer'

# Enter a context with an instance of the API client
with skybox_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = skybox_openapi_client.TagsApi(api_client)

    try:
        api_response = api_instance.tags_list()
        print("The response of TagsApi->tags_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tags_summary**
> List[TagSummary] tags_tags_summary(limit=limit, sort_dir=sort_dir, page_number=page_number, id=id, tag=tag)



Tags summary

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.tag_summary import TagSummary
from skybox_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://skybox.vividseats.com/services
# See configuration.py for a list of all supported configuration parameters.
configuration = skybox_openapi_client.Configuration(
    host = "https://skybox.vividseats.com/services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Account
configuration.api_key['Account'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Account'] = 'Bearer'

# Configure API key authorization: Authorization_Token
configuration.api_key['Authorization_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization_Token'] = 'Bearer'

# Configure API key authorization: Application_Token
configuration.api_key['Application_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Application_Token'] = 'Bearer'

# Enter a context with an instance of the API client
with skybox_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = skybox_openapi_client.TagsApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    id = 56 # int | Tag Id (optional)
    tag = 'tag_example' # str | Tag name (optional)

    try:
        api_response = api_instance.tags_tags_summary(limit=limit, sort_dir=sort_dir, page_number=page_number, id=id, tag=tag)
        print("The response of TagsApi->tags_tags_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_tags_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **id** | **int**| Tag Id | [optional] 
 **tag** | **str**| Tag name | [optional] 

### Return type

[**List[TagSummary]**](TagSummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tag summary returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_update_color**
> tags_update_color(tag_color_update_request)



Set color used to render a tag in the user interface

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.tag_color_update_request import TagColorUpdateRequest
from skybox_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://skybox.vividseats.com/services
# See configuration.py for a list of all supported configuration parameters.
configuration = skybox_openapi_client.Configuration(
    host = "https://skybox.vividseats.com/services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Account
configuration.api_key['Account'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Account'] = 'Bearer'

# Configure API key authorization: Authorization_Token
configuration.api_key['Authorization_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization_Token'] = 'Bearer'

# Configure API key authorization: Application_Token
configuration.api_key['Application_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Application_Token'] = 'Bearer'

# Enter a context with an instance of the API client
with skybox_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = skybox_openapi_client.TagsApi(api_client)
    tag_color_update_request = skybox_openapi_client.TagColorUpdateRequest() # TagColorUpdateRequest | Update payload

    try:
        api_instance.tags_update_color(tag_color_update_request)
    except Exception as e:
        print("Exception when calling TagsApi->tags_update_color: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_color_update_request** | [**TagColorUpdateRequest**](TagColorUpdateRequest.md)| Update payload | 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tag color updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

