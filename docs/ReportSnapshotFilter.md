# ReportSnapshotFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | [optional] 
**label_value** | **str** |  | [optional] 
**value** | **object** |  | 
**type** | **str** |  | [optional] 
**gmt** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.report_snapshot_filter import ReportSnapshotFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSnapshotFilter from a JSON string
report_snapshot_filter_instance = ReportSnapshotFilter.from_json(json)
# print the JSON string representation of the object
print(ReportSnapshotFilter.to_json())

# convert the object into a dict
report_snapshot_filter_dict = report_snapshot_filter_instance.to_dict()
# create an instance of ReportSnapshotFilter from a dict
report_snapshot_filter_from_dict = ReportSnapshotFilter.from_dict(report_snapshot_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


