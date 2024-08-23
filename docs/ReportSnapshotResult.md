# ReportSnapshotResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**schedule_id** | **int** |  | [optional] 
**report_id** | **int** |  | [optional] 
**filters** | [**List[ReportSnapshotFilter]**](ReportSnapshotFilter.md) |  | [optional] 
**asset_name** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**scheduled_date** | **datetime** |  | [optional] 
**number** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**notification_emails** | **List[str]** |  | [optional] 
**report** | [**Report**](Report.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.report_snapshot_result import ReportSnapshotResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSnapshotResult from a JSON string
report_snapshot_result_instance = ReportSnapshotResult.from_json(json)
# print the JSON string representation of the object
print(ReportSnapshotResult.to_json())

# convert the object into a dict
report_snapshot_result_dict = report_snapshot_result_instance.to_dict()
# create an instance of ReportSnapshotResult from a dict
report_snapshot_result_from_dict = ReportSnapshotResult.from_dict(report_snapshot_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


