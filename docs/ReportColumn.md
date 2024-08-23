# ReportColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**data_expression** | **str** |  | [optional] 
**total** | **bool** |  | [optional] 
**total_expression** | **str** |  | [optional] 
**default_hidden** | **bool** |  | [optional] 
**max_length** | **int** |  | [optional] 
**enum_name** | **str** |  | [optional] 
**link_expression** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**align** | **str** |  | [optional] 
**copy_to_clipboard** | **bool** |  | [optional] 
**click_expression** | **str** |  | [optional] 
**minimum** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.report_column import ReportColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ReportColumn from a JSON string
report_column_instance = ReportColumn.from_json(json)
# print the JSON string representation of the object
print(ReportColumn.to_json())

# convert the object into a dict
report_column_dict = report_column_instance.to_dict()
# create an instance of ReportColumn from a dict
report_column_from_dict = ReportColumn.from_dict(report_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


