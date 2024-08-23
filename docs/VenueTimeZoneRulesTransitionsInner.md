# VenueTimeZoneRulesTransitionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset_before** | [**VenueTimeZoneRulesTransitionsInnerOffsetBefore**](VenueTimeZoneRulesTransitionsInnerOffsetBefore.md) |  | [optional] 
**offset_after** | [**VenueTimeZoneRulesTransitionsInnerOffsetBefore**](VenueTimeZoneRulesTransitionsInnerOffsetBefore.md) |  | [optional] 
**instant** | **datetime** |  | [optional] 
**duration** | [**VenueTimeZoneRulesTransitionsInnerDuration**](VenueTimeZoneRulesTransitionsInnerDuration.md) |  | [optional] 
**gap** | **bool** |  | [optional] 
**date_time_after** | **datetime** |  | [optional] 
**date_time_before** | **datetime** |  | [optional] 
**overlap** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.venue_time_zone_rules_transitions_inner import VenueTimeZoneRulesTransitionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VenueTimeZoneRulesTransitionsInner from a JSON string
venue_time_zone_rules_transitions_inner_instance = VenueTimeZoneRulesTransitionsInner.from_json(json)
# print the JSON string representation of the object
print(VenueTimeZoneRulesTransitionsInner.to_json())

# convert the object into a dict
venue_time_zone_rules_transitions_inner_dict = venue_time_zone_rules_transitions_inner_instance.to_dict()
# create an instance of VenueTimeZoneRulesTransitionsInner from a dict
venue_time_zone_rules_transitions_inner_from_dict = VenueTimeZoneRulesTransitionsInner.from_dict(venue_time_zone_rules_transitions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


