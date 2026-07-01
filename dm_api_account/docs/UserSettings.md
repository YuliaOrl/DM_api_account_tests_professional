# UserSettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_schema** | [**ColorSchema**](ColorSchema.md) |  | [optional]
**nanny_greetings_message** | **str** | Message that user&#39;s newbies will receive once they are connected | [optional]
**paging** | [**PagingSettings**](PagingSettings.md) |  | [optional]

## Example

```python
from dm_api_account.models.user_settings import UserSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettings from a JSON string
user_settings_instance = UserSettings.from_json(json)
# print the JSON string representation of the object
print(UserSettings.to_json())

# convert the object into a dict
user_settings_dict = user_settings_instance.to_dict()
# create an instance of UserSettings from a dict
user_settings_from_dict = UserSettings.from_dict(user_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
