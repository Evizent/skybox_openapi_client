# InventoryPriceUpdateBulk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_price** | **float** | Amount to increase or decrease each ticket by | 
**id** | **int** | ID of inventory to update | 
**broadcast** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.inventory_price_update_bulk import InventoryPriceUpdateBulk

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryPriceUpdateBulk from a JSON string
inventory_price_update_bulk_instance = InventoryPriceUpdateBulk.from_json(json)
# print the JSON string representation of the object
print(InventoryPriceUpdateBulk.to_json())

# convert the object into a dict
inventory_price_update_bulk_dict = inventory_price_update_bulk_instance.to_dict()
# create an instance of InventoryPriceUpdateBulk from a dict
inventory_price_update_bulk_from_dict = InventoryPriceUpdateBulk.from_dict(inventory_price_update_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


