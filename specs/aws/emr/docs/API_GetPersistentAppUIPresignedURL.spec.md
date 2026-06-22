---
id: "@specs/aws/emr/docs/API_GetPersistentAppUIPresignedURL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPersistentAppUIPresignedURL"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# GetPersistentAppUIPresignedURL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_GetPersistentAppUIPresignedURL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPersistentAppUIPresignedURL
<a name="API_GetPersistentAppUIPresignedURL"></a>

The presigned URL properties for the cluster's application user interface.

## Request Syntax
<a name="API_GetPersistentAppUIPresignedURL_RequestSyntax"></a>

```
{
   "ApplicationId": "{{string}}",
   "AuthProxyCall": {{boolean}},
   "ExecutionRoleArn": "{{string}}",
   "PersistentAppUIId": "{{string}}",
   "PersistentAppUIType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPersistentAppUIPresignedURL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_GetPersistentAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetPersistentAppUIPresignedURL-request-ApplicationId"></a>
The application ID associated with the presigned URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [AuthProxyCall](#API_GetPersistentAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetPersistentAppUIPresignedURL-request-AuthProxyCall"></a>
A boolean that represents if the caller is an authentication proxy call.  
Type: Boolean  
Required: No

 ** [ExecutionRoleArn](#API_GetPersistentAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetPersistentAppUIPresignedURL-request-ExecutionRoleArn"></a>
The execution role ARN associated with the presigned URL.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** [PersistentAppUIId](#API_GetPersistentAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetPersistentAppUIPresignedURL-request-PersistentAppUIId"></a>
The persistent application user interface ID associated with the presigned URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [PersistentAppUIType](#API_GetPersistentAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetPersistentAppUIPresignedURL-request-PersistentAppUIType"></a>
The persistent application user interface type associated with the presigned URL.  
Type: String  
Valid Values: `SHS | TEZ | YTS`   
Required: No

## Response Syntax
<a name="API_GetPersistentAppUIPresignedURL_ResponseSyntax"></a>

```
{
   "PresignedURL": "string",
   "PresignedURLReady": boolean
}
```

## Response Elements
<a name="API_GetPersistentAppUIPresignedURL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PresignedURL](#API_GetPersistentAppUIPresignedURL_ResponseSyntax) **   <a name="EMR-GetPersistentAppUIPresignedURL-response-PresignedURL"></a>
The returned presigned URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

 ** [PresignedURLReady](#API_GetPersistentAppUIPresignedURL_ResponseSyntax) **   <a name="EMR-GetPersistentAppUIPresignedURL-response-PresignedURLReady"></a>
Used to determine if the presigned URL is ready.  
Type: Boolean

## Errors
<a name="API_GetPersistentAppUIPresignedURL_Errors"></a>

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
<a name="API_GetPersistentAppUIPresignedURL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetPersistentAppUIPresignedURL) 