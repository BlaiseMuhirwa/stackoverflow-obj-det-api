# UsersPost200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The ID of the user | [optional] 
**display_name** | **str** | The display name of the user | [optional] 
**profile_image** | **str** | The URL of the user&#39;s profile image | [optional] 
**object_detected** | **bool** | Whether the specified object was detected in the profile image | [optional] 
**bounding_boxes** | [**List[UsersPost200ResponseInnerBoundingBoxesInner]**](UsersPost200ResponseInnerBoundingBoxesInner.md) |  | [optional] 
**detection_time_ms** | **float** | The time in milliseconds it took to detect the object | [optional] 

## Example

```python
from openapi_client.models.users_post200_response_inner import UsersPost200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPost200ResponseInner from a JSON string
users_post200_response_inner_instance = UsersPost200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(UsersPost200ResponseInner.to_json())

# convert the object into a dict
users_post200_response_inner_dict = users_post200_response_inner_instance.to_dict()
# create an instance of UsersPost200ResponseInner from a dict
users_post200_response_inner_from_dict = UsersPost200ResponseInner.from_dict(users_post200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


