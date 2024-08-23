# EventPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 
**performer_id** | **int** |  | [optional] 
**performer** | [**Performer**](Performer.md) |  | [optional] 
**keywords** | **str** |  | [optional] 
**chart_url** | **str** |  | [optional] 
**stubhub_event_id** | **int** |  | [optional] 
**stubhub_event_url** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**ei_event_id** | **int** |  | [optional] 
**opt_out_replenishment** | **bool** |  | [optional] 
**ticket_count** | **int** |  | [optional] 
**my_sold_tickets** | **int** |  | [optional] 
**my_cancelled_tickets** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**quantity** | **int** |  | [optional] 
**cost** | **float** |  | [optional] 
**last_price_update** | **datetime** |  | [optional] 
**listing_count** | **int** |  | [optional] 
**vivid_seats_event_url** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.event_position import EventPosition

# TODO update the JSON string below
json = "{}"
# create an instance of EventPosition from a JSON string
event_position_instance = EventPosition.from_json(json)
# print the JSON string representation of the object
print(EventPosition.to_json())

# convert the object into a dict
event_position_dict = event_position_instance.to_dict()
# create an instance of EventPosition from a dict
event_position_from_dict = EventPosition.from_dict(event_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


