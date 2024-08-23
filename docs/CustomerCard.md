# CustomerCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Required for updates, ignored on inserts. | [optional] 
**account_id** | **int** |  | [optional] 
**card_type** | **str** |  | 
**last_four_digits** | **int** |  | 
**external_id** | **str** |  | 
**customer_external_id** | **str** |  | 
**address_external_id** | **str** |  | 
**cardholder_name** | **str** |  | [optional] 
**expiration_month** | **int** |  | [optional] 
**expiration_year** | **int** |  | [optional] 
**customer_id** | **int** | Required for updates, ignored on inserts. | [optional] 
**default_card** | **bool** |  | [optional] 
**last_date_used** | **datetime** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.customer_card import CustomerCard

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCard from a JSON string
customer_card_instance = CustomerCard.from_json(json)
# print the JSON string representation of the object
print(CustomerCard.to_json())

# convert the object into a dict
customer_card_dict = customer_card_instance.to_dict()
# create an instance of CustomerCard from a dict
customer_card_from_dict = CustomerCard.from_dict(customer_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


