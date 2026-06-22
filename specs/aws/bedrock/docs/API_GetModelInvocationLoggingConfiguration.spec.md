---
id: "@specs/aws/bedrock/docs/API_GetModelInvocationLoggingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetModelInvocationLoggingConfiguration"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetModelInvocationLoggingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetModelInvocationLoggingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetModelInvocationLoggingConfiguration
<a name="API_GetModelInvocationLoggingConfiguration"></a>

Get the current configuration values for model invocation logging.

## Request Syntax
<a name="API_GetModelInvocationLoggingConfiguration_RequestSyntax"></a>

```
GET /logging/modelinvocations HTTP/1.1
```

## URI Request Parameters
<a name="API_GetModelInvocationLoggingConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetModelInvocationLoggingConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetModelInvocationLoggingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "loggingConfig": { 
      "audioDataDeliveryEnabled": boolean,
      "cloudWatchConfig": { 
         "largeDataDeliveryS3Config": { 
            "bucketName": "string",
            "keyPrefix": "string"
         },
         "logGroupName": "string",
         "roleArn": "string"
      },
      "embeddingDataDeliveryEnabled": boolean,
      "imageDataDeliveryEnabled": boolean,
      "s3Config": { 
         "bucketName": "string",
         "keyPrefix": "string"
      },
      "textDataDeliveryEnabled": boolean,
      "videoDataDeliveryEnabled": boolean
   }
}
```

## Response Elements
<a name="API_GetModelInvocationLoggingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [loggingConfig](#API_GetModelInvocationLoggingConfiguration_ResponseSyntax) **   <a name="bedrock-GetModelInvocationLoggingConfiguration-response-loggingConfig"></a>
The current configuration values.  
Type: [LoggingConfig](API_LoggingConfig.md) object

## Errors
<a name="API_GetModelInvocationLoggingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

## See Also
<a name="API_GetModelInvocationLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetModelInvocationLoggingConfiguration) 