---
id: "@specs/aws/batch/docs/API_TerminateServiceJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TerminateServiceJob"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# TerminateServiceJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_TerminateServiceJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TerminateServiceJob
<a name="API_TerminateServiceJob"></a>

Terminates a service job in a job queue. 

## Request Syntax
<a name="API_TerminateServiceJob_RequestSyntax"></a>

```
POST /v1/terminateservicejob HTTP/1.1
Content-type: application/json

{
   "jobId": "{{string}}",
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_TerminateServiceJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TerminateServiceJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobId](#API_TerminateServiceJob_RequestSyntax) **   <a name="Batch-TerminateServiceJob-request-jobId"></a>
The service job ID of the service job to terminate.  
Type: String  
Required: Yes

 ** [reason](#API_TerminateServiceJob_RequestSyntax) **   <a name="Batch-TerminateServiceJob-request-reason"></a>
A message to attach to the service job that explains the reason for canceling it. This message is returned by `DescribeServiceJob` operations on the service job.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_TerminateServiceJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TerminateServiceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TerminateServiceJob_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_TerminateServiceJob_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_TerminateServiceJob_Example_1"></a>

This example terminates the specified service job with a reason.

#### Sample Request
<a name="API_TerminateServiceJob_Example_1_Request"></a>

```
POST /v1/terminateservicejob HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T164055Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "jobId": "a4d6c728-8ee8-4c65-8e2a-9a5e8f4b7c3d",
  "reason": "Job terminated by user request"
}
```

#### Sample Response
<a name="API_TerminateServiceJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 0
Connection: keep-alive
Date: Fri, 01 Aug 2025 16:40:56 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 254fde64p7r0s3t6u9v2w5x8y1zexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: pqr8stu1vwx4yz7012fghijklmnopqrstuvwxyzabexample
```

## See Also
<a name="API_TerminateServiceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/TerminateServiceJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TerminateServiceJob) 