---
id: "@specs/aws/codepipeline/docs/API_AcknowledgeThirdPartyJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AcknowledgeThirdPartyJob"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# AcknowledgeThirdPartyJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_AcknowledgeThirdPartyJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AcknowledgeThirdPartyJob
<a name="API_AcknowledgeThirdPartyJob"></a>

Confirms a job worker has received the specified job. Used for partner actions only.

## Request Syntax
<a name="API_AcknowledgeThirdPartyJob_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "jobId": "{{string}}",
   "nonce": "{{string}}"
}
```

## Request Parameters
<a name="API_AcknowledgeThirdPartyJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_AcknowledgeThirdPartyJob_RequestSyntax) **   <a name="CodePipeline-AcknowledgeThirdPartyJob-request-clientToken"></a>
The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** [jobId](#API_AcknowledgeThirdPartyJob_RequestSyntax) **   <a name="CodePipeline-AcknowledgeThirdPartyJob-request-jobId"></a>
The unique system-generated ID of the job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

 ** [nonce](#API_AcknowledgeThirdPartyJob_RequestSyntax) **   <a name="CodePipeline-AcknowledgeThirdPartyJob-request-nonce"></a>
A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response to a [GetThirdPartyJobDetails](API_GetThirdPartyJobDetails.md) request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

## Response Syntax
<a name="API_AcknowledgeThirdPartyJob_ResponseSyntax"></a>

```
{
   "status": "string"
}
```

## Response Elements
<a name="API_AcknowledgeThirdPartyJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_AcknowledgeThirdPartyJob_ResponseSyntax) **   <a name="CodePipeline-AcknowledgeThirdPartyJob-response-status"></a>
The status information for the third party job, if any.  
Type: String  
Valid Values: `Created | Queued | Dispatched | InProgress | TimedOut | Succeeded | Failed` 

## Errors
<a name="API_AcknowledgeThirdPartyJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidClientTokenException **   
The client token was specified in an invalid format  
HTTP Status Code: 400

 ** InvalidNonceException **   
The nonce was specified in an invalid format.  
HTTP Status Code: 400

 ** JobNotFoundException **   
The job was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_AcknowledgeThirdPartyJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/AcknowledgeThirdPartyJob) 