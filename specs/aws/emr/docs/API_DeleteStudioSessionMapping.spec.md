---
id: "@specs/aws/emr/docs/API_DeleteStudioSessionMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteStudioSessionMapping"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# DeleteStudioSessionMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_DeleteStudioSessionMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteStudioSessionMapping
<a name="API_DeleteStudioSessionMapping"></a>

Removes a user or group from an Amazon EMR Studio.

## Request Syntax
<a name="API_DeleteStudioSessionMapping_RequestSyntax"></a>

```
{
   "IdentityId": "{{string}}",
   "IdentityName": "{{string}}",
   "IdentityType": "{{string}}",
   "StudioId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteStudioSessionMapping_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityId](#API_DeleteStudioSessionMapping_RequestSyntax) **   <a name="EMR-DeleteStudioSessionMapping-request-IdentityId"></a>
The globally unique identifier (GUID) of the user or group to remove from the Amazon EMR Studio. For more information, see [UserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId) and [GroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId) in the *IAM Identity Center Identity Store API Reference*. Either `IdentityName` or `IdentityId` must be specified.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityName](#API_DeleteStudioSessionMapping_RequestSyntax) **   <a name="EMR-DeleteStudioSessionMapping-request-IdentityName"></a>
The name of the user name or group to remove from the Amazon EMR Studio. For more information, see [UserName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName) and [DisplayName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName) in the *IAM Identity Center Store API Reference*. Either `IdentityName` or `IdentityId` must be specified.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityType](#API_DeleteStudioSessionMapping_RequestSyntax) **   <a name="EMR-DeleteStudioSessionMapping-request-IdentityType"></a>
Specifies whether the identity to delete from the Amazon EMR Studio is a user or a group.  
Type: String  
Valid Values: `USER | GROUP`   
Required: Yes

 ** [StudioId](#API_DeleteStudioSessionMapping_RequestSyntax) **   <a name="EMR-DeleteStudioSessionMapping-request-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Elements
<a name="API_DeleteStudioSessionMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteStudioSessionMapping_Errors"></a>

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
<a name="API_DeleteStudioSessionMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/DeleteStudioSessionMapping) 