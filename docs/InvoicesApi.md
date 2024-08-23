# skybox_openapi_client.InvoicesApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_bulk_remove_tags**](InvoicesApi.md#invoices_bulk_remove_tags) | **POST** /invoices/tags/remove | 
[**invoices_delete**](InvoicesApi.md#invoices_delete) | **POST** /invoices/{invoice-id}/tags/actions/delete | 
[**invoices_delete_invoice_line**](InvoicesApi.md#invoices_delete_invoice_line) | **DELETE** /invoices/{invoice-id}/lines/{line-id} | 
[**invoices_get_assets**](InvoicesApi.md#invoices_get_assets) | **GET** /invoices/{invoice-id}/assets | 
[**invoices_get_invoice_by_id**](InvoicesApi.md#invoices_get_invoice_by_id) | **GET** /invoices/{invoice-id} | 
[**invoices_get_invoice_line**](InvoicesApi.md#invoices_get_invoice_line) | **GET** /invoices/{invoice-id}/lines/{line-id} | 
[**invoices_get_invoice_line_tickets**](InvoicesApi.md#invoices_get_invoice_line_tickets) | **GET** /invoices/{invoice-id}/lines/{line-id}/tickets | 
[**invoices_get_invoice_lines**](InvoicesApi.md#invoices_get_invoice_lines) | **GET** /invoices/{invoice-id}/lines | 
[**invoices_get_invoice_tickets_by_external_ref_v2**](InvoicesApi.md#invoices_get_invoice_tickets_by_external_ref_v2) | **GET** /invoices/external-ref | 
[**invoices_get_transaction_history**](InvoicesApi.md#invoices_get_transaction_history) | **GET** /invoices/{invoice-id}/transactions | 
[**invoices_insert_invoice**](InvoicesApi.md#invoices_insert_invoice) | **POST** /invoices | 
[**invoices_insert_invoice_line**](InvoicesApi.md#invoices_insert_invoice_line) | **POST** /invoices/{invoice-id}/lines | 
[**invoices_print**](InvoicesApi.md#invoices_print) | **GET** /invoices/{invoice-id}/print | 
[**invoices_print_custom_auth_form**](InvoicesApi.md#invoices_print_custom_auth_form) | **GET** /invoices/{invoice-id}/print-auth-form | 
[**invoices_process_payment**](InvoicesApi.md#invoices_process_payment) | **POST** /invoices/{invoice-id}/payment | 
[**invoices_process_refund**](InvoicesApi.md#invoices_process_refund) | **POST** /invoices/{invoice-id}/transactions/{transaction-id}/refund | 
[**invoices_remove_tag**](InvoicesApi.md#invoices_remove_tag) | **DELETE** /invoices/{invoice-id}/tags/{tag} | 
[**invoices_search**](InvoicesApi.md#invoices_search) | **GET** /invoices | 
[**invoices_send**](InvoicesApi.md#invoices_send) | **GET** /invoices/{invoice-id}/send | 
[**invoices_tag**](InvoicesApi.md#invoices_tag) | **POST** /invoices/{invoice-id}/tags | 
[**invoices_update**](InvoicesApi.md#invoices_update) | **PUT** /invoices/bulk | 
[**invoices_update_currency**](InvoicesApi.md#invoices_update_currency) | **PUT** /invoices/actions/update-invoice-currency | 
[**invoices_update_invoice**](InvoicesApi.md#invoices_update_invoice) | **PUT** /invoices/{invoice-id} | 
[**invoices_update_invoice_line**](InvoicesApi.md#invoices_update_invoice_line) | **PUT** /invoices/{invoice-id}/lines/{line-id} | 


# **invoices_bulk_remove_tags**
> invoices_bulk_remove_tags(request_body)



Deletes all tags from invoices with given ids

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    request_body = [56] # List[int] | Invoice Ids

    try:
        api_instance.invoices_bulk_remove_tags(request_body)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_bulk_remove_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| Invoice Ids | 

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

# **invoices_delete**
> invoices_delete(invoice_id, tag_request)



Deletes tags for an invoice

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The invoice Id
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to be removed from the invoice

    try:
        api_instance.invoices_delete(invoice_id, tag_request)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The invoice Id | 
 **tag_request** | [**List[TagRequest]**](TagRequest.md)| Tags to be removed from the invoice | 

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

# **invoices_delete_invoice_line**
> invoices_delete_invoice_line(invoice_id, line_id)



Deletes an invoice line. Tickets are returned back to the inventory pool.

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    line_id = 56 # int | The line id of the invoice

    try:
        api_instance.invoices_delete_invoice_line(invoice_id, line_id)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_delete_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **line_id** | **int**| The line id of the invoice | 

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
**200** | invoice line deleted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_assets**
> str invoices_get_assets(invoice_id)



Gets invoice assets

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice

    try:
        api_response = api_instance.invoices_get_assets(invoice_id)
        print("The response of InvoicesApi->invoices_get_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 

### Return type

**str**

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoice lines returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |
**404** | no pdf files for invoice tickets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice_by_id**
> Invoice invoices_get_invoice_by_id(invoice_id)



Retrieves an invoice by the invoice id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.invoice import Invoice
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice

    try:
        api_response = api_instance.invoices_get_invoice_by_id(invoice_id)
        print("The response of InvoicesApi->invoices_get_invoice_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoice returned |  -  |
**401** | not authorized |  -  |
**404** | invoice not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice_line**
> Line invoices_get_invoice_line(invoice_id, line_id)



Gets an invoice line

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    line_id = 56 # int | The line id of the invoice

    try:
        api_response = api_instance.invoices_get_invoice_line(invoice_id, line_id)
        print("The response of InvoicesApi->invoices_get_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **line_id** | **int**| The line id of the invoice | 

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
**200** | invoice line returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice_line_tickets**
> Ticket invoices_get_invoice_line_tickets(invoice_id, line_id)



Get tickets for inventory

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    line_id = 56 # int | The line id of the invoice

    try:
        api_response = api_instance.invoices_get_invoice_line_tickets(invoice_id, line_id)
        print("The response of InvoicesApi->invoices_get_invoice_line_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoice_line_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **line_id** | **int**| The line id of the invoice | 

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

# **invoices_get_invoice_lines**
> List[Line] invoices_get_invoice_lines(invoice_id)



Gets invoice lines

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice

    try:
        api_response = api_instance.invoices_get_invoice_lines(invoice_id)
        print("The response of InvoicesApi->invoices_get_invoice_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoice_lines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 

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
**200** | invoice lines returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_invoice_tickets_by_external_ref_v2**
> List[InvoiceTicket] invoices_get_invoice_tickets_by_external_ref_v2(external_ref)



Returns tickets on an invoice by external ref

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.invoice_ticket import InvoiceTicket
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    external_ref = 'external_ref_example' # str | The external ref of the invoice

    try:
        api_response = api_instance.invoices_get_invoice_tickets_by_external_ref_v2(external_ref)
        print("The response of InvoicesApi->invoices_get_invoice_tickets_by_external_ref_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_invoice_tickets_by_external_ref_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_ref** | **str**| The external ref of the invoice | 

### Return type

[**List[InvoiceTicket]**](InvoiceTicket.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoice tickets returned |  -  |
**401** | not authorized |  -  |
**404** | invoice tickets not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_transaction_history**
> invoices_get_transaction_history(invoice_id)



List all transactions appearing on an invoice

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice

    try:
        api_instance.invoices_get_transaction_history(invoice_id)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get_transaction_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_insert_invoice**
> Invoice invoices_insert_invoice(invoice, force=force)



Creates an invoice. The minimum fields required for creating an invoices are customerId, lines, line.amount, line.itemIds, line.lineItemType.

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.invoice import Invoice
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice = skybox_openapi_client.Invoice() # Invoice | An invoice object to create.
    force = True # bool | Whether is forced to invoice held inventory (optional)

    try:
        api_response = api_instance.invoices_insert_invoice(invoice, force=force)
        print("The response of InvoicesApi->invoices_insert_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_insert_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**Invoice**](Invoice.md)| An invoice object to create. | 
 **force** | **bool**| Whether is forced to invoice held inventory | [optional] 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoice created |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_insert_invoice_line**
> Line invoices_insert_invoice_line(invoice_id, line)



Adds an invoice line

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    line = skybox_openapi_client.Line() # Line | An invoice object to update.

    try:
        api_response = api_instance.invoices_insert_invoice_line(invoice_id, line)
        print("The response of InvoicesApi->invoices_insert_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_insert_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **line** | [**Line**](Line.md)| An invoice object to update. | 

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
**200** | invoice line updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_print**
> invoices_print(invoice_id, time_zone_offset=time_zone_offset)



Prints an Invoice

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    time_zone_offset = 56 # int | Time zone off set (optional)

    try:
        api_instance.invoices_print(invoice_id, time_zone_offset=time_zone_offset)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_print: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
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
**200** | Invoice sent |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_print_custom_auth_form**
> invoices_print_custom_auth_form(invoice_id, time_zone_offset=time_zone_offset)



Prints an Invoice Custom Auth Form

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    time_zone_offset = 56 # int | Time zone off set (optional)

    try:
        api_instance.invoices_print_custom_auth_form(invoice_id, time_zone_offset=time_zone_offset)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_print_custom_auth_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
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
**200** | Invoice custom auth form printed |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_process_payment**
> invoices_process_payment(invoice_id, payment)



Process a payment for a invoice

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.payment import Payment
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    payment = skybox_openapi_client.Payment() # Payment | Payment object

    try:
        api_instance.invoices_process_payment(invoice_id, payment)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_process_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **payment** | [**Payment**](Payment.md)| Payment object | 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_process_refund**
> invoices_process_refund(invoice_id, transaction_id, refund_request)



Refunds a payment to the card used

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.refund_request import RefundRequest
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    transaction_id = 56 # int | The transaction id
    refund_request = skybox_openapi_client.RefundRequest() # RefundRequest | Refund object

    try:
        api_instance.invoices_process_refund(invoice_id, transaction_id, refund_request)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_process_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **transaction_id** | **int**| The transaction id | 
 **refund_request** | [**RefundRequest**](RefundRequest.md)| Refund object | 

### Return type

void (empty response body)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_remove_tag**
> invoices_remove_tag(invoice_id, tag)



Deletes a tag for an invoice

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The invoice Id
    tag = 'tag_example' # str | Tag to be removed from the invoice

    try:
        api_instance.invoices_remove_tag(invoice_id, tag)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_remove_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The invoice Id | 
 **tag** | **str**| Tag to be removed from the invoice | 

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

# **invoices_search**
> List[InvoiceSummary] invoices_search(limit=limit, sort_dir=sort_dir, page_number=page_number, delivery_method=delivery_method, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, display_name=display_name, vendor_id=vendor_id, id=id, created_date_from=created_date_from, created_date_to=created_date_to, last_update_from=last_update_from, last_update_to=last_update_to, external_ref=external_ref, payment_status=payment_status, payment_date_from=payment_date_from, payment_date_to=payment_date_to, invoice_status=invoice_status, fulfillment_status=fulfillment_status, fulfillment_date_from=fulfillment_date_from, fulfillment_date_to=fulfillment_date_to, payment_ref=payment_ref, barcodes_entered=barcodes_entered, files_uploaded=files_uploaded, zone_seating=zone_seating, performer_id=performer_id, performer=performer, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, event_date_from=event_date_from, event_date_to=event_date_to, customer_id=customer_id, event_type=event_type, category_id=category_id, created_by=created_by, created_by_user_id=created_by_user_id, no_tags=no_tags, currency_code=currency_code, event_id=event_id, internal_id=internal_id, purchase_id=purchase_id, purchase_line_id=purchase_line_id, sorted_by=sorted_by, include_transaction_info=include_transaction_info, received=received, venue_id=venue_id, venue=venue, stock_type=stock_type, min_total=min_total, max_total=max_total, min_outstanding_balance=min_outstanding_balance, max_outstanding_balance=max_outstanding_balance, invoice_notes_user_id=invoice_notes_user_id)



Searches invoices

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.invoice_summary import InvoiceSummary
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    delivery_method = ['delivery_method_example'] # List[str] | Delivery method search filter (optional)
    tag = ['tag_example'] # List[str] | Tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | Tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    display_name = 'display_name_example' # str | Customer display name search filter (optional)
    vendor_id = [56] # List[int] | Vendor Id search filter (optional)
    id = [56] # List[int] | Invoice Id search filter (optional)
    created_date_from = '2013-10-20T19:20:30+01:00' # datetime | Invoice creation date from range filter (optional)
    created_date_to = '2013-10-20T19:20:30+01:00' # datetime | Invoice creation date to range filter (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | Invoice last update date from range filter (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | Invoice last update date to range filter (optional)
    external_ref = ['external_ref_example'] # List[str] | External reference search filter (optional)
    payment_status = ['payment_status_example'] # List[str] | Payment status search filter (optional)
    payment_date_from = '2013-10-20T19:20:30+01:00' # datetime | Invoice payment date from range filter (optional)
    payment_date_to = '2013-10-20T19:20:30+01:00' # datetime | Invoice payment date to range filter (optional)
    invoice_status = ['invoice_status_example'] # List[str] | Invoice status search filter (optional)
    fulfillment_status = 'fulfillment_status_example' # str | Fulfillment status search filter (optional)
    fulfillment_date_from = '2013-10-20T19:20:30+01:00' # datetime | Invoice fulfillment date from range filter (optional)
    fulfillment_date_to = '2013-10-20T19:20:30+01:00' # datetime | Invoice fulfillment date to range filter (optional)
    payment_ref = 'payment_ref_example' # str | Payment reference search filter (optional)
    barcodes_entered = True # bool | Whether the results should have Bar Codes entered in all tickets (optional)
    files_uploaded = True # bool | Whether the results should have Pdfs attached to all tickets (optional)
    zone_seating = True # bool | Whether the results should have zone seating (optional)
    performer_id = 56 # int | Performer Id search filter (optional)
    performer = 'performer_example' # str | Performer search filter (optional)
    in_hand_date_from = '2013-10-20T19:20:30+01:00' # datetime | In hand date from range filter (optional)
    in_hand_date_to = '2013-10-20T19:20:30+01:00' # datetime | In hand date to range filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Event date from range filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Event date to range filter (optional)
    customer_id = 56 # int | Customer Id search filter (optional)
    event_type = 'event_type_example' # str | Event Type search filter (optional)
    category_id = 56 # int | Category Id search filter (optional)
    created_by = 'created_by_example' # str | Email search filter for invoice creator (optional)
    created_by_user_id = 56 # int | Id search filter for invoice creator (optional)
    no_tags = True # bool | Whether the results should have tags (optional)
    currency_code = 'currency_code_example' # str | Currency type search filter (optional)
    event_id = [56] # List[int] | Event Id search filter (optional)
    internal_id = 56 # int | Internal Id search filter (optional)
    purchase_id = 56 # int | Purchase Id search filter (optional)
    purchase_line_id = 56 # int | Purchase line Id search filter (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)
    include_transaction_info = True # bool | Whether the results include transaction info (optional)
    received = 'received_example' # str | Whether the results are received (optional)
    venue_id = 56 # int | Venue id search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    stock_type = 'stock_type_example' # str | Stock Type search filter (optional)
    min_total = 3.4 # float | Minimum total search filter (optional)
    max_total = 3.4 # float | Maximum total search filter (optional)
    min_outstanding_balance = 3.4 # float | Minimum outstanding balance (optional)
    max_outstanding_balance = 3.4 # float | Maximum outstanding balance (optional)
    invoice_notes_user_id = 56 # int | User id that added the last invoice note search filter (optional)

    try:
        api_response = api_instance.invoices_search(limit=limit, sort_dir=sort_dir, page_number=page_number, delivery_method=delivery_method, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, display_name=display_name, vendor_id=vendor_id, id=id, created_date_from=created_date_from, created_date_to=created_date_to, last_update_from=last_update_from, last_update_to=last_update_to, external_ref=external_ref, payment_status=payment_status, payment_date_from=payment_date_from, payment_date_to=payment_date_to, invoice_status=invoice_status, fulfillment_status=fulfillment_status, fulfillment_date_from=fulfillment_date_from, fulfillment_date_to=fulfillment_date_to, payment_ref=payment_ref, barcodes_entered=barcodes_entered, files_uploaded=files_uploaded, zone_seating=zone_seating, performer_id=performer_id, performer=performer, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, event_date_from=event_date_from, event_date_to=event_date_to, customer_id=customer_id, event_type=event_type, category_id=category_id, created_by=created_by, created_by_user_id=created_by_user_id, no_tags=no_tags, currency_code=currency_code, event_id=event_id, internal_id=internal_id, purchase_id=purchase_id, purchase_line_id=purchase_line_id, sorted_by=sorted_by, include_transaction_info=include_transaction_info, received=received, venue_id=venue_id, venue=venue, stock_type=stock_type, min_total=min_total, max_total=max_total, min_outstanding_balance=min_outstanding_balance, max_outstanding_balance=max_outstanding_balance, invoice_notes_user_id=invoice_notes_user_id)
        print("The response of InvoicesApi->invoices_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **delivery_method** | [**List[str]**](str.md)| Delivery method search filter | [optional] 
 **tag** | [**List[str]**](str.md)| Tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| Tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **display_name** | **str**| Customer display name search filter | [optional] 
 **vendor_id** | [**List[int]**](int.md)| Vendor Id search filter | [optional] 
 **id** | [**List[int]**](int.md)| Invoice Id search filter | [optional] 
 **created_date_from** | **datetime**| Invoice creation date from range filter | [optional] 
 **created_date_to** | **datetime**| Invoice creation date to range filter | [optional] 
 **last_update_from** | **datetime**| Invoice last update date from range filter | [optional] 
 **last_update_to** | **datetime**| Invoice last update date to range filter | [optional] 
 **external_ref** | [**List[str]**](str.md)| External reference search filter | [optional] 
 **payment_status** | [**List[str]**](str.md)| Payment status search filter | [optional] 
 **payment_date_from** | **datetime**| Invoice payment date from range filter | [optional] 
 **payment_date_to** | **datetime**| Invoice payment date to range filter | [optional] 
 **invoice_status** | [**List[str]**](str.md)| Invoice status search filter | [optional] 
 **fulfillment_status** | **str**| Fulfillment status search filter | [optional] 
 **fulfillment_date_from** | **datetime**| Invoice fulfillment date from range filter | [optional] 
 **fulfillment_date_to** | **datetime**| Invoice fulfillment date to range filter | [optional] 
 **payment_ref** | **str**| Payment reference search filter | [optional] 
 **barcodes_entered** | **bool**| Whether the results should have Bar Codes entered in all tickets | [optional] 
 **files_uploaded** | **bool**| Whether the results should have Pdfs attached to all tickets | [optional] 
 **zone_seating** | **bool**| Whether the results should have zone seating | [optional] 
 **performer_id** | **int**| Performer Id search filter | [optional] 
 **performer** | **str**| Performer search filter | [optional] 
 **in_hand_date_from** | **datetime**| In hand date from range filter | [optional] 
 **in_hand_date_to** | **datetime**| In hand date to range filter | [optional] 
 **event_date_from** | **datetime**| Event date from range filter | [optional] 
 **event_date_to** | **datetime**| Event date to range filter | [optional] 
 **customer_id** | **int**| Customer Id search filter | [optional] 
 **event_type** | **str**| Event Type search filter | [optional] 
 **category_id** | **int**| Category Id search filter | [optional] 
 **created_by** | **str**| Email search filter for invoice creator | [optional] 
 **created_by_user_id** | **int**| Id search filter for invoice creator | [optional] 
 **no_tags** | **bool**| Whether the results should have tags | [optional] 
 **currency_code** | **str**| Currency type search filter | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id search filter | [optional] 
 **internal_id** | **int**| Internal Id search filter | [optional] 
 **purchase_id** | **int**| Purchase Id search filter | [optional] 
 **purchase_line_id** | **int**| Purchase line Id search filter | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 
 **include_transaction_info** | **bool**| Whether the results include transaction info | [optional] 
 **received** | **str**| Whether the results are received | [optional] 
 **venue_id** | **int**| Venue id search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **stock_type** | **str**| Stock Type search filter | [optional] 
 **min_total** | **float**| Minimum total search filter | [optional] 
 **max_total** | **float**| Maximum total search filter | [optional] 
 **min_outstanding_balance** | **float**| Minimum outstanding balance | [optional] 
 **max_outstanding_balance** | **float**| Maximum outstanding balance | [optional] 
 **invoice_notes_user_id** | **int**| User id that added the last invoice note search filter | [optional] 

### Return type

[**List[InvoiceSummary]**](InvoiceSummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoices returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_send**
> invoices_send(invoice_id, email_address, cc_email_address=cc_email_address, bcc_email_address=bcc_email_address, subject=subject, message=message, include_invoice=include_invoice, attach_tickets=attach_tickets, attach_invoice_pdf=attach_invoice_pdf, attach_auth_form=attach_auth_form, time_zone_offset=time_zone_offset)



Sends an Invoice to the customer's email address

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | Id of the invoice
    email_address = ['email_address_example'] # List[str] | The customer's email addresses in the To email field
    cc_email_address = ['cc_email_address_example'] # List[str] | The customer's email addresses in the Cc email field (optional)
    bcc_email_address = ['bcc_email_address_example'] # List[str] | The customer's email addresses in the Bcc email field (optional)
    subject = 'subject_example' # str | Subject of the email (optional)
    message = 'message_example' # str | Message of the email (optional)
    include_invoice = True # bool | Whether the email includes the invoice in the body (optional)
    attach_tickets = True # bool | Whether the email includes tickets attached (optional)
    attach_invoice_pdf = True # bool | Whether the email includes the invoice PDF attached (optional)
    attach_auth_form = True # bool | Whether the email includes the auth form PDF attached (optional)
    time_zone_offset = 56 # int | Time zone off set (optional)

    try:
        api_instance.invoices_send(invoice_id, email_address, cc_email_address=cc_email_address, bcc_email_address=bcc_email_address, subject=subject, message=message, include_invoice=include_invoice, attach_tickets=attach_tickets, attach_invoice_pdf=attach_invoice_pdf, attach_auth_form=attach_auth_form, time_zone_offset=time_zone_offset)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| Id of the invoice | 
 **email_address** | [**List[str]**](str.md)| The customer&#39;s email addresses in the To email field | 
 **cc_email_address** | [**List[str]**](str.md)| The customer&#39;s email addresses in the Cc email field | [optional] 
 **bcc_email_address** | [**List[str]**](str.md)| The customer&#39;s email addresses in the Bcc email field | [optional] 
 **subject** | **str**| Subject of the email | [optional] 
 **message** | **str**| Message of the email | [optional] 
 **include_invoice** | **bool**| Whether the email includes the invoice in the body | [optional] 
 **attach_tickets** | **bool**| Whether the email includes tickets attached | [optional] 
 **attach_invoice_pdf** | **bool**| Whether the email includes the invoice PDF attached | [optional] 
 **attach_auth_form** | **bool**| Whether the email includes the auth form PDF attached | [optional] 
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
**200** | Invoice sent |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_tag**
> invoices_tag(invoice_id, tag_request)



Inserts a new tags for an invoice. Duplicates are ignored

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to add

    try:
        api_instance.invoices_tag(invoice_id, tag_request)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
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

# **invoices_update**
> invoices_update(bulk_invoice_update)



Bulk Invoice Update

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.bulk_invoice_update import BulkInvoiceUpdate
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    bulk_invoice_update = skybox_openapi_client.BulkInvoiceUpdate() # BulkInvoiceUpdate | Bulk invoice update

    try:
        api_instance.invoices_update(bulk_invoice_update)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_invoice_update** | [**BulkInvoiceUpdate**](BulkInvoiceUpdate.md)| Bulk invoice update | 

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
**200** | Invoices Updated |  -  |
**401** | not authorized |  -  |
**400** | Invalid fields (See Json response in javax.validation.Validator format) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_update_currency**
> invoices_update_currency(invoice_currency_update_bulk_action)



Converts invoice currency using an exchange rate

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.invoice_currency_update_bulk_action import InvoiceCurrencyUpdateBulkAction
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_currency_update_bulk_action = skybox_openapi_client.InvoiceCurrencyUpdateBulkAction() # InvoiceCurrencyUpdateBulkAction | Payload for bulk action

    try:
        api_instance.invoices_update_currency(invoice_currency_update_bulk_action)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_update_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_currency_update_bulk_action** | [**InvoiceCurrencyUpdateBulkAction**](InvoiceCurrencyUpdateBulkAction.md)| Payload for bulk action | 

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

# **invoices_update_invoice**
> Invoice invoices_update_invoice(invoice_id, invoice)



Updates an invoice

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.invoice import Invoice
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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    invoice = skybox_openapi_client.Invoice() # Invoice | An invoice object to update.

    try:
        api_response = api_instance.invoices_update_invoice(invoice_id, invoice)
        print("The response of InvoicesApi->invoices_update_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_update_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **invoice** | [**Invoice**](Invoice.md)| An invoice object to update. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | invoice updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_update_invoice_line**
> Line invoices_update_invoice_line(invoice_id, line_id, line)



Updates an invoice line. Only quantity, amount, and description can be updated.

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
    api_instance = skybox_openapi_client.InvoicesApi(api_client)
    invoice_id = 56 # int | The id of the invoice
    line_id = 56 # int | The line id of the invoice
    line = skybox_openapi_client.Line() # Line | An invoice object to update.

    try:
        api_response = api_instance.invoices_update_invoice_line(invoice_id, line_id, line)
        print("The response of InvoicesApi->invoices_update_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_update_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**| The id of the invoice | 
 **line_id** | **int**| The line id of the invoice | 
 **line** | [**Line**](Line.md)| An invoice object to update. | 

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
**200** | invoice line updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |
**404** | invoice line not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

