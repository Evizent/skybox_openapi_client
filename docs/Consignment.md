# Consignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**purchase_id** | **int** |  | [optional] 
**amount** | **float** |  | 
**mode** | **str** |  | 
**completed** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**lines** | [**List[ConsignmentLine]**](ConsignmentLine.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.consignment import Consignment

# TODO update the JSON string below
json = "{}"
# create an instance of Consignment from a JSON string
consignment_instance = Consignment.from_json(json)
# print the JSON string representation of the object
print(Consignment.to_json())

# convert the object into a dict
consignment_dict = consignment_instance.to_dict()
# create an instance of Consignment from a dict
consignment_from_dict = Consignment.from_dict(consignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


