# ReportDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | 
**help** | **str** |  | [optional] 
**is_filtering_required** | **bool** |  | [optional] 
**parameters** | [**List[ReportParameter]**](ReportParameter.md) |  | 
**groups** | [**List[ReportGroup]**](ReportGroup.md) |  | [optional] 
**columns** | [**List[ReportColumn]**](ReportColumn.md) |  | 
**validations** | **List[str]** |  | 
**mapper_method_name** | **str** |  | 
**default_sorted_by** | **str** |  | 
**default_sort_dir** | **str** |  | 
**sorting_disabled** | **bool** |  | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.report_definition import ReportDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDefinition from a JSON string
report_definition_instance = ReportDefinition.from_json(json)
# print the JSON string representation of the object
print(ReportDefinition.to_json())

# convert the object into a dict
report_definition_dict = report_definition_instance.to_dict()
# create an instance of ReportDefinition from a dict
report_definition_from_dict = ReportDefinition.from_dict(report_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


