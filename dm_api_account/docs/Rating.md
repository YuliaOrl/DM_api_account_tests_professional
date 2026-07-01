# Rating

DTO model for user rating

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Rating participation flag | [optional]
**quality** | **int** | Quality rating | [optional]
**quantity** | **int** | Quantity rating | [optional]

## Example

```python
from dm_api_account.models.rating import Rating

# TODO update the JSON string below
json = "{}"
# create an instance of Rating from a JSON string
rating_instance = Rating.from_json(json)
# print the JSON string representation of the object
print(Rating.to_json())

# convert the object into a dict
rating_dict = rating_instance.to_dict()
# create an instance of Rating from a dict
rating_from_dict = Rating.from_dict(rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
