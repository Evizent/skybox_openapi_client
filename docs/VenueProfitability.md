# VenueProfitability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**Venue**](Venue.md) |  | [optional] 
**profit** | [**ProfitAndLoss**](ProfitAndLoss.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.venue_profitability import VenueProfitability

# TODO update the JSON string below
json = "{}"
# create an instance of VenueProfitability from a JSON string
venue_profitability_instance = VenueProfitability.from_json(json)
# print the JSON string representation of the object
print(VenueProfitability.to_json())

# convert the object into a dict
venue_profitability_dict = venue_profitability_instance.to_dict()
# create an instance of VenueProfitability from a dict
venue_profitability_from_dict = VenueProfitability.from_dict(venue_profitability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


