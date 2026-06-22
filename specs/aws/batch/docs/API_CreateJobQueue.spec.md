---
id: "@specs/aws/batch/docs/API_CreateJobQueue"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateJobQueue"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CreateJobQueue

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CreateJobQueue
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateJobQueue
<a name="API_CreateJobQueue"></a>

Creates an AWS Batch job queue. When you create a job queue, you associate one or more compute environments to the queue and assign an order of preference for the compute environments.

You also set a priority to the job queue that determines the order that the AWS Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.

## Request Syntax
<a name="API_CreateJobQueue_RequestSyntax"></a>

```
POST /v1/createjobqueue HTTP/1.1
Content-type: application/json

{
   "computeEnvironmentOrder": [ 
      { 
         "computeEnvironment": "{{string}}",
         "order": {{number}}
      }
   ],
   "jobQueueName": "{{string}}",
   "jobQueueType": "{{string}}",
   "jobStateTimeLimitActions": [ 
      { 
         "action": "{{string}}",
         "maxTimeSeconds": {{number}},
         "reason": "{{string}}",
         "state": "{{string}}"
      }
   ],
   "priority": {{number}},
   "schedulingPolicyArn": "{{string}}",
   "serviceEnvironmentOrder": [ 
      { 
         "order": {{number}},
         "serviceEnvironment": "{{string}}"
      }
   ],
   "state": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateJobQueue_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateJobQueue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [computeEnvironmentOrder](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-computeEnvironmentOrder"></a>
The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the `VALID` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 (`EC2` or `SPOT`) or Fargate (`FARGATE` or `FARGATE_SPOT`); EC2 and Fargate compute environments can't be mixed.  
All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.
Type: Array of [ComputeEnvironmentOrder](API_ComputeEnvironmentOrder.md) objects  
Required: No

 ** [jobQueueName](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-jobQueueName"></a>
The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).  
Type: String  
Required: Yes

 ** [jobQueueType](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-jobQueueType"></a>
The type of job queue. For service jobs that run on SageMaker Training, this value is `SAGEMAKER_TRAINING`. For regular container jobs, this value is `EKS`, `ECS`, or `ECS_FARGATE` depending on the compute environment.  
Type: String  
Valid Values: `EKS | ECS | ECS_FARGATE | SAGEMAKER_TRAINING`   
Required: No

 ** [jobStateTimeLimitActions](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-jobStateTimeLimitActions"></a>
The set of actions that AWS Batch performs on jobs that remain at the head of the job queue in the specified state longer than specified times. AWS Batch will perform each action after `maxTimeSeconds` has passed. (**Note**: The minimum value for maxTimeSeconds is 600 (10 minutes) and its maximum value is 86,400 (24 hours).)  
Type: Array of [JobStateTimeLimitAction](API_JobStateTimeLimitAction.md) objects  
Required: No

 ** [priority](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-priority"></a>
The priority of the job queue. Job queues with a higher priority (or a higher integer value for the `priority` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of `10` is given scheduling preference over a job queue with a priority value of `1`. All of the compute environments must be either EC2 (`EC2` or `SPOT`) or Fargate (`FARGATE` or `FARGATE_SPOT`); EC2 and Fargate compute environments can't be mixed.  
Type: Integer  
Required: Yes

 ** [schedulingPolicyArn](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-schedulingPolicyArn"></a>
The Amazon Resource Name (ARN) of the fair-share scheduling policy. Job queues that don't have a fair-share scheduling policy are scheduled in a first-in, first-out (FIFO) model. After a job queue has a fair-share scheduling policy, it can be replaced but can't be removed.  
The format is `aws:Partition:batch:Region:Account:scheduling-policy/Name `.  
An example is `aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy`.  
A job queue without a fair-share scheduling policy is scheduled as a FIFO job queue and can't have a fair-share scheduling policy added. Jobs queues with a fair-share scheduling policy can have a maximum of 500 active share identifiers. When the limit has been reached, submissions of any jobs that add a new share identifier fail.  
Type: String  
Required: No

 ** [serviceEnvironmentOrder](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-serviceEnvironmentOrder"></a>
A list of service environments that this job queue can use to allocate jobs. All serviceEnvironments must have the same type. A job queue can't have both a serviceEnvironmentOrder and a computeEnvironmentOrder field.  
Type: Array of [ServiceEnvironmentOrder](API_ServiceEnvironmentOrder.md) objects  
Required: No

 ** [state](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-state"></a>
The state of the job queue. If the job queue state is `ENABLED`, it is able to accept jobs. If the job queue state is `DISABLED`, new jobs can't be added to the queue, but jobs already in the queue can finish.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [tags](#API_CreateJobQueue_RequestSyntax) **   <a name="Batch-CreateJobQueue-request-tags"></a>
The tags that you apply to the job queue to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) in * AWS Batch User Guide*.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_CreateJobQueue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobQueueArn": "string",
   "jobQueueName": "string"
}
```

## Response Elements
<a name="API_CreateJobQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobQueueArn](#API_CreateJobQueue_ResponseSyntax) **   <a name="Batch-CreateJobQueue-response-jobQueueArn"></a>
The Amazon Resource Name (ARN) of the job queue.  
Type: String

 ** [jobQueueName](#API_CreateJobQueue_ResponseSyntax) **   <a name="Batch-CreateJobQueue-response-jobQueueName"></a>
The name of the job queue.  
Type: String

## Errors
<a name="API_CreateJobQueue_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_CreateJobQueue_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateJobQueue_Example_1"></a>

This example creates a job queue called `LowPriority` that uses the `M4Spot` compute environment.

#### Sample Request
<a name="API_CreateJobQueue_Example_1_Request"></a>

```
POST /v1/createjobqueue HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161128T234201Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "priority": 1,
  "state": "ENABLED",
  "computeEnvironmentOrder": [
    {
      "computeEnvironment": "M4Spot",
      "order": 1
    }
  ],
  "jobQueueName": "LowPriority"
}
```

#### Sample Response
<a name="API_CreateJobQueue_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Mon, 28 Nov 2016 23:42:02 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 a44b4468444ef3ee67472bd5c5016098.cloudfront.net (CloudFront)
X-Amz-Cf-Id: bz9IuCM5FNkDfge5y-Zw7nFEjDdTHDYFwbEY2AKUqrt9l2XeKUcuyA==

{
  "jobQueueName": "LowPriority",
  "jobQueueArn": "arn:aws:batch:us-east-1:123456789012:job-queue/LowPriority"
}
```

### Example
<a name="API_CreateJobQueue_Example_2"></a>

This example creates a job queue called `HighPriority` that uses the `C4OnDemand` compute environment with an order of 1 and the `M4Spot` compute environment with an order of 2.

#### Sample Request
<a name="API_CreateJobQueue_Example_2_Request"></a>

```
POST /v1/createjobqueue HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161128T234933Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "priority": 10,
  "state": "ENABLED",
  "computeEnvironmentOrder": [
    {
      "computeEnvironment": "C4OnDemand",
      "order": 1
    },
    {
      "computeEnvironment": "M4Spot",
      "order": 2
    }
  ],
  "jobQueueName": "HighPriority"
}
```

#### Sample Response
<a name="API_CreateJobQueue_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 28 Nov 2016 23:49:34 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 e81bbcbc86832b655de5b9a19317ad01.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 8NB20odDPMaKy9zHa6GPaGN_r562QsynDTRYPuhKwHSvQrMG70IHSQ==

{
  "jobQueueName": "HighPriority",
  "jobQueueArn": "arn:aws:batch:us-east-1:123456789012:job-queue/HighPriority"
}
```

## See Also
<a name="API_CreateJobQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CreateJobQueue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CreateJobQueue) 