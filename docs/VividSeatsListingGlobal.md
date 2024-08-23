# VividSeatsListingGlobal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**event_date** | **datetime** |  | [optional] 
**production_name** | **str** |  | [optional] 
**json_file_name** | **str** |  | [optional] 
**json_active** | **bool** |  | [optional] 
**static_map_url** | **str** |  | [optional] 
**map_title** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**dte** | **int** |  | [optional] 
**days_to_event** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.vivid_seats_listing_global import VividSeatsListingGlobal

# TODO update the JSON string below
json = "{}"
# create an instance of VividSeatsListingGlobal from a JSON string
vivid_seats_listing_global_instance = VividSeatsListingGlobal.from_json(json)
# print the JSON string representation of the object
print(VividSeatsListingGlobal.to_json())

# convert the object into a dict
vivid_seats_listing_global_dict = vivid_seats_listing_global_instance.to_dict()
# create an instance of VividSeatsListingGlobal from a dict
vivid_seats_listing_global_from_dict = VividSeatsListingGlobal.from_dict(vivid_seats_listing_global_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


