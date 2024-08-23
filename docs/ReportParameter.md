# ReportParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**default_value** | **str** |  | [optional] 
**options** | **List[object]** |  | [optional] 
**gmt** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**is_illegal_filter** | **bool** |  | [optional] 
**default_hidden** | **bool** |  | [optional] 
**disable_all_any_selector** | **bool** |  | [optional] 
**table** | **str** |  | [optional] 
**column** | **str** |  | [optional] 
**pattern** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**is_multi** | **bool** |  | [optional] 
**illegal_filter** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.report_parameter import ReportParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ReportParameter from a JSON string
report_parameter_instance = ReportParameter.from_json(json)
# print the JSON string representation of the object
print(ReportParameter.to_json())

# convert the object into a dict
report_parameter_dict = report_parameter_instance.to_dict()
# create an instance of ReportParameter from a dict
report_parameter_from_dict = ReportParameter.from_dict(report_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


