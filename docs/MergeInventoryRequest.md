# MergeInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_ids** | **List[int]** | Inventory id&#39;s which will be merged. | 
**public_notes** | **str** | Public notes of the merged inventory. | [optional] 
**merging_type** | **str** | Strategy to merge public notes in the inventory | [optional] 

## Example

```python
from skybox_openapi_client.models.merge_inventory_request import MergeInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeInventoryRequest from a JSON string
merge_inventory_request_instance = MergeInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(MergeInventoryRequest.to_json())

# convert the object into a dict
merge_inventory_request_dict = merge_inventory_request_instance.to_dict()
# create an instance of MergeInventoryRequest from a dict
merge_inventory_request_from_dict = MergeInventoryRequest.from_dict(merge_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


