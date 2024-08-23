# skybox_openapi_client.HoldsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**holds_delete_by_id**](HoldsApi.md#holds_delete_by_id) | **DELETE** /holds/{hold-id} | 
[**holds_get_by_id**](HoldsApi.md#holds_get_by_id) | **GET** /holds/{hold-id} | 
[**holds_insert**](HoldsApi.md#holds_insert) | **POST** /holds | 
[**holds_search**](HoldsApi.md#holds_search) | **GET** /holds | 
[**holds_update**](HoldsApi.md#holds_update) | **PUT** /holds/{hold-id} | 


# **holds_delete_by_id**
> Hold holds_delete_by_id(hold_id)



Deletes a hold by the hold id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.hold import Hold
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
    api_instance = skybox_openapi_client.HoldsApi(api_client)
    hold_id = 56 # int | The id of the hold

    try:
        api_response = api_instance.holds_delete_by_id(hold_id)
        print("The response of HoldsApi->holds_delete_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoldsApi->holds_delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hold_id** | **int**| The id of the hold | 

### Return type

[**Hold**](Hold.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | hold deleted |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **holds_get_by_id**
> Hold holds_get_by_id(hold_id)



Retrieves a hold by the hold id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.hold import Hold
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
    api_instance = skybox_openapi_client.HoldsApi(api_client)
    hold_id = 56 # int | The id of the hold

    try:
        api_response = api_instance.holds_get_by_id(hold_id)
        print("The response of HoldsApi->holds_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoldsApi->holds_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hold_id** | **int**| The id of the hold | 

### Return type

[**Hold**](Hold.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | hold returned |  -  |
**401** | not authorized |  -  |
**404** | hold not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **holds_insert**
> Hold holds_insert(hold_request)



Creates a hold

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.hold import Hold
from skybox_openapi_client.models.hold_request import HoldRequest
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
    api_instance = skybox_openapi_client.HoldsApi(api_client)
    hold_request = skybox_openapi_client.HoldRequest() # HoldRequest | A hold request to create.

    try:
        api_response = api_instance.holds_insert(hold_request)
        print("The response of HoldsApi->holds_insert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoldsApi->holds_insert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hold_request** | [**HoldRequest**](HoldRequest.md)| A hold request to create. | 

### Return type

[**Hold**](Hold.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | hold created |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **holds_search**
> List[HoldSummary] holds_search(limit=limit, sort_dir=sort_dir, page_number=page_number, id=id, inventory_id=inventory_id, exchange_pos_id=exchange_pos_id, event=event, venue_id=venue_id, venue=venue, user=user, user_id=user_id, event_date_from=event_date_from, event_date_to=event_date_to, created_date_from=created_date_from, created_date_to=created_date_to, expiry_date_from=expiry_date_from, expiry_date_to=expiry_date_to, external_ref=external_ref, customer_id=customer_id, sorted_by=sorted_by)



Retrieves all holds

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.hold_summary import HoldSummary
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
    api_instance = skybox_openapi_client.HoldsApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    id = 56 # int | Id to filter (optional)
    inventory_id = 56 # int | Inventory Id to filter (optional)
    exchange_pos_id = [56] # List[int] | Exchange pos Id filter (optional)
    event = 'event_example' # str | Event to filter (optional)
    venue_id = 56 # int | Venue Id filter (optional)
    venue = 'venue_example' # str | Venue filter (optional)
    user = 'user_example' # str | User filter (optional)
    user_id = 'user_id_example' # str | User id filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | From event date filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | To event date filter (optional)
    created_date_from = '2013-10-20T19:20:30+01:00' # datetime | From created date filter (optional)
    created_date_to = '2013-10-20T19:20:30+01:00' # datetime | To created date filter (optional)
    expiry_date_from = '2013-10-20T19:20:30+01:00' # datetime | From expiry date filter (optional)
    expiry_date_to = '2013-10-20T19:20:30+01:00' # datetime | To expiry date filter (optional)
    external_ref = ['external_ref_example'] # List[str] | External reference to filter (optional)
    customer_id = 56 # int | Category Id filter (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.holds_search(limit=limit, sort_dir=sort_dir, page_number=page_number, id=id, inventory_id=inventory_id, exchange_pos_id=exchange_pos_id, event=event, venue_id=venue_id, venue=venue, user=user, user_id=user_id, event_date_from=event_date_from, event_date_to=event_date_to, created_date_from=created_date_from, created_date_to=created_date_to, expiry_date_from=expiry_date_from, expiry_date_to=expiry_date_to, external_ref=external_ref, customer_id=customer_id, sorted_by=sorted_by)
        print("The response of HoldsApi->holds_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoldsApi->holds_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **id** | **int**| Id to filter | [optional] 
 **inventory_id** | **int**| Inventory Id to filter | [optional] 
 **exchange_pos_id** | [**List[int]**](int.md)| Exchange pos Id filter | [optional] 
 **event** | **str**| Event to filter | [optional] 
 **venue_id** | **int**| Venue Id filter | [optional] 
 **venue** | **str**| Venue filter | [optional] 
 **user** | **str**| User filter | [optional] 
 **user_id** | **str**| User id filter | [optional] 
 **event_date_from** | **datetime**| From event date filter | [optional] 
 **event_date_to** | **datetime**| To event date filter | [optional] 
 **created_date_from** | **datetime**| From created date filter | [optional] 
 **created_date_to** | **datetime**| To created date filter | [optional] 
 **expiry_date_from** | **datetime**| From expiry date filter | [optional] 
 **expiry_date_to** | **datetime**| To expiry date filter | [optional] 
 **external_ref** | [**List[str]**](str.md)| External reference to filter | [optional] 
 **customer_id** | **int**| Category Id filter | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[HoldSummary]**](HoldSummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | holds returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **holds_update**
> Hold holds_update(hold_id, hold)



Updates a hold

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.hold import Hold
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
    api_instance = skybox_openapi_client.HoldsApi(api_client)
    hold_id = 56 # int | The id of the hold
    hold = skybox_openapi_client.Hold() # Hold | The hold object to update.

    try:
        api_response = api_instance.holds_update(hold_id, hold)
        print("The response of HoldsApi->holds_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoldsApi->holds_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hold_id** | **int**| The id of the hold | 
 **hold** | [**Hold**](Hold.md)| The hold object to update. | 

### Return type

[**Hold**](Hold.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | hold updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

