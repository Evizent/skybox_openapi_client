# InventoryMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** |  | 
**venue_name** | **str** |  | 
**event_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**purchase_line_id** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**response_status** | **int** |  | [optional] 
**send_count** | **int** |  | [optional] 
**mapped_by_user_id** | **int** |  | [optional] 
**mapped_date** | **datetime** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.inventory_mapping import InventoryMapping

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryMapping from a JSON string
inventory_mapping_instance = InventoryMapping.from_json(json)
# print the JSON string representation of the object
print(InventoryMapping.to_json())

# convert the object into a dict
inventory_mapping_dict = inventory_mapping_instance.to_dict()
# create an instance of InventoryMapping from a dict
inventory_mapping_from_dict = InventoryMapping.from_dict(inventory_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


