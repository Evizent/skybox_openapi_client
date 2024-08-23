# Invoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Required for updates, ignored on inserts. | [optional] 
**customer_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**internal_id** | **int** |  | [optional] 
**lines** | [**List[Line]**](Line.md) |  | 
**sales_term** | **str** |  | 
**payment_method** | **str** |  | [optional] 
**payment_ref** | **str** |  | [optional] 
**delivery_method** | **str** |  | [optional] 
**shipping_address_id** | **int** |  | [optional] 
**billing_address_id** | **int** |  | [optional] 
**tax_amount** | **float** |  | 
**shipping_amount** | **float** |  | 
**other_amount** | **float** |  | 
**internal_notes** | **str** |  | [optional] 
**public_notes** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**tags** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_update_by** | **str** |  | [optional] 
**payment_status** | **str** | Payment status. | 
**fulfillment_status** | **str** | Inventory fulfillment status. | 
**external_ref** | **str** | External reference number for invoice | [optional] 
**airbill** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**payments** | [**List[InvoicePayment]**](InvoicePayment.md) |  | [optional] 
**invoice_delivery_link** | [**InvoiceDeliveryLink**](InvoiceDeliveryLink.md) |  | [optional] 
**notes** | [**List[InvoiceNote]**](InvoiceNote.md) |  | [optional] 
**fulfillment_date** | **datetime** |  | [optional] 
**fulfillment_by_user_id** | **int** |  | [optional] 
**outstanding_balance** | **float** |  | [optional] 
**barcodes_entered** | **bool** |  | [optional] 
**external_ticket_id_entered** | **bool** |  | [optional] 
**files_uploaded** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print(Invoice.to_json())

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_from_dict = Invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


