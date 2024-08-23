# PdfUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdf** | **List[bytearray]** |  | [optional] 

## Example

```python
from skybox_openapi_client.models.pdf_upload import PdfUpload

# TODO update the JSON string below
json = "{}"
# create an instance of PdfUpload from a JSON string
pdf_upload_instance = PdfUpload.from_json(json)
# print the JSON string representation of the object
print(PdfUpload.to_json())

# convert the object into a dict
pdf_upload_dict = pdf_upload_instance.to_dict()
# create an instance of PdfUpload from a dict
pdf_upload_from_dict = PdfUpload.from_dict(pdf_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


