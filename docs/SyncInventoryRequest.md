# SyncInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_ids** | **List[int]** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.sync_inventory_request import SyncInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncInventoryRequest from a JSON string
sync_inventory_request_instance = SyncInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(SyncInventoryRequest.to_json())

# convert the object into a dict
sync_inventory_request_dict = sync_inventory_request_instance.to_dict()
# create an instance of SyncInventoryRequest from a dict
sync_inventory_request_from_dict = SyncInventoryRequest.from_dict(sync_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


