---
id: "@specs/aws/quicksight/docs/API_GetDashboardEmbedUrl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDashboardEmbedUrl"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# GetDashboardEmbedUrl

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_GetDashboardEmbedUrl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDashboardEmbedUrl
<a name="API_GetDashboardEmbedUrl"></a>

Generates a temporary session URL and authorization code(bearer token) that you can use to embed an Amazon Quick Sight read-only dashboard in your website or application. Before you use this command, make sure that you have configured the dashboards and permissions. 

Currently, you can use `GetDashboardEmbedURL` only from the server, not from the user's browser. The following rules apply to the generated URL:
+ They must be used together.
+ They can be used one time only.
+ They are valid for 5 minutes after you run this command.
+ You are charged only when the URL is used or there is interaction with Quick.
+ The resulting user session is valid for 15 minutes (default) up to 10 hours (maximum). You can use the optional `SessionLifetimeInMinutes` parameter to customize session duration.

For more information, see [Embedding Analytics Using GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-deprecated.html) in the *Amazon Quick User Guide*.

For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the [Amazon Quick Developer Portal](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html).

## Request Syntax
<a name="API_GetDashboardEmbedUrl_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/embed-url?additional-dashboard-ids={{AdditionalDashboardIds}}&creds-type={{IdentityType}}&namespace={{Namespace}}&reset-disabled={{ResetDisabled}}&session-lifetime={{SessionLifetimeInMinutes}}&state-persistence-enabled={{StatePersistenceEnabled}}&undo-redo-disabled={{UndoRedoDisabled}}&user-arn={{UserArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDashboardEmbedUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AdditionalDashboardIds](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-AdditionalDashboardIds"></a>
A list of one or more dashboard IDs that you want anonymous users to have tempporary access to. Currently, the `IdentityType` parameter must be set to `ANONYMOUS` because other identity types authenticate as Quick or IAM users. For example, if you set "`--dashboard-id dash_id1 --dashboard-id dash_id2 dash_id3 identity-type ANONYMOUS`", the session can access all three dashboards.  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [AwsAccountId](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the dashboard that you're embedding.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-DashboardId"></a>
The ID for the dashboard, also added to the AWS Identity and Access Management (IAM) policy.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [IdentityType](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-IdentityType"></a>
The authentication method that the user uses to sign in.  
Valid Values: `IAM | QUICKSIGHT | ANONYMOUS`   
Required: Yes

 ** [Namespace](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-Namespace"></a>
The Amazon Quick Sight namespace that contains the dashboard IDs in this request. If you're not using a custom namespace, set `Namespace = default`.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$` 

 ** [ResetDisabled](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-ResetDisabled"></a>
Remove the reset button on the embedded dashboard. The default is FALSE, which enables the reset button.

 ** [SessionLifetimeInMinutes](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-SessionLifetimeInMinutes"></a>
How many minutes the session is valid. The session lifetime must be 15-600 minutes.  
Valid Range: Minimum value of 15. Maximum value of 600.

 ** [StatePersistenceEnabled](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-StatePersistenceEnabled"></a>
Adds persistence of state for the user session in an embedded dashboard. Persistence applies to the sheet and the parameter settings. These are control settings that the dashboard subscriber (Amazon Quick Sight reader) chooses while viewing the dashboard. If this is set to `TRUE`, the settings are the same when the subscriber reopens the same dashboard URL. The state is stored in Amazon Quick Sight, not in a browser cookie. If this is set to FALSE, the state of the user session is not persisted. The default is `FALSE`.

 ** [UndoRedoDisabled](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-UndoRedoDisabled"></a>
Remove the undo/redo button on the embedded dashboard. The default is FALSE, which enables the undo/redo button.

 ** [UserArn](#API_GetDashboardEmbedUrl_RequestSyntax) **   <a name="QS-GetDashboardEmbedUrl-request-uri-UserArn"></a>
The Amazon Quick user's Amazon Resource Name (ARN), for use with `QUICKSIGHT` identity type. You can use this for any Amazon Quick users in your account (readers, authors, or admins) authenticated as one of the following:  
+ Active Directory (AD) users or group members
+ Invited nonfederated users
+ IAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation.
Omit this parameter for users in the third group – IAM users and IAM role-based sessions.

## Request Body
<a name="API_GetDashboardEmbedUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDashboardEmbedUrl_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "EmbedUrl": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_GetDashboardEmbedUrl_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_GetDashboardEmbedUrl_ResponseSyntax) **   <a name="QS-GetDashboardEmbedUrl-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [EmbedUrl](#API_GetDashboardEmbedUrl_ResponseSyntax) **   <a name="QS-GetDashboardEmbedUrl-response-EmbedUrl"></a>
A single-use URL that you can put into your server-side webpage to embed your dashboard. This URL is valid for 5 minutes. The API operation provides the URL with an `auth_code` value that enables one (and only one) sign-on to a user session that is valid for 10 hours.   
Type: String

 ** [RequestId](#API_GetDashboardEmbedUrl_ResponseSyntax) **   <a name="QS-GetDashboardEmbedUrl-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_GetDashboardEmbedUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** DomainNotWhitelistedException **   
The domain specified isn't on the allow list. All domains for embedded dashboards must be added to the approved list by an Amazon Quick Suite admin.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

 ** IdentityTypeNotSupportedException **   
The identity type specified isn't supported. Supported identity types include `IAM` and `QUICKSIGHT`.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** QuickSightUserNotFoundException **   
The user with the provided name isn't found. This error can happen in any operation that requires finding a user based on a provided user name, such as `DeleteUser`, `DescribeUser`, and so on.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 404

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** SessionLifetimeInMinutesInvalidException **   
The number of minutes specified for the lifetime of a session isn't valid. The session lifetime must be 15-600 minutes.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedPricingPlanException **   
This error indicates that you are calling an embedding operation in Amazon Quick Sight without the required pricing plan on your AWS account. Before you can use embedding for anonymous users, a Quick Suite administrator needs to add capacity pricing to Quick Sight. You can do this on the **Manage Quick Suite** page.   
After capacity pricing is added, you can use the ` [GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetDashboardEmbedUrl.html) ` API operation with the `--identity-type ANONYMOUS` option.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_GetDashboardEmbedUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/GetDashboardEmbedUrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GetDashboardEmbedUrl) 