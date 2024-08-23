# EventProfitability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**Event**](Event.md) |  | [optional] 
**profit** | [**ProfitAndLoss**](ProfitAndLoss.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.event_profitability import EventProfitability

# TODO update the JSON string below
json = "{}"
# create an instance of EventProfitability from a JSON string
event_profitability_instance = EventProfitability.from_json(json)
# print the JSON string representation of the object
print(EventProfitability.to_json())

# convert the object into a dict
event_profitability_dict = event_profitability_instance.to_dict()
# create an instance of EventProfitability from a dict
event_profitability_from_dict = EventProfitability.from_dict(event_profitability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


