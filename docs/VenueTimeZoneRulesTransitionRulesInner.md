# VenueTimeZoneRulesTransitionRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **str** |  | [optional] 
**time_definition** | **str** |  | [optional] 
**standard_offset** | [**VenueTimeZoneRulesTransitionsInnerOffsetBefore**](VenueTimeZoneRulesTransitionsInnerOffsetBefore.md) |  | [optional] 
**offset_before** | [**VenueTimeZoneRulesTransitionsInnerOffsetBefore**](VenueTimeZoneRulesTransitionsInnerOffsetBefore.md) |  | [optional] 
**offset_after** | [**VenueTimeZoneRulesTransitionsInnerOffsetBefore**](VenueTimeZoneRulesTransitionsInnerOffsetBefore.md) |  | [optional] 
**day_of_week** | **str** |  | [optional] 
**day_of_month_indicator** | **int** |  | [optional] 
**local_time** | **str** |  | [optional] 
**midnight_end_of_day** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.venue_time_zone_rules_transition_rules_inner import VenueTimeZoneRulesTransitionRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VenueTimeZoneRulesTransitionRulesInner from a JSON string
venue_time_zone_rules_transition_rules_inner_instance = VenueTimeZoneRulesTransitionRulesInner.from_json(json)
# print the JSON string representation of the object
print(VenueTimeZoneRulesTransitionRulesInner.to_json())

# convert the object into a dict
venue_time_zone_rules_transition_rules_inner_dict = venue_time_zone_rules_transition_rules_inner_instance.to_dict()
# create an instance of VenueTimeZoneRulesTransitionRulesInner from a dict
venue_time_zone_rules_transition_rules_inner_from_dict = VenueTimeZoneRulesTransitionRulesInner.from_dict(venue_time_zone_rules_transition_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


