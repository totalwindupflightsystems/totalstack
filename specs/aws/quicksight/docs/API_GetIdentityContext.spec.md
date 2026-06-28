---
id: "@specs/aws/quicksight/docs/API_GetIdentityContext"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetIdentityContext"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# GetIdentityContext

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_GetIdentityContext
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetIdentityContext
<a name="API_GetIdentityContext"></a>

Retrieves the identity context for a Quick Sight user in a specified namespace, allowing you to obtain identity tokens that can be used with identity-enhanced IAM role sessions to call identity-aware APIs.

Currently, you can call the following APIs with identity-enhanced Credentials
+  [StartDashboardSnapshotJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartDashboardSnapshotJob.html) 
+  [DescribeDashboardSnapshotJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardSnapshotJob.html) 
+  [DescribeDashboardSnapshotJobResult](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardSnapshotJobResult.html) 

 **Supported Authentication Methods** 

This API supports Quick Sight native users, IAM federated users, and Active Directory users. For Quick Sight users authenticated by AWS Identity Center, see [Identity Center documentation on identity-enhanced IAM role sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.html).

 **Supported Regions** 

The GetIdentityContext API works only in regions that support at least one of these identity types:
+ Amazon Quick Sight native identity
+ IAM federated identity
+ Active Directory

To use this API successfully, call it in the same region where your user's identity resides. For example, if your user's identity is in us-east-1, make the API call in us-east-1. For more information about managing identities in Amazon Quick Sight, see [Identity and access management in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/userguide/identity.html) in the Amazon Quick Sight User Guide.

 **Getting Identity-Enhanced Credentials** 

To obtain identity-enhanced credentials, follow these steps:
+ Call the GetIdentityContext API to retrieve an identity token for the specified user.
+ Use the identity token with the [STS AssumeRole API](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) to obtain identity-enhanced IAM role session credentials.

 **Usage with STS AssumeRole** 

The identity token returned by this API should be used with the STS AssumeRole API to obtain credentials for an identity-enhanced IAM role session. When calling AssumeRole, include the identity token in the `ProvidedContexts` parameter with `ProviderArn` set to `arn:aws:iam::aws:contextProvider/QuickSight` and `ContextAssertion` set to the identity token received from this API.

The assumed role must allow the `sts:SetContext` action in addition to `sts:AssumeRole` in its trust relationship policy. The trust policy should include both actions for the principal that will be assuming the role.

## Request Syntax
<a name="API_GetIdentityContext_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/identity-context HTTP/1.1
Content-type: application/json

{
   "ContextRegion": "{{string}}",
   "Namespace": "{{string}}",
   "SessionExpiresAt": {{number}},
   "UserIdentifier": { ... }
}
```

## URI Request Parameters
<a name="API_GetIdentityContext_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_GetIdentityContext_RequestSyntax) **   <a name="QS-GetIdentityContext-request-uri-AwsAccountId"></a>
The ID for the AWS account that the user whose identity context you want to retrieve is in. Currently, you use the ID for the AWS account that contains your Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_GetIdentityContext_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UserIdentifier](#API_GetIdentityContext_RequestSyntax) **   <a name="QS-GetIdentityContext-request-UserIdentifier"></a>
The identifier for the user whose identity context you want to retrieve.  
Type: [UserIdentifier](API_UserIdentifier.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [ContextRegion](#API_GetIdentityContext_RequestSyntax) **   <a name="QS-GetIdentityContext-request-ContextRegion"></a>
The region in which the context is to be used. Use this parameter to obtain an identity context for cross-region use.  
The specified region must meet the following conditions:  
+ The region must be in the same AWS partition as the region you are calling from. Cross-partition requests are not supported. For example, you cannot specify a region in the `aws-cn` partition when calling from a region in the `aws` partition.
+ It must be a valid Amazon QuickSight supported region.
+ The calling customer account must be enabled in the specified context region.
+ This parameter is not supported when calling from an opt-in region.
Type: String  
Pattern: `[a-z]+-[a-z]+-[0-9]{1}`   
Required: No

 ** [Namespace](#API_GetIdentityContext_RequestSyntax) **   <a name="QS-GetIdentityContext-request-Namespace"></a>
The namespace of the user that you want to get identity context for. This parameter is required when the UserIdentifier is specified using Email or UserName.  
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: No

 ** [SessionExpiresAt](#API_GetIdentityContext_RequestSyntax) **   <a name="QS-GetIdentityContext-request-SessionExpiresAt"></a>
The timestamp at which the session will expire.  
Type: Timestamp  
Required: No

## Response Syntax
<a name="API_GetIdentityContext_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Context": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_GetIdentityContext_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_GetIdentityContext_ResponseSyntax) **   <a name="QS-GetIdentityContext-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_GetIdentityContext_ResponseSyntax) **   <a name="QS-GetIdentityContext-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Context](#API_GetIdentityContext_ResponseSyntax) **   <a name="QS-GetIdentityContext-response-Context"></a>
The identity context information for the user. This is an identity token that should be used as the ContextAssertion parameter in the [STS AssumeRole API](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) call to obtain identity enhanced AWS credentials.  
Type: String

## Errors
<a name="API_GetIdentityContext_Errors"></a>

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

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_GetIdentityContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/GetIdentityContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GetIdentityContext) 