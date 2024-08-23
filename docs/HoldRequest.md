# HoldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**expiry_date** | **datetime** |  | 
**external_ref** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**inventory_id** | **int** |  | [optional] 
**exchange_pos_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**low_seat** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.hold_request import HoldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HoldRequest from a JSON string
hold_request_instance = HoldRequest.from_json(json)
# print the JSON string representation of the object
print(HoldRequest.to_json())

# convert the object into a dict
hold_request_dict = hold_request_instance.to_dict()
# create an instance of HoldRequest from a dict
hold_request_from_dict = HoldRequest.from_dict(hold_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


