# PurchasedInventorySummaryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_line_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**purchase** | [**Purchase**](Purchase.md) |  | [optional] 
**all_purchase_line_ids** | **List[int]** |  | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 
**section** | **str** |  | [optional] 
**row** | **str** |  | [optional] 
**second_row** | **str** |  | [optional] 
**zone_seating** | **str** |  | [optional] 
**seat_type** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**available_cost** | **float** |  | [optional] 
**sold_cost** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**available_quantity** | **int** |  | [optional] 
**sold_quantity** | **int** |  | [optional] 
**cancelled_quantity** | **int** |  | [optional] 
**seat_numbers** | **List[int]** |  | [optional] 
**in_hand_date** | **List[date]** |  | [optional] 
**ticket_status** | **List[str]** |  | [optional] 
**hold_inventory** | **bool** |  | [optional] 
**stock_type** | **List[str]** |  | [optional] 
**notes** | **str** |  | [optional] 
**inventory_ids** | **List[int]** |  | [optional] 
**invoice_ids** | **List[int]** |  | [optional] 
**tags** | **str** |  | [optional] 
**ticket_ids** | **List[int]** |  | [optional] 
**vendor_display_name** | **str** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**consignment_status** | **str** |  | [optional] 
**ticket_face_value_average** | **float** |  | [optional] 
**received** | **str** |  | [optional] 
**credit_card_group** | **str** |  | [optional] 
**credit_card_last_digits** | **str** |  | [optional] 
**bar_codes_entered** | **bool** |  | [optional] 
**external_ticket_id_entered** | **bool** |  | [optional] 
**files_uploaded** | **bool** |  | [optional] 
**tickets_merged** | **bool** |  | [optional] 
**last_purchase_note** | **str** |  | [optional] 
**last_purchase_note_date** | **datetime** |  | [optional] 
**inventory_public_notes** | **str** |  | [optional] 
**taxed_cost** | **float** |  | [optional] 
**unit_taxed_cost** | **float** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.purchased_inventory_summary_v2 import PurchasedInventorySummaryV2

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasedInventorySummaryV2 from a JSON string
purchased_inventory_summary_v2_instance = PurchasedInventorySummaryV2.from_json(json)
# print the JSON string representation of the object
print(PurchasedInventorySummaryV2.to_json())

# convert the object into a dict
purchased_inventory_summary_v2_dict = purchased_inventory_summary_v2_instance.to_dict()
# create an instance of PurchasedInventorySummaryV2 from a dict
purchased_inventory_summary_v2_from_dict = PurchasedInventorySummaryV2.from_dict(purchased_inventory_summary_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


