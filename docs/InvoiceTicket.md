# InvoiceTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **int** |  | [optional] 
**ticket_id** | **int** |  | [optional] 
**section** | **str** |  | [optional] 
**row** | **str** |  | [optional] 
**seat_number** | **int** |  | [optional] 
**bar_code** | **str** |  | [optional] 
**external_ticket_id** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.invoice_ticket import InvoiceTicket

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTicket from a JSON string
invoice_ticket_instance = InvoiceTicket.from_json(json)
# print the JSON string representation of the object
print(InvoiceTicket.to_json())

# convert the object into a dict
invoice_ticket_dict = invoice_ticket_instance.to_dict()
# create an instance of InvoiceTicket from a dict
invoice_ticket_from_dict = InvoiceTicket.from_dict(invoice_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


