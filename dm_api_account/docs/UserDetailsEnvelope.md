# UserDetailsEnvelope

Enveloped DTO model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**UserDetails**](UserDetails.md) |  | [optional]
**metadata** | **object** | Additional metadata | [optional]

## Example

```python
from dm_api_account.models.user_details_envelope import UserDetailsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailsEnvelope from a JSON string
user_details_envelope_instance = UserDetailsEnvelope.from_json(json)
# print the JSON string representation of the object
print(UserDetailsEnvelope.to_json())

# convert the object into a dict
user_details_envelope_dict = user_details_envelope_instance.to_dict()
# create an instance of UserDetailsEnvelope from a dict
user_details_envelope_from_dict = UserDetailsEnvelope.from_dict(user_details_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
