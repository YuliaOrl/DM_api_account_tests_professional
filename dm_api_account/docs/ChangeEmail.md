# ChangeEmail

API DTO model for changing user email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | User login | [optional]
**password** | **str** | User password | [optional]
**email** | **str** | New user email | [optional]

## Example

```python
from dm_api_account.models.change_email import ChangeEmail

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEmail from a JSON string
change_email_instance = ChangeEmail.from_json(json)
# print the JSON string representation of the object
print(ChangeEmail.to_json())

# convert the object into a dict
change_email_dict = change_email_instance.to_dict()
# create an instance of ChangeEmail from a dict
change_email_from_dict = ChangeEmail.from_dict(change_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
