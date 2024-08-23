# TicketSale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**performer** | [**Performer**](Performer.md) |  | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | [optional] 
**inventory** | [**Inventory**](Inventory.md) |  | [optional] 
**days_to_event** | **int** |  | [optional] 
**profit** | [**ProfitAndLoss**](ProfitAndLoss.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.ticket_sale import TicketSale

# TODO update the JSON string below
json = "{}"
# create an instance of TicketSale from a JSON string
ticket_sale_instance = TicketSale.from_json(json)
# print the JSON string representation of the object
print(TicketSale.to_json())

# convert the object into a dict
ticket_sale_dict = ticket_sale_instance.to_dict()
# create an instance of TicketSale from a dict
ticket_sale_from_dict = TicketSale.from_dict(ticket_sale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


