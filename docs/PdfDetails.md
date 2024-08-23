# PdfDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** | the page number within the original PDF | [optional] 
**pdf_url** | **str** | the url for the individual pdf page | [optional] 

## Example

```python
from skybox_openapi_client.models.pdf_details import PdfDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PdfDetails from a JSON string
pdf_details_instance = PdfDetails.from_json(json)
# print the JSON string representation of the object
print(PdfDetails.to_json())

# convert the object into a dict
pdf_details_dict = pdf_details_instance.to_dict()
# create an instance of PdfDetails from a dict
pdf_details_from_dict = PdfDetails.from_dict(pdf_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


