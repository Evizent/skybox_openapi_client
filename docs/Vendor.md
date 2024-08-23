# Vendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Required for updates, ignored on inserts. | [optional] 
**account_id** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**last_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**email** | **str** |  | 
**email2** | **str** |  | [optional] 
**use_email2** | **bool** |  | [optional] 
**company** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | 
**notes** | **str** |  | [optional] 
**display_name** | **str** |  | 
**type** | **str** |  | 
**payment_method** | **str** |  | 
**purchase_term** | **str** |  | 
**deleted** | **bool** |  | [optional] 
**tags** | **str** |  | [optional] 
**default_delivery_method** | **str** | The default delivery method to use on purchases. | 
**account_default** | **bool** | True if this is the account&#39;s default vendor. Read-only. | [optional] 
**client_id** | **int** |  | [optional] 
**broker_id** | **int** |  | [optional] 
**vsr_account_id** | **int** |  | [optional] 
**outlawed_payment_methods** | **List[str]** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.vendor import Vendor

# TODO update the JSON string below
json = "{}"
# create an instance of Vendor from a JSON string
vendor_instance = Vendor.from_json(json)
# print the JSON string representation of the object
print(Vendor.to_json())

# convert the object into a dict
vendor_dict = vendor_instance.to_dict()
# create an instance of Vendor from a dict
vendor_from_dict = Vendor.from_dict(vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


