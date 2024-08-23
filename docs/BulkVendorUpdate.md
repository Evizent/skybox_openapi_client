# BulkVendorUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_ids** | **List[int]** | Vendor id&#39;s which will be updated. | 
**payment_method** | **str** | Payment method to update. | 

## Example

```python
from skybox_openapi_client.models.bulk_vendor_update import BulkVendorUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkVendorUpdate from a JSON string
bulk_vendor_update_instance = BulkVendorUpdate.from_json(json)
# print the JSON string representation of the object
print(BulkVendorUpdate.to_json())

# convert the object into a dict
bulk_vendor_update_dict = bulk_vendor_update_instance.to_dict()
# create an instance of BulkVendorUpdate from a dict
bulk_vendor_update_from_dict = BulkVendorUpdate.from_dict(bulk_vendor_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


