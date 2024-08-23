# PricingGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**production_id** | **int** |  | 
**pricing_group_id** | **str** |  | 
**pricing_group_name** | **str** |  | [optional] 
**active** | **bool** |  | 
**inventory** | [**List[PricingGroupInventory]**](PricingGroupInventory.md) |  | 
**updated_by_user** | **int** |  | 
**updated_date** | **datetime** |  | 

## Example

```python
from skybox_openapi_client.models.pricing_group import PricingGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PricingGroup from a JSON string
pricing_group_instance = PricingGroup.from_json(json)
# print the JSON string representation of the object
print(PricingGroup.to_json())

# convert the object into a dict
pricing_group_dict = pricing_group_instance.to_dict()
# create an instance of PricingGroup from a dict
pricing_group_from_dict = PricingGroup.from_dict(pricing_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


