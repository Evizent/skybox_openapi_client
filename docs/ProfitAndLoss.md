# ProfitAndLoss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales** | **float** |  | [optional] 
**pl_value** | **float** |  | [optional] 
**pl_percentage** | **float** |  | [optional] 
**roi** | **float** |  | [optional] 
**avg_ticket_sales** | **float** |  | [optional] 
**tickets_profitability** | **float** |  | [optional] 
**num_tickets** | **int** |  | [optional] 
**profitable_tickets** | **int** |  | [optional] 
**costs** | **float** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.profit_and_loss import ProfitAndLoss

# TODO update the JSON string below
json = "{}"
# create an instance of ProfitAndLoss from a JSON string
profit_and_loss_instance = ProfitAndLoss.from_json(json)
# print the JSON string representation of the object
print(ProfitAndLoss.to_json())

# convert the object into a dict
profit_and_loss_dict = profit_and_loss_instance.to_dict()
# create an instance of ProfitAndLoss from a dict
profit_and_loss_from_dict = ProfitAndLoss.from_dict(profit_and_loss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


