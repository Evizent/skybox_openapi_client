# BulkSwapEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_ids** | **List[int]** | Inventory ids whose event will be swapped. | [optional] 
**event_id** | **int** | The new event id for the inventory items. | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_swap_event_request import BulkSwapEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSwapEventRequest from a JSON string
bulk_swap_event_request_instance = BulkSwapEventRequest.from_json(json)
# print the JSON string representation of the object
print(BulkSwapEventRequest.to_json())

# convert the object into a dict
bulk_swap_event_request_dict = bulk_swap_event_request_instance.to_dict()
# create an instance of BulkSwapEventRequest from a dict
bulk_swap_event_request_from_dict = BulkSwapEventRequest.from_dict(bulk_swap_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


