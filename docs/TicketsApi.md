# skybox_openapi_client.TicketsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tickets_get_by_id**](TicketsApi.md#tickets_get_by_id) | **GET** /tickets/{ticket-id} | 
[**tickets_search**](TicketsApi.md#tickets_search) | **GET** /tickets | 


# **tickets_get_by_id**
> Ticket tickets_get_by_id(ticket_id)



Retrieves a ticket by id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.ticket import Ticket
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
    api_instance = skybox_openapi_client.TicketsApi(api_client)
    ticket_id = 56 # int | The ticket id

    try:
        api_response = api_instance.tickets_get_by_id(ticket_id)
        print("The response of TicketsApi->tickets_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketsApi->tickets_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **int**| The ticket id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticket returned |  -  |
**401** | not authorized |  -  |
**404** | ticket not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickets_search**
> Ticket tickets_search(barcode=barcode, last_update_from=last_update_from, last_update_to=last_update_to, event_id=event_id, section=section, row=row, seat_number=seat_number, ticket_ids=ticket_ids)



Searches a ticket with the given barcode

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.ticket import Ticket
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
    api_instance = skybox_openapi_client.TicketsApi(api_client)
    barcode = 'barcode_example' # str | Ticket barcode to look for (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | Ticket last update date from range filter (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | Ticket last update date to range filter (optional)
    event_id = [56] # List[int] |  (optional)
    section = 'section_example' # str |  (optional)
    row = ['row_example'] # List[str] |  (optional)
    seat_number = [56] # List[int] |  (optional)
    ticket_ids = [56] # List[int] | Ticket ids search filter (optional)

    try:
        api_response = api_instance.tickets_search(barcode=barcode, last_update_from=last_update_from, last_update_to=last_update_to, event_id=event_id, section=section, row=row, seat_number=seat_number, ticket_ids=ticket_ids)
        print("The response of TicketsApi->tickets_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketsApi->tickets_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**| Ticket barcode to look for | [optional] 
 **last_update_from** | **datetime**| Ticket last update date from range filter | [optional] 
 **last_update_to** | **datetime**| Ticket last update date to range filter | [optional] 
 **event_id** | [**List[int]**](int.md)|  | [optional] 
 **section** | **str**|  | [optional] 
 **row** | [**List[str]**](str.md)|  | [optional] 
 **seat_number** | [**List[int]**](int.md)|  | [optional] 
 **ticket_ids** | [**List[int]**](int.md)| Ticket ids search filter | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tickets returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

