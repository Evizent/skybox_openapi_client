# InventoryPriceHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**action** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**date_of_action** | **datetime** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.inventory_price_history import InventoryPriceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryPriceHistory from a JSON string
inventory_price_history_instance = InventoryPriceHistory.from_json(json)
# print the JSON string representation of the object
print(InventoryPriceHistory.to_json())

# convert the object into a dict
inventory_price_history_dict = inventory_price_history_instance.to_dict()
# create an instance of InventoryPriceHistory from a dict
inventory_price_history_from_dict = InventoryPriceHistory.from_dict(inventory_price_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


