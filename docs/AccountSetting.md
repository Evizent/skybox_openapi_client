# AccountSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**setting_name** | **str** |  | 
**value** | [**AccountSettingValue**](AccountSettingValue.md) |  | [optional] 

## Example

```python
from skybox_openapi_client.models.account_setting import AccountSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSetting from a JSON string
account_setting_instance = AccountSetting.from_json(json)
# print the JSON string representation of the object
print(AccountSetting.to_json())

# convert the object into a dict
account_setting_dict = account_setting_instance.to_dict()
# create an instance of AccountSetting from a dict
account_setting_from_dict = AccountSetting.from_dict(account_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


