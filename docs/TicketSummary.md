# TicketSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the ticket. | [optional] 
**seat_number** | **int** | Seat number, must be numeric and passed low to high. | 
**file_name** | **str** | If present, a pdf file exists for this ticket. | [optional] 
**bar_code** | **str** | The barcode associated with this ticket. | [optional] 
**external_ticket_id** | **str** | External Id connecting skybox ticket with external systems/marketplaces. | [optional] 
**inventory_id** | **int** |  | [optional] 
**invoice_line_id** | **int** |  | [optional] 
**purchase_line_id** | **int** |  | [optional] 
**friendly_section** | **str** | Friendly name for Section. | [optional] 
**section** | **str** |  | 
**friendly_row** | **str** | Friendly name for Row. | [optional] 
**row** | **str** |  | 
**notes** | **str** |  | [optional] 
**cost** | **float** |  | 
**face_value** | **float** |  | 
**taxed_cost** | **float** |  | [optional] 
**sell_price** | **float** |  | 
**stock_type** | **str** |  | 
**event_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**status** | **str** |  | 
**base64_file_bytes** | **str** | Base64 encoded byte array of the ticket file. Only used in write operations. | [optional] 
**disclosures** | **List[str]** |  | [optional] 
**attributes** | **List[str]** | List of attributes for the ticket | [optional] 
**created_date** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**last_update_by** | **str** |  | [optional] 
**date_cancelled** | **datetime** |  | [optional] 
**cancelled_by_user_id** | **int** |  | [optional] 
**audit_note** | **str** |  | [optional] 
**invoice_date** | **datetime** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.ticket_summary import TicketSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TicketSummary from a JSON string
ticket_summary_instance = TicketSummary.from_json(json)
# print the JSON string representation of the object
print(TicketSummary.to_json())

# convert the object into a dict
ticket_summary_dict = ticket_summary_instance.to_dict()
# create an instance of TicketSummary from a dict
ticket_summary_from_dict = TicketSummary.from_dict(ticket_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


