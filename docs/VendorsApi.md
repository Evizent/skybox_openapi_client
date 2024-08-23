# skybox_openapi_client.VendorsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendors_bulk_remove_tags**](VendorsApi.md#vendors_bulk_remove_tags) | **POST** /vendors/tags/remove | 
[**vendors_bulk_update**](VendorsApi.md#vendors_bulk_update) | **PUT** /vendors/bulk | 
[**vendors_delete**](VendorsApi.md#vendors_delete) | **POST** /vendors/{vendor-id}/tags/actions/delete | 
[**vendors_get_by_id**](VendorsApi.md#vendors_get_by_id) | **GET** /vendors/{vendor-id} | 
[**vendors_get_default**](VendorsApi.md#vendors_get_default) | **GET** /vendors/default | 
[**vendors_insert**](VendorsApi.md#vendors_insert) | **POST** /vendors | 
[**vendors_search**](VendorsApi.md#vendors_search) | **GET** /vendors | 
[**vendors_tag**](VendorsApi.md#vendors_tag) | **POST** /vendors/{vendor-id}/tags | 
[**vendors_update**](VendorsApi.md#vendors_update) | **PUT** /vendors/{vendor-id} | 
[**vendors_update_default_vendor**](VendorsApi.md#vendors_update_default_vendor) | **PUT** /vendors/default | 


# **vendors_bulk_remove_tags**
> vendors_bulk_remove_tags(request_body)



Deletes all tags from vendors with given ids

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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    request_body = [56] # List[int] | Vendor Ids

    try:
        api_instance.vendors_bulk_remove_tags(request_body)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_bulk_remove_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)| Vendor Ids | 

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

# **vendors_bulk_update**
> vendors_bulk_update(bulk_vendor_update)



Bulk Vendor Update

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.bulk_vendor_update import BulkVendorUpdate
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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    bulk_vendor_update = skybox_openapi_client.BulkVendorUpdate() # BulkVendorUpdate | Bulk vendor update

    try:
        api_instance.vendors_bulk_update(bulk_vendor_update)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_vendor_update** | [**BulkVendorUpdate**](BulkVendorUpdate.md)| Bulk vendor update | 

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

# **vendors_delete**
> vendors_delete(vendor_id, tag_request)



Deletes tags for a vendor

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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    vendor_id = 56 # int | The vendor Id
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to be removed from the vendor

    try:
        api_instance.vendors_delete(vendor_id, tag_request)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| The vendor Id | 
 **tag_request** | [**List[TagRequest]**](TagRequest.md)| Tags to be removed from the vendor | 

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

# **vendors_get_by_id**
> Vendor vendors_get_by_id(vendor_id)



Retrieves a vendor by the vendor id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.vendor import Vendor
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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    vendor_id = 56 # int | The id of the vendor

    try:
        api_response = api_instance.vendors_get_by_id(vendor_id)
        print("The response of VendorsApi->vendors_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| The id of the vendor | 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | vendor returned |  -  |
**401** | not authorized |  -  |
**404** | vendor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_get_default**
> vendors_get_default()



Retrieves the default vendor for the account

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
    api_instance = skybox_openapi_client.VendorsApi(api_client)

    try:
        api_instance.vendors_get_default()
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_get_default: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | default vendor returned |  -  |
**401** | not authorized |  -  |
**404** | default vendor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_insert**
> List[Vendor] vendors_insert(vendor)



Creates vendors

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.vendor import Vendor
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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    vendor = skybox_openapi_client.Vendor() # Vendor | A vendor object to create.

    try:
        api_response = api_instance.vendors_insert(vendor)
        print("The response of VendorsApi->vendors_insert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_insert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor** | [**Vendor**](Vendor.md)| A vendor object to create. | 

### Return type

[**List[Vendor]**](Vendor.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | vendor created |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_search**
> List[Vendor] vendors_search(limit=limit, sort_dir=sort_dir, page_number=page_number, id=id, vendor_type=vendor_type, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, display_name=display_name, email=email, last_name=last_name, company=company, city=city, state=state, country=country, phone=phone, sorted_by=sorted_by)



Retrieves all vendors

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.vendor import Vendor
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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    limit = 56 # int | Number of results per page (optional)
    sort_dir = 'sort_dir_example' # str | Direction to sort (optional)
    page_number = 56 # int | Page number of results to show (optional)
    id = [56] # List[int] | Vendor Id search filter (optional)
    vendor_type = ['vendor_type_example'] # List[str] | Vendor type search filter (optional)
    tag = ['tag_example'] # List[str] | Tags to include (optional)
    tags_match_all = True # bool | Whether the results should have all the tags or only some (optional)
    anti_tag = ['anti_tag_example'] # List[str] | Tags to exclude (optional)
    anti_tags_match_all = True # bool | Whether the results should not have all the tags or only some (optional)
    display_name = 'display_name_example' # str | Vendor display name search filter (optional)
    email = 'email_example' # str | Email search filter (optional)
    last_name = 'last_name_example' # str | Last name search filter (optional)
    company = 'company_example' # str | Company search filter (optional)
    city = 'city_example' # str | City search filter (optional)
    state = ['state_example'] # List[str] | State search filter (optional)
    country = ['country_example'] # List[str] | Country search filter (optional)
    phone = 'phone_example' # str | Phone number to search by (matching phone 1 and phone 2 fields) (optional)
    sorted_by = 'sorted_by_example' # str | Field to sort by (optional)

    try:
        api_response = api_instance.vendors_search(limit=limit, sort_dir=sort_dir, page_number=page_number, id=id, vendor_type=vendor_type, tag=tag, tags_match_all=tags_match_all, anti_tag=anti_tag, anti_tags_match_all=anti_tags_match_all, display_name=display_name, email=email, last_name=last_name, company=company, city=city, state=state, country=country, phone=phone, sorted_by=sorted_by)
        print("The response of VendorsApi->vendors_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page | [optional] 
 **sort_dir** | **str**| Direction to sort | [optional] 
 **page_number** | **int**| Page number of results to show | [optional] 
 **id** | [**List[int]**](int.md)| Vendor Id search filter | [optional] 
 **vendor_type** | [**List[str]**](str.md)| Vendor type search filter | [optional] 
 **tag** | [**List[str]**](str.md)| Tags to include | [optional] 
 **tags_match_all** | **bool**| Whether the results should have all the tags or only some | [optional] 
 **anti_tag** | [**List[str]**](str.md)| Tags to exclude | [optional] 
 **anti_tags_match_all** | **bool**| Whether the results should not have all the tags or only some | [optional] 
 **display_name** | **str**| Vendor display name search filter | [optional] 
 **email** | **str**| Email search filter | [optional] 
 **last_name** | **str**| Last name search filter | [optional] 
 **company** | **str**| Company search filter | [optional] 
 **city** | **str**| City search filter | [optional] 
 **state** | [**List[str]**](str.md)| State search filter | [optional] 
 **country** | [**List[str]**](str.md)| Country search filter | [optional] 
 **phone** | **str**| Phone number to search by (matching phone 1 and phone 2 fields) | [optional] 
 **sorted_by** | **str**| Field to sort by | [optional] 

### Return type

[**List[Vendor]**](Vendor.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | vendors returned |  -  |
**401** | not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_tag**
> vendors_tag(vendor_id, tag_request)



Inserts a new tags for a vendor. Duplicates are ignored

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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    vendor_id = 56 # int | The id of the vendor
    tag_request = [skybox_openapi_client.TagRequest()] # List[TagRequest] | Tags to add

    try:
        api_instance.vendors_tag(vendor_id, tag_request)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| The id of the vendor | 
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

# **vendors_update**
> Vendor vendors_update(vendor_id, vendor)



Updates a vendor

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.vendor import Vendor
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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    vendor_id = 56 # int | The id of the vendor
    vendor = skybox_openapi_client.Vendor() # Vendor | The vendor object to update.

    try:
        api_response = api_instance.vendors_update(vendor_id, vendor)
        print("The response of VendorsApi->vendors_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| The id of the vendor | 
 **vendor** | [**Vendor**](Vendor.md)| The vendor object to update. | 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | vendor updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_update_default_vendor**
> vendors_update_default_vendor(body)



Sets the default vendor for the account

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
    api_instance = skybox_openapi_client.VendorsApi(api_client)
    body = 56 # int | The vendor id of the default vendor

    try:
        api_instance.vendors_update_default_vendor(body)
    except Exception as e:
        print("Exception when calling VendorsApi->vendors_update_default_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **int**| The vendor id of the default vendor | 

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
**200** | default vendor updated |  -  |
**401** | not authorized |  -  |
**400** | invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

