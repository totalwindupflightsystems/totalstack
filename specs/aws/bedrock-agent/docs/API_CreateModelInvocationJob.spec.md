---
id: "@specs/aws/bedrock-agent/docs/API_CreateModelInvocationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateModelInvocationJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateModelInvocationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CreateModelInvocationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateModelInvocationJob
<a name="API_CreateModelInvocationJob"></a>

Creates a batch inference job to invoke a model on multiple prompts. Format your data according to [Format your inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data) and upload it to an Amazon S3 bucket. For more information, see [Process multiple prompts with batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html).

The response returns a `jobArn` that you can use to stop or get details about the job.

## Request Syntax
<a name="API_CreateModelInvocationJob_RequestSyntax"></a>

```
POST /model-invocation-job HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "inputDataConfig": { ... },
   "jobName": "{{string}}",
   "modelId": "{{string}}",
   "modelInvocationType": "{{string}}",
   "outputDataConfig": { ... },
   "roleArn": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "timeoutDurationInHours": {{number}},
   "vpcConfig": { 
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateModelInvocationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateModelInvocationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]{1,256}(-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [inputDataConfig](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-inputDataConfig"></a>
Details about the location of the input to the batch inference job.  
Type: [ModelInvocationJobInputDataConfig](API_ModelInvocationJobInputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [jobName](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-jobName"></a>
A name to give the batch inference job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z0-9]{1,63}(-*[a-zA-Z0-9\+\-\.]){0,63}`   
Required: Yes

 ** [modelId](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-modelId"></a>
The unique identifier of the foundation model to use for the batch inference job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-:]{1,63}/[a-z0-9]{12}$)|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)$)|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+$)))|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})|(([0-9a-zA-Z][_-]?)+)`   
Required: Yes

 ** [modelInvocationType](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-modelInvocationType"></a>
The invocation endpoint for ModelInvocationJob  
Type: String  
Valid Values: `InvokeModel | Converse`   
Required: No

 ** [outputDataConfig](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-outputDataConfig"></a>
Details about the location of the output of the batch inference job.  
Type: [ModelInvocationJobOutputDataConfig](API_ModelInvocationJobOutputDataConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [roleArn](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-roleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at [Create a service role for batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [tags](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-tags"></a>
Any tags to associate with the batch inference job. For more information, see [Tagging Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [timeoutDurationInHours](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-timeoutDurationInHours"></a>
The number of hours after which to force the batch inference job to time out.  
Type: Integer  
Valid Range: Minimum value of 24. Maximum value of 168.  
Required: No

 ** [vpcConfig](#API_CreateModelInvocationJob_RequestSyntax) **   <a name="bedrock-CreateModelInvocationJob-request-vpcConfig"></a>
The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see [Protect batch inference jobs using a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc).  
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateModelInvocationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobArn": "string"
}
```

## Response Elements
<a name="API_CreateModelInvocationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_CreateModelInvocationJob_ResponseSyntax) **   <a name="bedrock-CreateModelInvocationJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the batch inference job.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:model-invocation-job/[a-z0-9]{12})` 

## Errors
<a name="API_CreateModelInvocationJob_Errors"></a>

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

## Examples
<a name="API_CreateModelInvocationJob_Examples"></a>

### Create a batch inference job
<a name="API_CreateModelInvocationJob_Example_1"></a>

This example illustrates one usage of CreateModelInvocationJob.

```
POST /model-invocation-job HTTP/1.1
Content-type: application/json
                
{
    "clientRequestToken": "string",
    "inputDataConfig": {
        "s3InputDataConfig": {
            "s3Uri": "s3://input-bucket/abc.jsonl"
        }
    },
    "jobName": "my-batch-job",
    "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
    "outputDataConfig": {
        "s3OutputDataConfig": {
            "s3Uri": "s3://output-bucket/"
        }
    },
    "roleArn": "arn:aws:iam::123456789012:role/MyBatchInferenceRole"
}
```

## See Also
<a name="API_CreateModelInvocationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateModelInvocationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateModelInvocationJob) 