# InventoryBarcodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_pos_id** | **int** |  | [optional] 
**inventory_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**section** | **str** |  | [optional] 
**row** | **str** |  | [optional] 
**seat_number** | **int** |  | [optional] 
**bar_code** | **str** |  | [optional] 
**external_ticket_id** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.inventory_barcode_response import InventoryBarcodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryBarcodeResponse from a JSON string
inventory_barcode_response_instance = InventoryBarcodeResponse.from_json(json)
# print the JSON string representation of the object
print(InventoryBarcodeResponse.to_json())

# convert the object into a dict
inventory_barcode_response_dict = inventory_barcode_response_instance.to_dict()
# create an instance of InventoryBarcodeResponse from a dict
inventory_barcode_response_from_dict = InventoryBarcodeResponse.from_dict(inventory_barcode_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


