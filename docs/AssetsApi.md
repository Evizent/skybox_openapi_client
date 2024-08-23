# skybox_openapi_client.AssetsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_get**](AssetsApi.md#assets_get) | **GET** /assets/{filename} | 
[**assets_upload**](AssetsApi.md#assets_upload) | **POST** /assets | 


# **assets_get**
> assets_get(filename)



Retrieves a file, base64 encoded

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
    api_instance = skybox_openapi_client.AssetsApi(api_client)
    filename = 'filename_example' # str | Asset file name

    try:
        api_instance.assets_get(filename)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Asset file name | 

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
**200** | File returned |  -  |
**401** | not authorized |  -  |
**500** | error contacting file store |  -  |
**404** | file not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_upload**
> PdfDetails assets_upload(pdf_upload)



Uploads a PDF and returns a list of details

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.pdf_details import PdfDetails
from skybox_openapi_client.models.pdf_upload import PdfUpload
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
    api_instance = skybox_openapi_client.AssetsApi(api_client)
    pdf_upload = skybox_openapi_client.PdfUpload() # PdfUpload | The byte array of the PDF

    try:
        api_response = api_instance.assets_upload(pdf_upload)
        print("The response of AssetsApi->assets_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_upload** | [**PdfUpload**](PdfUpload.md)| The byte array of the PDF | 

### Return type

[**PdfDetails**](PdfDetails.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF stored |  -  |
**401** | not authorized |  -  |
**500** | error storing PDF |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

