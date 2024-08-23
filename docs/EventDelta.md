# EventDelta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**event_id** | **int** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**venue_id** | **int** |  | [optional] 
**change_date** | **datetime** |  | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.event_delta import EventDelta

# TODO update the JSON string below
json = "{}"
# create an instance of EventDelta from a JSON string
event_delta_instance = EventDelta.from_json(json)
# print the JSON string representation of the object
print(EventDelta.to_json())

# convert the object into a dict
event_delta_dict = event_delta_instance.to_dict()
# create an instance of EventDelta from a dict
event_delta_from_dict = EventDelta.from_dict(event_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


