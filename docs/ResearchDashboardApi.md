# skybox_openapi_client.ResearchDashboardApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**researchdashboard_get_event_profitability**](ResearchDashboardApi.md#researchdashboard_get_event_profitability) | **GET** /research-dashboard/past-events/events | 
[**researchdashboard_get_events_profitability**](ResearchDashboardApi.md#researchdashboard_get_events_profitability) | **GET** /research-dashboard/events-profitability | 
[**researchdashboard_get_lifetime_pl**](ResearchDashboardApi.md#researchdashboard_get_lifetime_pl) | **GET** /research-dashboard/lifetime-pl | 
[**researchdashboard_get_performer_profitability**](ResearchDashboardApi.md#researchdashboard_get_performer_profitability) | **GET** /research-dashboard/past-events/performers | 
[**researchdashboard_get_seat_map_heat_map**](ResearchDashboardApi.md#researchdashboard_get_seat_map_heat_map) | **GET** /research-dashboard/seat-map-heat-map | 
[**researchdashboard_get_section_profitability**](ResearchDashboardApi.md#researchdashboard_get_section_profitability) | **GET** /research-dashboard/past-events/sections | 
[**researchdashboard_get_tickets_profitability**](ResearchDashboardApi.md#researchdashboard_get_tickets_profitability) | **GET** /research-dashboard/tickets-profitability | 
[**researchdashboard_get_tickets_sales**](ResearchDashboardApi.md#researchdashboard_get_tickets_sales) | **GET** /research-dashboard/tickets-sales | 
[**researchdashboard_get_venue_profitability**](ResearchDashboardApi.md#researchdashboard_get_venue_profitability) | **GET** /research-dashboard/past-events/venues | 


# **researchdashboard_get_event_profitability**
> List[EventProfitability] researchdashboard_get_event_profitability(performer_id=performer_id, venue_id=venue_id)



Retrieves the past profitable events for a performer and/or venue

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.event_profitability import EventProfitability
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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_response = api_instance.researchdashboard_get_event_profitability(performer_id=performer_id, venue_id=venue_id)
        print("The response of ResearchDashboardApi->researchdashboard_get_event_profitability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_event_profitability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

[**List[EventProfitability]**](EventProfitability.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Past profitable events |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_events_profitability**
> researchdashboard_get_events_profitability(performer_id=performer_id, venue_id=venue_id)



Retrieves the events profitability for a performer and/or venue

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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_instance.researchdashboard_get_events_profitability(performer_id=performer_id, venue_id=venue_id)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_events_profitability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profitable events |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_lifetime_pl**
> researchdashboard_get_lifetime_pl(performer_id=performer_id, venue_id=venue_id)



Retrieves the lifetime P/L for a performer and/or venue

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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_instance.researchdashboard_get_lifetime_pl(performer_id=performer_id, venue_id=venue_id)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_lifetime_pl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lifetime P/L |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_performer_profitability**
> List[PerformerProfitability] researchdashboard_get_performer_profitability(performer_id=performer_id, venue_id=venue_id)



Retrieves the past profitable performers for a performer and/or venue

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.performer_profitability import PerformerProfitability
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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_response = api_instance.researchdashboard_get_performer_profitability(performer_id=performer_id, venue_id=venue_id)
        print("The response of ResearchDashboardApi->researchdashboard_get_performer_profitability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_performer_profitability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

[**List[PerformerProfitability]**](PerformerProfitability.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Past profitable performers |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_seat_map_heat_map**
> List[HeatMapSeatMapResponse] researchdashboard_get_seat_map_heat_map(performer_id=performer_id, venue_id=venue_id)



Retrieves profitable sections and groups for a performer and venue

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.heat_map_seat_map_response import HeatMapSeatMapResponse
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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_response = api_instance.researchdashboard_get_seat_map_heat_map(performer_id=performer_id, venue_id=venue_id)
        print("The response of ResearchDashboardApi->researchdashboard_get_seat_map_heat_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_seat_map_heat_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

[**List[HeatMapSeatMapResponse]**](HeatMapSeatMapResponse.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Past profitable sections |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_section_profitability**
> List[SectionProfitability] researchdashboard_get_section_profitability(performer_id=performer_id, venue_id=venue_id)



Retrieves the past profitable sections for a performer and/or venue

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.section_profitability import SectionProfitability
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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_response = api_instance.researchdashboard_get_section_profitability(performer_id=performer_id, venue_id=venue_id)
        print("The response of ResearchDashboardApi->researchdashboard_get_section_profitability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_section_profitability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

[**List[SectionProfitability]**](SectionProfitability.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Past profitable sections and groups |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_tickets_profitability**
> researchdashboard_get_tickets_profitability(performer_id=performer_id, venue_id=venue_id)



Retrieves the tickets profitability for a performer and/or venue

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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_instance.researchdashboard_get_tickets_profitability(performer_id=performer_id, venue_id=venue_id)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_tickets_profitability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profitable tickets |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_tickets_sales**
> List[TicketSales] researchdashboard_get_tickets_sales(performer_id=performer_id, venue_id=venue_id, limit=limit, sort_by=sort_by, sort_dir=sort_dir, events=events)



Retrieves the tickets sales occurring for a performer and/or venue

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.ticket_sales import TicketSales
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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)
    limit = 56 # int | Number of results to return (optional)
    sort_by = 'sort_by_example' # str | Field to sort by (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    events = [56] # List[int] | Set of event ids to search for - results might be returned in alphabetical order (optional)

    try:
        api_response = api_instance.researchdashboard_get_tickets_sales(performer_id=performer_id, venue_id=venue_id, limit=limit, sort_by=sort_by, sort_dir=sort_dir, events=events)
        print("The response of ResearchDashboardApi->researchdashboard_get_tickets_sales:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_tickets_sales: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 
 **limit** | **int**| Number of results to return | [optional] 
 **sort_by** | **str**| Field to sort by | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **events** | [**List[int]**](int.md)| Set of event ids to search for - results might be returned in alphabetical order | [optional] 

### Return type

[**List[TicketSales]**](TicketSales.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tickets sales |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **researchdashboard_get_venue_profitability**
> List[VenueProfitability] researchdashboard_get_venue_profitability(performer_id=performer_id, venue_id=venue_id)



Retrieves the past profitable venues for a performer and/or venue

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.venue_profitability import VenueProfitability
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
    api_instance = skybox_openapi_client.ResearchDashboardApi(api_client)
    performer_id = 56 # int | Performer Id (optional)
    venue_id = 56 # int | Venue Id (optional)

    try:
        api_response = api_instance.researchdashboard_get_venue_profitability(performer_id=performer_id, venue_id=venue_id)
        print("The response of ResearchDashboardApi->researchdashboard_get_venue_profitability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResearchDashboardApi->researchdashboard_get_venue_profitability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer Id | [optional] 
 **venue_id** | **int**| Venue Id | [optional] 

### Return type

[**List[VenueProfitability]**](VenueProfitability.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Past profitable venues |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

