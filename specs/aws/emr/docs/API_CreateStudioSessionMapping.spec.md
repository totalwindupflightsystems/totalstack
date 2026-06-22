---
id: "@specs/aws/emr/docs/API_CreateStudioSessionMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateStudioSessionMapping"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# CreateStudioSessionMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_CreateStudioSessionMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateStudioSessionMapping
<a name="API_CreateStudioSessionMapping"></a>

Maps a user or group to the Amazon EMR Studio specified by `StudioId`, and applies a session policy to refine Studio permissions for that user or group. Use `CreateStudioSessionMapping` to assign users to a Studio when you use IAM Identity Center authentication. For instructions on how to assign users to a Studio when you use IAM authentication, see [Assign a user or group to your EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-manage-users.html#emr-studio-assign-users-groups).

## Request Syntax
<a name="API_CreateStudioSessionMapping_RequestSyntax"></a>

```
{
   "IdentityId": "{{string}}",
   "IdentityName": "{{string}}",
   "IdentityType": "{{string}}",
   "SessionPolicyArn": "{{string}}",
   "StudioId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateStudioSessionMapping_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityId](#API_CreateStudioSessionMapping_RequestSyntax) **   <a name="EMR-CreateStudioSessionMapping-request-IdentityId"></a>
The globally unique identifier (GUID) of the user or group from the IAM Identity Center Identity Store. For more information, see [UserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId) and [GroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId) in the *IAM Identity Center Identity Store API Reference*. Either `IdentityName` or `IdentityId` must be specified, but not both.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityName](#API_CreateStudioSessionMapping_RequestSyntax) **   <a name="EMR-CreateStudioSessionMapping-request-IdentityName"></a>
The name of the user or group. For more information, see [UserName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName) and [DisplayName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName) in the *IAM Identity Center Identity Store API Reference*. Either `IdentityName` or `IdentityId` must be specified, but not both.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityType](#API_CreateStudioSessionMapping_RequestSyntax) **   <a name="EMR-CreateStudioSessionMapping-request-IdentityType"></a>
Specifies whether the identity to map to the Amazon EMR Studio is a user or a group.  
Type: String  
Valid Values: `USER | GROUP`   
Required: Yes

 ** [SessionPolicyArn](#API_CreateStudioSessionMapping_RequestSyntax) **   <a name="EMR-CreateStudioSessionMapping-request-SessionPolicyArn"></a>
The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. You should specify the ARN for the session policy that you want to apply, not the ARN of your user role. For more information, see [Create an Amazon EMR Studio User Role with Session Policies](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-user-role.html).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [StudioId](#API_CreateStudioSessionMapping_RequestSyntax) **   <a name="EMR-CreateStudioSessionMapping-request-StudioId"></a>
The ID of the Amazon EMR Studio to which the user or group will be mapped.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Elements
<a name="API_CreateStudioSessionMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateStudioSessionMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateStudioSessionMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/CreateStudioSessionMapping) 