---
id: "@specs/aws/emr/docs/API_GetOnClusterAppUIPresignedURL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetOnClusterAppUIPresignedURL"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# GetOnClusterAppUIPresignedURL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_GetOnClusterAppUIPresignedURL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetOnClusterAppUIPresignedURL
<a name="API_GetOnClusterAppUIPresignedURL"></a>

The presigned URL properties for the cluster's application user interface.

## Request Syntax
<a name="API_GetOnClusterAppUIPresignedURL_RequestSyntax"></a>

```
{
   "ApplicationId": "{{string}}",
   "ClusterId": "{{string}}",
   "DryRun": {{boolean}},
   "ExecutionRoleArn": "{{string}}",
   "OnClusterAppUIType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOnClusterAppUIPresignedURL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_GetOnClusterAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetOnClusterAppUIPresignedURL-request-ApplicationId"></a>
The application ID associated with the cluster's application user interface presigned URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [ClusterId](#API_GetOnClusterAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetOnClusterAppUIPresignedURL-request-ClusterId"></a>
The cluster ID associated with the cluster's application user interface presigned URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [DryRun](#API_GetOnClusterAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetOnClusterAppUIPresignedURL-request-DryRun"></a>
Determines if the user interface presigned URL is for a dry run.  
Type: Boolean  
Required: No

 ** [ExecutionRoleArn](#API_GetOnClusterAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetOnClusterAppUIPresignedURL-request-ExecutionRoleArn"></a>
The execution role ARN associated with the cluster's application user interface presigned URL.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** [OnClusterAppUIType](#API_GetOnClusterAppUIPresignedURL_RequestSyntax) **   <a name="EMR-GetOnClusterAppUIPresignedURL-request-OnClusterAppUIType"></a>
The application UI type associated with the cluster's application user interface presigned URL.  
Type: String  
Valid Values: `SparkHistoryServer | YarnTimelineService | TezUI | ApplicationMaster | JobHistoryServer | ResourceManager`   
Required: No

## Response Syntax
<a name="API_GetOnClusterAppUIPresignedURL_ResponseSyntax"></a>

```
{
   "PresignedURL": "string",
   "PresignedURLReady": boolean
}
```

## Response Elements
<a name="API_GetOnClusterAppUIPresignedURL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PresignedURL](#API_GetOnClusterAppUIPresignedURL_ResponseSyntax) **   <a name="EMR-GetOnClusterAppUIPresignedURL-response-PresignedURL"></a>
The cluster's generated presigned URL.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

 ** [PresignedURLReady](#API_GetOnClusterAppUIPresignedURL_ResponseSyntax) **   <a name="EMR-GetOnClusterAppUIPresignedURL-response-PresignedURLReady"></a>
Used to determine if the presigned URL is ready.  
Type: Boolean

## Errors
<a name="API_GetOnClusterAppUIPresignedURL_Errors"></a>

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
<a name="API_GetOnClusterAppUIPresignedURL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetOnClusterAppUIPresignedURL) 