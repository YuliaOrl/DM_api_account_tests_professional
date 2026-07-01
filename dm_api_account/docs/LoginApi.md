# dm_api_account.LoginApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_account_login_all_delete**](LoginApi.md#v1_account_login_all_delete) | **DELETE** /v1/account/login/all | Logout from every device
[**v1_account_login_delete**](LoginApi.md#v1_account_login_delete) | **DELETE** /v1/account/login | Logout as current user
[**v1_account_login_post**](LoginApi.md#v1_account_login_post) | **POST** /v1/account/login | Authenticate via credentials


# **v1_account_login_all_delete**
> v1_account_login_all_delete(x_dm_auth_token, x_dm_bb_render_mode=x_dm_bb_render_mode)

Logout from every device

### Example


```python
import dm_api_account
from dm_api_account.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dm_api_account.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with dm_api_account.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dm_api_account.LoginApi(api_client)
    x_dm_auth_token = 'x_dm_auth_token_example' # str | Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field
    x_dm_bb_render_mode = 'x_dm_bb_render_mode_example' # str | Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml (optional)

    try:
        # Logout from every device
        await api_instance.v1_account_login_all_delete(x_dm_auth_token, x_dm_bb_render_mode=x_dm_bb_render_mode)
    except Exception as e:
        print("Exception when calling LoginApi->v1_account_login_all_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_dm_auth_token** | **str**| Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \&quot;token\&quot; response field |
 **x_dm_bb_render_mode** | **str**| Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**401** | User must be authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_login_delete**
> v1_account_login_delete(x_dm_auth_token, x_dm_bb_render_mode=x_dm_bb_render_mode)

Logout as current user

### Example


```python
import dm_api_account
from dm_api_account.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dm_api_account.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with dm_api_account.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dm_api_account.LoginApi(api_client)
    x_dm_auth_token = 'x_dm_auth_token_example' # str | Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \"token\" response field
    x_dm_bb_render_mode = 'x_dm_bb_render_mode_example' # str | Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml (optional)

    try:
        # Logout as current user
        await api_instance.v1_account_login_delete(x_dm_auth_token, x_dm_bb_render_mode=x_dm_bb_render_mode)
    except Exception as e:
        print("Exception when calling LoginApi->v1_account_login_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_dm_auth_token** | **str**| Authenticated requests require X-Dm-Auth-Token header. You can get the data from POST /account/ method, sending login and password in \&quot;token\&quot; response field |
 **x_dm_bb_render_mode** | **str**| Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**401** | User must be authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_account_login_post**
> UserEnvelope v1_account_login_post(x_dm_bb_render_mode=x_dm_bb_render_mode, login_credentials=login_credentials)

Authenticate via credentials

### Example


```python
import dm_api_account
from dm_api_account.models.login_credentials import LoginCredentials
from dm_api_account.models.user_envelope import UserEnvelope
from dm_api_account.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dm_api_account.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with dm_api_account.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dm_api_account.LoginApi(api_client)
    x_dm_bb_render_mode = 'x_dm_bb_render_mode_example' # str | Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml (optional)
    login_credentials = dm_api_account.LoginCredentials() # LoginCredentials | Login credentials (optional)

    try:
        # Authenticate via credentials
        api_response = await api_instance.v1_account_login_post(x_dm_bb_render_mode=x_dm_bb_render_mode, login_credentials=login_credentials)
        print("The response of LoginApi->v1_account_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginApi->v1_account_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_dm_bb_render_mode** | **str**| Requests with user defined texts that allows usage of BB-codes may be rendered differently by passing the X-Dm-Bb-Render-Mode header of one of following values Html, Bb, Text, SafeHtml | [optional]
 **login_credentials** | [**LoginCredentials**](LoginCredentials.md)| Login credentials | [optional]

### Return type

[**UserEnvelope**](UserEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | User not found or password is incorrect |  -  |
**403** | User is inactive or banned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
