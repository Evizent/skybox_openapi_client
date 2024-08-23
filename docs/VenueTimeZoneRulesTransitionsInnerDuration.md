# VenueTimeZoneRulesTransitionsInnerDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** |  | [optional] 
**zero** | **bool** |  | [optional] 
**nano** | **int** |  | [optional] 
**negative** | **bool** |  | [optional] 
**units** | [**List[VenueTimeZoneRulesTransitionsInnerDurationUnitsInner]**](VenueTimeZoneRulesTransitionsInnerDurationUnitsInner.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.venue_time_zone_rules_transitions_inner_duration import VenueTimeZoneRulesTransitionsInnerDuration

# TODO update the JSON string below
json = "{}"
# create an instance of VenueTimeZoneRulesTransitionsInnerDuration from a JSON string
venue_time_zone_rules_transitions_inner_duration_instance = VenueTimeZoneRulesTransitionsInnerDuration.from_json(json)
# print the JSON string representation of the object
print(VenueTimeZoneRulesTransitionsInnerDuration.to_json())

# convert the object into a dict
venue_time_zone_rules_transitions_inner_duration_dict = venue_time_zone_rules_transitions_inner_duration_instance.to_dict()
# create an instance of VenueTimeZoneRulesTransitionsInnerDuration from a dict
venue_time_zone_rules_transitions_inner_duration_from_dict = VenueTimeZoneRulesTransitionsInnerDuration.from_dict(venue_time_zone_rules_transitions_inner_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


