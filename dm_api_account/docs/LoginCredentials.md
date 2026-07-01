# LoginCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | [optional]
**password** | **str** |  | [optional]
**remember_me** | **bool** |  | [optional]

## Example

```python
from dm_api_account.models.login_credentials import LoginCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of LoginCredentials from a JSON string
login_credentials_instance = LoginCredentials.from_json(json)
# print the JSON string representation of the object
print(LoginCredentials.to_json())

# convert the object into a dict
login_credentials_dict = login_credentials_instance.to_dict()
# create an instance of LoginCredentials from a dict
login_credentials_from_dict = LoginCredentials.from_dict(login_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
