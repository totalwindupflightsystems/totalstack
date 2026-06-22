---
id: "@specs/aws/bedrock-agent/docs/API_CreateAdvancedPromptOptimizationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAdvancedPromptOptimizationJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateAdvancedPromptOptimizationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CreateAdvancedPromptOptimizationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAdvancedPromptOptimizationJob
<a name="API_CreateAdvancedPromptOptimizationJob"></a>

Creates an advanced prompt optimization job.

## Request Syntax
<a name="API_CreateAdvancedPromptOptimizationJob_RequestSyntax"></a>

```
POST /advanced-prompt-optimization-jobs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "encryptionKeyArn": "{{string}}",
   "inputConfig": { 
      "s3Uri": "{{string}}"
   },
   "jobDescription": "{{string}}",
   "jobName": "{{string}}",
   "modelConfigurations": [ 
      { 
         "additionalModelRequestFields": { 
            "{{string}}" : {{JSON value}} 
         },
         "inferenceConfig": { 
            "maxTokens": {{number}},
            "stopSequences": [ "{{string}}" ],
            "temperature": {{number}},
            "topP": {{number}}
         },
         "modelId": "{{string}}"
      }
   ],
   "outputConfig": { 
      "s3Uri": "{{string}}"
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAdvancedPromptOptimizationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAdvancedPromptOptimizationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [encryptionKeyArn](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-encryptionKeyArn"></a>
The ARN of the KMS key to use for encrypting the output data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [inputConfig](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-inputConfig"></a>
The input data configuration for the optimization job.  
Type: [AdvancedPromptOptimizationInputConfig](API_AdvancedPromptOptimizationInputConfig.md) object  
Required: Yes

 ** [jobDescription](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-jobDescription"></a>
A description of the advanced prompt optimization job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

 ** [jobName](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-jobName"></a>
A name for the advanced prompt optimization job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9.+-]*`   
Required: Yes

 ** [modelConfigurations](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-modelConfigurations"></a>
A list of model configurations for the optimization job.  
Type: Array of [ModelConfiguration](API_ModelConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** [outputConfig](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-outputConfig"></a>
The output data configuration for the optimization job.  
Type: [AdvancedPromptOptimizationOutputConfig](API_AdvancedPromptOptimizationOutputConfig.md) object  
Required: Yes

 ** [tags](#API_CreateAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-request-tags"></a>
Tags to associate with the advanced prompt optimization job.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateAdvancedPromptOptimizationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobArn": "string"
}
```

## Response Elements
<a name="API_CreateAdvancedPromptOptimizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_CreateAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-CreateAdvancedPromptOptimizationJob-response-jobArn"></a>
The ARN of the created advanced prompt optimization job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/[a-z0-9]{12}` 

## Errors
<a name="API_CreateAdvancedPromptOptimizationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.     
 ** resourceName **   
The name of the resource with too many tags.
HTTP Status Code: 400

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateAdvancedPromptOptimizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateAdvancedPromptOptimizationJob) 