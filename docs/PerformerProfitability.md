# PerformerProfitability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**Performer**](Performer.md) |  | [optional] 
**profit** | [**ProfitAndLoss**](ProfitAndLoss.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.performer_profitability import PerformerProfitability

# TODO update the JSON string below
json = "{}"
# create an instance of PerformerProfitability from a JSON string
performer_profitability_instance = PerformerProfitability.from_json(json)
# print the JSON string representation of the object
print(PerformerProfitability.to_json())

# convert the object into a dict
performer_profitability_dict = performer_profitability_instance.to_dict()
# create an instance of PerformerProfitability from a dict
performer_profitability_from_dict = PerformerProfitability.from_dict(performer_profitability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


