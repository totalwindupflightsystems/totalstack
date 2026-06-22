---
id: "@specs/aws/bedrock-agent/docs/API_GetEvaluationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetEvaluationJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetEvaluationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetEvaluationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetEvaluationJob
<a name="API_GetEvaluationJob"></a>

Gets information about an evaluation job, such as the status of the job.

## Request Syntax
<a name="API_GetEvaluationJob_RequestSyntax"></a>

```
GET /evaluation-jobs/{{jobIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEvaluationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobIdentifier](#API_GetEvaluationJob_RequestSyntax) **   <a name="bedrock-GetEvaluationJob-request-uri-jobIdentifier"></a>
The Amazon Resource Name (ARN) of the evaluation job you want get information on.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12})`   
Required: Yes

## Request Body
<a name="API_GetEvaluationJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEvaluationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationType": "string",
   "creationTime": "string",
   "customerEncryptionKeyId": "string",
   "evaluationConfig": { ... },
   "failureMessages": [ "string" ],
   "inferenceConfig": { ... },
   "jobArn": "string",
   "jobDescription": "string",
   "jobName": "string",
   "jobType": "string",
   "lastModifiedTime": "string",
   "outputDataConfig": { 
      "s3Uri": "string"
   },
   "roleArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_GetEvaluationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationType](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-applicationType"></a>
Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).  
Type: String  
Valid Values: `ModelEvaluation | RagEvaluation` 

 ** [creationTime](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-creationTime"></a>
The time the evaluation job was created.  
Type: Timestamp

 ** [customerEncryptionKeyId](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-customerEncryptionKeyId"></a>
The Amazon Resource Name (ARN) of the customer managed encryption key specified when the evaluation job was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)` 

 ** [evaluationConfig](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-evaluationConfig"></a>
Contains the configuration details of either an automated or human-based evaluation job.  
Type: [EvaluationConfig](API_EvaluationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [failureMessages](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-failureMessages"></a>
A list of strings that specify why the evaluation job failed to create.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 20 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [inferenceConfig](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-inferenceConfig"></a>
Contains the configuration details of the inference model used for the evaluation job.   
Type: [EvaluationInferenceConfig](API_EvaluationInferenceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [jobArn](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the evaluation job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12}` 

 ** [jobDescription](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-jobDescription"></a>
The description of the evaluation job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `.+` 

 ** [jobName](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-jobName"></a>
The name for the evaluation job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-z0-9](-*[a-z0-9]){0,62}` 

 ** [jobType](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-jobType"></a>
Specifies whether the evaluation job is automated or human-based.  
Type: String  
Valid Values: `Human | Automated` 

 ** [lastModifiedTime](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-lastModifiedTime"></a>
The time the evaluation job was last modified.  
Type: Timestamp

 ** [outputDataConfig](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-outputDataConfig"></a>
Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.  
Type: [EvaluationOutputDataConfig](API_EvaluationOutputDataConfig.md) object

 ** [roleArn](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role used in the evaluation job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_GetEvaluationJob_ResponseSyntax) **   <a name="bedrock-GetEvaluationJob-response-status"></a>
The current status of the evaluation job.  
Type: String  
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting` 

## Errors
<a name="API_GetEvaluationJob_Errors"></a>

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
<a name="API_GetEvaluationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetEvaluationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetEvaluationJob) 