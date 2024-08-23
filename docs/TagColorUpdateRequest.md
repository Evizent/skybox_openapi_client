# TagColorUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_name** | **str** |  | 
**color_value** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.tag_color_update_request import TagColorUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagColorUpdateRequest from a JSON string
tag_color_update_request_instance = TagColorUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TagColorUpdateRequest.to_json())

# convert the object into a dict
tag_color_update_request_dict = tag_color_update_request_instance.to_dict()
# create an instance of TagColorUpdateRequest from a dict
tag_color_update_request_from_dict = TagColorUpdateRequest.from_dict(tag_color_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


