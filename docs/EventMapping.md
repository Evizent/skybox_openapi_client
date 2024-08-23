# EventMapping

Event mapping information, required on inserts if eventId is empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** |  | 
**venue_name** | **str** |  | 
**event_date** | **datetime** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.event_mapping import EventMapping

# TODO update the JSON string below
json = "{}"
# create an instance of EventMapping from a JSON string
event_mapping_instance = EventMapping.from_json(json)
# print the JSON string representation of the object
print(EventMapping.to_json())

# convert the object into a dict
event_mapping_dict = event_mapping_instance.to_dict()
# create an instance of EventMapping from a dict
event_mapping_from_dict = EventMapping.from_dict(event_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


