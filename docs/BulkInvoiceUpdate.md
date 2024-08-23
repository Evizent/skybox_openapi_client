# BulkInvoiceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_ids** | **List[int]** |  | 
**payment_status** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**fulfillment_status** | **str** |  | [optional] 
**payment_ref** | **str** |  | [optional] 
**payment_ref_payment_method** | **str** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**invoice_note** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_invoice_update import BulkInvoiceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInvoiceUpdate from a JSON string
bulk_invoice_update_instance = BulkInvoiceUpdate.from_json(json)
# print the JSON string representation of the object
print(BulkInvoiceUpdate.to_json())

# convert the object into a dict
bulk_invoice_update_dict = bulk_invoice_update_instance.to_dict()
# create an instance of BulkInvoiceUpdate from a dict
bulk_invoice_update_from_dict = BulkInvoiceUpdate.from_dict(bulk_invoice_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


