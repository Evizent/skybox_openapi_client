# PurchaseLineReplaceAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | **str** |  | [optional] 
**row** | **str** |  | [optional] 
**low_seat** | **int** |  | [optional] 
**force** | **bool** |  | [optional] 
**seat_type** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.purchase_line_replace_action import PurchaseLineReplaceAction

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseLineReplaceAction from a JSON string
purchase_line_replace_action_instance = PurchaseLineReplaceAction.from_json(json)
# print the JSON string representation of the object
print(PurchaseLineReplaceAction.to_json())

# convert the object into a dict
purchase_line_replace_action_dict = purchase_line_replace_action_instance.to_dict()
# create an instance of PurchaseLineReplaceAction from a dict
purchase_line_replace_action_from_dict = PurchaseLineReplaceAction.from_dict(purchase_line_replace_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


