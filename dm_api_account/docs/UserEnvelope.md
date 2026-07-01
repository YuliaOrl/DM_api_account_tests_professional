# UserEnvelope

Enveloped DTO model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**User**](User.md) |  | [optional]
**metadata** | **object** | Additional metadata | [optional]

## Example

```python
from dm_api_account.models.user_envelope import UserEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserEnvelope from a JSON string
user_envelope_instance = UserEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserEnvelope.to_json())

# convert the object into a dict
user_envelope_dict = user_envelope_instance.to_dict()
# create an instance of UserEnvelope from a dict
user_envelope_from_dict = UserEnvelope.from_dict(user_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
