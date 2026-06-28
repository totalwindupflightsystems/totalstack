---
id: "@specs/aws/quicksight/docs/API_RegisterUser"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RegisterUser"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# RegisterUser

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_RegisterUser
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RegisterUser
<a name="API_RegisterUser"></a>

Creates an Amazon Quick Sight user whose identity is associated with the AWS Identity and Access Management (IAM) identity or role specified in the request. When you register a new user from the Quick Sight API, Quick Sight generates a registration URL. The user accesses this registration URL to create their account. Quick Sight doesn't send a registration email to users who are registered from the Quick Sight API. If you want new users to receive a registration email, then add those users in the Quick Sight console. For more information on registering a new user in the Quick Sight console, see [ Inviting users to access Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/managing-users.html#inviting-users).

## Request Syntax
<a name="API_RegisterUser_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/users HTTP/1.1
Content-type: application/json

{
   "CustomFederationProviderUrl": "{{string}}",
   "CustomPermissionsName": "{{string}}",
   "Email": "{{string}}",
   "ExternalLoginFederationProviderType": "{{string}}",
   "ExternalLoginId": "{{string}}",
   "IamArn": "{{string}}",
   "IdentityType": "{{string}}",
   "SessionName": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserName": "{{string}}",
   "UserRole": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-uri-AwsAccountId"></a>
The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-uri-Namespace"></a>
The namespace. Currently, you should set this to `default`.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

## Request Body
<a name="API_RegisterUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Email](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-Email"></a>
The email address of the user that you want to register.  
Type: String  
Required: Yes

 ** [IdentityType](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-IdentityType"></a>
The identity type that your Quick Sight account uses to manage the identity of users.  
Type: String  
Valid Values: `IAM | QUICKSIGHT | IAM_IDENTITY_CENTER`   
Required: Yes

 ** [UserRole](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-UserRole"></a>
The Amazon Quick Sight role for the user. The user role can be one of the following:  
+  `READER`: A user who has read-only access to dashboards.
+  `AUTHOR`: A user who can create data sources, datasets, analyses, and dashboards.
+  `ADMIN`: A user who is an author, who can also manage Amazon Quick Sight settings.
+  `READER_PRO`: Reader Pro adds Generative BI capabilities to the Reader role. Reader Pros have access to Amazon Q in Quick Sight, can build stories with Amazon Q, and can generate executive summaries from dashboards.
+  `AUTHOR_PRO`: Author Pro adds Generative BI capabilities to the Author role. Author Pros can author dashboards with natural language with Amazon Q, build stories with Amazon Q, create Topics for Q&A, and generate executive summaries from dashboards.
+  `ADMIN_PRO`: Admin Pros are Author Pros who can also manage Amazon Quick Sight administrative settings. Admin Pro users are billed at Author Pro pricing.
+  `RESTRICTED_READER`: This role isn't currently available for use.
+  `RESTRICTED_AUTHOR`: This role isn't currently available for use.
Type: String  
Valid Values: `ADMIN | AUTHOR | READER | RESTRICTED_AUTHOR | RESTRICTED_READER | ADMIN_PRO | AUTHOR_PRO | READER_PRO`   
Required: Yes

 ** [CustomFederationProviderUrl](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-CustomFederationProviderUrl"></a>
The URL of the custom OpenID Connect (OIDC) provider that provides identity to let a user federate into Quick Sight with an associated AWS Identity and Access Management(IAM) role. This parameter should only be used when `ExternalLoginFederationProviderType` parameter is set to `CUSTOM_OIDC`.  
Type: String  
Required: No

 ** [CustomPermissionsName](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-CustomPermissionsName"></a>
(Enterprise edition only) The name of the custom permissions profile that you want to assign to this user. Customized permissions allows you to control a user's access by restricting access the following operations:  
+ Create and update data sources
+ Create and update datasets
+ Create and update email reports
+ Subscribe to email reports
To add custom permissions to an existing user, use ` [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html) ` instead.  
A set of custom permissions includes any combination of these restrictions. Currently, you need to create the profile names for custom permission sets by using the Quick Sight console. Then, you use the `RegisterUser` API operation to assign the named set of permissions to a Quick Sight user.   
Quick Sight custom permissions are applied through IAM policies. Therefore, they override the permissions typically granted by assigning Quick Sight users to one of the default security cohorts in Quick Sight (admin, author, reader, admin pro, author pro, reader pro).  
This feature is available only to Quick Sight Enterprise edition subscriptions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9+=,.@_-]+$`   
Required: No

 ** [ExternalLoginFederationProviderType](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-ExternalLoginFederationProviderType"></a>
The type of supported external login provider that provides identity to let a user federate into Amazon Quick Sight with an associated AWS Identity and Access Management(IAM) role. The type of supported external login provider can be one of the following.  
+  `COGNITO`: Amazon Cognito. The provider URL is cognito-identity.amazonaws.com. When choosing the `COGNITO` provider type, don’t use the "CustomFederationProviderUrl" parameter which is only needed when the external provider is custom.
+  `CUSTOM_OIDC`: Custom OpenID Connect (OIDC) provider. When choosing `CUSTOM_OIDC` type, use the `CustomFederationProviderUrl` parameter to provide the custom OIDC provider URL.
Type: String  
Required: No

 ** [ExternalLoginId](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-ExternalLoginId"></a>
The identity ID for a user in the external login provider.  
Type: String  
Required: No

 ** [IamArn](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-IamArn"></a>
The ARN of the IAM user or role that you are registering with Amazon Quick Sight.   
Type: String  
Required: No

 ** [SessionName](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-SessionName"></a>
You need to use this parameter only when you register one or more users using an assumed IAM role. You don't need to provide the session name for other scenarios, for example when you are registering an IAM user or an Amazon Quick Sight user. You can register multiple users using the same IAM role if each user has a different session name. For more information on assuming IAM roles, see [https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html) in the * AWS CLI Reference.*   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `[\w+=.@-]*`   
Required: No

 ** [Tags](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-Tags"></a>
The tags to associate with the user.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [UserName](#API_RegisterUser_RequestSyntax) **   <a name="QS-RegisterUser-request-UserName"></a>
The Amazon Quick Sight user name that you want to create for the user you are registering.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `[\u0020-\u00FF]+`   
Required: No

## Response Syntax
<a name="API_RegisterUser_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "User": { 
      "Active": boolean,
      "Arn": "string",
      "CustomPermissionsName": "string",
      "Email": "string",
      "ExternalLoginFederationProviderType": "string",
      "ExternalLoginFederationProviderUrl": "string",
      "ExternalLoginId": "string",
      "IdentityType": "string",
      "PrincipalId": "string",
      "Role": "string",
      "UserName": "string"
   },
   "UserInvitationUrl": "string"
}
```

## Response Elements
<a name="API_RegisterUser_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_RegisterUser_ResponseSyntax) **   <a name="QS-RegisterUser-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_RegisterUser_ResponseSyntax) **   <a name="QS-RegisterUser-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [User](#API_RegisterUser_ResponseSyntax) **   <a name="QS-RegisterUser-response-User"></a>
The user's user name.  
Type: [User](API_User.md) object

 ** [UserInvitationUrl](#API_RegisterUser_ResponseSyntax) **   <a name="QS-RegisterUser-response-UserInvitationUrl"></a>
The URL the user visits to complete registration and provide a password. This is returned only for users with an identity type of `QUICKSIGHT`.  
Type: String

## Errors
<a name="API_RegisterUser_Errors"></a>

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

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

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

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_RegisterUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/RegisterUser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisterUser) 