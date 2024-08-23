# CreditCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**cardholder_name** | **str** |  | [optional] 
**default_card** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.credit_card import CreditCard

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCard from a JSON string
credit_card_instance = CreditCard.from_json(json)
# print the JSON string representation of the object
print(CreditCard.to_json())

# convert the object into a dict
credit_card_dict = credit_card_instance.to_dict()
# create an instance of CreditCard from a dict
credit_card_from_dict = CreditCard.from_dict(credit_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


