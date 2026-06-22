---
id: "@specs/aws/emr/docs/API_UpdateStudioSessionMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateStudioSessionMapping"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# UpdateStudioSessionMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_UpdateStudioSessionMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateStudioSessionMapping
<a name="API_UpdateStudioSessionMapping"></a>

Updates the session policy attached to the user or group for the specified Amazon EMR Studio.

## Request Syntax
<a name="API_UpdateStudioSessionMapping_RequestSyntax"></a>

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
<a name="API_UpdateStudioSessionMapping_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityId](#API_UpdateStudioSessionMapping_RequestSyntax) **   <a name="EMR-UpdateStudioSessionMapping-request-IdentityId"></a>
The globally unique identifier (GUID) of the user or group. For more information, see [UserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId) and [GroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId) in the *IAM Identity Center Identity Store API Reference*. Either `IdentityName` or `IdentityId` must be specified.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityName](#API_UpdateStudioSessionMapping_RequestSyntax) **   <a name="EMR-UpdateStudioSessionMapping-request-IdentityName"></a>
The name of the user or group to update. For more information, see [UserName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName) and [DisplayName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName) in the *IAM Identity Center Identity Store API Reference*. Either `IdentityName` or `IdentityId` must be specified.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityType](#API_UpdateStudioSessionMapping_RequestSyntax) **   <a name="EMR-UpdateStudioSessionMapping-request-IdentityType"></a>
Specifies whether the identity to update is a user or a group.  
Type: String  
Valid Values: `USER | GROUP`   
Required: Yes

 ** [SessionPolicyArn](#API_UpdateStudioSessionMapping_RequestSyntax) **   <a name="EMR-UpdateStudioSessionMapping-request-SessionPolicyArn"></a>
The Amazon Resource Name (ARN) of the session policy to associate with the specified user or group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [StudioId](#API_UpdateStudioSessionMapping_RequestSyntax) **   <a name="EMR-UpdateStudioSessionMapping-request-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Elements
<a name="API_UpdateStudioSessionMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateStudioSessionMapping_Errors"></a>

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
<a name="API_UpdateStudioSessionMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/UpdateStudioSessionMapping) 