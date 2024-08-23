# TagSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**tag_type** | **str** |  | [optional] 
**inventory_count** | **int** |  | [optional] 
**invoice_count** | **int** |  | [optional] 
**po_count** | **int** |  | [optional] 
**event_count** | **int** |  | [optional] 
**customer_count** | **int** |  | [optional] 
**vendor_count** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.tag_summary import TagSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TagSummary from a JSON string
tag_summary_instance = TagSummary.from_json(json)
# print the JSON string representation of the object
print(TagSummary.to_json())

# convert the object into a dict
tag_summary_dict = tag_summary_instance.to_dict()
# create an instance of TagSummary from a dict
tag_summary_from_dict = TagSummary.from_dict(tag_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


