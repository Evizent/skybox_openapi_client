# skybox_openapi_client.QuickReportsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quick_reports_get_purchases**](QuickReportsApi.md#quick_reports_get_purchases) | **GET** /quick-report/purchases | 
[**quick_reports_get_sales**](QuickReportsApi.md#quick_reports_get_sales) | **GET** /quick-report/sales | 


# **quick_reports_get_purchases**
> quick_reports_get_purchases(purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, performer_id=performer_id, category_id=category_id, event=event, venue=venue, event_date_from=event_date_from, event_date_to=event_date_to, payment_status=payment_status, inventory_tag=inventory_tag, inventory_tags_match_all=inventory_tags_match_all, inventory_tags=inventory_tags)



Retrieves the purchases quick report

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
    api_instance = skybox_openapi_client.QuickReportsApi(api_client)
    purchase_date_from = '2013-10-20T19:20:30+01:00' # datetime | Purchase date from range filter (optional)
    purchase_date_to = '2013-10-20T19:20:30+01:00' # datetime | Purchase date to range filter (optional)
    performer_id = 56 # int | Performer Id search filter (optional)
    category_id = [56] # List[int] | Category Id search filter (optional)
    event = 'event_example' # str | Event to filter (optional)
    venue = 'venue_example' # str | Venue filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | From event date filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | To event date filter (optional)
    payment_status = 'payment_status_example' # str | Payment status search filter (optional)
    inventory_tag = ['inventory_tag_example'] # List[str] | Inventory tags to include (optional)
    inventory_tags_match_all = True # bool | Whether the results should have all inventory tags or only some (optional)
    inventory_tags = ['inventory_tags_example'] # List[str] |  (optional)

    try:
        api_instance.quick_reports_get_purchases(purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, performer_id=performer_id, category_id=category_id, event=event, venue=venue, event_date_from=event_date_from, event_date_to=event_date_to, payment_status=payment_status, inventory_tag=inventory_tag, inventory_tags_match_all=inventory_tags_match_all, inventory_tags=inventory_tags)
    except Exception as e:
        print("Exception when calling QuickReportsApi->quick_reports_get_purchases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_date_from** | **datetime**| Purchase date from range filter | [optional] 
 **purchase_date_to** | **datetime**| Purchase date to range filter | [optional] 
 **performer_id** | **int**| Performer Id search filter | [optional] 
 **category_id** | [**List[int]**](int.md)| Category Id search filter | [optional] 
 **event** | **str**| Event to filter | [optional] 
 **venue** | **str**| Venue filter | [optional] 
 **event_date_from** | **datetime**| From event date filter | [optional] 
 **event_date_to** | **datetime**| To event date filter | [optional] 
 **payment_status** | **str**| Payment status search filter | [optional] 
 **inventory_tag** | [**List[str]**](str.md)| Inventory tags to include | [optional] 
 **inventory_tags_match_all** | **bool**| Whether the results should have all inventory tags or only some | [optional] 
 **inventory_tags** | [**List[str]**](str.md)|  | [optional] 

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
**200** | Sales report |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quick_reports_get_sales**
> quick_reports_get_sales(invoice_date_from=invoice_date_from, invoice_date_to=invoice_date_to, performer_id=performer_id, category_id=category_id, event=event, venue=venue, event_date_from=event_date_from, event_date_to=event_date_to, fulfillment_status=fulfillment_status, payment_status=payment_status, inventory_tag=inventory_tag, inventory_tags_match_all=inventory_tags_match_all, inventory_tags=inventory_tags)



Retrieves the sales quick report

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
    api_instance = skybox_openapi_client.QuickReportsApi(api_client)
    invoice_date_from = '2013-10-20T19:20:30+01:00' # datetime | Invoice date from range filter (optional)
    invoice_date_to = '2013-10-20T19:20:30+01:00' # datetime | Invoice date to range filter (optional)
    performer_id = 56 # int | Performer Id search filter (optional)
    category_id = [56] # List[int] | Category Id search filter (optional)
    event = 'event_example' # str | Event to filter (optional)
    venue = 'venue_example' # str | Venue filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | From event date filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | To event date filter (optional)
    fulfillment_status = 'fulfillment_status_example' # str | Fulfillment status search filter (optional)
    payment_status = 'payment_status_example' # str | Payment status search filter (optional)
    inventory_tag = ['inventory_tag_example'] # List[str] | Inventory tags to include (optional)
    inventory_tags_match_all = True # bool | Whether the results should have all inventory tags or only some (optional)
    inventory_tags = ['inventory_tags_example'] # List[str] |  (optional)

    try:
        api_instance.quick_reports_get_sales(invoice_date_from=invoice_date_from, invoice_date_to=invoice_date_to, performer_id=performer_id, category_id=category_id, event=event, venue=venue, event_date_from=event_date_from, event_date_to=event_date_to, fulfillment_status=fulfillment_status, payment_status=payment_status, inventory_tag=inventory_tag, inventory_tags_match_all=inventory_tags_match_all, inventory_tags=inventory_tags)
    except Exception as e:
        print("Exception when calling QuickReportsApi->quick_reports_get_sales: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_date_from** | **datetime**| Invoice date from range filter | [optional] 
 **invoice_date_to** | **datetime**| Invoice date to range filter | [optional] 
 **performer_id** | **int**| Performer Id search filter | [optional] 
 **category_id** | [**List[int]**](int.md)| Category Id search filter | [optional] 
 **event** | **str**| Event to filter | [optional] 
 **venue** | **str**| Venue filter | [optional] 
 **event_date_from** | **datetime**| From event date filter | [optional] 
 **event_date_to** | **datetime**| To event date filter | [optional] 
 **fulfillment_status** | **str**| Fulfillment status search filter | [optional] 
 **payment_status** | **str**| Payment status search filter | [optional] 
 **inventory_tag** | [**List[str]**](str.md)| Inventory tags to include | [optional] 
 **inventory_tags_match_all** | **bool**| Whether the results should have all inventory tags or only some | [optional] 
 **inventory_tags** | [**List[str]**](str.md)|  | [optional] 

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
**200** | Sales report |  -  |
**401** | not authorized |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

