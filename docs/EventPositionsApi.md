# skybox_openapi_client.EventPositionsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_positions_event_positions_totals**](EventPositionsApi.md#event_positions_event_positions_totals) | **GET** /event_positions/totals | 
[**event_positions_event_positions_values**](EventPositionsApi.md#event_positions_event_positions_values) | **GET** /event_positions/values | 
[**event_positions_get_categories**](EventPositionsApi.md#event_positions_get_categories) | **GET** /event_positions/categories | 
[**event_positions_get_performers**](EventPositionsApi.md#event_positions_get_performers) | **GET** /event_positions/performers | 
[**event_positions_index**](EventPositionsApi.md#event_positions_index) | **GET** /event_positions | 


# **event_positions_event_positions_totals**
> List[EventPosition] event_positions_event_positions_totals(limit=limit, sort_dir=sort_dir, page_number=page_number, section=section, row=row, listed=listed, event_id=event_id, event=event, keywords=keywords, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, day_of_week=day_of_week, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, performer_id=performer_id, tags_match_all=tags_match_all, anti_tags_match_all=anti_tags_match_all, inventory_tags_match_all=inventory_tags_match_all, no_tags=no_tags, exclude_only_zone_inventory=exclude_only_zone_inventory, exclude_parking=exclude_parking, sorted_by=sorted_by)



Retrieves event positions totals

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.event_position import EventPosition
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
    api_instance = skybox_openapi_client.EventPositionsApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    section = 'section_example' # str | Section search filter (optional)
    row = 'row_example' # str | Row search filter (optional)
    listed = True # bool | Whether inventories are listed (optional)
    event_id = [56] # List[int] | Event Id to search by (optional)
    event = 'event_example' # str | Event search term (optional)
    keywords = ['keywords_example'] # List[str] | Search Keywords (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Minimum event date in yyyy-MM-dd format (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Maximum event date in yyyy-MM-dd format (optional)
    event_time_from = 'event_time_from_example' # str | Only search events starting not earlier than (optional)
    event_time_to = 'event_time_to_example' # str | Only search events starting not later than (optional)
    day_of_week = [56] # List[int] | Day of the week of events that occur on that day of the week (optional)
    event_type = 'event_type_example' # str | Event Type search filter (optional)
    category_id = 56 # int | Category Id search filter (optional)
    category = 'category_example' # str | Category search filter (optional)
    venue_id = 56 # int | Venue Id search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    performer_id = 56 # int | Performer Id filter (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    inventory_tags_match_all = True # bool | Whether the results should have all inventory tags or only some (optional)
    no_tags = True # bool | Inventory tags to exclude (optional)
    exclude_only_zone_inventory = True # bool | Whether to exclude events with all zoned inventories (optional)
    exclude_parking = True # bool | Whether parking events are excluded (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.event_positions_event_positions_totals(limit=limit, sort_dir=sort_dir, page_number=page_number, section=section, row=row, listed=listed, event_id=event_id, event=event, keywords=keywords, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, day_of_week=day_of_week, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, performer_id=performer_id, tags_match_all=tags_match_all, anti_tags_match_all=anti_tags_match_all, inventory_tags_match_all=inventory_tags_match_all, no_tags=no_tags, exclude_only_zone_inventory=exclude_only_zone_inventory, exclude_parking=exclude_parking, sorted_by=sorted_by)
        print("The response of EventPositionsApi->event_positions_event_positions_totals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventPositionsApi->event_positions_event_positions_totals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **section** | **str**| Section search filter | [optional] 
 **row** | **str**| Row search filter | [optional] 
 **listed** | **bool**| Whether inventories are listed | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id to search by | [optional] 
 **event** | **str**| Event search term | [optional] 
 **keywords** | [**List[str]**](str.md)| Search Keywords | [optional] 
 **event_date_from** | **datetime**| Minimum event date in yyyy-MM-dd format | [optional] 
 **event_date_to** | **datetime**| Maximum event date in yyyy-MM-dd format | [optional] 
 **event_time_from** | **str**| Only search events starting not earlier than | [optional] 
 **event_time_to** | **str**| Only search events starting not later than | [optional] 
 **day_of_week** | [**List[int]**](int.md)| Day of the week of events that occur on that day of the week | [optional] 
 **event_type** | **str**| Event Type search filter | [optional] 
 **category_id** | **int**| Category Id search filter | [optional] 
 **category** | **str**| Category search filter | [optional] 
 **venue_id** | **int**| Venue Id search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **performer_id** | **int**| Performer Id filter | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **inventory_tags_match_all** | **bool**| Whether the results should have all inventory tags or only some | [optional] 
 **no_tags** | **bool**| Inventory tags to exclude | [optional] 
 **exclude_only_zone_inventory** | **bool**| Whether to exclude events with all zoned inventories | [optional] 
 **exclude_parking** | **bool**| Whether parking events are excluded | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[EventPosition]**](EventPosition.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | events positions totals returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_positions_event_positions_values**
> List[EventPosition] event_positions_event_positions_values(limit=limit, sort_dir=sort_dir, page_number=page_number, section=section, row=row, listed=listed, event_id=event_id, event=event, keywords=keywords, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, day_of_week=day_of_week, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, performer_id=performer_id, tags_match_all=tags_match_all, anti_tags_match_all=anti_tags_match_all, inventory_tags_match_all=inventory_tags_match_all, no_tags=no_tags, exclude_only_zone_inventory=exclude_only_zone_inventory, exclude_parking=exclude_parking, sorted_by=sorted_by)



Retrieves event positions without totals

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.event_position import EventPosition
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
    api_instance = skybox_openapi_client.EventPositionsApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    section = 'section_example' # str | Section search filter (optional)
    row = 'row_example' # str | Row search filter (optional)
    listed = True # bool | Whether inventories are listed (optional)
    event_id = [56] # List[int] | Event Id to search by (optional)
    event = 'event_example' # str | Event search term (optional)
    keywords = ['keywords_example'] # List[str] | Search Keywords (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Minimum event date in yyyy-MM-dd format (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Maximum event date in yyyy-MM-dd format (optional)
    event_time_from = 'event_time_from_example' # str | Only search events starting not earlier than (optional)
    event_time_to = 'event_time_to_example' # str | Only search events starting not later than (optional)
    day_of_week = [56] # List[int] | Day of the week of events that occur on that day of the week (optional)
    event_type = 'event_type_example' # str | Event Type search filter (optional)
    category_id = 56 # int | Category Id search filter (optional)
    category = 'category_example' # str | Category search filter (optional)
    venue_id = 56 # int | Venue Id search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    performer_id = 56 # int | Performer Id filter (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    inventory_tags_match_all = True # bool | Whether the results should have all inventory tags or only some (optional)
    no_tags = True # bool | Inventory tags to exclude (optional)
    exclude_only_zone_inventory = True # bool | Whether to exclude events with all zoned inventories (optional)
    exclude_parking = True # bool | Whether parking events are excluded (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.event_positions_event_positions_values(limit=limit, sort_dir=sort_dir, page_number=page_number, section=section, row=row, listed=listed, event_id=event_id, event=event, keywords=keywords, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, day_of_week=day_of_week, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, performer_id=performer_id, tags_match_all=tags_match_all, anti_tags_match_all=anti_tags_match_all, inventory_tags_match_all=inventory_tags_match_all, no_tags=no_tags, exclude_only_zone_inventory=exclude_only_zone_inventory, exclude_parking=exclude_parking, sorted_by=sorted_by)
        print("The response of EventPositionsApi->event_positions_event_positions_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventPositionsApi->event_positions_event_positions_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **section** | **str**| Section search filter | [optional] 
 **row** | **str**| Row search filter | [optional] 
 **listed** | **bool**| Whether inventories are listed | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id to search by | [optional] 
 **event** | **str**| Event search term | [optional] 
 **keywords** | [**List[str]**](str.md)| Search Keywords | [optional] 
 **event_date_from** | **datetime**| Minimum event date in yyyy-MM-dd format | [optional] 
 **event_date_to** | **datetime**| Maximum event date in yyyy-MM-dd format | [optional] 
 **event_time_from** | **str**| Only search events starting not earlier than | [optional] 
 **event_time_to** | **str**| Only search events starting not later than | [optional] 
 **day_of_week** | [**List[int]**](int.md)| Day of the week of events that occur on that day of the week | [optional] 
 **event_type** | **str**| Event Type search filter | [optional] 
 **category_id** | **int**| Category Id search filter | [optional] 
 **category** | **str**| Category search filter | [optional] 
 **venue_id** | **int**| Venue Id search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **performer_id** | **int**| Performer Id filter | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **inventory_tags_match_all** | **bool**| Whether the results should have all inventory tags or only some | [optional] 
 **no_tags** | **bool**| Inventory tags to exclude | [optional] 
 **exclude_only_zone_inventory** | **bool**| Whether to exclude events with all zoned inventories | [optional] 
 **exclude_parking** | **bool**| Whether parking events are excluded | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[EventPosition]**](EventPosition.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | events positions without totals returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_positions_get_categories**
> List[Category] event_positions_get_categories()



Retrieves event positions grouped by category

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
    api_instance = skybox_openapi_client.EventPositionsApi(api_client)

    try:
        api_response = api_instance.event_positions_get_categories()
        print("The response of EventPositionsApi->event_positions_get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventPositionsApi->event_positions_get_categories: %s\n" % e)
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

# **event_positions_get_performers**
> List[PerformerPosition] event_positions_get_performers(limit=limit, sort_dir=sort_dir, page_number=page_number, performer_id=performer_id, performer=performer, event_type=event_type, category_id=category_id, event_date_from=event_date_from, event_date_to=event_date_to, day_of_week=day_of_week, exclude_parking=exclude_parking, sorted_by=sorted_by)



Retrieves event positions grouped by performer

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.performer_position import PerformerPosition
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
    api_instance = skybox_openapi_client.EventPositionsApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    performer_id = [56] # List[int] | Performer Id search filter (optional)
    performer = 'performer_example' # str | Performer name search filter (optional)
    event_type = 'event_type_example' # str | Event Type search filter (optional)
    category_id = 56 # int | Category Id search filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Minimum event date in yyyy-MM-dd format (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Maximum event date in yyyy-MM-dd format (optional)
    day_of_week = [56] # List[int] | Day of the week of events that occur on that day of the week (optional)
    exclude_parking = True # bool | Whether parking events are excluded (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.event_positions_get_performers(limit=limit, sort_dir=sort_dir, page_number=page_number, performer_id=performer_id, performer=performer, event_type=event_type, category_id=category_id, event_date_from=event_date_from, event_date_to=event_date_to, day_of_week=day_of_week, exclude_parking=exclude_parking, sorted_by=sorted_by)
        print("The response of EventPositionsApi->event_positions_get_performers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventPositionsApi->event_positions_get_performers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **performer_id** | [**List[int]**](int.md)| Performer Id search filter | [optional] 
 **performer** | **str**| Performer name search filter | [optional] 
 **event_type** | **str**| Event Type search filter | [optional] 
 **category_id** | **int**| Category Id search filter | [optional] 
 **event_date_from** | **datetime**| Minimum event date in yyyy-MM-dd format | [optional] 
 **event_date_to** | **datetime**| Maximum event date in yyyy-MM-dd format | [optional] 
 **day_of_week** | [**List[int]**](int.md)| Day of the week of events that occur on that day of the week | [optional] 
 **exclude_parking** | **bool**| Whether parking events are excluded | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[PerformerPosition]**](PerformerPosition.md)

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

# **event_positions_index**
> List[EventPosition] event_positions_index(limit=limit, sort_dir=sort_dir, page_number=page_number, section=section, row=row, listed=listed, event_id=event_id, event=event, keywords=keywords, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, day_of_week=day_of_week, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, performer_id=performer_id, tags_match_all=tags_match_all, anti_tags_match_all=anti_tags_match_all, inventory_tags_match_all=inventory_tags_match_all, no_tags=no_tags, exclude_only_zone_inventory=exclude_only_zone_inventory, exclude_parking=exclude_parking, sorted_by=sorted_by)



Retrieves event positions

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.event_position import EventPosition
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
    api_instance = skybox_openapi_client.EventPositionsApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    section = 'section_example' # str | Section search filter (optional)
    row = 'row_example' # str | Row search filter (optional)
    listed = True # bool | Whether inventories are listed (optional)
    event_id = [56] # List[int] | Event Id to search by (optional)
    event = 'event_example' # str | Event search term (optional)
    keywords = ['keywords_example'] # List[str] | Search Keywords (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Minimum event date in yyyy-MM-dd format (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Maximum event date in yyyy-MM-dd format (optional)
    event_time_from = 'event_time_from_example' # str | Only search events starting not earlier than (optional)
    event_time_to = 'event_time_to_example' # str | Only search events starting not later than (optional)
    day_of_week = [56] # List[int] | Day of the week of events that occur on that day of the week (optional)
    event_type = 'event_type_example' # str | Event Type search filter (optional)
    category_id = 56 # int | Category Id search filter (optional)
    category = 'category_example' # str | Category search filter (optional)
    venue_id = 56 # int | Venue Id search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    performer_id = 56 # int | Performer Id filter (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    inventory_tags_match_all = True # bool | Whether the results should have all inventory tags or only some (optional)
    no_tags = True # bool | Inventory tags to exclude (optional)
    exclude_only_zone_inventory = True # bool | Whether to exclude events with all zoned inventories (optional)
    exclude_parking = True # bool | Whether parking events are excluded (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.event_positions_index(limit=limit, sort_dir=sort_dir, page_number=page_number, section=section, row=row, listed=listed, event_id=event_id, event=event, keywords=keywords, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, day_of_week=day_of_week, event_type=event_type, category_id=category_id, category=category, venue_id=venue_id, venue=venue, city=city, state=state, performer_id=performer_id, tags_match_all=tags_match_all, anti_tags_match_all=anti_tags_match_all, inventory_tags_match_all=inventory_tags_match_all, no_tags=no_tags, exclude_only_zone_inventory=exclude_only_zone_inventory, exclude_parking=exclude_parking, sorted_by=sorted_by)
        print("The response of EventPositionsApi->event_positions_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventPositionsApi->event_positions_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **section** | **str**| Section search filter | [optional] 
 **row** | **str**| Row search filter | [optional] 
 **listed** | **bool**| Whether inventories are listed | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id to search by | [optional] 
 **event** | **str**| Event search term | [optional] 
 **keywords** | [**List[str]**](str.md)| Search Keywords | [optional] 
 **event_date_from** | **datetime**| Minimum event date in yyyy-MM-dd format | [optional] 
 **event_date_to** | **datetime**| Maximum event date in yyyy-MM-dd format | [optional] 
 **event_time_from** | **str**| Only search events starting not earlier than | [optional] 
 **event_time_to** | **str**| Only search events starting not later than | [optional] 
 **day_of_week** | [**List[int]**](int.md)| Day of the week of events that occur on that day of the week | [optional] 
 **event_type** | **str**| Event Type search filter | [optional] 
 **category_id** | **int**| Category Id search filter | [optional] 
 **category** | **str**| Category search filter | [optional] 
 **venue_id** | **int**| Venue Id search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **performer_id** | **int**| Performer Id filter | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **inventory_tags_match_all** | **bool**| Whether the results should have all inventory tags or only some | [optional] 
 **no_tags** | **bool**| Inventory tags to exclude | [optional] 
 **exclude_only_zone_inventory** | **bool**| Whether to exclude events with all zoned inventories | [optional] 
 **exclude_parking** | **bool**| Whether parking events are excluded | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[EventPosition]**](EventPosition.md)

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

