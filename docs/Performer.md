# Performer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.performer import Performer

# TODO update the JSON string below
json = "{}"
# create an instance of Performer from a JSON string
performer_instance = Performer.from_json(json)
# print the JSON string representation of the object
print(Performer.to_json())

# convert the object into a dict
performer_dict = performer_instance.to_dict()
# create an instance of Performer from a dict
performer_from_dict = Performer.from_dict(performer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


