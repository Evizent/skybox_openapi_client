# BulkInventoryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_ids** | **List[int]** | Inventory id&#39;s which will be update. | 
**public_notes_to_replace** | **str** | New public notes. | [optional] 
**public_notes_to_add** | **str** | Public notes to add to existing notes. | [optional] 
**internal_notes_to_replace** | **str** | New internal notes. | [optional] 
**internal_notes_to_add** | **str** | Internal notes to add to existing notes. | [optional] 
**split_type** | **str** | Split type to update | [optional] 
**custom_split** | **str** | Valid split quantities | [optional] 
**seat_type** | **str** | Seat type to update | [optional] 
**in_hand_days_before_event** | **int** | In-hand days before event to update | [optional] 
**stock_type** | **str** | Stock type to update | [optional] 
**zone_seating** | **bool** | Zone seating | [optional] 
**hide_seat_numbers** | **bool** | Hide seat numbers | [optional] 
**friendly_section** | **str** | Friendly Section | [optional] 
**section** | **str** | Section | [optional] 
**friendly_row** | **str** | Friendly Row | [optional] 
**row** | **str** | Row | [optional] 
**remove_barcode** | **bool** | Barcodes should be removed | [optional] 
**remove_pdf** | **bool** | Whether pdfs should be removed | [optional] 
**remove_external_ticket_id** | **bool** | Whether external ticket IDs should be removed | [optional] 
**ticket_disclosure** | **str** | Ticket disclosure to update | [optional] 
**inventory_attribute** | **str** | Inventory attribute to update | [optional] 
**face_value** | **float** | Amount to set to each ticket&#39;s face value | [optional] 
**opt_out_auto_price** | **bool** | Opt-out auto-price | [optional] 
**broadcast** | **bool** | Broadcast to exchanges | [optional] 
**electronic_transfer** | **bool** | Electronic transfer to set | [optional] 
**no_split** | **bool** | Whether split type is full quantity (no splits) | [optional] 
**received** | **bool** | Received status to be set to the purchases of the inventories. | [optional] 
**vsr_option** | **str** | VSR option | [optional] 
**replenishment_group_id** | **int** |  | [optional] 
**clear_disclosures** | **bool** |  | [optional] 
**clear_attributes** | **bool** |  | [optional] 
**shown_quantity** | **int** |  | [optional] 
**force** | **bool** |  | [optional] 
**instant_transfer** | **bool** | Received instant transfer value to be set to the inventories. | [optional] 
**instant_transfer_opted_out** | **bool** | Received instant transfer Opted Out value to be set to the inventories. | [optional] 
**integrated_listing** | **bool** |  | [optional] 
**in_hand_date** | **date** | In-hand date to update | [optional] 

## Example

```python
from skybox_openapi_client.models.bulk_inventory_update_request import BulkInventoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInventoryUpdateRequest from a JSON string
bulk_inventory_update_request_instance = BulkInventoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BulkInventoryUpdateRequest.to_json())

# convert the object into a dict
bulk_inventory_update_request_dict = bulk_inventory_update_request_instance.to_dict()
# create an instance of BulkInventoryUpdateRequest from a dict
bulk_inventory_update_request_from_dict = BulkInventoryUpdateRequest.from_dict(bulk_inventory_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


