# VividSeatsMapGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**map_id** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.vivid_seats_map_groups import VividSeatsMapGroups

# TODO update the JSON string below
json = "{}"
# create an instance of VividSeatsMapGroups from a JSON string
vivid_seats_map_groups_instance = VividSeatsMapGroups.from_json(json)
# print the JSON string representation of the object
print(VividSeatsMapGroups.to_json())

# convert the object into a dict
vivid_seats_map_groups_dict = vivid_seats_map_groups_instance.to_dict()
# create an instance of VividSeatsMapGroups from a dict
vivid_seats_map_groups_from_dict = VividSeatsMapGroups.from_dict(vivid_seats_map_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


