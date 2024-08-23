# InventoryFaceValueUpdateBulk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_face_value** | **float** | Amount to increase or decrease each face value ticket by | 
**id** | **int** | ID of inventory to update | 

## Example

```python
from skybox_openapi_client.models.inventory_face_value_update_bulk import InventoryFaceValueUpdateBulk

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryFaceValueUpdateBulk from a JSON string
inventory_face_value_update_bulk_instance = InventoryFaceValueUpdateBulk.from_json(json)
# print the JSON string representation of the object
print(InventoryFaceValueUpdateBulk.to_json())

# convert the object into a dict
inventory_face_value_update_bulk_dict = inventory_face_value_update_bulk_instance.to_dict()
# create an instance of InventoryFaceValueUpdateBulk from a dict
inventory_face_value_update_bulk_from_dict = InventoryFaceValueUpdateBulk.from_dict(inventory_face_value_update_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


