---
id: "@specs/aws/batch/docs/API_SubmitServiceJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubmitServiceJob"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# SubmitServiceJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_SubmitServiceJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubmitServiceJob
<a name="API_SubmitServiceJob"></a>

Submits a service job to a specified job queue to run on SageMaker AI. A service job is a unit of work that you submit to AWS Batch for execution on SageMaker AI.

## Request Syntax
<a name="API_SubmitServiceJob_RequestSyntax"></a>

```
POST /v1/submitservicejob HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "jobName": "{{string}}",
   "jobQueue": "{{string}}",
   "preemptionConfiguration": { 
      "preemptionRetriesBeforeTermination": {{number}}
   },
   "quotaShareName": "{{string}}",
   "retryStrategy": { 
      "attempts": {{number}},
      "evaluateOnExit": [ 
         { 
            "action": "{{string}}",
            "onStatusReason": "{{string}}"
         }
      ]
   },
   "schedulingPriority": {{number}},
   "serviceJobType": "{{string}}",
   "serviceRequestPayload": "{{string}}",
   "shareIdentifier": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "timeoutConfig": { 
      "attemptDurationSeconds": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_SubmitServiceJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SubmitServiceJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-clientToken"></a>
A unique identifier for the request. This token is used to ensure idempotency of requests. If this parameter is specified and two submit requests with identical payloads and `clientToken`s are received, these requests are considered the same request and the second request is rejected.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** [jobName](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-jobName"></a>
The name of the service job. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [jobQueue](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-jobQueue"></a>
The job queue into which the service job is submitted. You can specify either the name or the ARN of the queue. The job queue must have the type `SAGEMAKER_TRAINING`.  
Type: String  
Required: Yes

 ** [preemptionConfiguration](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-preemptionConfiguration"></a>
Specifies the service job behavior when preempted.  
Type: [ServiceJobPreemptionConfiguration](API_ServiceJobPreemptionConfiguration.md) object  
Required: No

 ** [quotaShareName](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-quotaShareName"></a>
The quota share for the service job. Don't specify this parameter if the job queue doesn't have a quota share scheduling policy. If the job queue has a quota share scheduling policy, then this parameter must be specified.  
Type: String  
Required: No

 ** [retryStrategy](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-retryStrategy"></a>
The retry strategy to use for failed service jobs that are submitted with this service job request.   
Type: [ServiceJobRetryStrategy](API_ServiceJobRetryStrategy.md) object  
Required: No

 ** [schedulingPriority](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-schedulingPriority"></a>
The scheduling priority of the service job. Valid values are integers between 0 and 9999.  
Type: Integer  
Required: No

 ** [serviceJobType](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-serviceJobType"></a>
The type of service job. For SageMaker Training jobs, specify `SAGEMAKER_TRAINING`.  
Type: String  
Valid Values: `SAGEMAKER_TRAINING`   
Required: Yes

 ** [serviceRequestPayload](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-serviceRequestPayload"></a>
The request, in JSON, for the service that the SubmitServiceJob operation is queueing.   
Type: String  
Required: Yes

 ** [shareIdentifier](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-shareIdentifier"></a>
The share identifier for the service job. Don't specify this parameter if the job queue doesn't have a fair-share scheduling policy. If the job queue has a fair-share scheduling policy, then this parameter must be specified.  
Type: String  
Required: No

 ** [tags](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-tags"></a>
The tags that you apply to the service job request. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [timeoutConfig](#API_SubmitServiceJob_RequestSyntax) **   <a name="Batch-SubmitServiceJob-request-timeoutConfig"></a>
The timeout configuration for the service job. If none is specified, AWS Batch defers to the default timeout of the underlying service handling the job.  
Type: [ServiceJobTimeout](API_ServiceJobTimeout.md) object  
Required: No

## Response Syntax
<a name="API_SubmitServiceJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobArn": "string",
   "jobId": "string",
   "jobName": "string"
}
```

## Response Elements
<a name="API_SubmitServiceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_SubmitServiceJob_ResponseSyntax) **   <a name="Batch-SubmitServiceJob-response-jobArn"></a>
The Amazon Resource Name (ARN) for the service job.  
Type: String

 ** [jobId](#API_SubmitServiceJob_ResponseSyntax) **   <a name="Batch-SubmitServiceJob-response-jobId"></a>
The unique identifier for the service job.  
Type: String

 ** [jobName](#API_SubmitServiceJob_ResponseSyntax) **   <a name="Batch-SubmitServiceJob-response-jobName"></a>
The name of the service job.  
Type: String

## Errors
<a name="API_SubmitServiceJob_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_SubmitServiceJob_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_SubmitServiceJob_Example_1"></a>

This example submits a SageMaker training job to the specified job queue.

#### Sample Request
<a name="API_SubmitServiceJob_Example_1_Request"></a>

```
POST /v1/submitservicejob HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T083015Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
    "jobName": "sagemaker-training-job-example",
    "jobQueue": "sagemaker-training-queue",
    "retryStrategy": {
        "attempts": 2,
        "evaluateOnExit": [
            {
                "action": "Retry",
                "onStatusReason": "Received status from SageMaker: AlgorithmError: *"
            },
            {
                "action": "EXIT",
                "onStatusReason": "*"
            }
        ]
    },
    "serviceJobType": "SAGEMAKER_TRAINING",
    "serviceRequestPayload": "{\"TrainingJobName\": \"sagemaker-training-job-example\", \"AlgorithmSpecification\": {\"TrainingImage\": \"123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.8.0-cpu-py3\", \"TrainingInputMode\": \"File\", \"ContainerEntrypoint\":  [\"sleep\", \"1\"]}, \"RoleArn\":\"arn:aws:iam::123456789012:role/SageMakerExecutionRole\", \"OutputDataConfig\": {\"S3OutputPath\": \"s3://example-bucket/model-output/\"}, \"ResourceConfig\": {\"InstanceType\": \"ml.m5.large\", \"InstanceCount\": 1, \"VolumeSizeInGB\": 1}}",
    "timeoutConfig": {
        "attemptDurationSeconds": 300
    },
    "tags": {
        "tag-name": "value-123"
    }
}
```

#### Sample Response
<a name="API_SubmitServiceJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Fri, 01 Aug 2025 08:30:16 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 hf65sd33h6j9k2l5m8n1p4q7r0sexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: jkl5mno8pqr1stu4vwx7yz0123ghijklmnopqrstuvwexample

{
  "jobName": "sagemaker-training-job-example",
  "jobId": "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
  "jobArn": "arn:aws:batch:us-east-1:123456789012:service-job/a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d"
}
```

## See Also
<a name="API_SubmitServiceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/SubmitServiceJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/SubmitServiceJob) 