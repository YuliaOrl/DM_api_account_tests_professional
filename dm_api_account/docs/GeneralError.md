# GeneralError

General error DTO model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Client message | [optional]

## Example

```python
from dm_api_account.models.general_error import GeneralError

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralError from a JSON string
general_error_instance = GeneralError.from_json(json)
# print the JSON string representation of the object
print(GeneralError.to_json())

# convert the object into a dict
general_error_dict = general_error_instance.to_dict()
# create an instance of GeneralError from a dict
general_error_from_dict = GeneralError.from_dict(general_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
