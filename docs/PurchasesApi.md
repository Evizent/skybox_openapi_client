# skybox_openapi_client.PurchasesApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchases_add_purchase_note**](PurchasesApi.md#purchases_add_purchase_note) | **POST** /purchases/{purchase-id}/notes | 
[**purchases_bulk_cancel_lines**](PurchasesApi.md#purchases_bulk_cancel_lines) | **POST** /purchases/actions/cancel-lines | 
[**purchases_bulk_remove_tags**](PurchasesApi.md#purchases_bulk_remove_tags) | **POST** /purchases/tags/remove | 
[**purchases_cancel_purchase_line**](PurchasesApi.md#purchases_cancel_purchase_line) | **PUT** /purchases/{purchase-id}/lines/{line-id}/cancel | 
[**purchases_delete**](PurchasesApi.md#purchases_delete) | **POST** /purchases/{purchase-id}/tags/actions/delete | 
[**purchases_get_airbill**](PurchasesApi.md#purchases_get_airbill) | **GET** /purchases/{purchase-id}/airbill | 
[**purchases_get_purchase_by_id**](PurchasesApi.md#purchases_get_purchase_by_id) | **GET** /purchases/{purchase-id} | 
[**purchases_get_purchase_line**](PurchasesApi.md#purchases_get_purchase_line) | **GET** /purchases/{purchase-id}/lines/{line-id} | 
[**purchases_get_purchase_line_tickets**](PurchasesApi.md#purchases_get_purchase_line_tickets) | **GET** /purchases/{purchase-id}/lines/{line-id}/tickets | 
[**purchases_get_purchase_lines**](PurchasesApi.md#purchases_get_purchase_lines) | **GET** /purchases/{purchase-id}/lines | 
[**purchases_insert_purchase**](PurchasesApi.md#purchases_insert_purchase) | **POST** /purchases | 
[**purchases_insert_purchase_line**](PurchasesApi.md#purchases_insert_purchase_line) | **POST** /purchases/{purchase-id}/lines | 
[**purchases_multi_with_purchase_id**](PurchasesApi.md#purchases_multi_with_purchase_id) | **POST** /purchases/{purchase-id}/inventory | 
[**purchases_print**](PurchasesApi.md#purchases_print) | **GET** /purchases/{purchase-id}/print | 
[**purchases_remove_tag**](PurchasesApi.md#purchases_remove_tag) | **DELETE** /purchases/{purchase-id}/tags/{tag} | 
[**purchases_replace_purchase_line**](PurchasesApi.md#purchases_replace_purchase_line) | **POST** /purchases/{purchase-id}/lines/{line-id}/actions/replace | 
[**purchases_search**](PurchasesApi.md#purchases_search) | **GET** /purchases | 
[**purchases_search_auto_purchases**](PurchasesApi.md#purchases_search_auto_purchases) | **GET** /purchases/auto-purchases | 
[**purchases_send**](PurchasesApi.md#purchases_send) | **GET** /purchases/{purchase-id}/send | 
[**purchases_tag**](PurchasesApi.md#purchases_tag) | **POST** /purchases/{purchase-id}/tags | 
[**purchases_update**](PurchasesApi.md#purchases_update) | **PUT** /purchases/bulk | 
[**purchases_update_currency**](PurchasesApi.md#purchases_update_currency) | **PUT** /purchases/actions/update-purchase-currency | 
[**purchases_update_purchase**](PurchasesApi.md#purchases_update_purchase) | **PUT** /purchases/{purchase-id} | 
[**purchases_update_purchase_inventory**](PurchasesApi.md#purchases_update_purchase_inventory) | **POST** /purchases/{purchase-id}/lines/{line-id}/inventory | 
[**purchases_update_purchase_line**](PurchasesApi.md#purchases_update_purchase_line) | **PUT** /purchases/{purchase-id}/lines/{line-id} | 


# **purchases_add_purchase_note**
> PurchaseNote purchases_add_purchase_note(purchase_id, purchase_note)



Adds a purchase note

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchase_note import PurchaseNote
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    purchase_note = skybox_openapi_client.PurchaseNote() # PurchaseNote | Purchase note object

    try:
        api_response = api_instance.purchases_add_purchase_note(purchase_id, purchase_note)
        print("The response of PurchasesApi->purchases_add_purchase_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_add_purchase_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **purchase_note** | [**PurchaseNote**](PurchaseNote.md)| Purchase note object | 

### Return type

[**PurchaseNote**](PurchaseNote.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | note added is returned |  -  |
**401** | not authorized |  -  |
**404** | purchase not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_bulk_cancel_lines**
> purchases_bulk_cancel_lines(request_body)



Cancels a list of purchase lines

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    request_body = [56] # List[int] | The list of purchase ids to cancel

    try:
        api_instance.purchases_bulk_cancel_lines(request_body)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_bulk_cancel_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| The list of purchase ids to cancel | 

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
**200** | purchase lines cancelled |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_bulk_remove_tags**
> purchases_bulk_remove_tags(request_body)



Deletes all tags from purchases with given ids

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    request_body = [56] # List[int] | Purchase Ids

    try:
        api_instance.purchases_bulk_remove_tags(request_body)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_bulk_remove_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| Purchase Ids | 

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

# **purchases_cancel_purchase_line**
> purchases_cancel_purchase_line(purchase_id, line_id)



Cancels a purchase line

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    line_id = 56 # int | The line id of the purchase

    try:
        api_instance.purchases_cancel_purchase_line(purchase_id, line_id)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_cancel_purchase_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **line_id** | **int**| The line id of the purchase | 

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
**200** | purchase line cancelled |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_delete**
> purchases_delete(purchase_id, tag_request)



Deletes tags for a purchase

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The purchase Id
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to be removed from the purchase

    try:
        api_instance.purchases_delete(purchase_id, tag_request)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The purchase Id | 
 **tag_request** | [**List[TagRequest]**](TagRequest.md)| Tags to be removed from the purchase | 

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

# **purchases_get_airbill**
> PurchaseNote purchases_get_airbill(purchase_id)



Retrieves a purchase's airbill

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchase_note import PurchaseNote
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase

    try:
        api_response = api_instance.purchases_get_airbill(purchase_id)
        print("The response of PurchasesApi->purchases_get_airbill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_get_airbill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 

### Return type

[**PurchaseNote**](PurchaseNote.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | retrieves the purchase&#39;s airbill |  -  |
**401** | not authorized |  -  |
**404** | purchase not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_get_purchase_by_id**
> Purchase purchases_get_purchase_by_id(purchase_id)



Retrieves a purchase by the purchase id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchase import Purchase
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase

    try:
        api_response = api_instance.purchases_get_purchase_by_id(purchase_id)
        print("The response of PurchasesApi->purchases_get_purchase_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_get_purchase_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 

### Return type

[**Purchase**](Purchase.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchase returned |  -  |
**401** | not authorized |  -  |
**404** | purchase not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_get_purchase_line**
> Line purchases_get_purchase_line(purchase_id, line_id)



Gets a purchase line

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.line import Line
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    line_id = 56 # int | The line id of the purchase

    try:
        api_response = api_instance.purchases_get_purchase_line(purchase_id, line_id)
        print("The response of PurchasesApi->purchases_get_purchase_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_get_purchase_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **line_id** | **int**| The line id of the purchase | 

### Return type

[**Line**](Line.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchase line returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_get_purchase_line_tickets**
> List[Ticket] purchases_get_purchase_line_tickets(purchase_id, line_id)



Gets the tickets of a purchase line

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    line_id = 56 # int | The line id of the purchase

    try:
        api_response = api_instance.purchases_get_purchase_line_tickets(purchase_id, line_id)
        print("The response of PurchasesApi->purchases_get_purchase_line_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_get_purchase_line_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **line_id** | **int**| The line id of the purchase | 

### Return type

[**List[Ticket]**](Ticket.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tickets of the purchase line returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_get_purchase_lines**
> List[Line] purchases_get_purchase_lines(purchase_id)



Gets purchase lines

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.line import Line
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase

    try:
        api_response = api_instance.purchases_get_purchase_lines(purchase_id)
        print("The response of PurchasesApi->purchases_get_purchase_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_get_purchase_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 

### Return type

[**List[Line]**](Line.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchase lines returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_insert_purchase**
> Purchase purchases_insert_purchase(purchase)



Creates a purchase. The minimum required field to insert a purchase is the vendorId. Inventory purchase lines must include quantity, section, row, cost, lowSeat, highSeat, stockType,  seatType and either an eventId or eventMapping.

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchase import Purchase
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase = {"vendorId":1994249,"lines":[{"quantity":4,"amount":99,"lineType":"PURCHASE","lineItemType":"INVENTORY","inventory":{"eventId":4936321,"quantity":4,"section":"ORCH-L","row":"T","lowSeat":9,"highSeat":12,"cost":99,"faceValue":99,"stockType":"MOBILE_TRANSFER","seatType":"CONSECUTIVE","broadcast":false,"hideSeatNumbers":true,"zoneSeating":false,"filesUploaded":false,"barCodesEntered":false,"instantTransfer":false},"cancelled":false,"delete":false,"cancel":false,"fillLineId":0}]} # Purchase | A purchase object to create.

    try:
        api_response = api_instance.purchases_insert_purchase(purchase)
        print("The response of PurchasesApi->purchases_insert_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_insert_purchase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase** | [**Purchase**](Purchase.md)| A purchase object to create. | 

### Return type

[**Purchase**](Purchase.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchase created |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_insert_purchase_line**
> Line purchases_insert_purchase_line(purchase_id, line)



Adds a purchase line

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.line import Line
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    line = skybox_openapi_client.Line() # Line | The purchase line to add.

    try:
        api_response = api_instance.purchases_insert_purchase_line(purchase_id, line)
        print("The response of PurchasesApi->purchases_insert_purchase_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_insert_purchase_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **line** | [**Line**](Line.md)| The purchase line to add. | 

### Return type

[**Line**](Line.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | line added successfully |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_multi_with_purchase_id**
> List[Inventory] purchases_multi_with_purchase_id(purchase_id, inventory)



Creates inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory import Inventory
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The purchase order id on which to attach the tickets
    inventory = [skybox_openapi_client.Inventory()] # List[Inventory] | Array of inventory objects to create.

    try:
        api_response = api_instance.purchases_multi_with_purchase_id(purchase_id, inventory)
        print("The response of PurchasesApi->purchases_multi_with_purchase_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_multi_with_purchase_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The purchase order id on which to attach the tickets | 
 **inventory** | [**List[Inventory]**](Inventory.md)| Array of inventory objects to create. | 

### Return type

[**List[Inventory]**](Inventory.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory order created |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_print**
> purchases_print(purchase_id, time_zone_offset=time_zone_offset)



Prints a Purchase Order

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    time_zone_offset = 56 # int | Time zone off set (optional)

    try:
        api_instance.purchases_print(purchase_id, time_zone_offset=time_zone_offset)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_print: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **time_zone_offset** | **int**| Time zone off set | [optional] 

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
**200** | Purchase Order sent |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_remove_tag**
> purchases_remove_tag(purchase_id, tag)



Deletes a tag for a purchase

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    tag = 'tag_example' # str | Tag to be removed from the purchase

    try:
        api_instance.purchases_remove_tag(purchase_id, tag)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_remove_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **tag** | **str**| Tag to be removed from the purchase | 

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
**200** | tag deleted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_replace_purchase_line**
> Line purchases_replace_purchase_line(purchase_id, line_id, purchase_line_replace_action)



Replaces a purchase line. Allows changing section, row, low seat and seat type.

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.line import Line
from skybox_openapi_client.models.purchase_line_replace_action import PurchaseLineReplaceAction
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    line_id = 56 # int | The line id of the purchase
    purchase_line_replace_action = skybox_openapi_client.PurchaseLineReplaceAction() # PurchaseLineReplaceAction | 

    try:
        api_response = api_instance.purchases_replace_purchase_line(purchase_id, line_id, purchase_line_replace_action)
        print("The response of PurchasesApi->purchases_replace_purchase_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_replace_purchase_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **line_id** | **int**| The line id of the purchase | 
 **purchase_line_replace_action** | [**PurchaseLineReplaceAction**](PurchaseLineReplaceAction.md)|  | 

### Return type

[**Line**](Line.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchase line replaced |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_search**
> List[PurchaseSummary] purchases_search(limit=limit, sort_dir=sort_dir, page_number=page_number, delivery_method=delivery_method, payment_method=payment_method, vendor_type=vendor_type, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, vendor_tag=vendor_tag, vendor_tags_match_all=vendor_tags_match_all, vendor_id=vendor_id, display_name=display_name, id=id, inventory_id=inventory_id, invoice_line_id=invoice_line_id, credit_card_id=credit_card_id, created_date_from=created_date_from, created_date_to=created_date_to, last_update_from=last_update_from, last_update_to=last_update_to, external_ref=external_ref, simplified_external_ref=simplified_external_ref, payment_status=payment_status, purchase_status=purchase_status, min_cost=min_cost, max_cost=max_cost, currency_code=currency_code, internal_id=internal_id, sorted_by=sorted_by, include_has_zone_seating_inventory=include_has_zone_seating_inventory, zero_outstanding_balance=zero_outstanding_balance, min_outstanding_balance=min_outstanding_balance, max_outstanding_balance=max_outstanding_balance, consignment=consignment, event_id=event_id, event_name=event_name, cooperative=cooperative, created_by=created_by, created_by_user_id=created_by_user_id, last_purchase_payment_note=last_purchase_payment_note, vendor_tags=vendor_tags)



Searches purchases

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchase_summary import PurchaseSummary
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    delivery_method = ['delivery_method_example'] # List[str] | Delivery method search filter (optional)
    payment_method = ['payment_method_example'] # List[str] | Payment method search filter (optional)
    vendor_type = ['vendor_type_example'] # List[str] | Vendor type search filter (optional)
    tag = ['tag_example'] # List[str] | Tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | Tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    vendor_tag = ['vendor_tag_example'] # List[str] |  (optional)
    vendor_tags_match_all = True # bool |  (optional)
    vendor_id = 56 # int | Vendor Id search filter (optional)
    display_name = 'display_name_example' # str | Vendor display name search filter (optional)
    id = [56] # List[int] | Purchase Id search filter (optional)
    inventory_id = 56 # int | Inventory Id search filter (optional)
    invoice_line_id = 56 # int | Invoice line Id search filter (optional)
    credit_card_id = 56 # int | Invoice line Id search filter (optional)
    created_date_from = '2013-10-20T19:20:30+01:00' # datetime | Purchase creation date from range filter (optional)
    created_date_to = '2013-10-20T19:20:30+01:00' # datetime | Purchase creation date to range filter (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | Purchase last update date from range filter (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | Purchase last update date to range filter (optional)
    external_ref = 'external_ref_example' # str | External reference search filter (optional)
    simplified_external_ref = ['simplified_external_ref_example'] # List[str] | Simplified external reference (ignoring dashes, slashes or spaces) search filter (optional)
    payment_status = ['payment_status_example'] # List[str] | Payment status search filter (optional)
    purchase_status = ['purchase_status_example'] # List[str] | Purchase status search filter (optional)
    min_cost = 3.4 # float | Minimum cost search filter (optional)
    max_cost = 3.4 # float | Maximum cost search filter (optional)
    currency_code = 'currency_code_example' # str | Currency type search filter (optional)
    internal_id = 56 # int | Internal Id search filter (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)
    include_has_zone_seating_inventory = True # bool | Whether the results should include inventory zone seating (optional)
    zero_outstanding_balance = True # bool | Whether the results should have zero outstanding balance (optional)
    min_outstanding_balance = 3.4 # float | Minimum outstanding balance search filter (optional)
    max_outstanding_balance = 3.4 # float | Maximum outstanding balance search filter (optional)
    consignment = 'consignment_example' # str | Whether the results have a consignment type POs (optional)
    event_id = [56] # List[int] | Event Id search filter (optional)
    event_name = 'event_name_example' # str | Event Name search filter (optional)
    cooperative = True # bool | Whether the results have cooperative POs (optional)
    created_by = 'created_by_example' # str | User email for purchase creator (optional)
    created_by_user_id = 56 # int | User id for purchase creator (optional)
    last_purchase_payment_note = 'last_purchase_payment_note_example' # str | Last purchase payment note search filter (optional)
    vendor_tags = ['vendor_tags_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.purchases_search(limit=limit, sort_dir=sort_dir, page_number=page_number, delivery_method=delivery_method, payment_method=payment_method, vendor_type=vendor_type, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, vendor_tag=vendor_tag, vendor_tags_match_all=vendor_tags_match_all, vendor_id=vendor_id, display_name=display_name, id=id, inventory_id=inventory_id, invoice_line_id=invoice_line_id, credit_card_id=credit_card_id, created_date_from=created_date_from, created_date_to=created_date_to, last_update_from=last_update_from, last_update_to=last_update_to, external_ref=external_ref, simplified_external_ref=simplified_external_ref, payment_status=payment_status, purchase_status=purchase_status, min_cost=min_cost, max_cost=max_cost, currency_code=currency_code, internal_id=internal_id, sorted_by=sorted_by, include_has_zone_seating_inventory=include_has_zone_seating_inventory, zero_outstanding_balance=zero_outstanding_balance, min_outstanding_balance=min_outstanding_balance, max_outstanding_balance=max_outstanding_balance, consignment=consignment, event_id=event_id, event_name=event_name, cooperative=cooperative, created_by=created_by, created_by_user_id=created_by_user_id, last_purchase_payment_note=last_purchase_payment_note, vendor_tags=vendor_tags)
        print("The response of PurchasesApi->purchases_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **delivery_method** | [**List[str]**](str.md)| Delivery method search filter | [optional] 
 **payment_method** | [**List[str]**](str.md)| Payment method search filter | [optional] 
 **vendor_type** | [**List[str]**](str.md)| Vendor type search filter | [optional] 
 **tag** | [**List[str]**](str.md)| Tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| Tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **vendor_tag** | [**List[str]**](str.md)|  | [optional] 
 **vendor_tags_match_all** | **bool**|  | [optional] 
 **vendor_id** | **int**| Vendor Id search filter | [optional] 
 **display_name** | **str**| Vendor display name search filter | [optional] 
 **id** | [**List[int]**](int.md)| Purchase Id search filter | [optional] 
 **inventory_id** | **int**| Inventory Id search filter | [optional] 
 **invoice_line_id** | **int**| Invoice line Id search filter | [optional] 
 **credit_card_id** | **int**| Invoice line Id search filter | [optional] 
 **created_date_from** | **datetime**| Purchase creation date from range filter | [optional] 
 **created_date_to** | **datetime**| Purchase creation date to range filter | [optional] 
 **last_update_from** | **datetime**| Purchase last update date from range filter | [optional] 
 **last_update_to** | **datetime**| Purchase last update date to range filter | [optional] 
 **external_ref** | **str**| External reference search filter | [optional] 
 **simplified_external_ref** | [**List[str]**](str.md)| Simplified external reference (ignoring dashes, slashes or spaces) search filter | [optional] 
 **payment_status** | [**List[str]**](str.md)| Payment status search filter | [optional] 
 **purchase_status** | [**List[str]**](str.md)| Purchase status search filter | [optional] 
 **min_cost** | **float**| Minimum cost search filter | [optional] 
 **max_cost** | **float**| Maximum cost search filter | [optional] 
 **currency_code** | **str**| Currency type search filter | [optional] 
 **internal_id** | **int**| Internal Id search filter | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 
 **include_has_zone_seating_inventory** | **bool**| Whether the results should include inventory zone seating | [optional] 
 **zero_outstanding_balance** | **bool**| Whether the results should have zero outstanding balance | [optional] 
 **min_outstanding_balance** | **float**| Minimum outstanding balance search filter | [optional] 
 **max_outstanding_balance** | **float**| Maximum outstanding balance search filter | [optional] 
 **consignment** | **str**| Whether the results have a consignment type POs | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id search filter | [optional] 
 **event_name** | **str**| Event Name search filter | [optional] 
 **cooperative** | **bool**| Whether the results have cooperative POs | [optional] 
 **created_by** | **str**| User email for purchase creator | [optional] 
 **created_by_user_id** | **int**| User id for purchase creator | [optional] 
 **last_purchase_payment_note** | **str**| Last purchase payment note search filter | [optional] 
 **vendor_tags** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[PurchaseSummary]**](PurchaseSummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchases returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_search_auto_purchases**
> List[PurchaseSummary] purchases_search_auto_purchases(limit=limit, sort_dir=sort_dir, page_number=page_number, event_id=event_id, purchase_id=purchase_id, user=user, user_id=user_id, external_ref=external_ref, from_purchase_date=from_purchase_date, to_purchase_date=to_purchase_date, event_name=event_name, venue_id=venue_id, venue=venue, ticket_status=ticket_status, sorted_by=sorted_by)



Searches auto purchases

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchase_summary import PurchaseSummary
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    event_id = 56 # int | Event Id search filter (optional)
    purchase_id = 56 # int | Purchase Id search filter (optional)
    user = 'user_example' # str | User email search filter (optional)
    user_id = 56 # int | User id search filter (optional)
    external_ref = 'external_ref_example' # str | External reference search filter (optional)
    from_purchase_date = '2013-10-20T19:20:30+01:00' # datetime | Purchase date from range filter (optional)
    to_purchase_date = '2013-10-20T19:20:30+01:00' # datetime | Purchase date to range filter (optional)
    event_name = 'event_name_example' # str | Event name search filter (optional)
    venue_id = 56 # int | Venue id search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    ticket_status = 'ticket_status_example' # str | Ticket Status search filter (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.purchases_search_auto_purchases(limit=limit, sort_dir=sort_dir, page_number=page_number, event_id=event_id, purchase_id=purchase_id, user=user, user_id=user_id, external_ref=external_ref, from_purchase_date=from_purchase_date, to_purchase_date=to_purchase_date, event_name=event_name, venue_id=venue_id, venue=venue, ticket_status=ticket_status, sorted_by=sorted_by)
        print("The response of PurchasesApi->purchases_search_auto_purchases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_search_auto_purchases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **event_id** | **int**| Event Id search filter | [optional] 
 **purchase_id** | **int**| Purchase Id search filter | [optional] 
 **user** | **str**| User email search filter | [optional] 
 **user_id** | **int**| User id search filter | [optional] 
 **external_ref** | **str**| External reference search filter | [optional] 
 **from_purchase_date** | **datetime**| Purchase date from range filter | [optional] 
 **to_purchase_date** | **datetime**| Purchase date to range filter | [optional] 
 **event_name** | **str**| Event name search filter | [optional] 
 **venue_id** | **int**| Venue id search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **ticket_status** | **str**| Ticket Status search filter | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[PurchaseSummary]**](PurchaseSummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | auto purchases returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_send**
> purchases_send(purchase_id, email_address, cc_email_address=cc_email_address, bcc_email_address=bcc_email_address, subject=subject, message=message, include_airbill=include_airbill, time_zone_offset=time_zone_offset)



Sends a Purchase Order to the vendor's email address

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | Id of the purchase
    email_address = ['email_address_example'] # List[str] | The vendor's email addresses in the To email field
    cc_email_address = ['cc_email_address_example'] # List[str] | The vendor's email addresses in the Cc email field (optional)
    bcc_email_address = ['bcc_email_address_example'] # List[str] | The vendor's email addresses in the Bcc email field (optional)
    subject = 'subject_example' # str | Subject of the email (optional)
    message = 'message_example' # str | Message of the email (optional)
    include_airbill = True # bool | Whether the email includes the airbill PDF attached (optional)
    time_zone_offset = 56 # int | Time zone off set (optional)

    try:
        api_instance.purchases_send(purchase_id, email_address, cc_email_address=cc_email_address, bcc_email_address=bcc_email_address, subject=subject, message=message, include_airbill=include_airbill, time_zone_offset=time_zone_offset)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| Id of the purchase | 
 **email_address** | [**List[str]**](str.md)| The vendor&#39;s email addresses in the To email field | 
 **cc_email_address** | [**List[str]**](str.md)| The vendor&#39;s email addresses in the Cc email field | [optional] 
 **bcc_email_address** | [**List[str]**](str.md)| The vendor&#39;s email addresses in the Bcc email field | [optional] 
 **subject** | **str**| Subject of the email | [optional] 
 **message** | **str**| Message of the email | [optional] 
 **include_airbill** | **bool**| Whether the email includes the airbill PDF attached | [optional] 
 **time_zone_offset** | **int**| Time zone off set | [optional] 

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
**200** | Purchase Order sent |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_tag**
> purchases_tag(purchase_id, tag_request)



Inserts a new tags for a purchase. Duplicates are ignored.

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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to add

    try:
        api_instance.purchases_tag(purchase_id, tag_request)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **tag_request** | [**List[TagRequest]**](TagRequest.md)| Tags to add | 

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

# **purchases_update**
> purchases_update(bulk_purchase_update)



Bulk Purchase Update

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.bulk_purchase_update import BulkPurchaseUpdate
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    bulk_purchase_update = skybox_openapi_client.BulkPurchaseUpdate() # BulkPurchaseUpdate | Bulk purchase update

    try:
        api_instance.purchases_update(bulk_purchase_update)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_purchase_update** | [**BulkPurchaseUpdate**](BulkPurchaseUpdate.md)| Bulk purchase update | 

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
**200** | Updated |  -  |
**401** | not authorized |  -  |
**400** | Invalid fields (See Json response in javax.validation.Validator format) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_update_currency**
> purchases_update_currency(currency_update_bulk_action)



Converts purchases currency using an exchange rate

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.currency_update_bulk_action import CurrencyUpdateBulkAction
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    currency_update_bulk_action = skybox_openapi_client.CurrencyUpdateBulkAction() # CurrencyUpdateBulkAction | Payload for bulk action

    try:
        api_instance.purchases_update_currency(currency_update_bulk_action)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_update_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_update_bulk_action** | [**CurrencyUpdateBulkAction**](CurrencyUpdateBulkAction.md)| Payload for bulk action | 

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
**200** | currency successfully updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_update_purchase**
> Purchase purchases_update_purchase(purchase_id, purchase)



Updates a purchase

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchase import Purchase
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    purchase = skybox_openapi_client.Purchase() # Purchase | A purchase object to update.

    try:
        api_response = api_instance.purchases_update_purchase(purchase_id, purchase)
        print("The response of PurchasesApi->purchases_update_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_update_purchase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **purchase** | [**Purchase**](Purchase.md)| A purchase object to update. | 

### Return type

[**Purchase**](Purchase.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchase updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_update_purchase_inventory**
> purchases_update_purchase_inventory(purchase_id, line_id, update_purchase_inventory_request)



Updates section and row for a purchase line

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.update_purchase_inventory_request import UpdatePurchaseInventoryRequest
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    line_id = 56 # int | The line id of the purchase
    update_purchase_inventory_request = skybox_openapi_client.UpdatePurchaseInventoryRequest() # UpdatePurchaseInventoryRequest | 

    try:
        api_instance.purchases_update_purchase_inventory(purchase_id, line_id, update_purchase_inventory_request)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_update_purchase_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **line_id** | **int**| The line id of the purchase | 
 **update_purchase_inventory_request** | [**UpdatePurchaseInventoryRequest**](UpdatePurchaseInventoryRequest.md)|  | 

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
**200** | update successful |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchases_update_purchase_line**
> Line purchases_update_purchase_line(purchase_id, line_id, line)



Updates a purchase line. Only amount and description can be updated.

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.line import Line
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
    api_instance = skybox_openapi_client.PurchasesApi(api_client)
    purchase_id = 56 # int | The id of the purchase
    line_id = 56 # int | The line id of the purchase
    line = skybox_openapi_client.Line() # Line | A purchase line object to update.

    try:
        api_response = api_instance.purchases_update_purchase_line(purchase_id, line_id, line)
        print("The response of PurchasesApi->purchases_update_purchase_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasesApi->purchases_update_purchase_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_id** | **int**| The id of the purchase | 
 **line_id** | **int**| The line id of the purchase | 
 **line** | [**Line**](Line.md)| A purchase line object to update. | 

### Return type

[**Line**](Line.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchase line updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |
**404** | line not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

