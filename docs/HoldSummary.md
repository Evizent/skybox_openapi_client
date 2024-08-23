# HoldSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**inventory_id** | **int** |  | [optional] 
**user** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**removed_by_user_id** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**expiry_date** | **datetime** |  | 
**customer_id** | **int** |  | [optional] 
**removed_date** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 
**external_ref** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**section** | **str** |  | [optional] 
**row** | **str** |  | [optional] 
**seats** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**list_price** | **float** |  | [optional] [readonly] 
**event_id** | **int** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**inventory** | [**Inventory**](Inventory.md) |  | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.hold_summary import HoldSummary

# TODO update the JSON string below
json = "{}"
# create an instance of HoldSummary from a JSON string
hold_summary_instance = HoldSummary.from_json(json)
# print the JSON string representation of the object
print(HoldSummary.to_json())

# convert the object into a dict
hold_summary_dict = hold_summary_instance.to_dict()
# create an instance of HoldSummary from a dict
hold_summary_from_dict = HoldSummary.from_dict(hold_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


