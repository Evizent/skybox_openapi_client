# skybox_openapi_client.ReportsApi

All URIs are relative to *https://skybox.vividseats.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_get_report_snapshot**](ReportsApi.md#reports_get_report_snapshot) | **GET** /reports/snapshots/{id} | 
[**reports_query_report_snapshots**](ReportsApi.md#reports_query_report_snapshots) | **GET** /reports/snapshots | 


# **reports_get_report_snapshot**
> ReportSnapshotResult reports_get_report_snapshot(id)



Retrieves a snapshot by the snapshot id

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.report_snapshot_result import ReportSnapshotResult
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
    api_instance = skybox_openapi_client.ReportsApi(api_client)
    id = 56 # int | The id of the snapshot

    try:
        api_response = api_instance.reports_get_report_snapshot(id)
        print("The response of ReportsApi->reports_get_report_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_get_report_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the snapshot | 

### Return type

[**ReportSnapshotResult**](ReportSnapshotResult.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot returned |  -  |
**401** | not authorized |  -  |
**404** | Snapshots not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_query_report_snapshots**
> List[ReportSnapshot] reports_query_report_snapshots(report_id=report_id, snapshot_date_from=snapshot_date_from, snapshot_date_to=snapshot_date_to)



Searches snapshots

### Example

* Api Key Authentication (Account):
* Api Key Authentication (Authorization_Token):
* Api Key Authentication (Application_Token):

```python
import skybox_openapi_client
from skybox_openapi_client.models.report_snapshot import ReportSnapshot
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
    api_instance = skybox_openapi_client.ReportsApi(api_client)
    report_id = 56 # int | Report Id search filter (optional)
    snapshot_date_from = '2013-10-20T19:20:30+01:00' # datetime | Snapshot creation date from range filter (optional)
    snapshot_date_to = '2013-10-20T19:20:30+01:00' # datetime | Snapshot creation date to range filter (optional)

    try:
        api_response = api_instance.reports_query_report_snapshots(report_id=report_id, snapshot_date_from=snapshot_date_from, snapshot_date_to=snapshot_date_to)
        print("The response of ReportsApi->reports_query_report_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->reports_query_report_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| Report Id search filter | [optional] 
 **snapshot_date_from** | **datetime**| Snapshot creation date from range filter | [optional] 
 **snapshot_date_to** | **datetime**| Snapshot creation date to range filter | [optional] 

### Return type

[**List[ReportSnapshot]**](ReportSnapshot.md)

### Authorization

[Account](../README.md#Account), [Authorization_Token](../README.md#Authorization_Token), [Application_Token](../README.md#Application_Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshots returned |  -  |
**401** | Not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

