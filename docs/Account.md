# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the account id (ignored by API) | [optional] 
**company** | **str** | the company name | [optional] 
**email** | **str** | the account contact email address | [optional] 
**first_name** | **str** | account contact&#39;s first name | [optional] 
**last_name** | **str** | account contact&#39;s last name | [optional] 
**phone** | **str** | account contact&#39;s phone number | [optional] 
**external_merchant_id** | **str** | account external merchant id | [optional] 
**creation_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**address1** | **str** | the company&#39;s 1st address line | [optional] 
**address2** | **str** | the company&#39;s 2nd address line | [optional] 
**city** | **str** | the company&#39;s city | [optional] 
**state** | **str** | the company&#39;s state | [optional] 
**postal_code** | **str** | the company&#39;s postal code | [optional] 
**country** | **str** | the company&#39;s country | [optional] 
**logo** | **str** | the company logo | [optional] 
**native_integration_enabled** | **bool** |  | [optional] 
**opt_in_stf** | **bool** |  | [optional] 
**accounting** | **bool** |  | [optional] 
**delete_cancelled_tickets** | **bool** |  | [optional] 
**account_settings** | [**List[AccountSetting]**](AccountSetting.md) |  | [optional] 
**tax_cost_opt_in** | [**List[TaxedCostMarketplaceOptIn]**](TaxedCostMarketplaceOptIn.md) |  | [optional] 
**opt_in_non_integrated** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


