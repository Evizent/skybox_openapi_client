# SkyboxWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**topic** | **str** |  | 
**url** | **str** |  | 
**headers** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from skybox_openapi_client.models.skybox_webhook import SkyboxWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SkyboxWebhook from a JSON string
skybox_webhook_instance = SkyboxWebhook.from_json(json)
# print the JSON string representation of the object
print(SkyboxWebhook.to_json())

# convert the object into a dict
skybox_webhook_dict = skybox_webhook_instance.to_dict()
# create an instance of SkyboxWebhook from a dict
skybox_webhook_from_dict = SkyboxWebhook.from_dict(skybox_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


