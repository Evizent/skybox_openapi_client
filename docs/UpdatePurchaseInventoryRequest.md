# UpdatePurchaseInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_id** | **int** |  | [optional] 
**friendly_section** | **str** | Friendly Section | [optional] 
**section** | **str** |  | 
**friendly_row** | **str** | Friendly Row | [optional] 
**row** | **str** |  | 
**second_row** | **str** |  | [optional] 
**force** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.update_purchase_inventory_request import UpdatePurchaseInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseInventoryRequest from a JSON string
update_purchase_inventory_request_instance = UpdatePurchaseInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseInventoryRequest.to_json())

# convert the object into a dict
update_purchase_inventory_request_dict = update_purchase_inventory_request_instance.to_dict()
# create an instance of UpdatePurchaseInventoryRequest from a dict
update_purchase_inventory_request_from_dict = UpdatePurchaseInventoryRequest.from_dict(update_purchase_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


