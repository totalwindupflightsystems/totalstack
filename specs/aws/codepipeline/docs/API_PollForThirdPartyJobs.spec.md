---
id: "@specs/aws/codepipeline/docs/API_PollForThirdPartyJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PollForThirdPartyJobs"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PollForThirdPartyJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PollForThirdPartyJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PollForThirdPartyJobs
<a name="API_PollForThirdPartyJobs"></a>

Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.

**Important**  
When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.

## Request Syntax
<a name="API_PollForThirdPartyJobs_RequestSyntax"></a>

```
{
   "actionTypeId": { 
      "category": "{{string}}",
      "owner": "{{string}}",
      "provider": "{{string}}",
      "version": "{{string}}"
   },
   "maxBatchSize": {{number}}
}
```

## Request Parameters
<a name="API_PollForThirdPartyJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actionTypeId](#API_PollForThirdPartyJobs_RequestSyntax) **   <a name="CodePipeline-PollForThirdPartyJobs-request-actionTypeId"></a>
Represents information about an action type.  
Type: [ActionTypeId](API_ActionTypeId.md) object  
Required: Yes

 ** [maxBatchSize](#API_PollForThirdPartyJobs_RequestSyntax) **   <a name="CodePipeline-PollForThirdPartyJobs-request-maxBatchSize"></a>
The maximum number of jobs to return in a poll for jobs call.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## Response Syntax
<a name="API_PollForThirdPartyJobs_ResponseSyntax"></a>

```
{
   "jobs": [ 
      { 
         "clientId": "string",
         "jobId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PollForThirdPartyJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_PollForThirdPartyJobs_ResponseSyntax) **   <a name="CodePipeline-PollForThirdPartyJobs-response-jobs"></a>
Information about the jobs to take action on.  
Type: Array of [ThirdPartyJob](API_ThirdPartyJob.md) objects

## Errors
<a name="API_PollForThirdPartyJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActionTypeNotFoundException **   
The specified action type cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_PollForThirdPartyJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/PollForThirdPartyJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PollForThirdPartyJobs) 