---
id: "@specs/aws/emr/docs/API_UpdateStudio"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateStudio"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# UpdateStudio

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_UpdateStudio
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateStudio
<a name="API_UpdateStudio"></a>

Updates an Amazon EMR Studio configuration, including attributes such as name, description, and subnets.

## Request Syntax
<a name="API_UpdateStudio_RequestSyntax"></a>

```
{
   "DefaultS3Location": "{{string}}",
   "Description": "{{string}}",
   "EncryptionKeyArn": "{{string}}",
   "Name": "{{string}}",
   "StudioId": "{{string}}",
   "SubnetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateStudio_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DefaultS3Location](#API_UpdateStudio_RequestSyntax) **   <a name="EMR-UpdateStudio-request-DefaultS3Location"></a>
The Amazon S3 location to back up Workspaces and notebook files for the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [Description](#API_UpdateStudio_RequestSyntax) **   <a name="EMR-UpdateStudio-request-Description"></a>
A detailed description to assign to the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [EncryptionKeyArn](#API_UpdateStudio_RequestSyntax) **   <a name="EMR-UpdateStudio-request-EncryptionKeyArn"></a>
The AWS KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [Name](#API_UpdateStudio_RequestSyntax) **   <a name="EMR-UpdateStudio-request-Name"></a>
A descriptive name for the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [StudioId](#API_UpdateStudio_RequestSyntax) **   <a name="EMR-UpdateStudio-request-StudioId"></a>
The ID of the Amazon EMR Studio to update.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [SubnetIds](#API_UpdateStudio_RequestSyntax) **   <a name="EMR-UpdateStudio-request-SubnetIds"></a>
A list of subnet IDs to associate with the Amazon EMR Studio. The list can include new subnet IDs, but must also include all of the subnet IDs previously associated with the Studio. The list order does not matter. A Studio can have a maximum of 5 subnets. The subnets must belong to the same VPC as the Studio.   
Type: Array of strings  
Required: No

## Response Elements
<a name="API_UpdateStudio_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateStudio_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateStudio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/UpdateStudio) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/UpdateStudio) 