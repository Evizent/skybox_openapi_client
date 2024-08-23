# InvoiceCurrencyUpdateBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_ids** | **List[int]** | List or invoice ids. | 
**invoice_line_ids** | **List[int]** | List of invoice line ids. | 
**currency_code** | **str** | New currency code. | 
**exchange_rate** | **float** | Exchange rate (null means ignored) | [optional] 
**force** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.invoice_currency_update_bulk_action import InvoiceCurrencyUpdateBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceCurrencyUpdateBulkAction from a JSON string
invoice_currency_update_bulk_action_instance = InvoiceCurrencyUpdateBulkAction.from_json(json)
# print the JSON string representation of the object
print(InvoiceCurrencyUpdateBulkAction.to_json())

# convert the object into a dict
invoice_currency_update_bulk_action_dict = invoice_currency_update_bulk_action_instance.to_dict()
# create an instance of InvoiceCurrencyUpdateBulkAction from a dict
invoice_currency_update_bulk_action_from_dict = InvoiceCurrencyUpdateBulkAction.from_dict(invoice_currency_update_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


