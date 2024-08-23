# InvoiceDeliveryLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**all_tickets_with_barcodes** | **bool** |  | [optional] 
**all_tickets_with_pdfs** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.invoice_delivery_link import InvoiceDeliveryLink

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDeliveryLink from a JSON string
invoice_delivery_link_instance = InvoiceDeliveryLink.from_json(json)
# print the JSON string representation of the object
print(InvoiceDeliveryLink.to_json())

# convert the object into a dict
invoice_delivery_link_dict = invoice_delivery_link_instance.to_dict()
# create an instance of InvoiceDeliveryLink from a dict
invoice_delivery_link_from_dict = InvoiceDeliveryLink.from_dict(invoice_delivery_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


