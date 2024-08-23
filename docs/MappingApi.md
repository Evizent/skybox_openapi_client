# skybox_openapi_client.MappingApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapping_bulk_delete**](MappingApi.md#mapping_bulk_delete) | **POST** /mappings/actions/bulk-cancel | 
[**mapping_delete**](MappingApi.md#mapping_delete) | **DELETE** /mappings/{mapping-id} | 
[**mapping_find_pending_by_id**](MappingApi.md#mapping_find_pending_by_id) | **GET** /mappings/{mapping-id} | 
[**mapping_get_pending_by_account**](MappingApi.md#mapping_get_pending_by_account) | **GET** /mappings | 
[**mapping_resend_mapping_request**](MappingApi.md#mapping_resend_mapping_request) | **GET** /mappings/{mapping-id}/resend | 


# **mapping_bulk_delete**
> mapping_bulk_delete(request_body)



Deletes a bulk of mappings and cancels the purchase lines they are associated with

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
    api_instance = skybox_openapi_client.MappingApi(api_client)
    request_body = [56] # List[int] | The id of the mapping

    try:
        api_instance.mapping_bulk_delete(request_body)
    except Exception as e:
        print("Exception when calling MappingApi->mapping_bulk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| The id of the mapping | 

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
**200** | mappings deleted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |
**404** | mappings not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_delete**
> mapping_delete(mapping_id)



Deletes a mapping and cancels the purchase line it's associated with

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
    api_instance = skybox_openapi_client.MappingApi(api_client)
    mapping_id = 56 # int | The id of the mapping

    try:
        api_instance.mapping_delete(mapping_id)
    except Exception as e:
        print("Exception when calling MappingApi->mapping_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| The id of the mapping | 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | mapping deleted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |
**404** | mapping not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_find_pending_by_id**
> InventoryMapping mapping_find_pending_by_id(mapping_id)



Returns a mapping

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_mapping import InventoryMapping
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
    api_instance = skybox_openapi_client.MappingApi(api_client)
    mapping_id = 56 # int | The id of the mapping to retrieve

    try:
        api_response = api_instance.mapping_find_pending_by_id(mapping_id)
        print("The response of MappingApi->mapping_find_pending_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->mapping_find_pending_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| The id of the mapping to retrieve | 

### Return type

[**InventoryMapping**](InventoryMapping.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | mappings returned |  -  |
**401** | not authorized |  -  |
**404** | mapping not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_get_pending_by_account**
> List[InventoryMappingSummary] mapping_get_pending_by_account(purchase_id=purchase_id, external_ref=external_ref, event=event, venue=venue, event_date_from=event_date_from, event_date_to=event_date_to, mapping_date_from=mapping_date_from, mapping_date_to=mapping_date_to)



Gets all pending mappings

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_mapping_summary import InventoryMappingSummary
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
    api_instance = skybox_openapi_client.MappingApi(api_client)
    purchase_id = [56] # List[int] | Purchase Id search filter (optional)
    external_ref = 'external_ref_example' # str | External reference search filter (optional)
    event = 'event_example' # str | Event search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Event date from range filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Event date to range filter (optional)
    mapping_date_from = '2013-10-20T19:20:30+01:00' # datetime | Mapping date from range filter (optional)
    mapping_date_to = '2013-10-20T19:20:30+01:00' # datetime | Mapping date to range filter (optional)

    try:
        api_response = api_instance.mapping_get_pending_by_account(purchase_id=purchase_id, external_ref=external_ref, event=event, venue=venue, event_date_from=event_date_from, event_date_to=event_date_to, mapping_date_from=mapping_date_from, mapping_date_to=mapping_date_to)
        print("The response of MappingApi->mapping_get_pending_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->mapping_get_pending_by_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | [**List[int]**](int.md)| Purchase Id search filter | [optional] 
 **external_ref** | **str**| External reference search filter | [optional] 
 **event** | **str**| Event search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **event_date_from** | **datetime**| Event date from range filter | [optional] 
 **event_date_to** | **datetime**| Event date to range filter | [optional] 
 **mapping_date_from** | **datetime**| Mapping date from range filter | [optional] 
 **mapping_date_to** | **datetime**| Mapping date to range filter | [optional] 

### Return type

[**List[InventoryMappingSummary]**](InventoryMappingSummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | mappings returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_resend_mapping_request**
> int mapping_resend_mapping_request(mapping_id)



Re-sends a mapping to the mapping queue. Returns the mapping id

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
    api_instance = skybox_openapi_client.MappingApi(api_client)
    mapping_id = 56 # int | The id of the mapping

    try:
        api_response = api_instance.mapping_resend_mapping_request(mapping_id)
        print("The response of MappingApi->mapping_resend_mapping_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingApi->mapping_resend_mapping_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| The id of the mapping | 

### Return type

**int**

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | mapping re-sent successfully |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |
**404** | mapping not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

