# PurchasePayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | 
**reference_number** | **str** |  | [optional] 
**amount** | **float** | The total for this payment. | 
**payment_date** | **datetime** |  | [optional] 
**user_id** | **int** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**purchase_id** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.purchase_payment import PurchasePayment

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasePayment from a JSON string
purchase_payment_instance = PurchasePayment.from_json(json)
# print the JSON string representation of the object
print(PurchasePayment.to_json())

# convert the object into a dict
purchase_payment_dict = purchase_payment_instance.to_dict()
# create an instance of PurchasePayment from a dict
purchase_payment_from_dict = PurchasePayment.from_dict(purchase_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


