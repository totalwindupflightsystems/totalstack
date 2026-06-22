---
id: "@specs/aws/batch/docs/API_DescribeServiceJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeServiceJob"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeServiceJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeServiceJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeServiceJob
<a name="API_DescribeServiceJob"></a>

The details of a service job.

## Request Syntax
<a name="API_DescribeServiceJob_RequestSyntax"></a>

```
POST /v1/describeservicejob HTTP/1.1
Content-type: application/json

{
   "jobId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeServiceJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeServiceJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobId](#API_DescribeServiceJob_RequestSyntax) **   <a name="Batch-DescribeServiceJob-request-jobId"></a>
The job ID for the service job to describe.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_DescribeServiceJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attempts": [ 
      { 
         "serviceResourceId": { 
            "name": "string",
            "value": "string"
         },
         "startedAt": number,
         "statusReason": "string",
         "stoppedAt": number
      }
   ],
   "capacityUsage": [ 
      { 
         "capacityUnit": "string",
         "quantity": number
      }
   ],
   "createdAt": number,
   "isTerminated": boolean,
   "jobArn": "string",
   "jobId": "string",
   "jobName": "string",
   "jobQueue": "string",
   "latestAttempt": { 
      "serviceResourceId": { 
         "name": "string",
         "value": "string"
      }
   },
   "preemptionConfiguration": { 
      "preemptionRetriesBeforeTermination": number
   },
   "preemptionSummary": { 
      "preemptedAttemptCount": number,
      "recentPreemptedAttempts": [ 
         { 
            "serviceResourceId": { 
               "name": "string",
               "value": "string"
            },
            "startedAt": number,
            "statusReason": "string",
            "stoppedAt": number
         }
      ]
   },
   "quotaShareName": "string",
   "retryStrategy": { 
      "attempts": number,
      "evaluateOnExit": [ 
         { 
            "action": "string",
            "onStatusReason": "string"
         }
      ]
   },
   "scheduledAt": number,
   "schedulingPriority": number,
   "serviceJobType": "string",
   "serviceRequestPayload": "string",
   "shareIdentifier": "string",
   "startedAt": number,
   "status": "string",
   "statusReason": "string",
   "stoppedAt": number,
   "tags": { 
      "string" : "string" 
   },
   "timeoutConfig": { 
      "attemptDurationSeconds": number
   }
}
```

## Response Elements
<a name="API_DescribeServiceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attempts](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-attempts"></a>
A list of job attempts associated with the service job.  
Type: Array of [ServiceJobAttemptDetail](API_ServiceJobAttemptDetail.md) objects

 ** [capacityUsage](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-capacityUsage"></a>
The configured capacity for the service job, such as the number of instances. The number of instances should be the same value as the `serviceRequestPayload.InstanceCount` field.  
Type: Array of [ServiceJobCapacityUsageDetail](API_ServiceJobCapacityUsageDetail.md) objects

 ** [createdAt](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-createdAt"></a>
The Unix timestamp (in milliseconds) for when the service job was created.  
Type: Long

 ** [isTerminated](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-isTerminated"></a>
Indicates whether the service job has been terminated.  
Type: Boolean

 ** [jobArn](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-jobArn"></a>
The Amazon Resource Name (ARN) of the service job.  
Type: String

 ** [jobId](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-jobId"></a>
The job ID for the service job.  
Type: String

 ** [jobName](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-jobName"></a>
The name of the service job.  
Type: String

 ** [jobQueue](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-jobQueue"></a>
The ARN of the job queue that the service job is associated with.  
Type: String

 ** [latestAttempt](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-latestAttempt"></a>
The latest attempt associated with the service job.  
Type: [LatestServiceJobAttempt](API_LatestServiceJobAttempt.md) object

 ** [preemptionConfiguration](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-preemptionConfiguration"></a>
Specifies the service job behavior when preempted.  
Type: [ServiceJobPreemptionConfiguration](API_ServiceJobPreemptionConfiguration.md) object

 ** [preemptionSummary](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-preemptionSummary"></a>
Summarizes the preemptions of the service job. This field appears on a service job when it has been preempted.  
Type: [ServiceJobPreemptionSummary](API_ServiceJobPreemptionSummary.md) object

 ** [quotaShareName](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-quotaShareName"></a>
The name of the quota share that the service job is associated with.  
Type: String

 ** [retryStrategy](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-retryStrategy"></a>
The retry strategy to use for failed service jobs that are submitted with this service job.  
Type: [ServiceJobRetryStrategy](API_ServiceJobRetryStrategy.md) object

 ** [scheduledAt](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-scheduledAt"></a>
The Unix timestamp (in milliseconds) for when the service job was scheduled. This represents when the service job was dispatched to SageMaker and the service job transitioned to the `SCHEDULED` state.  
Type: Long

 ** [schedulingPriority](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-schedulingPriority"></a>
The scheduling priority of the service job.   
Type: Integer

 ** [serviceJobType](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-serviceJobType"></a>
The type of service job. For SageMaker Training jobs, this value is `SAGEMAKER_TRAINING`.  
Type: String  
Valid Values: `SAGEMAKER_TRAINING` 

 ** [serviceRequestPayload](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-serviceRequestPayload"></a>
The request, in JSON, for the service that the `SubmitServiceJob` operation is queueing.   
Type: String

 ** [shareIdentifier](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-shareIdentifier"></a>
The share identifier for the service job. This is used for fair-share scheduling.  
Type: String

 ** [startedAt](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-startedAt"></a>
The Unix timestamp (in milliseconds) for when the service job was started.  
Type: Long

 ** [status](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-status"></a>
The current status of the service job.   
Type: String  
Valid Values: `SUBMITTED | PENDING | RUNNABLE | SCHEDULED | STARTING | RUNNING | SUCCEEDED | FAILED` 

 ** [statusReason](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-statusReason"></a>
A short, human-readable string to provide more details for the current status of the service job.  
Type: String

 ** [stoppedAt](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-stoppedAt"></a>
The Unix timestamp (in milliseconds) for when the service job stopped running.  
Type: Long

 ** [tags](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-tags"></a>
The tags that are associated with the service job. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.

 ** [timeoutConfig](#API_DescribeServiceJob_ResponseSyntax) **   <a name="Batch-DescribeServiceJob-response-timeoutConfig"></a>
The timeout configuration for the service job.  
Type: [ServiceJobTimeout](API_ServiceJobTimeout.md) object

## Errors
<a name="API_DescribeServiceJob_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_DescribeServiceJob_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeServiceJob_Example_1"></a>

This example describes the specified service job.

#### Sample Request
<a name="API_DescribeServiceJob_Example_1_Request"></a>

```
POST /v1/describeservicejob HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T092145Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "jobId": "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d"
}
```

#### Sample Response
<a name="API_DescribeServiceJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Fri, 01 Aug 2025 09:21:46 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 49j3k6m2n8p5q7r4s1t9w2f76dsexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: def3ghi6jkl9mno2pqr5stu8vwx2yz5012cdefghijklmnopqrexample

{
  "jobId": "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
  "jobName": "sagemaker-training-job-example",
  "jobArn": "arn:aws:batch:us-east-1:123456789012:service-job/a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
  "jobQueue": "arn:aws:batch:us-east-1:123456789012:job-queue/sagemaker-training-queue",
  "status": "SUCCEEDED",
  "statusReason": "Job completed successfully",
  "serviceJobType": "SAGEMAKER_TRAINING",
  "schedulingPriority": 100,
  "isTerminated": false,
  "createdAt": 1722507600000,
  "startedAt": 1722507660000,
  "stoppedAt": 1722511260000,
  "serviceRequestPayload": "{\"TrainingJobName\": \"sagemaker-training-job-example\", \"AlgorithmSpecification\": {\"TrainingImage\": \"123456789012.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:1.8.0-cpu-py3\", \"TrainingInputMode\": \"File\", \"ContainerEntrypoint\": [\"sleep\", \"1\"]}, \"RoleArn\":\"arn:aws:iam::123456789012:role/SageMakerExecutionRole\", \"OutputDataConfig\": {\"S3OutputPath\": \"s3://example-bucket/model-output/\"}, \"ResourceConfig\": {\"InstanceType\": \"ml.m5.large\", \"InstanceCount\": 1, \"VolumeSizeInGB\": 1}}",  
  "latestAttempt": {
   "serviceResourceId": {
     "name": "TrainingJobArn",
     "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/sagemaker-training-job-example"
     }
  },
  "attempts": [
    {
      "serviceResourceId": {
    	 "name": "TrainingJobArn",
    	 "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/sagemaker-training-job-example"
    	},
      "startedAt": 1722507660000,
      "stoppedAt": 1722511260000,
      "statusReason": "Completed"
    }
  ],
  "tags": {}
}
```

## See Also
<a name="API_DescribeServiceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeServiceJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeServiceJob) 