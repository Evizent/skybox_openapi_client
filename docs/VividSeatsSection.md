# VividSeatsSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**group_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**section_id** | **int** |  | [optional] 
**pattern** | **List[str]** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.vivid_seats_section import VividSeatsSection

# TODO update the JSON string below
json = "{}"
# create an instance of VividSeatsSection from a JSON string
vivid_seats_section_instance = VividSeatsSection.from_json(json)
# print the JSON string representation of the object
print(VividSeatsSection.to_json())

# convert the object into a dict
vivid_seats_section_dict = vivid_seats_section_instance.to_dict()
# create an instance of VividSeatsSection from a dict
vivid_seats_section_from_dict = VividSeatsSection.from_dict(vivid_seats_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


