# BulkCustomerUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[int]** | Customer id&#39;s which will be updated. | 
**payment_method** | **str** | Payment method to update. | [optional] 
**customer_type** | **str** | Customer type to update. | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_customer_update import BulkCustomerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCustomerUpdate from a JSON string
bulk_customer_update_instance = BulkCustomerUpdate.from_json(json)
# print the JSON string representation of the object
print(BulkCustomerUpdate.to_json())

# convert the object into a dict
bulk_customer_update_dict = bulk_customer_update_instance.to_dict()
# create an instance of BulkCustomerUpdate from a dict
bulk_customer_update_from_dict = BulkCustomerUpdate.from_dict(bulk_customer_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


