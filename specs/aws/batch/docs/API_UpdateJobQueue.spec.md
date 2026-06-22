---
id: "@specs/aws/batch/docs/API_UpdateJobQueue"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateJobQueue"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdateJobQueue

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdateJobQueue
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateJobQueue
<a name="API_UpdateJobQueue"></a>

Updates a job queue.

## Request Syntax
<a name="API_UpdateJobQueue_RequestSyntax"></a>

```
POST /v1/updatejobqueue HTTP/1.1
Content-type: application/json

{
   "computeEnvironmentOrder": [ 
      { 
         "computeEnvironment": "{{string}}",
         "order": {{number}}
      }
   ],
   "jobQueue": "{{string}}",
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
   "state": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateJobQueue_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateJobQueue_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [computeEnvironmentOrder](#API_UpdateJobQueue_RequestSyntax) **   <a name="Batch-UpdateJobQueue-request-computeEnvironmentOrder"></a>
Details the set of compute environments mapped to a job queue and their order relative to each other. This is one of the parameters used by the job scheduler to determine which compute environment runs a given job. Compute environments must be in the `VALID` state before you can associate them with a job queue. All of the compute environments must be either EC2 (`EC2` or `SPOT`) or Fargate (`FARGATE` or `FARGATE_SPOT`). EC2 and Fargate compute environments can't be mixed.  
All compute environments that are associated with a job queue must share the same architecture. AWS Batch doesn't support mixing compute environment architecture types in a single job queue.
Type: Array of [ComputeEnvironmentOrder](API_ComputeEnvironmentOrder.md) objects  
Required: No

 ** [jobQueue](#API_UpdateJobQueue_RequestSyntax) **   <a name="Batch-UpdateJobQueue-request-jobQueue"></a>
The name or the Amazon Resource Name (ARN) of the job queue.  
Type: String  
Required: Yes

 ** [jobStateTimeLimitActions](#API_UpdateJobQueue_RequestSyntax) **   <a name="Batch-UpdateJobQueue-request-jobStateTimeLimitActions"></a>
The set of actions that AWS Batch perform on jobs that remain at the head of the job queue in the specified state longer than specified times. AWS Batch will perform each action after `maxTimeSeconds` has passed. (**Note**: The minimum value for maxTimeSeconds is 600 (10 minutes) and its maximum value is 86,400 (24 hours).)  
Type: Array of [JobStateTimeLimitAction](API_JobStateTimeLimitAction.md) objects  
Required: No

 ** [priority](#API_UpdateJobQueue_RequestSyntax) **   <a name="Batch-UpdateJobQueue-request-priority"></a>
The priority of the job queue. Job queues with a higher priority (or a higher integer value for the `priority` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of `10` is given scheduling preference over a job queue with a priority value of `1`. All of the compute environments must be either EC2 (`EC2` or `SPOT`) or Fargate (`FARGATE` or `FARGATE_SPOT`). EC2 and Fargate compute environments can't be mixed.  
Type: Integer  
Required: No

 ** [schedulingPolicyArn](#API_UpdateJobQueue_RequestSyntax) **   <a name="Batch-UpdateJobQueue-request-schedulingPolicyArn"></a>
Amazon Resource Name (ARN) of the fair-share scheduling policy. Once a job queue is created, the fair-share scheduling policy can be replaced but not removed. The format is `aws:Partition:batch:Region:Account:scheduling-policy/Name `. For example, `aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy`.  
Type: String  
Required: No

 ** [serviceEnvironmentOrder](#API_UpdateJobQueue_RequestSyntax) **   <a name="Batch-UpdateJobQueue-request-serviceEnvironmentOrder"></a>
The order of the service environment associated with the job queue. Job queues with a higher priority are evaluated first when associated with the same service environment.  
Type: Array of [ServiceEnvironmentOrder](API_ServiceEnvironmentOrder.md) objects  
Required: No

 ** [state](#API_UpdateJobQueue_RequestSyntax) **   <a name="Batch-UpdateJobQueue-request-state"></a>
Describes the queue's ability to accept new jobs. If the job queue state is `ENABLED`, it can accept jobs. If the job queue state is `DISABLED`, new jobs can't be added to the queue, but jobs already in the queue can finish.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## Response Syntax
<a name="API_UpdateJobQueue_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobQueueArn": "string",
   "jobQueueName": "string"
}
```

## Response Elements
<a name="API_UpdateJobQueue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobQueueArn](#API_UpdateJobQueue_ResponseSyntax) **   <a name="Batch-UpdateJobQueue-response-jobQueueArn"></a>
The Amazon Resource Name (ARN) of the job queue.  
Type: String

 ** [jobQueueName](#API_UpdateJobQueue_ResponseSyntax) **   <a name="Batch-UpdateJobQueue-response-jobQueueName"></a>
The name of the job queue.  
Type: String

## Errors
<a name="API_UpdateJobQueue_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_UpdateJobQueue_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateJobQueue_Example_1"></a>

This example disables a job queue so that it can be deleted.

#### Sample Request
<a name="API_UpdateJobQueue_Example_1_Request"></a>

```
POST /v1/updatejobqueue HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161128T201802Z
User-Agent: aws-cli/1.11.21 Python/2.7.12 Darwin/16.1.0 botocore/1.4.78

{
  "state": "DISABLED",
  "jobQueue": "GPGPU"
}
```

#### Sample Response
<a name="API_UpdateJobQueue_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 28 Nov 2016 20:18:03 GMT
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 17de248e6d780f737234d37cc490dbe3.cloudfront.net (CloudFront)
X-Amz-Cf-Id: aVju0hE8eLpjSFl8Y3fOuxgOZXdigQlLcDMwO0plxnynw0dEsOsEgw==

{
  "jobQueueName": "GPGPU",
  "jobQueueArn": "arn:aws:batch:us-east-1:123456789012:job-queue/GPGPU"
}
```

## See Also
<a name="API_UpdateJobQueue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateJobQueue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateJobQueue) 