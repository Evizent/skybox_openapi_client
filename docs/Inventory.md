# Inventory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_hand_date** | **date** | The  date that the tickets will be in hand | [optional] 
**id** | **int** | Required for updates, ignored on inserts. | [optional] 
**account_id** | **int** |  | [optional] 
**event_id** | **int** | Required on inserts if event mapping is empty. | 
**quantity** | **int** | Number of tickets available, implied from tickets array if present. | 
**notes** | **str** |  | [optional] 
**section** | **str** |  | 
**friendly_section** | **str** | Friendly name for Section. | [optional] 
**row** | **str** |  | 
**friendly_row** | **str** | Friendly name for Row. | [optional] 
**second_row** | **str** |  | [optional] 
**low_seat** | **int** | Required on inserts if tickets array is empty. | [optional] 
**high_seat** | **int** | Required on inserts if tickets array is empty. | [optional] 
**cost** | **float** |  | 
**taxed_cost** | **float** |  | [optional] 
**taxed_cost_average** | **float** |  | [optional] 
**face_value** | **float** |  | [optional] 
**tickets** | [**List[Ticket]**](Ticket.md) |  | [optional] 
**ticket_ids** | **List[int]** |  | [optional] 
**stock_type** | **str** |  | 
**split_type** | **str** | How the tickets may be split | 
**custom_split** | **str** |  | [optional] 
**list_price** | **float** |  | [optional] 
**vivid_retail_price** | **float** |  | [optional] 
**expected_value** | **float** |  | [optional] 
**public_notes** | **str** |  | [optional] 
**attributes** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**in_hand_days_before_event** | **int** |  | [optional] 
**last_price_update** | **datetime** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_by_user_id** | **int** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**last_update_by** | **str** |  | [optional] 
**last_delta_update** | **datetime** |  | [optional] 
**version** | **int** |  | [optional] 
**tags** | **str** |  | [optional] 
**seat_type** | **str** | Seat type. | 
**event_mapping** | [**EventMapping**](EventMapping.md) |  | [optional] 
**mapping_id** | **int** | Mapping id if this inventory was sent to mapping. Read-only. | [optional] 
**exchange_pos_id** | **int** | Id to provide to exchanges for listing delete and regeneration compatibility. This id is automatically regenerated when files or bar codes are edited or remove and section or rows get updated. Read-only. | [optional] 
**broadcast** | **bool** | Broadcast. | [optional] 
**zone_seating** | **bool** | Zone seating | [optional] 
**electronic_transfer** | **bool** |  | [optional] 
**opt_out_auto_price** | **bool** |  | [optional] 
**hide_seat_numbers** | **bool** | Hide seat numbers from exchanges. | [optional] 
**vsr_option** | **str** |  | [optional] 
**replenishment_group_id** | **int** |  | [optional] 
**replenishment_group** | **str** |  | [optional] 
**shown_quantity** | **int** |  | [optional] 
**integrated_listing** | **bool** |  | [optional] 
**tickets_merged** | **bool** |  | [optional] [readonly] 
**tickets_split** | **bool** |  | [optional] [readonly] 
**audit_note** | **str** |  | [optional] 
**files_uploaded** | **bool** |  | [optional] 
**bar_codes_entered** | **bool** |  | [optional] 
**external_ticket_id_entered** | **bool** |  | [optional] 
**instant_transfer** | **bool** | Is instant transfer. | [optional] 

## Example

```python
from skybox_openapi_client.models.inventory import Inventory

# TODO update the JSON string below
json = "{}"
# create an instance of Inventory from a JSON string
inventory_instance = Inventory.from_json(json)
# print the JSON string representation of the object
print(Inventory.to_json())

# convert the object into a dict
inventory_dict = inventory_instance.to_dict()
# create an instance of Inventory from a dict
inventory_from_dict = Inventory.from_dict(inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


