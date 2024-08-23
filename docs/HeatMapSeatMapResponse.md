# HeatMapSeatMapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | [**VividSeatsListingGlobal**](VividSeatsListingGlobal.md) |  | [optional] 
**sections** | [**List[SectionProfitability]**](SectionProfitability.md) |  | [optional] 
**groups** | [**List[GroupProfitability]**](GroupProfitability.md) |  | [optional] 
**sales_in_multiple_events** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.heat_map_seat_map_response import HeatMapSeatMapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeatMapSeatMapResponse from a JSON string
heat_map_seat_map_response_instance = HeatMapSeatMapResponse.from_json(json)
# print the JSON string representation of the object
print(HeatMapSeatMapResponse.to_json())

# convert the object into a dict
heat_map_seat_map_response_dict = heat_map_seat_map_response_instance.to_dict()
# create an instance of HeatMapSeatMapResponse from a dict
heat_map_seat_map_response_from_dict = HeatMapSeatMapResponse.from_dict(heat_map_seat_map_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


