---
id: "@specs/aws/codepipeline/docs/API_PutJobFailureResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutJobFailureResult"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PutJobFailureResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PutJobFailureResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutJobFailureResult
<a name="API_PutJobFailureResult"></a>

Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.

## Request Syntax
<a name="API_PutJobFailureResult_RequestSyntax"></a>

```
{
   "failureDetails": { 
      "externalExecutionId": "{{string}}",
      "message": "{{string}}",
      "type": "{{string}}"
   },
   "jobId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutJobFailureResult_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [failureDetails](#API_PutJobFailureResult_RequestSyntax) **   <a name="CodePipeline-PutJobFailureResult-request-failureDetails"></a>
The details about the failure of a job.  
Type: [FailureDetails](API_FailureDetails.md) object  
Required: Yes

 ** [jobId](#API_PutJobFailureResult_RequestSyntax) **   <a name="CodePipeline-PutJobFailureResult-request-jobId"></a>
The unique system-generated ID of the job that failed. This is the same ID returned from `PollForJobs`.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

## Response Elements
<a name="API_PutJobFailureResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutJobFailureResult_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidJobStateException **   
The job state was specified in an invalid format.  
HTTP Status Code: 400

 ** JobNotFoundException **   
The job was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_PutJobFailureResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/PutJobFailureResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PutJobFailureResult) 