---
id: "@specs/aws/codepipeline/docs/API_AcknowledgeJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AcknowledgeJob"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# AcknowledgeJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_AcknowledgeJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AcknowledgeJob
<a name="API_AcknowledgeJob"></a>

Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.

## Request Syntax
<a name="API_AcknowledgeJob_RequestSyntax"></a>

```
{
   "jobId": "{{string}}",
   "nonce": "{{string}}"
}
```

## Request Parameters
<a name="API_AcknowledgeJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [jobId](#API_AcknowledgeJob_RequestSyntax) **   <a name="CodePipeline-AcknowledgeJob-request-jobId"></a>
The unique system-generated ID of the job for which you want to confirm receipt.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** [nonce](#API_AcknowledgeJob_RequestSyntax) **   <a name="CodePipeline-AcknowledgeJob-request-nonce"></a>
A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the [PollForJobs](API_PollForJobs.md) request that returned this job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

## Response Syntax
<a name="API_AcknowledgeJob_ResponseSyntax"></a>

```
{
   "status": "string"
}
```

## Response Elements
<a name="API_AcknowledgeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_AcknowledgeJob_ResponseSyntax) **   <a name="CodePipeline-AcknowledgeJob-response-status"></a>
Whether the job worker has received the specified job.  
Type: String  
Valid Values: `Created | Queued | Dispatched | InProgress | TimedOut | Succeeded | Failed` 

## Errors
<a name="API_AcknowledgeJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNonceException **   
The nonce was specified in an invalid format.  
HTTP Status Code: 400

 ** JobNotFoundException **   
The job was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_AcknowledgeJob_Examples"></a>

### Example
<a name="API_AcknowledgeJob_Example_1"></a>

This example illustrates one usage of AcknowledgeJob.

#### Sample Request
<a name="API_AcknowledgeJob_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 63
X-Amz-Target: CodePipeline_20150709.AcknowledgeJob
X-Amz-Date: 20160707T205252Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "nonce": "3",
  "jobId": "f4f4ff82-2d11-EXAMPLE"
}
```

#### Sample Response
<a name="API_AcknowledgeJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 23

{
  "status": "InProgress"
}
```

## See Also
<a name="API_AcknowledgeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/AcknowledgeJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/AcknowledgeJob) 