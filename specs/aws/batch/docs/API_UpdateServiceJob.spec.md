---
id: "@specs/aws/batch/docs/API_UpdateServiceJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateServiceJob"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# UpdateServiceJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_UpdateServiceJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateServiceJob
<a name="API_UpdateServiceJob"></a>

Updates the priority of a specified service job in an AWS Batch job queue.

## Request Syntax
<a name="API_UpdateServiceJob_RequestSyntax"></a>

```
POST /v1/updateservicejob HTTP/1.1
Content-type: application/json

{
   "jobId": "{{string}}",
   "schedulingPriority": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateServiceJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateServiceJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobId](#API_UpdateServiceJob_RequestSyntax) **   <a name="Batch-UpdateServiceJob-request-jobId"></a>
The AWS Batch job ID of the job to update.  
Type: String  
Required: Yes

 ** [schedulingPriority](#API_UpdateServiceJob_RequestSyntax) **   <a name="Batch-UpdateServiceJob-request-schedulingPriority"></a>
The scheduling priority for the job. This only affects jobs in job queues with a quota-share or fair-share scheduling policy. Jobs with a higher scheduling priority are scheduled before jobs with a lower scheduling priority within a share.  
The minimum supported value is 0 and the maximum supported value is 9999.  
Type: Integer  
Required: Yes

## Response Syntax
<a name="API_UpdateServiceJob_ResponseSyntax"></a>

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
<a name="API_UpdateServiceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobArn](#API_UpdateServiceJob_ResponseSyntax) **   <a name="Batch-UpdateServiceJob-response-jobArn"></a>
The Amazon Resource Name (ARN) for the job.  
Type: String

 ** [jobId](#API_UpdateServiceJob_ResponseSyntax) **   <a name="Batch-UpdateServiceJob-response-jobId"></a>
The unique identifier for the job.  
Type: String

 ** [jobName](#API_UpdateServiceJob_ResponseSyntax) **   <a name="Batch-UpdateServiceJob-response-jobName"></a>
The name of the job.  
Type: String

## Errors
<a name="API_UpdateServiceJob_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## See Also
<a name="API_UpdateServiceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/UpdateServiceJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/UpdateServiceJob) 