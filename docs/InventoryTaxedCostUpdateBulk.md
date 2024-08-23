# InventoryTaxedCostUpdateBulk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_taxed_cost** | **float** | Amount to increase or decrease each taxed cost ticket by | 
**id** | **int** | ID of inventory to update | 

## Example

```python
from skybox_openapi_client.models.inventory_taxed_cost_update_bulk import InventoryTaxedCostUpdateBulk

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryTaxedCostUpdateBulk from a JSON string
inventory_taxed_cost_update_bulk_instance = InventoryTaxedCostUpdateBulk.from_json(json)
# print the JSON string representation of the object
print(InventoryTaxedCostUpdateBulk.to_json())

# convert the object into a dict
inventory_taxed_cost_update_bulk_dict = inventory_taxed_cost_update_bulk_instance.to_dict()
# create an instance of InventoryTaxedCostUpdateBulk from a dict
inventory_taxed_cost_update_bulk_from_dict = InventoryTaxedCostUpdateBulk.from_dict(inventory_taxed_cost_update_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


