# Purchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Required for updates, ignored on inserts. | [optional] 
**vendor_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**internal_id** | **int** |  | [optional] 
**lines** | [**List[Line]**](Line.md) |  | 
**purchase_term** | **str** |  | 
**payment_method** | **str** |  | 
**payment_ref** | **str** |  | [optional] 
**delivery_method** | **str** |  | 
**shipping_address_id** | **int** |  | [optional] 
**billing_address_id** | **int** |  | [optional] 
**tax_amount** | **float** |  | 
**shipping_amount** | **float** |  | 
**other_amount** | **float** |  | 
**internal_notes** | **str** |  | [optional] 
**public_notes** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | 
**tags** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_update_by** | **str** |  | [optional] 
**external_ref** | **str** | External reference number for purchase | [optional] 
**payment_status** | **str** | Payment status | 
**credit_card_id** | **int** |  | [optional] 
**credit_card_group_id** | **int** |  | [optional] 
**currency_code** | **str** |  | 
**payments** | [**List[PurchasePayment]**](PurchasePayment.md) |  | [optional] 
**notes** | [**List[PurchaseNote]**](PurchaseNote.md) |  | [optional] 
**received** | **bool** |  | [optional] 
**consignment** | [**Consignment**](Consignment.md) |  | [optional] 
**cooperative** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**airbill** | **str** |  | [optional] 
**outstanding_balance** | **float** |  | [optional] 
**auto_po** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.purchase import Purchase

# TODO update the JSON string below
json = "{}"
# create an instance of Purchase from a JSON string
purchase_instance = Purchase.from_json(json)
# print the JSON string representation of the object
print(Purchase.to_json())

# convert the object into a dict
purchase_dict = purchase_instance.to_dict()
# create an instance of Purchase from a dict
purchase_from_dict = Purchase.from_dict(purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


