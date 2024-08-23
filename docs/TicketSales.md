# TicketSales


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**Event**](Event.md) |  | [optional] 
**sales** | [**List[TicketSale]**](TicketSale.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.ticket_sales import TicketSales

# TODO update the JSON string below
json = "{}"
# create an instance of TicketSales from a JSON string
ticket_sales_instance = TicketSales.from_json(json)
# print the JSON string representation of the object
print(TicketSales.to_json())

# convert the object into a dict
ticket_sales_dict = ticket_sales_instance.to_dict()
# create an instance of TicketSales from a dict
ticket_sales_from_dict = TicketSales.from_dict(ticket_sales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


