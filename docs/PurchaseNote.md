# PurchaseNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**purchase_id** | **int** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**text** | **str** |  | 
**author** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.purchase_note import PurchaseNote

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseNote from a JSON string
purchase_note_instance = PurchaseNote.from_json(json)
# print the JSON string representation of the object
print(PurchaseNote.to_json())

# convert the object into a dict
purchase_note_dict = purchase_note_instance.to_dict()
# create an instance of PurchaseNote from a dict
purchase_note_from_dict = PurchaseNote.from_dict(purchase_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


