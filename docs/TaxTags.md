# TaxTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.tax_tags import TaxTags

# TODO update the JSON string below
json = "{}"
# create an instance of TaxTags from a JSON string
tax_tags_instance = TaxTags.from_json(json)
# print the JSON string representation of the object
print(TaxTags.to_json())

# convert the object into a dict
tax_tags_dict = tax_tags_instance.to_dict()
# create an instance of TaxTags from a dict
tax_tags_from_dict = TaxTags.from_dict(tax_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


