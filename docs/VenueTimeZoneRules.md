# VenueTimeZoneRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_offset** | **bool** |  | [optional] 
**transitions** | [**List[VenueTimeZoneRulesTransitionsInner]**](VenueTimeZoneRulesTransitionsInner.md) |  | [optional] 
**transition_rules** | [**List[VenueTimeZoneRulesTransitionRulesInner]**](VenueTimeZoneRulesTransitionRulesInner.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.venue_time_zone_rules import VenueTimeZoneRules

# TODO update the JSON string below
json = "{}"
# create an instance of VenueTimeZoneRules from a JSON string
venue_time_zone_rules_instance = VenueTimeZoneRules.from_json(json)
# print the JSON string representation of the object
print(VenueTimeZoneRules.to_json())

# convert the object into a dict
venue_time_zone_rules_dict = venue_time_zone_rules_instance.to_dict()
# create an instance of VenueTimeZoneRules from a dict
venue_time_zone_rules_from_dict = VenueTimeZoneRules.from_dict(venue_time_zone_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


