# CurrencyUpdateBulkAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_ids** | **List[int]** | List or purchase ids. | 
**purchase_line_ids** | **List[int]** | List of purchase line ids. | 
**currency_code** | **str** | New currency code. | 
**exchange_rate** | **float** | Exchange rate (null means ignored) | [optional] 
**force** | **bool** |  | [optional] 
**purchase_line_id** | **List[int]** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.currency_update_bulk_action import CurrencyUpdateBulkAction

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyUpdateBulkAction from a JSON string
currency_update_bulk_action_instance = CurrencyUpdateBulkAction.from_json(json)
# print the JSON string representation of the object
print(CurrencyUpdateBulkAction.to_json())

# convert the object into a dict
currency_update_bulk_action_dict = currency_update_bulk_action_instance.to_dict()
# create an instance of CurrencyUpdateBulkAction from a dict
currency_update_bulk_action_from_dict = CurrencyUpdateBulkAction.from_dict(currency_update_bulk_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


