---
id: "@specs/aws/fsx/docs/API_DetachAndDeleteS3AccessPoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DetachAndDeleteS3AccessPoint"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DetachAndDeleteS3AccessPoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DetachAndDeleteS3AccessPoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DetachAndDeleteS3AccessPoint
<a name="API_DetachAndDeleteS3AccessPoint"></a>

Detaches an S3 access point from an Amazon FSx volume and deletes the S3 access point.

The requester requires the following permission to perform this action:
+  `fsx:DetachAndDeleteS3AccessPoint` 
+  `s3:DeleteAccessPoint` 

## Request Syntax
<a name="API_DetachAndDeleteS3AccessPoint_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DetachAndDeleteS3AccessPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DetachAndDeleteS3AccessPoint_RequestSyntax) **   <a name="FSx-DetachAndDeleteS3AccessPoint-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [Name](#API_DetachAndDeleteS3AccessPoint_RequestSyntax) **   <a name="FSx-DetachAndDeleteS3AccessPoint-request-Name"></a>
The name of the S3 access point attachment that you want to delete.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Pattern: `^(?=[a-z0-9])[a-z0-9-]{1,48}[a-z0-9]$`   
Required: Yes

## Response Syntax
<a name="API_DetachAndDeleteS3AccessPoint_ResponseSyntax"></a>

```
{
   "Lifecycle": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_DetachAndDeleteS3AccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Lifecycle](#API_DetachAndDeleteS3AccessPoint_ResponseSyntax) **   <a name="FSx-DetachAndDeleteS3AccessPoint-response-Lifecycle"></a>
The lifecycle status of the S3 access point attachment.  
Type: String  
Valid Values: `AVAILABLE | CREATING | DELETING | UPDATING | FAILED | MISCONFIGURED` 

 ** [Name](#API_DetachAndDeleteS3AccessPoint_ResponseSyntax) **   <a name="FSx-DetachAndDeleteS3AccessPoint-response-Name"></a>
The name of the S3 access point attachment being deleted.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Pattern: `^(?=[a-z0-9])[a-z0-9-]{1,48}[a-z0-9]$` 

## Errors
<a name="API_DetachAndDeleteS3AccessPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** S3AccessPointAttachmentNotFound **   
The access point specified was not found.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DetachAndDeleteS3AccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DetachAndDeleteS3AccessPoint) 