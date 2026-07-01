# PagingSettings

API DTO for user paging settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts_per_page** | **int** | Number of posts on a game room page | [optional]
**comments_per_page** | **int** | Number of commentaries on a game or a topic page | [optional]
**topics_per_page** | **int** | Number of detached topics on a forum page | [optional]
**messages_per_page** | **int** | Number of private messages and conversations on dialogue page | [optional]
**entities_per_page** | **int** | Number of other entities on page | [optional]

## Example

```python
from dm_api_account.models.paging_settings import PagingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PagingSettings from a JSON string
paging_settings_instance = PagingSettings.from_json(json)
# print the JSON string representation of the object
print(PagingSettings.to_json())

# convert the object into a dict
paging_settings_dict = paging_settings_instance.to_dict()
# create an instance of PagingSettings from a dict
paging_settings_from_dict = PagingSettings.from_dict(paging_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
