# ExchangePosIdHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_pos_id** | **int** |  | [optional] 
**inventory_id** | **int** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.exchange_pos_id_history_response import ExchangePosIdHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangePosIdHistoryResponse from a JSON string
exchange_pos_id_history_response_instance = ExchangePosIdHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangePosIdHistoryResponse.to_json())

# convert the object into a dict
exchange_pos_id_history_response_dict = exchange_pos_id_history_response_instance.to_dict()
# create an instance of ExchangePosIdHistoryResponse from a dict
exchange_pos_id_history_response_from_dict = ExchangePosIdHistoryResponse.from_dict(exchange_pos_id_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


