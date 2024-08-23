# Line


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | 
**target_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**description** | **str** | The description of the line. Ignored for inventory lines. | [optional] 
**amount** | **float** | The total for this line. Passed through to ticket.sellPrice or ticket.cost for inventory items. | 
**line_type** | **str** |  | [optional] 
**line_item_type** | **str** | The type of the line item. | 
**item_ids** | **List[int]** | The itemIds, representing ticketIds if the line item is Inventory. Required for invoice line inserts, ignored otherwise. | [optional] 
**inventory** | [**Inventory**](Inventory.md) |  | [optional] 
**cancelled** | **bool** | True if the tickets on this line are cancelled, false otherwise. Read-only. | [optional] 
**delete** | **bool** |  | [optional] 
**cancel** | **bool** |  | [optional] 
**fill_line_id** | **int** |  | [optional] 
**inventory_ids** | **List[int]** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**last_update_by** | **str** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.line import Line

# TODO update the JSON string below
json = "{}"
# create an instance of Line from a JSON string
line_instance = Line.from_json(json)
# print the JSON string representation of the object
print(Line.to_json())

# convert the object into a dict
line_dict = line_instance.to_dict()
# create an instance of Line from a dict
line_from_dict = Line.from_dict(line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


