# skybox_openapi_client.EventsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_bulk_remove_tags**](EventsApi.md#events_bulk_remove_tags) | **POST** /events/tags/remove | 
[**events_delete**](EventsApi.md#events_delete) | **POST** /events/{event-id}/tags/actions/delete | 
[**events_find_event_deltas**](EventsApi.md#events_find_event_deltas) | **GET** /events/{event_id}/deltas | 
[**events_get**](EventsApi.md#events_get) | **GET** /events/{event-id} | 
[**events_get_categories**](EventsApi.md#events_get_categories) | **GET** /events/categories | 
[**events_get_performer_by_id**](EventsApi.md#events_get_performer_by_id) | **GET** /events/performers/{performer-id} | 
[**events_get_performers**](EventsApi.md#events_get_performers) | **GET** /events/performers | 
[**events_index**](EventsApi.md#events_index) | **GET** /events | 
[**events_tag**](EventsApi.md#events_tag) | **POST** /events/{event-id}/tags | 


# **events_bulk_remove_tags**
> events_bulk_remove_tags(request_body)



Deletes all tags from events with given ids

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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    request_body = [56] # List[int] | Event Ids

    try:
        api_instance.events_bulk_remove_tags(request_body)
    except Exception as e:
        print("Exception when calling EventsApi->events_bulk_remove_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| Event Ids | 

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

# **events_delete**
> events_delete(event_id, tag_request)



Deletes tags for an event

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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    event_id = 56 # int | The event Id
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to be removed from the event

    try:
        api_instance.events_delete(event_id, tag_request)
    except Exception as e:
        print("Exception when calling EventsApi->events_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| The event Id | 
 **tag_request** | [**List[TagRequest]**](TagRequest.md)| Tags to be removed from the event | 

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

# **events_find_event_deltas**
> List[EventDelta] events_find_event_deltas(event_id)



Retrieves event deltas

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.event_delta import EventDelta
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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    event_id = 56 # int | The id of the event to retrieve

    try:
        api_response = api_instance.events_find_event_deltas(event_id)
        print("The response of EventsApi->events_find_event_deltas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_find_event_deltas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| The id of the event to retrieve | 

### Return type

[**List[EventDelta]**](EventDelta.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event deltas returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get**
> Event events_get(event_id)



Returns an event

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.event import Event
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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    event_id = 56 # int | The id of the event to retrieve

    try:
        api_response = api_instance.events_get(event_id)
        print("The response of EventsApi->events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| The id of the event to retrieve | 

### Return type

[**Event**](Event.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | event returned |  -  |
**401** | not authorized |  -  |
**404** | event not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get_categories**
> List[Category] events_get_categories()



Retrieves all categories

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.category import Category
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
    api_instance = skybox_openapi_client.EventsApi(api_client)

    try:
        api_response = api_instance.events_get_categories()
        print("The response of EventsApi->events_get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_get_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Category]**](Category.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | categories returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get_performer_by_id**
> Performer events_get_performer_by_id(performer_id)



Retrieves a performer by the performer id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.performer import Performer
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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    performer_id = 56 # int | Performer id

    try:
        api_response = api_instance.events_get_performer_by_id(performer_id)
        print("The response of EventsApi->events_get_performer_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_get_performer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performer_id** | **int**| Performer id | 

### Return type

[**Performer**](Performer.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | performer returned |  -  |
**401** | not authorized |  -  |
**404** | performer not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get_performers**
> List[Performer] events_get_performers(name=name)



Retrieves all performers

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.performer import Performer
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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        api_response = api_instance.events_get_performers(name=name)
        print("The response of EventsApi->events_get_performers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_get_performers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**List[Performer]**](Performer.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | performers returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_index**
> List[Event] events_index(limit=limit, sort_dir=sort_dir, page_number=page_number, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event=event, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, country=country, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, keywords=keywords, event_id=event_id, performer_id=performer_id, day_of_week=day_of_week, exclude_parking=exclude_parking, exclude_active_inventory=exclude_active_inventory, no_tags=no_tags, sorted_by=sorted_by, only_sold_tickets=only_sold_tickets)



Retrieves filtered events

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.event import Event
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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    limit = 56 # int | Page number of results to show. Limit size for Event searches is: 1000 (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    tag = ['tag_example'] # List[str] | Tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | Tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    event = 'event_example' # str | Event search term (optional)
    event_type = 'event_type_example' # str | Event Type (optional)
    category_id = 56 # int | Category ID filter (optional)
    category = 'category_example' # str | Category (optional)
    venue_id = 56 # int | The id of a venue (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    country = ['country_example'] # List[str] | Country search filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Minimum event date in yyyy-MM-dd format (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Maximum event date in yyyy-MM-dd format (optional)
    event_time_from = 'event_time_from_example' # str | Only search events starting not earlier than (optional)
    event_time_to = 'event_time_to_example' # str | Only search events starting not later than (optional)
    keywords = ['keywords_example'] # List[str] | Search Keywords (optional)
    event_id = [56] # List[int] | Event ID (optional)
    performer_id = 56 # int | Performer ID filter (optional)
    day_of_week = [56] # List[int] | Day of the week of events that occur on that day of the week (optional)
    exclude_parking = True # bool | Whether parking events are excluded (optional)
    exclude_active_inventory = True # bool | Whether active inventories are excluded (optional)
    no_tags = True # bool | Only return events with no tags (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)
    only_sold_tickets = True # bool | Get events with only sold tickets. Default value is false (optional)

    try:
        api_response = api_instance.events_index(limit=limit, sort_dir=sort_dir, page_number=page_number, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event=event, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, country=country, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, keywords=keywords, event_id=event_id, performer_id=performer_id, day_of_week=day_of_week, exclude_parking=exclude_parking, exclude_active_inventory=exclude_active_inventory, no_tags=no_tags, sorted_by=sorted_by, only_sold_tickets=only_sold_tickets)
        print("The response of EventsApi->events_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Page number of results to show. Limit size for Event searches is: 1000 | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **tag** | [**List[str]**](str.md)| Tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| Tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **event** | **str**| Event search term | [optional] 
 **event_type** | **str**| Event Type | [optional] 
 **category_id** | **int**| Category ID filter | [optional] 
 **category** | **str**| Category | [optional] 
 **venue_id** | **int**| The id of a venue | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **country** | [**List[str]**](str.md)| Country search filter | [optional] 
 **event_date_from** | **datetime**| Minimum event date in yyyy-MM-dd format | [optional] 
 **event_date_to** | **datetime**| Maximum event date in yyyy-MM-dd format | [optional] 
 **event_time_from** | **str**| Only search events starting not earlier than | [optional] 
 **event_time_to** | **str**| Only search events starting not later than | [optional] 
 **keywords** | [**List[str]**](str.md)| Search Keywords | [optional] 
 **event_id** | [**List[int]**](int.md)| Event ID | [optional] 
 **performer_id** | **int**| Performer ID filter | [optional] 
 **day_of_week** | [**List[int]**](int.md)| Day of the week of events that occur on that day of the week | [optional] 
 **exclude_parking** | **bool**| Whether parking events are excluded | [optional] 
 **exclude_active_inventory** | **bool**| Whether active inventories are excluded | [optional] 
 **no_tags** | **bool**| Only return events with no tags | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 
 **only_sold_tickets** | **bool**| Get events with only sold tickets. Default value is false | [optional] 

### Return type

[**List[Event]**](Event.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | events returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_tag**
> events_tag(event_id, tag_request)



Inserts a new tags for an event. Duplicates are ignored

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
    api_instance = skybox_openapi_client.EventsApi(api_client)
    event_id = 56 # int | 
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | 

    try:
        api_instance.events_tag(event_id, tag_request)
    except Exception as e:
        print("Exception when calling EventsApi->events_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**|  | 
 **tag_request** | [**List[TagRequest]**](TagRequest.md)|  | 

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
**200** | tag inserted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

