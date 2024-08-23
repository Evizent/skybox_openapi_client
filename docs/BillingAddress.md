# BillingAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**persist_in_vault** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.billing_address import BillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAddress from a JSON string
billing_address_instance = BillingAddress.from_json(json)
# print the JSON string representation of the object
print(BillingAddress.to_json())

# convert the object into a dict
billing_address_dict = billing_address_instance.to_dict()
# create an instance of BillingAddress from a dict
billing_address_from_dict = BillingAddress.from_dict(billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


