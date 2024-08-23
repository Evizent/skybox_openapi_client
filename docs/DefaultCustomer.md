# DefaultCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**marketplace** | **str** |  | 

## Example

```python
from skybox_openapi_client.models.default_customer import DefaultCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultCustomer from a JSON string
default_customer_instance = DefaultCustomer.from_json(json)
# print the JSON string representation of the object
print(DefaultCustomer.to_json())

# convert the object into a dict
default_customer_dict = default_customer_instance.to_dict()
# create an instance of DefaultCustomer from a dict
default_customer_from_dict = DefaultCustomer.from_dict(default_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


