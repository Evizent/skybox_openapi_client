# QuickSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**matched_field** | **str** |  | [optional] 
**external_ref** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.quick_search_result import QuickSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of QuickSearchResult from a JSON string
quick_search_result_instance = QuickSearchResult.from_json(json)
# print the JSON string representation of the object
print(QuickSearchResult.to_json())

# convert the object into a dict
quick_search_result_dict = quick_search_result_instance.to_dict()
# create an instance of QuickSearchResult from a dict
quick_search_result_from_dict = QuickSearchResult.from_dict(quick_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


