# BulkPurchaseUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_ids** | **List[int]** | Purchase id&#39;s which will be updated. | 
**payment_status** | **str** | Payment status to update. | [optional] 
**external_ref** | **str** | External reference to update. | [optional] 
**received** | **bool** | Updates whether PO is received. | [optional] 
**currency_code** | **str** |  | [optional] 
**payment_ref** | **str** |  | [optional] 
**payment_reference_number** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**vendor_id** | **int** |  | [optional] 
**cooperative** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**split_amount** | **float** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_purchase_update import BulkPurchaseUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPurchaseUpdate from a JSON string
bulk_purchase_update_instance = BulkPurchaseUpdate.from_json(json)
# print the JSON string representation of the object
print(BulkPurchaseUpdate.to_json())

# convert the object into a dict
bulk_purchase_update_dict = bulk_purchase_update_instance.to_dict()
# create an instance of BulkPurchaseUpdate from a dict
bulk_purchase_update_from_dict = BulkPurchaseUpdate.from_dict(bulk_purchase_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


