# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | for vivid seats use only | [optional] 
**account_id** | **int** | account id for this user. ignored on account sign up, required for user update | 
**email** | **str** | user&#39;s email | 
**password** | **str** | user&#39;s password only required for creation | [optional] 
**first_name** | **str** | user&#39;s first name | 
**last_name** | **str** | user&#39;s last name | 
**phone** | **str** | user&#39;s phone | 
**creation_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**agreed_to_terms** | **bool** |  | [optional] 
**agreed_to_replenishment_terms** | **bool** |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 
**deleted** | **bool** |  | [optional] 
**original_account** | **int** | Original account id for this user. ignored for user update, required on account sign up  | [optional] 
**update_by_user** | **int** | Last user that update user rol | [optional] 
**update_user** | [**User**](User.md) |  | [optional] 
**authentication_type** | **str** |  | [optional] 
**barcode_masking_enabled** | **bool** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


