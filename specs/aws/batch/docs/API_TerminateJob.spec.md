---
id: "@specs/aws/batch/docs/API_TerminateJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TerminateJob"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# TerminateJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_TerminateJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TerminateJob
<a name="API_TerminateJob"></a>

Terminates a job in a job queue. Jobs that are in the `STARTING` or `RUNNING` state are terminated, which causes them to transition to `FAILED`. Jobs that have not progressed to the `STARTING` state are cancelled.

## Request Syntax
<a name="API_TerminateJob_RequestSyntax"></a>

```
POST /v1/terminatejob HTTP/1.1
Content-type: application/json

{
   "jobId": "{{string}}",
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TerminateJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TerminateJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobId](#API_TerminateJob_RequestSyntax) **   <a name="Batch-TerminateJob-request-jobId"></a>
The AWS Batch job ID of the job to terminate.  
Type: String  
Required: Yes

 ** [reason](#API_TerminateJob_RequestSyntax) **   <a name="Batch-TerminateJob-request-reason"></a>
A message to attach to the job that explains the reason for canceling it. This message is returned by future [DescribeJobs](API_DescribeJobs.md) operations on the job. It is also recorded in the AWS Batch activity logs.  
This parameter has as limit of 1024 characters.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_TerminateJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TerminateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TerminateJob_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_TerminateJob_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_TerminateJob_Example_1"></a>

This example terminates a job with the specified job ID.

#### Sample Request
<a name="API_TerminateJob_Example_1_Request"></a>

```
POST /v1/terminatejob HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20161129T202905Z
User-Agent: aws-cli/1.11.22 Python/2.7.12 Darwin/16.1.0 botocore/1.4.79

{
  "reason": "Terminating job.",
  "jobId": "61e743ed-35e4-48da-b2de-5c8333821c84"
}
```

#### Sample Response
<a name="API_TerminateJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 2
Connection: keep-alive
Date: Tue, 29 Nov 2016 20:29:06 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 16d2657cebef5191828b055567b4efeb.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 681NTs_bPulMwja2HekWMwngcUzx2a8w_oaG27W0L4Pjct7W1T-Fvw==

{}
```

## See Also
<a name="API_TerminateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/TerminateJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TerminateJob) 