# CreditCardGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Required for updates, ignored on inserts. | [optional] 
**account_id** | **int** |  | [optional] 
**label** | **str** | The label of the credit card group. | [optional] 
**description** | **str** | The description of the credit card group. | [optional] 
**credit_cards** | [**List[CreditCard]**](CreditCard.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.credit_card_group import CreditCardGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardGroup from a JSON string
credit_card_group_instance = CreditCardGroup.from_json(json)
# print the JSON string representation of the object
print(CreditCardGroup.to_json())

# convert the object into a dict
credit_card_group_dict = credit_card_group_instance.to_dict()
# create an instance of CreditCardGroup from a dict
credit_card_group_from_dict = CreditCardGroup.from_dict(credit_card_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


