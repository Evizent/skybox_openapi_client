# skybox_openapi_client.InventoryApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_bulk_merge**](InventoryApi.md#inventory_bulk_merge) | **POST** /inventory/bulk-merge | 
[**inventory_bulk_remove_tags**](InventoryApi.md#inventory_bulk_remove_tags) | **POST** /inventory/tags/remove | 
[**inventory_bulk_swap_event**](InventoryApi.md#inventory_bulk_swap_event) | **POST** /inventory/bulk-swap-event | 
[**inventory_bulk_update**](InventoryApi.md#inventory_bulk_update) | **PUT** /inventory/bulk-update | 
[**inventory_bulk_update_expected_value**](InventoryApi.md#inventory_bulk_update_expected_value) | **PUT** /inventory/bulk-update-expected-value | 
[**inventory_bulk_update_face_value**](InventoryApi.md#inventory_bulk_update_face_value) | **PUT** /inventory/bulk-update-face-value | 
[**inventory_bulk_update_price**](InventoryApi.md#inventory_bulk_update_price) | **PUT** /inventory | 
[**inventory_bulk_update_taxed_cost**](InventoryApi.md#inventory_bulk_update_taxed_cost) | **PUT** /inventory/bulk-taxed-cost-value | 
[**inventory_delete**](InventoryApi.md#inventory_delete) | **POST** /inventory/{inventory-id}/tags/actions/delete | 
[**inventory_delete_holds_by_id**](InventoryApi.md#inventory_delete_holds_by_id) | **DELETE** /inventory/{inventory-id}/hold | 
[**inventory_export**](InventoryApi.md#inventory_export) | **GET** /inventory/export | 
[**inventory_export_delta**](InventoryApi.md#inventory_export_delta) | **GET** /inventory/export/delta | 
[**inventory_get_by_id**](InventoryApi.md#inventory_get_by_id) | **GET** /inventory/{inventory-id} | 
[**inventory_get_exchanges_pos_id**](InventoryApi.md#inventory_get_exchanges_pos_id) | **GET** /inventory/exchange_pos_id/{exchangePosId} | 
[**inventory_get_holds_by_id**](InventoryApi.md#inventory_get_holds_by_id) | **GET** /inventory/{inventory-id}/hold | 
[**inventory_get_inventory_barcodes**](InventoryApi.md#inventory_get_inventory_barcodes) | **GET** /inventory/barcodes/{exchange-pos-id} | 
[**inventory_get_inventory_deltas**](InventoryApi.md#inventory_get_inventory_deltas) | **GET** /inventory/delta | 
[**inventory_legacy_bulk_remove_tags**](InventoryApi.md#inventory_legacy_bulk_remove_tags) | **DELETE** /inventory/tags | 
[**inventory_merge**](InventoryApi.md#inventory_merge) | **POST** /inventory/merge | 
[**inventory_merge_as_piggyback**](InventoryApi.md#inventory_merge_as_piggyback) | **POST** /inventory/merge-as-piggyback | 
[**inventory_price_history**](InventoryApi.md#inventory_price_history) | **GET** /inventory/{inventory-id}/price-history | 
[**inventory_remove_tag**](InventoryApi.md#inventory_remove_tag) | **DELETE** /inventory/{inventory-id}/tags/{tag} | 
[**inventory_search**](InventoryApi.md#inventory_search) | **GET** /inventory | 
[**inventory_search_purchased**](InventoryApi.md#inventory_search_purchased) | **GET** /inventory/purchased | 
[**inventory_search_purchased_v2**](InventoryApi.md#inventory_search_purchased_v2) | **GET** /inventory/purchased/V2 | 
[**inventory_search_sold**](InventoryApi.md#inventory_search_sold) | **GET** /inventory/sold | 
[**inventory_sold_bulk_swap_event**](InventoryApi.md#inventory_sold_bulk_swap_event) | **POST** /inventory/sold/bulk-swap-event | 
[**inventory_split**](InventoryApi.md#inventory_split) | **PUT** /inventory/{inventory-id}/split | 
[**inventory_split_to_consecutive**](InventoryApi.md#inventory_split_to_consecutive) | **PUT** /inventory/{inventory-id}/split-to-consecutive | 
[**inventory_split_to_originals**](InventoryApi.md#inventory_split_to_originals) | **POST** /inventory/{inventory-id}/actions/split-to-originals | 
[**inventory_sync**](InventoryApi.md#inventory_sync) | **PUT** /inventory/sync | 
[**inventory_tag**](InventoryApi.md#inventory_tag) | **POST** /inventory/{inventory-id}/tags | 
[**inventory_update**](InventoryApi.md#inventory_update) | **PUT** /inventory/{inventory-id} | 
[**inventory_update_purchase_inventory**](InventoryApi.md#inventory_update_purchase_inventory) | **POST** /inventory/actions/edit-section-row | 


# **inventory_bulk_merge**
> List[Inventory] inventory_bulk_merge(merge_inventory_request)



Merge all eligible inventories

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory import Inventory
from skybox_openapi_client.models.merge_inventory_request import MergeInventoryRequest
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    merge_inventory_request = skybox_openapi_client.MergeInventoryRequest() # MergeInventoryRequest | Payload

    try:
        api_response = api_instance.inventory_bulk_merge(merge_inventory_request)
        print("The response of InventoryApi->inventory_bulk_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_inventory_request** | [**MergeInventoryRequest**](MergeInventoryRequest.md)| Payload | 

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
**200** | inventories merged |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_bulk_remove_tags**
> inventory_bulk_remove_tags(request_body)



Deletes all tags from inventories with given ids

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    request_body = [56] # List[int] | Inventory Ids

    try:
        api_instance.inventory_bulk_remove_tags(request_body)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_remove_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| Inventory Ids | 

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

# **inventory_bulk_swap_event**
> inventory_bulk_swap_event(bulk_swap_event_request)



Bulk swap event

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.bulk_swap_event_request import BulkSwapEventRequest
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    bulk_swap_event_request = skybox_openapi_client.BulkSwapEventRequest() # BulkSwapEventRequest | Payload

    try:
        api_instance.inventory_bulk_swap_event(bulk_swap_event_request)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_swap_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_swap_event_request** | [**BulkSwapEventRequest**](BulkSwapEventRequest.md)| Payload | 

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
**200** | Event swapped |  -  |
**401** | not authorized |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_bulk_update**
> inventory_bulk_update(bulk_inventory_update_request)



Bulk update inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.bulk_inventory_update_request import BulkInventoryUpdateRequest
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    bulk_inventory_update_request = skybox_openapi_client.BulkInventoryUpdateRequest() # BulkInventoryUpdateRequest | Bulk inventory attributes to update

    try:
        api_instance.inventory_bulk_update(bulk_inventory_update_request)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_inventory_update_request** | [**BulkInventoryUpdateRequest**](BulkInventoryUpdateRequest.md)| Bulk inventory attributes to update | 

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
**200** | inventory updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_bulk_update_expected_value**
> inventory_bulk_update_expected_value(expected_value_update_bulk)



Bulk Expected Value Update of Inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.expected_value_update_bulk import ExpectedValueUpdateBulk
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    expected_value_update_bulk = [skybox_openapi_client.ExpectedValueUpdateBulk()] # List[ExpectedValueUpdateBulk] | Inventory expected value update

    try:
        api_instance.inventory_bulk_update_expected_value(expected_value_update_bulk)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_update_expected_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expected_value_update_bulk** | [**List[ExpectedValueUpdateBulk]**](ExpectedValueUpdateBulk.md)| Inventory expected value update | 

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

# **inventory_bulk_update_face_value**
> inventory_bulk_update_face_value(inventory_face_value_update_bulk)



Bulk Face Value Update of Inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_face_value_update_bulk import InventoryFaceValueUpdateBulk
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_face_value_update_bulk = [skybox_openapi_client.InventoryFaceValueUpdateBulk()] # List[InventoryFaceValueUpdateBulk] | Inventory face value update

    try:
        api_instance.inventory_bulk_update_face_value(inventory_face_value_update_bulk)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_update_face_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_face_value_update_bulk** | [**List[InventoryFaceValueUpdateBulk]**](InventoryFaceValueUpdateBulk.md)| Inventory face value update | 

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

# **inventory_bulk_update_price**
> inventory_bulk_update_price(inventory_price_update_bulk)



Bulk Price Update of Inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_price_update_bulk import InventoryPriceUpdateBulk
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_price_update_bulk = [skybox_openapi_client.InventoryPriceUpdateBulk()] # List[InventoryPriceUpdateBulk] | Inventory price update

    try:
        api_instance.inventory_bulk_update_price(inventory_price_update_bulk)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_update_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_price_update_bulk** | [**List[InventoryPriceUpdateBulk]**](InventoryPriceUpdateBulk.md)| Inventory price update | 

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

# **inventory_bulk_update_taxed_cost**
> inventory_bulk_update_taxed_cost(inventory_taxed_cost_update_bulk)



Bulk Taxed Cost Update of Inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_taxed_cost_update_bulk import InventoryTaxedCostUpdateBulk
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_taxed_cost_update_bulk = [skybox_openapi_client.InventoryTaxedCostUpdateBulk()] # List[InventoryTaxedCostUpdateBulk] | Inventory taxed cost update

    try:
        api_instance.inventory_bulk_update_taxed_cost(inventory_taxed_cost_update_bulk)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_bulk_update_taxed_cost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_taxed_cost_update_bulk** | [**List[InventoryTaxedCostUpdateBulk]**](InventoryTaxedCostUpdateBulk.md)| Inventory taxed cost update | 

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

# **inventory_delete**
> inventory_delete(inventory_id, tag_request)



Deletes tags for an inventory

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The inventory Id
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to be removed from the inventory

    try:
        api_instance.inventory_delete(inventory_id, tag_request)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The inventory Id | 
 **tag_request** | [**List[TagRequest]**](TagRequest.md)| Tags to be removed from the inventory | 

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

# **inventory_delete_holds_by_id**
> inventory_delete_holds_by_id(inventory_id)



Delete holds for inventory

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The ID of the inventory from which to delete holds

    try:
        api_instance.inventory_delete_holds_by_id(inventory_id)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_delete_holds_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The ID of the inventory from which to delete holds | 

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
**200** | holds deleted |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_export**
> List[InventorySummary] inventory_export(include_zero_priced_listings=include_zero_priced_listings, include_held=include_held, include_taxed_costs=include_taxed_costs, version=version)



Exports inventory for exchange integration. Export is limited to future events with a list price greater than 0. The results from this method are un-sorted.

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_summary import InventorySummary
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    include_zero_priced_listings = True # bool | Whether the results includes zero price listings (optional)
    include_held = True # bool | Whether the results includes held (optional)
    include_taxed_costs = True # bool |  (optional)
    version = 'version_example' # str |  (optional)

    try:
        api_response = api_instance.inventory_export(include_zero_priced_listings=include_zero_priced_listings, include_held=include_held, include_taxed_costs=include_taxed_costs, version=version)
        print("The response of InventoryApi->inventory_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_zero_priced_listings** | **bool**| Whether the results includes zero price listings | [optional] 
 **include_held** | **bool**| Whether the results includes held | [optional] 
 **include_taxed_costs** | **bool**|  | [optional] 
 **version** | **str**|  | [optional] 

### Return type

[**List[InventorySummary]**](InventorySummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory summaries returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_export_delta**
> List[InventorySummary] inventory_export_delta(timestamp=timestamp, include_zero_priced_listings=include_zero_priced_listings, include_held=include_held, include_taxed_costs=include_taxed_costs)



Exports inventory for exchange integration. Export is limited to future events with a list price greater than 0. The results from this method are un-sorted.

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_summary import InventorySummary
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    timestamp = 'timestamp_example' # str | Results returned will have newer update timestamps than this value (optional)
    include_zero_priced_listings = True # bool | Whether the results includes zero price listings (optional)
    include_held = True # bool | Whether the results includes held (optional)
    include_taxed_costs = True # bool |  (optional)

    try:
        api_response = api_instance.inventory_export_delta(timestamp=timestamp, include_zero_priced_listings=include_zero_priced_listings, include_held=include_held, include_taxed_costs=include_taxed_costs)
        print("The response of InventoryApi->inventory_export_delta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_export_delta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Results returned will have newer update timestamps than this value | [optional] 
 **include_zero_priced_listings** | **bool**| Whether the results includes zero price listings | [optional] 
 **include_held** | **bool**| Whether the results includes held | [optional] 
 **include_taxed_costs** | **bool**|  | [optional] 

### Return type

[**List[InventorySummary]**](InventorySummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory summaries returned with timestamp of request |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get_by_id**
> Inventory inventory_get_by_id(inventory_id)



Get Inventory

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The ID of the inventory to return

    try:
        api_response = api_instance.inventory_get_by_id(inventory_id)
        print("The response of InventoryApi->inventory_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The ID of the inventory to return | 

### Return type

[**Inventory**](Inventory.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory returned |  -  |
**401** | not authorized |  -  |
**404** | inventory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get_exchanges_pos_id**
> ExchangePosIdHistoryResponse inventory_get_exchanges_pos_id(exchange_pos_id)



Get the history for a exchange pos id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.exchange_pos_id_history_response import ExchangePosIdHistoryResponse
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    exchange_pos_id = 56 # int | 

    try:
        api_response = api_instance.inventory_get_exchanges_pos_id(exchange_pos_id)
        print("The response of InventoryApi->inventory_get_exchanges_pos_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_get_exchanges_pos_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_pos_id** | **int**|  | 

### Return type

[**ExchangePosIdHistoryResponse**](ExchangePosIdHistoryResponse.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of exchange pos id history returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get_holds_by_id**
> Hold inventory_get_holds_by_id(inventory_id)



Get holds for inventory

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The ID of the inventory to return the hold

    try:
        api_response = api_instance.inventory_get_holds_by_id(inventory_id)
        print("The response of InventoryApi->inventory_get_holds_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_get_holds_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The ID of the inventory to return the hold | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get_inventory_barcodes**
> List[InventoryBarcodeResponse] inventory_get_inventory_barcodes(exchange_pos_id)



Get barcodes for inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_barcode_response import InventoryBarcodeResponse
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    exchange_pos_id = 56 # int | The Exchange POS ID of the inventory

    try:
        api_response = api_instance.inventory_get_inventory_barcodes(exchange_pos_id)
        print("The response of InventoryApi->inventory_get_inventory_barcodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_get_inventory_barcodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_pos_id** | **int**| The Exchange POS ID of the inventory | 

### Return type

[**List[InventoryBarcodeResponse]**](InventoryBarcodeResponse.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory bar codes returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get_inventory_deltas**
> List[float] inventory_get_inventory_deltas(start_time, end_time, ticket_status=ticket_status)



Get changed inventory (created, updated, deleted) by update time

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    start_time = 'start_time_example' # str | Returns inventory updates after this time, iso yyyy-MM-ddTHH:mm:ssZ format.
    end_time = 'end_time_example' # str | Returns inventory updates before this time, iso yyyy-MM-ddTHH:mm:ssZ format.
    ticket_status = 'ticket_status_example' # str | Returns inventory updates with requested ticket status. (optional)

    try:
        api_response = api_instance.inventory_get_inventory_deltas(start_time, end_time, ticket_status=ticket_status)
        print("The response of InventoryApi->inventory_get_inventory_deltas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_get_inventory_deltas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **str**| Returns inventory updates after this time, iso yyyy-MM-ddTHH:mm:ssZ format. | 
 **end_time** | **str**| Returns inventory updates before this time, iso yyyy-MM-ddTHH:mm:ssZ format. | 
 **ticket_status** | **str**| Returns inventory updates with requested ticket status. | [optional] 

### Return type

**List[float]**

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updated inventory ids returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_legacy_bulk_remove_tags**
> inventory_legacy_bulk_remove_tags(id)



Deletes all tags from inventories with given ids

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    id = [56] # List[int] | Inventory Ids

    try:
        api_instance.inventory_legacy_bulk_remove_tags(id)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_legacy_bulk_remove_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[int]**](int.md)| Inventory Ids | 

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
**200** | tags deleted |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_merge**
> Inventory inventory_merge(merge_inventory_request)



Merge the list of inventories into a new inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory import Inventory
from skybox_openapi_client.models.merge_inventory_request import MergeInventoryRequest
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    merge_inventory_request = skybox_openapi_client.MergeInventoryRequest() # MergeInventoryRequest | Payload

    try:
        api_response = api_instance.inventory_merge(merge_inventory_request)
        print("The response of InventoryApi->inventory_merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_inventory_request** | [**MergeInventoryRequest**](MergeInventoryRequest.md)| Payload | 

### Return type

[**Inventory**](Inventory.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory created |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_merge_as_piggyback**
> Inventory inventory_merge_as_piggyback(merge_inventory_request)



Merge inventories as piggyback

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory import Inventory
from skybox_openapi_client.models.merge_inventory_request import MergeInventoryRequest
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    merge_inventory_request = skybox_openapi_client.MergeInventoryRequest() # MergeInventoryRequest | Payload

    try:
        api_response = api_instance.inventory_merge_as_piggyback(merge_inventory_request)
        print("The response of InventoryApi->inventory_merge_as_piggyback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_merge_as_piggyback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_inventory_request** | [**MergeInventoryRequest**](MergeInventoryRequest.md)| Payload | 

### Return type

[**Inventory**](Inventory.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventories merged |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_price_history**
> List[InventoryPriceHistory] inventory_price_history(inventory_id)



Retrieves price update history for inventory

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_price_history import InventoryPriceHistory
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The Id of the inventory

    try:
        api_response = api_instance.inventory_price_history(inventory_id)
        print("The response of InventoryApi->inventory_price_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_price_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The Id of the inventory | 

### Return type

[**List[InventoryPriceHistory]**](InventoryPriceHistory.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | price history retrieved |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_remove_tag**
> inventory_remove_tag(inventory_id, tag)



Deletes a tag for an inventory

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The Id of the inventory
    tag = 'tag_example' # str | Tag to be removed from the inventory

    try:
        api_instance.inventory_remove_tag(inventory_id, tag)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_remove_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The Id of the inventory | 
 **tag** | **str**| Tag to be removed from the inventory | 

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

# **inventory_search**
> List[InventorySummary] inventory_search(limit=limit, sort_dir=sort_dir, page_number=page_number, sorted_by=sorted_by, stock_type=stock_type, ticket_status=ticket_status, event_id=event_id, inventory_id=inventory_id, purchase_id=purchase_id, exchange_pos_id=exchange_pos_id, performer_id=performer_id, category_id=category_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event_tags_match_all=event_tags_match_all, event=event, event_keywords=event_keywords, venue_id=venue_id, venue=venue, vendor_id=vendor_id, exclude_vendor_id=exclude_vendor_id, city=city, state=state, country=country, section=section, section_match_mode=section_match_mode, row=row, row_match_mode=row_match_mode, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, event_type=event_type, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, last_update_from=last_update_from, last_update_to=last_update_to, last_price_update_from=last_price_update_from, last_price_update_to=last_price_update_to, sorted_by_b=sorted_by_b, sort_dir_b=sort_dir_b, files_uploaded=files_uploaded, bar_codes_entered=bar_codes_entered, external_ticket_id_entered=external_ticket_id_entered, listed=listed, expected_value_set=expected_value_set, skip_sorting=skip_sorting, min_quantity=min_quantity, max_quantity=max_quantity, min_shown_quantity=min_shown_quantity, max_shown_quantity=max_shown_quantity, min_price=min_price, max_price=max_price, min_average_unit_cost=min_average_unit_cost, max_average_unit_cost=max_average_unit_cost, low_seat=low_seat, high_seat=high_seat, in_hand=in_hand, notes=notes, public_notes=public_notes, no_tags=no_tags, include_tickets=include_tickets, zone_seating=zone_seating, day_of_week=day_of_week, seat_type=seat_type, split_type=split_type, no_splits=no_splits, currency_code=currency_code, hidden_seats=hidden_seats, cooperative=cooperative, electronic_transfer=electronic_transfer, vsr_option=vsr_option, replenishment_group_id=replenishment_group_id, consignment=consignment, consignment_status=consignment_status, received=received, on_hold=on_hold, days_old_from=days_old_from, days_old_to=days_old_to, exclude_parking=exclude_parking, instant_transfer_status=instant_transfer_status)



Get inventory filtered by query parameters

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.inventory_summary import InventorySummary
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    sorted_by = 'sorted_by_example' # str | Primary field to sort by (optional)
    stock_type = 'stock_type_example' # str | Stock Type search filter (optional)
    ticket_status = ['ticket_status_example'] # List[str] | Ticket Status search filter (optional)
    event_id = [56] # List[int] | Event Id search filter (optional)
    inventory_id = [56] # List[int] | Inventory Id search filter (optional)
    purchase_id = [56] # List[int] | Purchase Id search filter (optional)
    exchange_pos_id = [56] # List[int] | Exchange pos Id filter (optional)
    performer_id = [56] # List[int] | Performer Id search filter (optional)
    category_id = [56] # List[int] | Category Id search filter (optional)
    tag = ['tag_example'] # List[str] | Tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | Tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    event_tags_match_all = True # bool | Whether the results should have all event tags or only some (optional)
    event = 'event_example' # str | Event search filter (optional)
    event_keywords = ['event_keywords_example'] # List[str] | Event keywords filter (optional)
    venue_id = 56 # int | Venue id search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    vendor_id = 56 # int | Vendor Id search filter (optional)
    exclude_vendor_id = 56 # int | Vendor Id to exclude (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    country = ['country_example'] # List[str] | Country search filter (optional)
    section = 'section_example' # str | Section search filter (optional)
    section_match_mode = 'section_match_mode_example' # str | Section search partial match filter (optional)
    row = 'row_example' # str | Row search filter (optional)
    row_match_mode = 'row_match_mode_example' # str | Row search partial match filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Event date from range filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Event date to range filter (optional)
    event_time_from = 'event_time_from_example' # str | Only search events starting not earlier than (optional)
    event_time_to = 'event_time_to_example' # str | Only search events starting not later than (optional)
    event_type = 'event_type_example' # str | Event Type search filter (optional)
    purchase_date_from = '2013-10-20T19:20:30+01:00' # datetime | Purchase date from range filter (optional)
    purchase_date_to = '2013-10-20T19:20:30+01:00' # datetime | Purchase date to range filter (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | Inventory last update date from range filter (optional)
    last_update_to = '2013-10-20T19:20:30+01:00' # datetime | Inventory last update date to range filter (optional)
    last_price_update_from = '2013-10-20T19:20:30+01:00' # datetime | Last price update date from range filter (optional)
    last_price_update_to = '2013-10-20T19:20:30+01:00' # datetime | Last price update date to range filter (optional)
    sorted_by_b = 'sorted_by_b_example' # str | Secondary field to sort by (optional)
    sort_dir_b = 'sort_dir_b_example' # str | Secondary direction to sort (asc, desc) (optional)
    files_uploaded = True # bool | Whether the results should have Pdfs attached to all tickets (optional)
    bar_codes_entered = True # bool | Whether the results should have Bar Codes entered in all tickets (optional)
    external_ticket_id_entered = True # bool | Whether the results should have external ticket IDs entered in all tickets (optional)
    listed = True # bool | Whether the results should have listed inventories (optional)
    expected_value_set = True # bool | Whether the results should have expected value set (optional)
    skip_sorting = True # bool | Skip sorting of results (optional)
    min_quantity = 56 # int | Minimum quantity search filter (optional)
    max_quantity = 56 # int | Maximum quantity search filter (optional)
    min_shown_quantity = 56 # int | Minimum shown quantity search filter (optional)
    max_shown_quantity = 56 # int | Maximum shown quantity search filter (optional)
    min_price = 3.4 # float | Minimum price search filter (optional)
    max_price = 3.4 # float | Maximum price search filter (optional)
    min_average_unit_cost = 3.4 # float | Minimum average unit cost search filter (optional)
    max_average_unit_cost = 3.4 # float | Maximum average unit cost search filter (optional)
    low_seat = 56 # int | Low seat search filter (optional)
    high_seat = 56 # int | High seat search filter (optional)
    in_hand = True # bool | Whether the results should be in hand (optional)
    notes = 'notes_example' # str | Notes search filter (optional)
    public_notes = 'public_notes_example' # str | Public notes search filter (optional)
    no_tags = True # bool | Whether the results should have tags (optional)
    include_tickets = True # bool | Whether the results should include tickets (optional)
    zone_seating = True # bool | Whether the results should have zone seating (optional)
    day_of_week = [56] # List[int] | Day of the week of events that occur on that day of the week (optional)
    seat_type = 'seat_type_example' # str | Seat Type search filter (optional)
    split_type = 'split_type_example' # str | Split Type search filter (optional)
    no_splits = True # bool | Whether the results should have splits (optional)
    currency_code = 'currency_code_example' # str | Currency type search filter (optional)
    hidden_seats = True # bool | Whether the results should have hidden seats (optional)
    cooperative = True # bool | Whether the results belong to a cooperative PO (optional)
    electronic_transfer = True # bool | Whether the results should have electronic transfer (optional)
    vsr_option = 'vsr_option_example' # str | VSR option search filter (optional)
    replenishment_group_id = 56 # int | Replenishment group id search filter (optional)
    consignment = 'consignment_example' # str | Whether the results belong to a consignment type PO (optional)
    consignment_status = True # bool | Whether the results belong to a consignment status (optional)
    received = True # bool | Whether the results are received (optional)
    on_hold = True # bool | Whether the results are on hold (optional)
    days_old_from = '2013-10-20T19:20:30+01:00' # datetime | Days Old date from range filter (optional)
    days_old_to = '2013-10-20T19:20:30+01:00' # datetime | Days Old date to range filter (optional)
    exclude_parking = True # bool | Whether parking events are excluded (optional)
    instant_transfer_status = 'instant_transfer_status_example' # str | Whether the results belong to a instant transfer status (optional)

    try:
        api_response = api_instance.inventory_search(limit=limit, sort_dir=sort_dir, page_number=page_number, sorted_by=sorted_by, stock_type=stock_type, ticket_status=ticket_status, event_id=event_id, inventory_id=inventory_id, purchase_id=purchase_id, exchange_pos_id=exchange_pos_id, performer_id=performer_id, category_id=category_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event_tags_match_all=event_tags_match_all, event=event, event_keywords=event_keywords, venue_id=venue_id, venue=venue, vendor_id=vendor_id, exclude_vendor_id=exclude_vendor_id, city=city, state=state, country=country, section=section, section_match_mode=section_match_mode, row=row, row_match_mode=row_match_mode, event_date_from=event_date_from, event_date_to=event_date_to, event_time_from=event_time_from, event_time_to=event_time_to, event_type=event_type, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, last_update_from=last_update_from, last_update_to=last_update_to, last_price_update_from=last_price_update_from, last_price_update_to=last_price_update_to, sorted_by_b=sorted_by_b, sort_dir_b=sort_dir_b, files_uploaded=files_uploaded, bar_codes_entered=bar_codes_entered, external_ticket_id_entered=external_ticket_id_entered, listed=listed, expected_value_set=expected_value_set, skip_sorting=skip_sorting, min_quantity=min_quantity, max_quantity=max_quantity, min_shown_quantity=min_shown_quantity, max_shown_quantity=max_shown_quantity, min_price=min_price, max_price=max_price, min_average_unit_cost=min_average_unit_cost, max_average_unit_cost=max_average_unit_cost, low_seat=low_seat, high_seat=high_seat, in_hand=in_hand, notes=notes, public_notes=public_notes, no_tags=no_tags, include_tickets=include_tickets, zone_seating=zone_seating, day_of_week=day_of_week, seat_type=seat_type, split_type=split_type, no_splits=no_splits, currency_code=currency_code, hidden_seats=hidden_seats, cooperative=cooperative, electronic_transfer=electronic_transfer, vsr_option=vsr_option, replenishment_group_id=replenishment_group_id, consignment=consignment, consignment_status=consignment_status, received=received, on_hold=on_hold, days_old_from=days_old_from, days_old_to=days_old_to, exclude_parking=exclude_parking, instant_transfer_status=instant_transfer_status)
        print("The response of InventoryApi->inventory_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **sorted_by** | **str**| Primary field to sort by | [optional] 
 **stock_type** | **str**| Stock Type search filter | [optional] 
 **ticket_status** | [**List[str]**](str.md)| Ticket Status search filter | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id search filter | [optional] 
 **inventory_id** | [**List[int]**](int.md)| Inventory Id search filter | [optional] 
 **purchase_id** | [**List[int]**](int.md)| Purchase Id search filter | [optional] 
 **exchange_pos_id** | [**List[int]**](int.md)| Exchange pos Id filter | [optional] 
 **performer_id** | [**List[int]**](int.md)| Performer Id search filter | [optional] 
 **category_id** | [**List[int]**](int.md)| Category Id search filter | [optional] 
 **tag** | [**List[str]**](str.md)| Tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| Tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **event_tags_match_all** | **bool**| Whether the results should have all event tags or only some | [optional] 
 **event** | **str**| Event search filter | [optional] 
 **event_keywords** | [**List[str]**](str.md)| Event keywords filter | [optional] 
 **venue_id** | **int**| Venue id search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **vendor_id** | **int**| Vendor Id search filter | [optional] 
 **exclude_vendor_id** | **int**| Vendor Id to exclude | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **country** | [**List[str]**](str.md)| Country search filter | [optional] 
 **section** | **str**| Section search filter | [optional] 
 **section_match_mode** | **str**| Section search partial match filter | [optional] 
 **row** | **str**| Row search filter | [optional] 
 **row_match_mode** | **str**| Row search partial match filter | [optional] 
 **event_date_from** | **datetime**| Event date from range filter | [optional] 
 **event_date_to** | **datetime**| Event date to range filter | [optional] 
 **event_time_from** | **str**| Only search events starting not earlier than | [optional] 
 **event_time_to** | **str**| Only search events starting not later than | [optional] 
 **event_type** | **str**| Event Type search filter | [optional] 
 **purchase_date_from** | **datetime**| Purchase date from range filter | [optional] 
 **purchase_date_to** | **datetime**| Purchase date to range filter | [optional] 
 **last_update_from** | **datetime**| Inventory last update date from range filter | [optional] 
 **last_update_to** | **datetime**| Inventory last update date to range filter | [optional] 
 **last_price_update_from** | **datetime**| Last price update date from range filter | [optional] 
 **last_price_update_to** | **datetime**| Last price update date to range filter | [optional] 
 **sorted_by_b** | **str**| Secondary field to sort by | [optional] 
 **sort_dir_b** | **str**| Secondary direction to sort (asc, desc) | [optional] 
 **files_uploaded** | **bool**| Whether the results should have Pdfs attached to all tickets | [optional] 
 **bar_codes_entered** | **bool**| Whether the results should have Bar Codes entered in all tickets | [optional] 
 **external_ticket_id_entered** | **bool**| Whether the results should have external ticket IDs entered in all tickets | [optional] 
 **listed** | **bool**| Whether the results should have listed inventories | [optional] 
 **expected_value_set** | **bool**| Whether the results should have expected value set | [optional] 
 **skip_sorting** | **bool**| Skip sorting of results | [optional] 
 **min_quantity** | **int**| Minimum quantity search filter | [optional] 
 **max_quantity** | **int**| Maximum quantity search filter | [optional] 
 **min_shown_quantity** | **int**| Minimum shown quantity search filter | [optional] 
 **max_shown_quantity** | **int**| Maximum shown quantity search filter | [optional] 
 **min_price** | **float**| Minimum price search filter | [optional] 
 **max_price** | **float**| Maximum price search filter | [optional] 
 **min_average_unit_cost** | **float**| Minimum average unit cost search filter | [optional] 
 **max_average_unit_cost** | **float**| Maximum average unit cost search filter | [optional] 
 **low_seat** | **int**| Low seat search filter | [optional] 
 **high_seat** | **int**| High seat search filter | [optional] 
 **in_hand** | **bool**| Whether the results should be in hand | [optional] 
 **notes** | **str**| Notes search filter | [optional] 
 **public_notes** | **str**| Public notes search filter | [optional] 
 **no_tags** | **bool**| Whether the results should have tags | [optional] 
 **include_tickets** | **bool**| Whether the results should include tickets | [optional] 
 **zone_seating** | **bool**| Whether the results should have zone seating | [optional] 
 **day_of_week** | [**List[int]**](int.md)| Day of the week of events that occur on that day of the week | [optional] 
 **seat_type** | **str**| Seat Type search filter | [optional] 
 **split_type** | **str**| Split Type search filter | [optional] 
 **no_splits** | **bool**| Whether the results should have splits | [optional] 
 **currency_code** | **str**| Currency type search filter | [optional] 
 **hidden_seats** | **bool**| Whether the results should have hidden seats | [optional] 
 **cooperative** | **bool**| Whether the results belong to a cooperative PO | [optional] 
 **electronic_transfer** | **bool**| Whether the results should have electronic transfer | [optional] 
 **vsr_option** | **str**| VSR option search filter | [optional] 
 **replenishment_group_id** | **int**| Replenishment group id search filter | [optional] 
 **consignment** | **str**| Whether the results belong to a consignment type PO | [optional] 
 **consignment_status** | **bool**| Whether the results belong to a consignment status | [optional] 
 **received** | **bool**| Whether the results are received | [optional] 
 **on_hold** | **bool**| Whether the results are on hold | [optional] 
 **days_old_from** | **datetime**| Days Old date from range filter | [optional] 
 **days_old_to** | **datetime**| Days Old date to range filter | [optional] 
 **exclude_parking** | **bool**| Whether parking events are excluded | [optional] 
 **instant_transfer_status** | **str**| Whether the results belong to a instant transfer status | [optional] 

### Return type

[**List[InventorySummary]**](InventorySummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory summaries returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_search_purchased**
> List[PurchasedInventorySummary] inventory_search_purchased(limit=limit, sort_dir=sort_dir, page_number=page_number, stock_type=stock_type, ticket_status=ticket_status, event_id=event_id, inventory_id=inventory_id, performer_id=performer_id, vendor_id=vendor_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event=event, venue=venue, city=city, state=state, country=country, section=section, row=row, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, event_date_from=event_date_from, event_date_to=event_date_to, external_ref=external_ref, payment_status=payment_status, partial_payment_ref=partial_payment_ref, display_name=display_name, zone_seating=zone_seating, notes=notes, performer=performer, purchase_id=purchase_id, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, received=received, venue_ids=venue_ids, consignment=consignment, cooperative=cooperative, sorted_by=sorted_by)



Gets purchased inventory filtered by query parameters

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchased_inventory_summary import PurchasedInventorySummary
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    stock_type = 'stock_type_example' # str | Stock Type search filter (optional)
    ticket_status = ['ticket_status_example'] # List[str] | Ticket Status search filter (optional)
    event_id = [56] # List[int] | Event Id search filter (optional)
    inventory_id = [56] # List[int] | Inventory Id search filter (optional)
    performer_id = [56] # List[int] | Performer Id search filter (optional)
    vendor_id = [56] # List[int] | Vendor Id search filter (optional)
    tag = ['tag_example'] # List[str] | Purchase tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all PO tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | PO tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all PO tags or only some (optional)
    event = 'event_example' # str | Event search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    country = ['country_example'] # List[str] | Country search filter (optional)
    section = 'section_example' # str | Section search filter (optional)
    row = 'row_example' # str | Row search filter (optional)
    purchase_date_from = '2013-10-20T19:20:30+01:00' # datetime | Purchase date from range filter (optional)
    purchase_date_to = '2013-10-20T19:20:30+01:00' # datetime | Purchase date to range filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Event date from range filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Event date to range filter (optional)
    external_ref = 'external_ref_example' # str | External reference search filter (optional)
    payment_status = ['payment_status_example'] # List[str] | Payment status search filter (optional)
    partial_payment_ref = 'partial_payment_ref_example' # str | Partial payment reference search filter (optional)
    display_name = 'display_name_example' # str | Vendor display name search filter (optional)
    zone_seating = True # bool | Whether the results should have zone seating (optional)
    notes = 'notes_example' # str | Notes search filter (optional)
    performer = 'performer_example' # str | Performer search filter (optional)
    purchase_id = [56] # List[int] | Purchase Id search filter (optional)
    in_hand_date_from = '2013-10-20T19:20:30+01:00' # datetime | In hand date from range filter (optional)
    in_hand_date_to = '2013-10-20T19:20:30+01:00' # datetime | In hand date to range filter (optional)
    received = True # bool | Whether the results have received POs (optional)
    venue_ids = [56] # List[int] | Venue id search filter (optional)
    consignment = 'consignment_example' # str | Whether the results have a consignment type POs (optional)
    cooperative = True # bool | Whether the results have cooperative POs (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.inventory_search_purchased(limit=limit, sort_dir=sort_dir, page_number=page_number, stock_type=stock_type, ticket_status=ticket_status, event_id=event_id, inventory_id=inventory_id, performer_id=performer_id, vendor_id=vendor_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event=event, venue=venue, city=city, state=state, country=country, section=section, row=row, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, event_date_from=event_date_from, event_date_to=event_date_to, external_ref=external_ref, payment_status=payment_status, partial_payment_ref=partial_payment_ref, display_name=display_name, zone_seating=zone_seating, notes=notes, performer=performer, purchase_id=purchase_id, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, received=received, venue_ids=venue_ids, consignment=consignment, cooperative=cooperative, sorted_by=sorted_by)
        print("The response of InventoryApi->inventory_search_purchased:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_search_purchased: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **stock_type** | **str**| Stock Type search filter | [optional] 
 **ticket_status** | [**List[str]**](str.md)| Ticket Status search filter | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id search filter | [optional] 
 **inventory_id** | [**List[int]**](int.md)| Inventory Id search filter | [optional] 
 **performer_id** | [**List[int]**](int.md)| Performer Id search filter | [optional] 
 **vendor_id** | [**List[int]**](int.md)| Vendor Id search filter | [optional] 
 **tag** | [**List[str]**](str.md)| Purchase tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all PO tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| PO tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all PO tags or only some | [optional] 
 **event** | **str**| Event search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **country** | [**List[str]**](str.md)| Country search filter | [optional] 
 **section** | **str**| Section search filter | [optional] 
 **row** | **str**| Row search filter | [optional] 
 **purchase_date_from** | **datetime**| Purchase date from range filter | [optional] 
 **purchase_date_to** | **datetime**| Purchase date to range filter | [optional] 
 **event_date_from** | **datetime**| Event date from range filter | [optional] 
 **event_date_to** | **datetime**| Event date to range filter | [optional] 
 **external_ref** | **str**| External reference search filter | [optional] 
 **payment_status** | [**List[str]**](str.md)| Payment status search filter | [optional] 
 **partial_payment_ref** | **str**| Partial payment reference search filter | [optional] 
 **display_name** | **str**| Vendor display name search filter | [optional] 
 **zone_seating** | **bool**| Whether the results should have zone seating | [optional] 
 **notes** | **str**| Notes search filter | [optional] 
 **performer** | **str**| Performer search filter | [optional] 
 **purchase_id** | [**List[int]**](int.md)| Purchase Id search filter | [optional] 
 **in_hand_date_from** | **datetime**| In hand date from range filter | [optional] 
 **in_hand_date_to** | **datetime**| In hand date to range filter | [optional] 
 **received** | **bool**| Whether the results have received POs | [optional] 
 **venue_ids** | [**List[int]**](int.md)| Venue id search filter | [optional] 
 **consignment** | **str**| Whether the results have a consignment type POs | [optional] 
 **cooperative** | **bool**| Whether the results have cooperative POs | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[PurchasedInventorySummary]**](PurchasedInventorySummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchased inventory summaries returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_search_purchased_v2**
> List[PurchasedInventorySummaryV2] inventory_search_purchased_v2(limit=limit, sort_dir=sort_dir, page_number=page_number, stock_type=stock_type, ticket_status=ticket_status, event_id=event_id, inventory_id=inventory_id, performer_id=performer_id, vendor_id=vendor_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event=event, venue=venue, city=city, state=state, country=country, section=section, row=row, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, event_date_from=event_date_from, event_date_to=event_date_to, external_ref=external_ref, payment_status=payment_status, partial_payment_ref=partial_payment_ref, display_name=display_name, zone_seating=zone_seating, notes=notes, performer=performer, purchase_id=purchase_id, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, received=received, venue_ids=venue_ids, consignment=consignment, cooperative=cooperative, sorted_by=sorted_by, credit_card_group_id=credit_card_group_id, credit_card_last_digits=credit_card_last_digits, event_type=event_type, in_hand=in_hand, inventory_tag=inventory_tag, inventory_tags_match_all=inventory_tags_match_all, anti_inventory_tag=anti_inventory_tag, anti_inventory_tags_match_all=anti_inventory_tags_match_all, no_tags=no_tags, includes_seat=includes_seat, payment_method=payment_method, min_unit_cost=min_unit_cost, max_unit_cost=max_unit_cost, min_total_cost=min_total_cost, max_total_cost=max_total_cost, created_by=created_by, created_by_user_id=created_by_user_id, currency_code=currency_code, purchase_status=purchase_status, category_id=category_id, last_purchase_order_note=last_purchase_order_note, inventory_public_notes=inventory_public_notes, event_tag=event_tag, event_tags_match_all=event_tags_match_all, anti_event_tag=anti_event_tag, anti_event_tags_match_all=anti_event_tags_match_all)



Gets purchased inventory filtered by query parameters

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.purchased_inventory_summary_v2 import PurchasedInventorySummaryV2
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    stock_type = 'stock_type_example' # str | Stock Type search filter (optional)
    ticket_status = ['ticket_status_example'] # List[str] | Ticket Status search filter (optional)
    event_id = [56] # List[int] | Event Id search filter (optional)
    inventory_id = [56] # List[int] | Inventory Id search filter (optional)
    performer_id = [56] # List[int] | Performer Id search filter (optional)
    vendor_id = [56] # List[int] | Vendor Id search filter (optional)
    tag = ['tag_example'] # List[str] | Purchase tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all PO tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | PO tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all PO tags or only some (optional)
    event = 'event_example' # str | Event search filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    country = ['country_example'] # List[str] | Country search filter (optional)
    section = 'section_example' # str | Section search filter (optional)
    row = 'row_example' # str | Row search filter (optional)
    purchase_date_from = '2013-10-20T19:20:30+01:00' # datetime | Purchase date from range filter (optional)
    purchase_date_to = '2013-10-20T19:20:30+01:00' # datetime | Purchase date to range filter (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | Event date from range filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | Event date to range filter (optional)
    external_ref = 'external_ref_example' # str | External reference search filter (optional)
    payment_status = ['payment_status_example'] # List[str] | Payment status search filter (optional)
    partial_payment_ref = 'partial_payment_ref_example' # str | Partial payment reference search filter (optional)
    display_name = 'display_name_example' # str | Vendor display name search filter (optional)
    zone_seating = True # bool | Whether the results should have zone seating (optional)
    notes = 'notes_example' # str | Notes search filter (optional)
    performer = 'performer_example' # str | Performer search filter (optional)
    purchase_id = [56] # List[int] | Purchase Id search filter (optional)
    in_hand_date_from = '2013-10-20T19:20:30+01:00' # datetime | In hand date from range filter (optional)
    in_hand_date_to = '2013-10-20T19:20:30+01:00' # datetime | In hand date to range filter (optional)
    received = True # bool | Whether the results have received POs (optional)
    venue_ids = [56] # List[int] | Venue id search filter (optional)
    consignment = 'consignment_example' # str | Whether the results have a consignment type POs (optional)
    cooperative = True # bool | Whether the results have cooperative POs (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)
    credit_card_group_id = 56 # int | Credit card group id search filter (optional)
    credit_card_last_digits = 'credit_card_last_digits_example' # str | Credit card last digits search filter (optional)
    event_type = 'event_type_example' # str | Event Type search filter (optional)
    in_hand = True # bool | Whether the results should be in hand (optional)
    inventory_tag = ['inventory_tag_example'] # List[str] | Inventory tags to include (optional)
    inventory_tags_match_all = True # bool | Whether the results should have all inventory tags or only some (optional)
    anti_inventory_tag = ['anti_inventory_tag_example'] # List[str] | Inventory tags to exclude (optional)
    anti_inventory_tags_match_all = True # bool | Whether the results should not have all inventory tags or only some (optional)
    no_tags = True # bool | Whether the results should have inventory tags (optional)
    includes_seat = 56 # int | Seat search filter (optional)
    payment_method = 'payment_method_example' # str | Payment method search filter (optional)
    min_unit_cost = 3.4 # float | Minimum unit cost search filter (optional)
    max_unit_cost = 3.4 # float | Maximum unit cost search filter (optional)
    min_total_cost = 3.4 # float | Minimum total cost search filter (optional)
    max_total_cost = 3.4 # float | Maximum total cost search filter (optional)
    created_by = 'created_by_example' # str | Email search filter for PO creator (optional)
    created_by_user_id = 56 # int | Id search filter for invoice creator (optional)
    currency_code = 'currency_code_example' # str | Currency filter (optional)
    purchase_status = ['purchase_status_example'] # List[str] | Purchase status search filter (optional)
    category_id = [56] # List[int] | Performer category search filter (optional)
    last_purchase_order_note = 'last_purchase_order_note_example' # str | Last purchase order note (optional)
    inventory_public_notes = 'inventory_public_notes_example' # str | Inventory public notes (optional)
    event_tag = ['event_tag_example'] # List[str] | Event tags to include (optional)
    event_tags_match_all = True # bool | Whether the results should have all event tags or only some (optional)
    anti_event_tag = ['anti_event_tag_example'] # List[str] | Event tags to exclude (optional)
    anti_event_tags_match_all = True # bool | Whether the results should not have all the event tags or only some (optional)

    try:
        api_response = api_instance.inventory_search_purchased_v2(limit=limit, sort_dir=sort_dir, page_number=page_number, stock_type=stock_type, ticket_status=ticket_status, event_id=event_id, inventory_id=inventory_id, performer_id=performer_id, vendor_id=vendor_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, event=event, venue=venue, city=city, state=state, country=country, section=section, row=row, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, event_date_from=event_date_from, event_date_to=event_date_to, external_ref=external_ref, payment_status=payment_status, partial_payment_ref=partial_payment_ref, display_name=display_name, zone_seating=zone_seating, notes=notes, performer=performer, purchase_id=purchase_id, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, received=received, venue_ids=venue_ids, consignment=consignment, cooperative=cooperative, sorted_by=sorted_by, credit_card_group_id=credit_card_group_id, credit_card_last_digits=credit_card_last_digits, event_type=event_type, in_hand=in_hand, inventory_tag=inventory_tag, inventory_tags_match_all=inventory_tags_match_all, anti_inventory_tag=anti_inventory_tag, anti_inventory_tags_match_all=anti_inventory_tags_match_all, no_tags=no_tags, includes_seat=includes_seat, payment_method=payment_method, min_unit_cost=min_unit_cost, max_unit_cost=max_unit_cost, min_total_cost=min_total_cost, max_total_cost=max_total_cost, created_by=created_by, created_by_user_id=created_by_user_id, currency_code=currency_code, purchase_status=purchase_status, category_id=category_id, last_purchase_order_note=last_purchase_order_note, inventory_public_notes=inventory_public_notes, event_tag=event_tag, event_tags_match_all=event_tags_match_all, anti_event_tag=anti_event_tag, anti_event_tags_match_all=anti_event_tags_match_all)
        print("The response of InventoryApi->inventory_search_purchased_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_search_purchased_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **stock_type** | **str**| Stock Type search filter | [optional] 
 **ticket_status** | [**List[str]**](str.md)| Ticket Status search filter | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id search filter | [optional] 
 **inventory_id** | [**List[int]**](int.md)| Inventory Id search filter | [optional] 
 **performer_id** | [**List[int]**](int.md)| Performer Id search filter | [optional] 
 **vendor_id** | [**List[int]**](int.md)| Vendor Id search filter | [optional] 
 **tag** | [**List[str]**](str.md)| Purchase tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all PO tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| PO tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all PO tags or only some | [optional] 
 **event** | **str**| Event search filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **country** | [**List[str]**](str.md)| Country search filter | [optional] 
 **section** | **str**| Section search filter | [optional] 
 **row** | **str**| Row search filter | [optional] 
 **purchase_date_from** | **datetime**| Purchase date from range filter | [optional] 
 **purchase_date_to** | **datetime**| Purchase date to range filter | [optional] 
 **event_date_from** | **datetime**| Event date from range filter | [optional] 
 **event_date_to** | **datetime**| Event date to range filter | [optional] 
 **external_ref** | **str**| External reference search filter | [optional] 
 **payment_status** | [**List[str]**](str.md)| Payment status search filter | [optional] 
 **partial_payment_ref** | **str**| Partial payment reference search filter | [optional] 
 **display_name** | **str**| Vendor display name search filter | [optional] 
 **zone_seating** | **bool**| Whether the results should have zone seating | [optional] 
 **notes** | **str**| Notes search filter | [optional] 
 **performer** | **str**| Performer search filter | [optional] 
 **purchase_id** | [**List[int]**](int.md)| Purchase Id search filter | [optional] 
 **in_hand_date_from** | **datetime**| In hand date from range filter | [optional] 
 **in_hand_date_to** | **datetime**| In hand date to range filter | [optional] 
 **received** | **bool**| Whether the results have received POs | [optional] 
 **venue_ids** | [**List[int]**](int.md)| Venue id search filter | [optional] 
 **consignment** | **str**| Whether the results have a consignment type POs | [optional] 
 **cooperative** | **bool**| Whether the results have cooperative POs | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 
 **credit_card_group_id** | **int**| Credit card group id search filter | [optional] 
 **credit_card_last_digits** | **str**| Credit card last digits search filter | [optional] 
 **event_type** | **str**| Event Type search filter | [optional] 
 **in_hand** | **bool**| Whether the results should be in hand | [optional] 
 **inventory_tag** | [**List[str]**](str.md)| Inventory tags to include | [optional] 
 **inventory_tags_match_all** | **bool**| Whether the results should have all inventory tags or only some | [optional] 
 **anti_inventory_tag** | [**List[str]**](str.md)| Inventory tags to exclude | [optional] 
 **anti_inventory_tags_match_all** | **bool**| Whether the results should not have all inventory tags or only some | [optional] 
 **no_tags** | **bool**| Whether the results should have inventory tags | [optional] 
 **includes_seat** | **int**| Seat search filter | [optional] 
 **payment_method** | **str**| Payment method search filter | [optional] 
 **min_unit_cost** | **float**| Minimum unit cost search filter | [optional] 
 **max_unit_cost** | **float**| Maximum unit cost search filter | [optional] 
 **min_total_cost** | **float**| Minimum total cost search filter | [optional] 
 **max_total_cost** | **float**| Maximum total cost search filter | [optional] 
 **created_by** | **str**| Email search filter for PO creator | [optional] 
 **created_by_user_id** | **int**| Id search filter for invoice creator | [optional] 
 **currency_code** | **str**| Currency filter | [optional] 
 **purchase_status** | [**List[str]**](str.md)| Purchase status search filter | [optional] 
 **category_id** | [**List[int]**](int.md)| Performer category search filter | [optional] 
 **last_purchase_order_note** | **str**| Last purchase order note | [optional] 
 **inventory_public_notes** | **str**| Inventory public notes | [optional] 
 **event_tag** | [**List[str]**](str.md)| Event tags to include | [optional] 
 **event_tags_match_all** | **bool**| Whether the results should have all event tags or only some | [optional] 
 **anti_event_tag** | [**List[str]**](str.md)| Event tags to exclude | [optional] 
 **anti_event_tags_match_all** | **bool**| Whether the results should not have all the event tags or only some | [optional] 

### Return type

[**List[PurchasedInventorySummaryV2]**](PurchasedInventorySummaryV2.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchased inventory summaries returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_search_sold**
> List[SoldInventorySummary] inventory_search_sold(limit=limit, sort_dir=sort_dir, page_number=page_number, sorted_by=sorted_by, event_id=event_id, inventory_id=inventory_id, exchange_pos_id=exchange_pos_id, invoice_id=invoice_id, purchase_ids=purchase_ids, vendor_id=vendor_id, event_type=event_type, category_id=category_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, anti_event_tag=anti_event_tag, anti_event_tags_match_all=anti_event_tags_match_all, no_tags=no_tags, invoice_tag=invoice_tag, invoice_tags_match_all=invoice_tags_match_all, event_tag=event_tag, event_tags_match_all=event_tags_match_all, purchase_tag=purchase_tag, purchase_tags_match_all=purchase_tags_match_all, customer_id=customer_id, customer_display_name=customer_display_name, performer_id=performer_id, performer=performer, event_keywords=event_keywords, event=event, event_date_from=event_date_from, event_date_to=event_date_to, venue_id=venue_id, venue=venue, section=section, row=row, includes_seat=includes_seat, invoice_date_from=invoice_date_from, invoice_date_to=invoice_date_to, currency_code=currency_code, external_ref=external_ref, purchase_external_ref=purchase_external_ref, payment_status=payment_status, invoice_status=invoice_status, fulfillment_status=fulfillment_status, stock_type=stock_type, zone_seating=zone_seating, pdfs_or_barcodes_attached=pdfs_or_barcodes_attached, files_uploaded=files_uploaded, barcodes_entered=barcodes_entered, electronic_transfer=electronic_transfer, internal_notes=internal_notes, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, fulfillment_date_from=fulfillment_date_from, fulfillment_date_to=fulfillment_date_to, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, cooperative=cooperative, received=received, invoice_notes=invoice_notes, public_notes=public_notes, state=state, country=country, due=due, invoice_created_by=invoice_created_by, created_by_user_id=created_by_user_id, day_of_week=day_of_week, last_update_from=last_update_from, invoice_notes_user_id=invoice_notes_user_id, consignment=consignment, customer_type=customer_type, exclude_parking=exclude_parking, min_total_cost=min_total_cost, max_total_cost=max_total_cost)



Gets sold inventory filtered by query parameters

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.sold_inventory_summary import SoldInventorySummary
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)
    event_id = [56] # List[int] | Event Id to search on (optional)
    inventory_id = [56] # List[int] | Inventory Id to search on (optional)
    exchange_pos_id = [56] # List[int] | Exchange pos Id filter (optional)
    invoice_id = [56] # List[int] | Invoice Id to search on (optional)
    purchase_ids = [56] # List[int] | Purchase Id to search on (optional)
    vendor_id = 56 # int | Vendor Id to search on (optional)
    event_type = 'event_type_example' # str | Event Type to search on (optional)
    category_id = [56] # List[int] | Category Id filter (optional)
    tag = ['tag_example'] # List[str] | Tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | Tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    anti_event_tag = ['anti_event_tag_example'] # List[str] | Event tags to exclude (optional)
    anti_event_tags_match_all = True # bool | Whether the results should not have all the event tags or only some (optional)
    no_tags = True # bool | Whether the results should have tags (optional)
    invoice_tag = ['invoice_tag_example'] # List[str] | Invoice tags to include (optional)
    invoice_tags_match_all = True # bool | Whether the results should have all invoice tags or only some (optional)
    event_tag = ['event_tag_example'] # List[str] | Event tags to include (optional)
    event_tags_match_all = True # bool | Whether the results should have all event tags or only some (optional)
    purchase_tag = ['purchase_tag_example'] # List[str] | Purchase tags to include (optional)
    purchase_tags_match_all = True # bool | Whether the results should have all purchase tags or only some (optional)
    customer_id = 56 # int | Customer Id to filter (optional)
    customer_display_name = 'customer_display_name_example' # str | Customer display name filter (optional)
    performer_id = 56 # int | Performer Id filter (optional)
    performer = 'performer_example' # str | Performer to search on (optional)
    event_keywords = ['event_keywords_example'] # List[str] | Event keywords filter (optional)
    event = 'event_example' # str | Event to search on (optional)
    event_date_from = '2013-10-20T19:20:30+01:00' # datetime | From event date filter (optional)
    event_date_to = '2013-10-20T19:20:30+01:00' # datetime | To event date filter (optional)
    venue_id = 56 # int | Venue Id filter (optional)
    venue = 'venue_example' # str | Venue search filter (optional)
    section = 'section_example' # str | Section search filter (optional)
    row = 'row_example' # str | Row search filter (optional)
    includes_seat = 56 # int | Seat search filter (optional)
    invoice_date_from = '2013-10-20T19:20:30+01:00' # datetime | Invoice date from range filter (optional)
    invoice_date_to = '2013-10-20T19:20:30+01:00' # datetime | Invoice date to range filter (optional)
    currency_code = 'currency_code_example' # str | Currency type search filter (optional)
    external_ref = ['external_ref_example'] # List[str] | Invoice external ref filter (optional)
    purchase_external_ref = 'purchase_external_ref_example' # str | Purchase external ref filter (optional)
    payment_status = ['payment_status_example'] # List[str] | Payment status to search on (optional)
    invoice_status = ['invoice_status_example'] # List[str] | Invoice status search filter (optional)
    fulfillment_status = 'fulfillment_status_example' # str | Fulfillment status search filter (optional)
    stock_type = 'stock_type_example' # str | Stock Type search filter (optional)
    zone_seating = True # bool | Whether the results should have zone seating (optional)
    pdfs_or_barcodes_attached = True # bool | Whether the results should have Pdfs or Bar Codes attached to all tickets (optional)
    files_uploaded = True # bool | Whether the results should have Pdfs attached to all tickets (optional)
    barcodes_entered = True # bool | Whether the results should have Bar Codes entered in all tickets (optional)
    electronic_transfer = True # bool | Whether the results should have electronic transfer (optional)
    internal_notes = 'internal_notes_example' # str | Internal notes search filter (optional)
    in_hand_date_from = '2013-10-20T19:20:30+01:00' # datetime | From in hand date filter (optional)
    in_hand_date_to = '2013-10-20T19:20:30+01:00' # datetime | To in hand date filter (optional)
    fulfillment_date_from = '2013-10-20T19:20:30+01:00' # datetime | From fulfillment date filter (optional)
    fulfillment_date_to = '2013-10-20T19:20:30+01:00' # datetime | To fulfillment date filter (optional)
    purchase_date_from = '2013-10-20T19:20:30+01:00' # datetime | Purchase date from range filter (optional)
    purchase_date_to = '2013-10-20T19:20:30+01:00' # datetime | Purchase date to range filter (optional)
    cooperative = True # bool | Whether the results are cooperative (optional)
    received = True # bool | Whether the results are received (optional)
    invoice_notes = 'invoice_notes_example' # str | Invoice notes search filter (optional)
    public_notes = 'public_notes_example' # str | Public notes search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    country = ['country_example'] # List[str] | Country search filter (optional)
    due = True # bool | Whether the inventories are due or not (optional)
    invoice_created_by = 'invoice_created_by_example' # str | Email search filter for invoice creator (optional)
    created_by_user_id = 56 # int | User id of invoice creator (optional)
    day_of_week = [56] # List[int] | Day of the week of events that occur on that day of the week (optional)
    last_update_from = '2013-10-20T19:20:30+01:00' # datetime | Inventory last update date from range filter (optional)
    invoice_notes_user_id = 56 # int | Invoice notes user id search filter (optional)
    consignment = 'consignment_example' # str | Whether the results have a consignment type POs (optional)
    customer_type = 'customer_type_example' # str | Whether the results have a customer type of the Invoice (optional)
    exclude_parking = True # bool | Whether parking events are excluded (optional)
    min_total_cost = 3.4 # float | Minimum total cost search filter (optional)
    max_total_cost = 3.4 # float | Maximum total cost search filter (optional)

    try:
        api_response = api_instance.inventory_search_sold(limit=limit, sort_dir=sort_dir, page_number=page_number, sorted_by=sorted_by, event_id=event_id, inventory_id=inventory_id, exchange_pos_id=exchange_pos_id, invoice_id=invoice_id, purchase_ids=purchase_ids, vendor_id=vendor_id, event_type=event_type, category_id=category_id, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, anti_event_tag=anti_event_tag, anti_event_tags_match_all=anti_event_tags_match_all, no_tags=no_tags, invoice_tag=invoice_tag, invoice_tags_match_all=invoice_tags_match_all, event_tag=event_tag, event_tags_match_all=event_tags_match_all, purchase_tag=purchase_tag, purchase_tags_match_all=purchase_tags_match_all, customer_id=customer_id, customer_display_name=customer_display_name, performer_id=performer_id, performer=performer, event_keywords=event_keywords, event=event, event_date_from=event_date_from, event_date_to=event_date_to, venue_id=venue_id, venue=venue, section=section, row=row, includes_seat=includes_seat, invoice_date_from=invoice_date_from, invoice_date_to=invoice_date_to, currency_code=currency_code, external_ref=external_ref, purchase_external_ref=purchase_external_ref, payment_status=payment_status, invoice_status=invoice_status, fulfillment_status=fulfillment_status, stock_type=stock_type, zone_seating=zone_seating, pdfs_or_barcodes_attached=pdfs_or_barcodes_attached, files_uploaded=files_uploaded, barcodes_entered=barcodes_entered, electronic_transfer=electronic_transfer, internal_notes=internal_notes, in_hand_date_from=in_hand_date_from, in_hand_date_to=in_hand_date_to, fulfillment_date_from=fulfillment_date_from, fulfillment_date_to=fulfillment_date_to, purchase_date_from=purchase_date_from, purchase_date_to=purchase_date_to, cooperative=cooperative, received=received, invoice_notes=invoice_notes, public_notes=public_notes, state=state, country=country, due=due, invoice_created_by=invoice_created_by, created_by_user_id=created_by_user_id, day_of_week=day_of_week, last_update_from=last_update_from, invoice_notes_user_id=invoice_notes_user_id, consignment=consignment, customer_type=customer_type, exclude_parking=exclude_parking, min_total_cost=min_total_cost, max_total_cost=max_total_cost)
        print("The response of InventoryApi->inventory_search_sold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_search_sold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 
 **event_id** | [**List[int]**](int.md)| Event Id to search on | [optional] 
 **inventory_id** | [**List[int]**](int.md)| Inventory Id to search on | [optional] 
 **exchange_pos_id** | [**List[int]**](int.md)| Exchange pos Id filter | [optional] 
 **invoice_id** | [**List[int]**](int.md)| Invoice Id to search on | [optional] 
 **purchase_ids** | [**List[int]**](int.md)| Purchase Id to search on | [optional] 
 **vendor_id** | **int**| Vendor Id to search on | [optional] 
 **event_type** | **str**| Event Type to search on | [optional] 
 **category_id** | [**List[int]**](int.md)| Category Id filter | [optional] 
 **tag** | [**List[str]**](str.md)| Tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| Tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **anti_event_tag** | [**List[str]**](str.md)| Event tags to exclude | [optional] 
 **anti_event_tags_match_all** | **bool**| Whether the results should not have all the event tags or only some | [optional] 
 **no_tags** | **bool**| Whether the results should have tags | [optional] 
 **invoice_tag** | [**List[str]**](str.md)| Invoice tags to include | [optional] 
 **invoice_tags_match_all** | **bool**| Whether the results should have all invoice tags or only some | [optional] 
 **event_tag** | [**List[str]**](str.md)| Event tags to include | [optional] 
 **event_tags_match_all** | **bool**| Whether the results should have all event tags or only some | [optional] 
 **purchase_tag** | [**List[str]**](str.md)| Purchase tags to include | [optional] 
 **purchase_tags_match_all** | **bool**| Whether the results should have all purchase tags or only some | [optional] 
 **customer_id** | **int**| Customer Id to filter | [optional] 
 **customer_display_name** | **str**| Customer display name filter | [optional] 
 **performer_id** | **int**| Performer Id filter | [optional] 
 **performer** | **str**| Performer to search on | [optional] 
 **event_keywords** | [**List[str]**](str.md)| Event keywords filter | [optional] 
 **event** | **str**| Event to search on | [optional] 
 **event_date_from** | **datetime**| From event date filter | [optional] 
 **event_date_to** | **datetime**| To event date filter | [optional] 
 **venue_id** | **int**| Venue Id filter | [optional] 
 **venue** | **str**| Venue search filter | [optional] 
 **section** | **str**| Section search filter | [optional] 
 **row** | **str**| Row search filter | [optional] 
 **includes_seat** | **int**| Seat search filter | [optional] 
 **invoice_date_from** | **datetime**| Invoice date from range filter | [optional] 
 **invoice_date_to** | **datetime**| Invoice date to range filter | [optional] 
 **currency_code** | **str**| Currency type search filter | [optional] 
 **external_ref** | [**List[str]**](str.md)| Invoice external ref filter | [optional] 
 **purchase_external_ref** | **str**| Purchase external ref filter | [optional] 
 **payment_status** | [**List[str]**](str.md)| Payment status to search on | [optional] 
 **invoice_status** | [**List[str]**](str.md)| Invoice status search filter | [optional] 
 **fulfillment_status** | **str**| Fulfillment status search filter | [optional] 
 **stock_type** | **str**| Stock Type search filter | [optional] 
 **zone_seating** | **bool**| Whether the results should have zone seating | [optional] 
 **pdfs_or_barcodes_attached** | **bool**| Whether the results should have Pdfs or Bar Codes attached to all tickets | [optional] 
 **files_uploaded** | **bool**| Whether the results should have Pdfs attached to all tickets | [optional] 
 **barcodes_entered** | **bool**| Whether the results should have Bar Codes entered in all tickets | [optional] 
 **electronic_transfer** | **bool**| Whether the results should have electronic transfer | [optional] 
 **internal_notes** | **str**| Internal notes search filter | [optional] 
 **in_hand_date_from** | **datetime**| From in hand date filter | [optional] 
 **in_hand_date_to** | **datetime**| To in hand date filter | [optional] 
 **fulfillment_date_from** | **datetime**| From fulfillment date filter | [optional] 
 **fulfillment_date_to** | **datetime**| To fulfillment date filter | [optional] 
 **purchase_date_from** | **datetime**| Purchase date from range filter | [optional] 
 **purchase_date_to** | **datetime**| Purchase date to range filter | [optional] 
 **cooperative** | **bool**| Whether the results are cooperative | [optional] 
 **received** | **bool**| Whether the results are received | [optional] 
 **invoice_notes** | **str**| Invoice notes search filter | [optional] 
 **public_notes** | **str**| Public notes search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **country** | [**List[str]**](str.md)| Country search filter | [optional] 
 **due** | **bool**| Whether the inventories are due or not | [optional] 
 **invoice_created_by** | **str**| Email search filter for invoice creator | [optional] 
 **created_by_user_id** | **int**| User id of invoice creator | [optional] 
 **day_of_week** | [**List[int]**](int.md)| Day of the week of events that occur on that day of the week | [optional] 
 **last_update_from** | **datetime**| Inventory last update date from range filter | [optional] 
 **invoice_notes_user_id** | **int**| Invoice notes user id search filter | [optional] 
 **consignment** | **str**| Whether the results have a consignment type POs | [optional] 
 **customer_type** | **str**| Whether the results have a customer type of the Invoice | [optional] 
 **exclude_parking** | **bool**| Whether parking events are excluded | [optional] 
 **min_total_cost** | **float**| Minimum total cost search filter | [optional] 
 **max_total_cost** | **float**| Maximum total cost search filter | [optional] 

### Return type

[**List[SoldInventorySummary]**](SoldInventorySummary.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | sold inventory summaries returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_sold_bulk_swap_event**
> inventory_sold_bulk_swap_event(bulk_sold_swap_event_request)



Sold bulk swap event

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.bulk_sold_swap_event_request import BulkSoldSwapEventRequest
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    bulk_sold_swap_event_request = skybox_openapi_client.BulkSoldSwapEventRequest() # BulkSoldSwapEventRequest | Payload

    try:
        api_instance.inventory_sold_bulk_swap_event(bulk_sold_swap_event_request)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_sold_bulk_swap_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_sold_swap_event_request** | [**BulkSoldSwapEventRequest**](BulkSoldSwapEventRequest.md)| Payload | 

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
**200** | Event swapped |  -  |
**401** | not authorized |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_split**
> List[float] inventory_split(inventory_id, body)



Splits inventory into 2 new inventory groups

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The ID of the inventory to update
    body = 56 # int | The ticket quantity of the first group

    try:
        api_response = api_instance.inventory_split(inventory_id, body)
        print("The response of InventoryApi->inventory_split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_split: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The ID of the inventory to update | 
 **body** | **int**| The ticket quantity of the first group | 

### Return type

**List[float]**

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory split, the new inventory id is returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_split_to_consecutive**
> List[float] inventory_split_to_consecutive(inventory_id)



Splits inventory into 2 new inventory consecutive groups

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The ID of the inventory to update

    try:
        api_response = api_instance.inventory_split_to_consecutive(inventory_id)
        print("The response of InventoryApi->inventory_split_to_consecutive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_split_to_consecutive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The ID of the inventory to update | 

### Return type

**List[float]**

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory split, the new inventory id is returned |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_split_to_originals**
> List[Inventory] inventory_split_to_originals(inventory_id)



Splits and merges inventories to leave them as they were when purchased

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The Id of the inventory to split

    try:
        api_response = api_instance.inventory_split_to_originals(inventory_id)
        print("The response of InventoryApi->inventory_split_to_originals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_split_to_originals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The Id of the inventory to split | 

### Return type

[**List[Inventory]**](Inventory.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | split was successful |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_sync**
> inventory_sync(sync_inventory_request)



Sync Inventory with integrated services

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.sync_inventory_request import SyncInventoryRequest
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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    sync_inventory_request = skybox_openapi_client.SyncInventoryRequest() # SyncInventoryRequest | The inventory Ids to sync

    try:
        api_instance.inventory_sync(sync_inventory_request)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_inventory_request** | [**SyncInventoryRequest**](SyncInventoryRequest.md)| The inventory Ids to sync | 

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
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_tag**
> inventory_tag(inventory_id, tag_request)



Inserts a new tags for an inventory. Duplicates are ignored

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The Id of the inventory
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to add

    try:
        api_instance.inventory_tag(inventory_id, tag_request)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The Id of the inventory | 
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

# **inventory_update**
> inventory_update(inventory_id, inventory, change_seat_numbers=change_seat_numbers)



Update Inventory

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    inventory_id = 56 # int | The Id of the inventory to update
    inventory = skybox_openapi_client.Inventory() # Inventory | Inventory update
    change_seat_numbers = True # bool | Whether is allow to change seat number (optional)

    try:
        api_instance.inventory_update(inventory_id, inventory, change_seat_numbers=change_seat_numbers)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **int**| The Id of the inventory to update | 
 **inventory** | [**Inventory**](Inventory.md)| Inventory update | 
 **change_seat_numbers** | **bool**| Whether is allow to change seat number | [optional] 

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
**200** | inventory updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_update_purchase_inventory**
> inventory_update_purchase_inventory(update_purchase_inventory_request)



Updates section and row for an inventory

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
    api_instance = skybox_openapi_client.InventoryApi(api_client)
    update_purchase_inventory_request = skybox_openapi_client.UpdatePurchaseInventoryRequest() # UpdatePurchaseInventoryRequest | 

    try:
        api_instance.inventory_update_purchase_inventory(update_purchase_inventory_request)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_update_purchase_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

