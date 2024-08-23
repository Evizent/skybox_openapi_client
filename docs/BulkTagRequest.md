# BulkTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_ids** | **List[int]** |  | 
**entity_type** | **str** |  | 
**tags_to_add** | **List[str]** |  | [optional] 
**tags_to_remove** | **List[str]** |  | [optional] 
**clean_old_tags** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_tag_request import BulkTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTagRequest from a JSON string
bulk_tag_request_instance = BulkTagRequest.from_json(json)
# print the JSON string representation of the object
print(BulkTagRequest.to_json())

# convert the object into a dict
bulk_tag_request_dict = bulk_tag_request_instance.to_dict()
# create an instance of BulkTagRequest from a dict
bulk_tag_request_from_dict = BulkTagRequest.from_dict(bulk_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


