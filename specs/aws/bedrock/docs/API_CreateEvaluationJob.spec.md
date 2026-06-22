---
id: "@specs/aws/bedrock/docs/API_CreateEvaluationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateEvaluationJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateEvaluationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_CreateEvaluationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateEvaluationJob
<a name="API_CreateEvaluationJob"></a>

Creates an evaluation job.

For code examples that demonstrate how to create evaluation jobs, see [Create a model evaluation job in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create.html#model-evaluation-jobs-management-create-auto).

## Request Syntax
<a name="API_CreateEvaluationJob_RequestSyntax"></a>

```
POST /evaluation-jobs HTTP/1.1
Content-type: application/json

{
   "applicationType": "{{string}}",
   "clientRequestToken": "{{string}}",
   "customerEncryptionKeyId": "{{string}}",
   "evaluationConfig": { ... },
   "inferenceConfig": { ... },
   "jobDescription": "{{string}}",
   "jobName": "{{string}}",
   "jobTags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "outputDataConfig": { 
      "s3Uri": "{{string}}"
   },
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateEvaluationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEvaluationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationType](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-applicationType"></a>
Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).  
Type: String  
Valid Values: `ModelEvaluation | RagEvaluation`   
Required: No

 ** [clientRequestToken](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [customerEncryptionKeyId](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-customerEncryptionKeyId"></a>
Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

 ** [evaluationConfig](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-evaluationConfig"></a>
Contains the configuration details of either an automated or human-based evaluation job.  
Type: [EvaluationConfig](API_EvaluationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [inferenceConfig](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-inferenceConfig"></a>
Contains the configuration details of the inference model for the evaluation job.  
For model evaluation jobs, automated jobs support a single model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html), and jobs that use human workers support two models or inference profiles.  
Type: [EvaluationInferenceConfig](API_EvaluationInferenceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [jobDescription](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-jobDescription"></a>
A description of the evaluation job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `.+`   
Required: No

 ** [jobName](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-jobName"></a>
A name for the evaluation job. Names must unique with your AWS account, and your account's AWS region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-z0-9](-*[a-z0-9]){0,62}`   
Required: Yes

 ** [jobTags](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-jobTags"></a>
Tags to attach to the model evaluation job.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [outputDataConfig](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-outputDataConfig"></a>
Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.  
Type: [EvaluationOutputDataConfig](API_EvaluationOutputDataConfig.md) object  
Required: Yes

 ** [roleArn](#API_CreateEvaluationJob_RequestSyntax) **   <a name="bedrock-CreateEvaluationJob-request-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see [Required permissions for model evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

## Response Syntax
<a name="API_CreateEvaluationJob_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "jobArn": "string"
}
```

## Response Elements
<a name="API_CreateEvaluationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_CreateEvaluationJob_ResponseSyntax) **   <a name="bedrock-CreateEvaluationJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the evaluation job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12}` 

## Errors
<a name="API_CreateEvaluationJob_Errors"></a>

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

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_CreateEvaluationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateEvaluationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateEvaluationJob) 