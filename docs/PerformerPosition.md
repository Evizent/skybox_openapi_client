# PerformerPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**cost** | **float** |  | [optional] 
**listing_count** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.performer_position import PerformerPosition

# TODO update the JSON string below
json = "{}"
# create an instance of PerformerPosition from a JSON string
performer_position_instance = PerformerPosition.from_json(json)
# print the JSON string representation of the object
print(PerformerPosition.to_json())

# convert the object into a dict
performer_position_dict = performer_position_instance.to_dict()
# create an instance of PerformerPosition from a dict
performer_position_from_dict = PerformerPosition.from_dict(performer_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


