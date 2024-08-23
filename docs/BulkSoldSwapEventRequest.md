# BulkSoldSwapEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_line_ids** | **List[int]** | Line ids whose event will be swapped. | 
**event_id** | **int** | The new event id for the lines items. | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_sold_swap_event_request import BulkSoldSwapEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSoldSwapEventRequest from a JSON string
bulk_sold_swap_event_request_instance = BulkSoldSwapEventRequest.from_json(json)
# print the JSON string representation of the object
print(BulkSoldSwapEventRequest.to_json())

# convert the object into a dict
bulk_sold_swap_event_request_dict = bulk_sold_swap_event_request_instance.to_dict()
# create an instance of BulkSoldSwapEventRequest from a dict
bulk_sold_swap_event_request_from_dict = BulkSoldSwapEventRequest.from_dict(bulk_sold_swap_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


