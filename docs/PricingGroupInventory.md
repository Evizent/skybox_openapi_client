# PricingGroupInventory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**operation** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.pricing_group_inventory import PricingGroupInventory

# TODO update the JSON string below
json = "{}"
# create an instance of PricingGroupInventory from a JSON string
pricing_group_inventory_instance = PricingGroupInventory.from_json(json)
# print the JSON string representation of the object
print(PricingGroupInventory.to_json())

# convert the object into a dict
pricing_group_inventory_dict = pricing_group_inventory_instance.to_dict()
# create an instance of PricingGroupInventory from a dict
pricing_group_inventory_from_dict = PricingGroupInventory.from_dict(pricing_group_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


