# openapi_client.DefaultApi

All URIs are relative to *http://localhost:80/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Get Top 10 Stack Overflow Users with Object Detection


# **users_post**
> List[UsersPost200ResponseInner] users_post(users_post_request)

Get Top 10 Stack Overflow Users with Object Detection

Fetches the top 10 users from the Stack Overflow Users API and detects specified objects in their profile images.

### Example


```python
import openapi_client
from openapi_client.models.users_post200_response_inner import UsersPost200ResponseInner
from openapi_client.models.users_post_request import UsersPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:80/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:80/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    users_post_request = openapi_client.UsersPostRequest() # UsersPostRequest | 

    try:
        # Get Top 10 Stack Overflow Users with Object Detection
        api_response = api_instance.users_post(users_post_request)
        print("The response of DefaultApi->users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_post_request** | [**UsersPostRequest**](UsersPostRequest.md)|  | 

### Return type

[**List[UsersPost200ResponseInner]**](UsersPost200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of the top 10 Stack Overflow users with object detection results |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

