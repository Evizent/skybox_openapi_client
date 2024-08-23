# SectionProfitability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**Ticket**](Ticket.md) |  | [optional] 
**profit** | [**ProfitAndLoss**](ProfitAndLoss.md) |  | [optional] 
**vivid_seats_section** | [**VividSeatsSection**](VividSeatsSection.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.section_profitability import SectionProfitability

# TODO update the JSON string below
json = "{}"
# create an instance of SectionProfitability from a JSON string
section_profitability_instance = SectionProfitability.from_json(json)
# print the JSON string representation of the object
print(SectionProfitability.to_json())

# convert the object into a dict
section_profitability_dict = section_profitability_instance.to_dict()
# create an instance of SectionProfitability from a dict
section_profitability_from_dict = SectionProfitability.from_dict(section_profitability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


