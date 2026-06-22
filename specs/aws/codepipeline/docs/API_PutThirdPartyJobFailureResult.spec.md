---
id: "@specs/aws/codepipeline/docs/API_PutThirdPartyJobFailureResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutThirdPartyJobFailureResult"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PutThirdPartyJobFailureResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PutThirdPartyJobFailureResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutThirdPartyJobFailureResult
<a name="API_PutThirdPartyJobFailureResult"></a>

Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.

## Request Syntax
<a name="API_PutThirdPartyJobFailureResult_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "failureDetails": { 
      "externalExecutionId": "{{string}}",
      "message": "{{string}}",
      "type": "{{string}}"
   },
   "jobId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutThirdPartyJobFailureResult_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutThirdPartyJobFailureResult_RequestSyntax) **   <a name="CodePipeline-PutThirdPartyJobFailureResult-request-clientToken"></a>
The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [failureDetails](#API_PutThirdPartyJobFailureResult_RequestSyntax) **   <a name="CodePipeline-PutThirdPartyJobFailureResult-request-failureDetails"></a>
Represents information about failure details.  
Type: [FailureDetails](API_FailureDetails.md) object  
Required: Yes

 ** [jobId](#API_PutThirdPartyJobFailureResult_RequestSyntax) **   <a name="CodePipeline-PutThirdPartyJobFailureResult-request-jobId"></a>
The ID of the job that failed. This is the same ID returned from `PollForThirdPartyJobs`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

## Response Elements
<a name="API_PutThirdPartyJobFailureResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutThirdPartyJobFailureResult_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidClientTokenException **   
The client token was specified in an invalid format  
HTTP Status Code: 400

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
<a name="API_PutThirdPartyJobFailureResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PutThirdPartyJobFailureResult) 