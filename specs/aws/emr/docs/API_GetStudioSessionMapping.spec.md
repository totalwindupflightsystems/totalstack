---
id: "@specs/aws/emr/docs/API_GetStudioSessionMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetStudioSessionMapping"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# GetStudioSessionMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_GetStudioSessionMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetStudioSessionMapping
<a name="API_GetStudioSessionMapping"></a>

Fetches mapping details for the specified Amazon EMR Studio and identity (user or group).

## Request Syntax
<a name="API_GetStudioSessionMapping_RequestSyntax"></a>

```
{
   "IdentityId": "{{string}}",
   "IdentityName": "{{string}}",
   "IdentityType": "{{string}}",
   "StudioId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetStudioSessionMapping_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityId](#API_GetStudioSessionMapping_RequestSyntax) **   <a name="EMR-GetStudioSessionMapping-request-IdentityId"></a>
The globally unique identifier (GUID) of the user or group. For more information, see [UserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId) and [GroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId) in the *IAM Identity Center Identity Store API Reference*. Either `IdentityName` or `IdentityId` must be specified.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityName](#API_GetStudioSessionMapping_RequestSyntax) **   <a name="EMR-GetStudioSessionMapping-request-IdentityName"></a>
The name of the user or group to fetch. For more information, see [UserName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName) and [DisplayName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName) in the *IAM Identity Center Identity Store API Reference*. Either `IdentityName` or `IdentityId` must be specified.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [IdentityType](#API_GetStudioSessionMapping_RequestSyntax) **   <a name="EMR-GetStudioSessionMapping-request-IdentityType"></a>
Specifies whether the identity to fetch is a user or a group.  
Type: String  
Valid Values: `USER | GROUP`   
Required: Yes

 ** [StudioId](#API_GetStudioSessionMapping_RequestSyntax) **   <a name="EMR-GetStudioSessionMapping-request-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Syntax
<a name="API_GetStudioSessionMapping_ResponseSyntax"></a>

```
{
   "SessionMapping": { 
      "CreationTime": number,
      "IdentityId": "string",
      "IdentityName": "string",
      "IdentityType": "string",
      "LastModifiedTime": number,
      "SessionPolicyArn": "string",
      "StudioId": "string"
   }
}
```

## Response Elements
<a name="API_GetStudioSessionMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SessionMapping](#API_GetStudioSessionMapping_ResponseSyntax) **   <a name="EMR-GetStudioSessionMapping-response-SessionMapping"></a>
The session mapping details for the specified Amazon EMR Studio and identity, including session policy ARN and creation time.  
Type: [SessionMappingDetail](API_SessionMappingDetail.md) object

## Errors
<a name="API_GetStudioSessionMapping_Errors"></a>

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
<a name="API_GetStudioSessionMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetStudioSessionMapping) 