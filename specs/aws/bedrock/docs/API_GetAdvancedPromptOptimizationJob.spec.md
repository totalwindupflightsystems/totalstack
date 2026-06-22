---
id: "@specs/aws/bedrock/docs/API_GetAdvancedPromptOptimizationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAdvancedPromptOptimizationJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetAdvancedPromptOptimizationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetAdvancedPromptOptimizationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAdvancedPromptOptimizationJob
<a name="API_GetAdvancedPromptOptimizationJob"></a>

Gets information about an advanced prompt optimization job.

## Request Syntax
<a name="API_GetAdvancedPromptOptimizationJob_RequestSyntax"></a>

```
GET /advanced-prompt-optimization-jobs/{{jobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAdvancedPromptOptimizationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobIdentifier](#API_GetAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-request-uri-jobIdentifier"></a>
The ARN or ID of the advanced prompt optimization job.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `((arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/)?[a-z0-9]{12})`   
Required: Yes

## Request Body
<a name="API_GetAdvancedPromptOptimizationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAdvancedPromptOptimizationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "encryptionKeyArn": "string",
   "failureMessage": "string",
   "inputConfig": { 
      "s3Uri": "string"
   },
   "jobArn": "string",
   "jobDescription": "string",
   "jobName": "string",
   "jobStatus": "string",
   "lastModifiedTime": "string",
   "modelConfigurations": [ 
      { 
         "additionalModelRequestFields": { 
            "string" : JSON value 
         },
         "inferenceConfig": { 
            "maxTokens": number,
            "stopSequences": [ "string" ],
            "temperature": number,
            "topP": number
         },
         "modelId": "string"
      }
   ],
   "outputConfig": { 
      "s3Uri": "string"
   }
}
```

## Response Elements
<a name="API_GetAdvancedPromptOptimizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-creationTime"></a>
The time at which the job was created.  
Type: Timestamp

 ** [encryptionKeyArn](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-encryptionKeyArn"></a>
The ARN of the KMS key used to encrypt the output data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [failureMessage](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-failureMessage"></a>
If the job failed, a message describing the failure.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [inputConfig](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-inputConfig"></a>
The input data configuration for the optimization job.  
Type: [AdvancedPromptOptimizationInputConfig](API_AdvancedPromptOptimizationInputConfig.md) object

 ** [jobArn](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-jobArn"></a>
The ARN of the advanced prompt optimization job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/[a-z0-9]{12}` 

 ** [jobDescription](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-jobDescription"></a>
The description of the advanced prompt optimization job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [jobName](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-jobName"></a>
The name of the advanced prompt optimization job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9.+-]*` 

 ** [jobStatus](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-jobStatus"></a>
The status of the advanced prompt optimization job.  
Type: String  
Valid Values: `InProgress | Completed | Failed | PartiallyCompleted | Stopping | Stopped | Deleting` 

 ** [lastModifiedTime](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-lastModifiedTime"></a>
The time at which the job was last modified.  
Type: Timestamp

 ** [modelConfigurations](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-modelConfigurations"></a>
The model configurations used in the optimization job.  
Type: Array of [ModelConfiguration](API_ModelConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [outputConfig](#API_GetAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-GetAdvancedPromptOptimizationJob-response-outputConfig"></a>
The output data configuration for the optimization job.  
Type: [AdvancedPromptOptimizationOutputConfig](API_AdvancedPromptOptimizationOutputConfig.md) object

## Errors
<a name="API_GetAdvancedPromptOptimizationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_GetAdvancedPromptOptimizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAdvancedPromptOptimizationJob) 