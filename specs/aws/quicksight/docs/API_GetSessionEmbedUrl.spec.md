---
id: "@specs/aws/quicksight/docs/API_GetSessionEmbedUrl"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSessionEmbedUrl"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# GetSessionEmbedUrl

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_GetSessionEmbedUrl
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSessionEmbedUrl
<a name="API_GetSessionEmbedUrl"></a>

Generates a session URL and authorization code that you can use to embed the Amazon Amazon Quick Sight console in your web server code. Use `GetSessionEmbedUrl` where you want to provide an authoring portal that allows users to create data sources, datasets, analyses, and dashboards. The users who access an embedded Amazon Quick Sight console need belong to the author or admin security cohort. If you want to restrict permissions to some of these features, add a custom permissions profile to the user with the ` [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html) ` API operation. Use ` [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html) ` API operation to add a new user with a custom permission profile attached. For more information, see the following sections in the *Amazon Quick User Guide*:
+  [Embedding Analytics](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics.html) 
+  [Customizing Access to the Amazon Quick Console](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html) 

## Request Syntax
<a name="API_GetSessionEmbedUrl_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/session-embed-url?entry-point={{EntryPoint}}&session-lifetime={{SessionLifetimeInMinutes}}&user-arn={{UserArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSessionEmbedUrl_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_GetSessionEmbedUrl_RequestSyntax) **   <a name="QS-GetSessionEmbedUrl-request-uri-AwsAccountId"></a>
The ID for the AWS account associated with your Amazon Quick Sight subscription.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [EntryPoint](#API_GetSessionEmbedUrl_RequestSyntax) **   <a name="QS-GetSessionEmbedUrl-request-uri-EntryPoint"></a>
The URL you use to access the embedded session. The entry point URL is constrained to the following paths:  
+  `/start` 
+  `/start/analyses` 
+  `/start/dashboards` 
+  `/start/favorites` 
+  `/dashboards/DashboardId ` - where `DashboardId` is the actual ID key from the Amazon Quick Sight console URL of the dashboard
+  `/analyses/AnalysisId ` - where `AnalysisId` is the actual ID key from the Amazon Quick Sight console URL of the analysis
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [SessionLifetimeInMinutes](#API_GetSessionEmbedUrl_RequestSyntax) **   <a name="QS-GetSessionEmbedUrl-request-uri-SessionLifetimeInMinutes"></a>
How many minutes the session is valid. The session lifetime must be 15-600 minutes.  
Valid Range: Minimum value of 15. Maximum value of 600.

 ** [UserArn](#API_GetSessionEmbedUrl_RequestSyntax) **   <a name="QS-GetSessionEmbedUrl-request-uri-UserArn"></a>
The Amazon Quick user's Amazon Resource Name (ARN), for use with `QUICKSIGHT` identity type. You can use this for any type of Amazon Quick users in your account (readers, authors, or admins). They need to be authenticated as one of the following:  

1. Active Directory (AD) users or group members

1. Invited nonfederated users

1. IAM users and IAM role-based sessions authenticated through Federated Single Sign-On using SAML, OpenID Connect, or IAM federation
Omit this parameter for users in the third group, IAM users and IAM role-based sessions.

## Request Body
<a name="API_GetSessionEmbedUrl_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSessionEmbedUrl_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "EmbedUrl": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_GetSessionEmbedUrl_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_GetSessionEmbedUrl_ResponseSyntax) **   <a name="QS-GetSessionEmbedUrl-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [EmbedUrl](#API_GetSessionEmbedUrl_ResponseSyntax) **   <a name="QS-GetSessionEmbedUrl-response-EmbedUrl"></a>
A single-use URL that you can put into your server-side web page to embed your Quick session. This URL is valid for 5 minutes. The API operation provides the URL with an `auth_code` value that enables one (and only one) sign-on to a user session that is valid for 10 hours.   
Type: String

 ** [RequestId](#API_GetSessionEmbedUrl_ResponseSyntax) **   <a name="QS-GetSessionEmbedUrl-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_GetSessionEmbedUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

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

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_GetSessionEmbedUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/GetSessionEmbedUrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GetSessionEmbedUrl) 