# GroupProfitability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**VividSeatsMapGroups**](VividSeatsMapGroups.md) |  | [optional] 
**profit** | [**ProfitAndLoss**](ProfitAndLoss.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.group_profitability import GroupProfitability

# TODO update the JSON string below
json = "{}"
# create an instance of GroupProfitability from a JSON string
group_profitability_instance = GroupProfitability.from_json(json)
# print the JSON string representation of the object
print(GroupProfitability.to_json())

# convert the object into a dict
group_profitability_dict = group_profitability_instance.to_dict()
# create an instance of GroupProfitability from a dict
group_profitability_from_dict = GroupProfitability.from_dict(group_profitability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


