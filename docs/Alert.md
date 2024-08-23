# Alert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**creator_id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**subject** | **str** |  | 
**message** | **str** |  | 
**alert_type** | **str** |  | 
**created_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**acknowledged** | **bool** |  | [optional] 
**sender_name** | **str** |  | [optional] 
**sender_email** | **str** |  | [optional] 
**release_alert_id** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


