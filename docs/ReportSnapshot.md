# ReportSnapshot


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

## Example

```python
from skybox_openapi_client.models.report_snapshot import ReportSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSnapshot from a JSON string
report_snapshot_instance = ReportSnapshot.from_json(json)
# print the JSON string representation of the object
print(ReportSnapshot.to_json())

# convert the object into a dict
report_snapshot_dict = report_snapshot_instance.to_dict()
# create an instance of ReportSnapshot from a dict
report_snapshot_from_dict = ReportSnapshot.from_dict(report_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


