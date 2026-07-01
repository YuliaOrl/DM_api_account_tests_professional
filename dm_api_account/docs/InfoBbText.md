# InfoBbText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Text | [optional]
**parse_mode** | [**BbParseMode**](BbParseMode.md) |  | [optional]

## Example

```python
from dm_api_account.models.info_bb_text import InfoBbText

# TODO update the JSON string below
json = "{}"
# create an instance of InfoBbText from a JSON string
info_bb_text_instance = InfoBbText.from_json(json)
# print the JSON string representation of the object
print(InfoBbText.to_json())

# convert the object into a dict
info_bb_text_dict = info_bb_text_instance.to_dict()
# create an instance of InfoBbText from a dict
info_bb_text_from_dict = InfoBbText.from_dict(info_bb_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
