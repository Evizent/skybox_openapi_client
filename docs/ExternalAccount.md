# ExternalAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**display_name** | **str** |  | 
**marketplace** | **str** |  | 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**integration_provider** | **str** |  | 
**last_sweep** | **datetime** |  | [optional] 
**credit_card_id** | **int** |  | [optional] 
**credit_card_group_id** | **int** |  | [optional] 
**encrypted_password** | **str** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**vendor_id** | **int** |  | [optional] 
**markup** | **float** |  | [optional] 
**fee** | **float** |  | [optional] 
**auto_hide_seat_numbers** | **bool** |  | [optional] 
**opt_in_stubhub_inhand_date_logic** | **bool** |  | [optional] 
**opt_in_stub_hub_transfer_details_sweep** | **bool** |  | [optional] 
**confirm_orders** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.external_account import ExternalAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccount from a JSON string
external_account_instance = ExternalAccount.from_json(json)
# print the JSON string representation of the object
print(ExternalAccount.to_json())

# convert the object into a dict
external_account_dict = external_account_instance.to_dict()
# create an instance of ExternalAccount from a dict
external_account_from_dict = ExternalAccount.from_dict(external_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


