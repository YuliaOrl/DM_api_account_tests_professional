# User

DTO model for user

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

## Example

```python
from dm_api_account.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
