---
id: "@specs/aws/batch/docs/API_CancelJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelJob"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# CancelJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_CancelJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelJob
<a name="API_CancelJob"></a>

Cancels a job in an AWS Batch job queue. Jobs that are in a `SUBMITTED`, `PENDING`, or `RUNNABLE` state are cancelled and the job status is updated to `FAILED`.

**Note**  
A `PENDING` job is canceled after all dependency jobs are completed. Therefore, it may take longer than expected to cancel a job in `PENDING` status.  
When you try to cancel an array parent job in `PENDING`, AWS Batch attempts to cancel all child jobs. The array parent job is canceled when all child jobs are completed.

Jobs that progressed to the `STARTING` or `RUNNING` state aren't canceled. However, the API operation still succeeds, even if no job is canceled. These jobs must be terminated with the [TerminateJob](API_TerminateJob.md) operation.

## Request Syntax
<a name="API_CancelJob_RequestSyntax"></a>

```
POST /v1/canceljob HTTP/1.1
Content-type: application/json

{
   "jobId": "{{string}}",
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CancelJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobId](#API_CancelJob_RequestSyntax) **   <a name="Batch-CancelJob-request-jobId"></a>
The AWS Batch job ID of the job to cancel.  
Type: String  
Required: Yes

 ** [reason](#API_CancelJob_RequestSyntax) **   <a name="Batch-CancelJob-request-reason"></a>
A message to attach to the job that explains the reason for canceling it. This message is returned by future [DescribeJobs](API_DescribeJobs.md) operations on the job. It is also recorded in the AWS Batch activity logs.  
This parameter has as limit of 1024 characters.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_CancelJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelJob_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_CancelJob_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CancelJob_Example_1"></a>

This example cancels a job with the specified job ID.

#### Sample Request
<a name="API_CancelJob_Example_1_Request"></a>

```
POST /v1/canceljob HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161130T001258Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.1.0 botocore/1.4.79

{
  "reason": "Cancelling job.",
  "jobId": "1d828f65-7a4d-42e8-996d-3b900ed59dc4"
}
```

#### Sample Response
<a name="API_CancelJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 2
Connection: keep-alive
Date: Wed, 30 Nov 2016 00:12:59 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 bfdd5909914586f5bc4851846228c27f.cloudfront.net (CloudFront)
X-Amz-Cf-Id: whn1dX1uTx34Lvao7-7ZdkDXEbCZ_sjn3v3hHVFgbo1ORJtXyeggSw==

{}
```

## See Also
<a name="API_CancelJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/CancelJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/CancelJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CancelJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/CancelJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CancelJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/CancelJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/CancelJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/CancelJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/CancelJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CancelJob) 