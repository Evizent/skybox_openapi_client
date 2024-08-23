# Customer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Required for updates, ignored on inserts. | [optional] 
**account_id** | **int** |  | 
**created_date** | **datetime** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**last_invoice_date** | **datetime** |  | [optional] 
**email** | **str** |  | 
**email2** | **str** |  | [optional] 
**use_email2** | **bool** |  | [optional] 
**company** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | 
**notes** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**outlawed_payment_methods** | **List[str]** |  | [optional] 
**display_name** | **str** |  | 
**customer_type** | **str** |  | 
**sales_term** | **str** |  | 
**payment_method** | **str** |  | 
**ar_threshold** | **float** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**tags** | **str** |  | [optional] 
**outstanding_balance** | **float** |  | [optional] 
**default_delivery_method** | **str** | The default delivery method to use on invoices. | 
**credit_balance** | **float** |  | [optional] [readonly] 

## Example

```python
from skybox_openapi_client.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


