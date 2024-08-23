# ExpectedValueUpdateBulk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_value** | **float** | Amount to increase or decrease each ticket by | 
**id** | **int** | ID of inventory to update | 

## Example

```python
from skybox_openapi_client.models.expected_value_update_bulk import ExpectedValueUpdateBulk

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectedValueUpdateBulk from a JSON string
expected_value_update_bulk_instance = ExpectedValueUpdateBulk.from_json(json)
# print the JSON string representation of the object
print(ExpectedValueUpdateBulk.to_json())

# convert the object into a dict
expected_value_update_bulk_dict = expected_value_update_bulk_instance.to_dict()
# create an instance of ExpectedValueUpdateBulk from a dict
expected_value_update_bulk_from_dict = ExpectedValueUpdateBulk.from_dict(expected_value_update_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


