# InventoryMappingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** |  | 
**venue_name** | **str** |  | 
**event_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**purchase_line_id** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**response_status** | **int** |  | [optional] 
**send_count** | **int** |  | [optional] 
**mapped_by_user_id** | **int** |  | [optional] 
**mapped_date** | **datetime** |  | [optional] 
**purchase_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**section** | **str** |  | [optional] 
**row** | **str** |  | [optional] 
**seats** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**external_ref** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.inventory_mapping_summary import InventoryMappingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryMappingSummary from a JSON string
inventory_mapping_summary_instance = InventoryMappingSummary.from_json(json)
# print the JSON string representation of the object
print(InventoryMappingSummary.to_json())

# convert the object into a dict
inventory_mapping_summary_dict = inventory_mapping_summary_instance.to_dict()
# create an instance of InventoryMappingSummary from a dict
inventory_mapping_summary_from_dict = InventoryMappingSummary.from_dict(inventory_mapping_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


