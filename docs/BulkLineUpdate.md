# BulkLineUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_ids** | **List[int]** | Line id&#39;s which will be updated. | 
**line_replace_action** | [**PurchaseLineReplaceAction**](PurchaseLineReplaceAction.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_line_update import BulkLineUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BulkLineUpdate from a JSON string
bulk_line_update_instance = BulkLineUpdate.from_json(json)
# print the JSON string representation of the object
print(BulkLineUpdate.to_json())

# convert the object into a dict
bulk_line_update_dict = bulk_line_update_instance.to_dict()
# create an instance of BulkLineUpdate from a dict
bulk_line_update_from_dict = BulkLineUpdate.from_dict(bulk_line_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


