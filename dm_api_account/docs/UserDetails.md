# UserDetails

DTO model for user details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Login | [optional]
**roles** | [**List[UserRole]**](UserRole.md) | Roles | [optional]
**medium_picture_url** | **str** | Profile picture URL M-size | [optional]
**small_picture_url** | **str** | Profile picture URL S-size | [optional]
**status** | **str** | User defined status | [optional]
**rating** | [**Rating**](Rating.md) |  | [optional]
**online** | **datetime** | Last seen online moment | [optional]
**name** | **str** | User real name | [optional]
**location** | **str** | User real location | [optional]
**registration** | **datetime** | User registration moment | [optional]
**icq** | **str** | User ICQ number | [optional]
**skype** | **str** | User Skype login | [optional]
**original_picture_url** | **str** | URL of profile picture original | [optional]
**info** | [**InfoBbText**](InfoBbText.md) |  | [optional]
**settings** | [**UserSettings**](UserSettings.md) |  | [optional]

## Example

```python
from dm_api_account.models.user_details import UserDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetails from a JSON string
user_details_instance = UserDetails.from_json(json)
# print the JSON string representation of the object
print(UserDetails.to_json())

# convert the object into a dict
user_details_dict = user_details_instance.to_dict()
# create an instance of UserDetails from a dict
user_details_from_dict = UserDetails.from_dict(user_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
