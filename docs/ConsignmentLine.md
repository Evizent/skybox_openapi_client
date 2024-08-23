# ConsignmentLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**consignment_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**invoice_line_id** | **int** |  | [optional] 
**open** | **bool** |  | [optional] 
**original_unit_cost** | **float** |  | [optional] 
**mode** | **str** |  | [optional] 
**consignment_value** | **float** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.consignment_line import ConsignmentLine

# TODO update the JSON string below
json = "{}"
# create an instance of ConsignmentLine from a JSON string
consignment_line_instance = ConsignmentLine.from_json(json)
# print the JSON string representation of the object
print(ConsignmentLine.to_json())

# convert the object into a dict
consignment_line_dict = consignment_line_instance.to_dict()
# create an instance of ConsignmentLine from a dict
consignment_line_from_dict = ConsignmentLine.from_dict(consignment_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


