---
id: "@specs/aws/transcribe/docs/API_DeleteCallAnalyticsJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCallAnalyticsJob"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# DeleteCallAnalyticsJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_DeleteCallAnalyticsJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCallAnalyticsJob
<a name="API_DeleteCallAnalyticsJob"></a>

Deletes a Call Analytics job. To use this operation, specify the name of the job you want to delete using `CallAnalyticsJobName`. Job names are case sensitive.

## Request Syntax
<a name="API_DeleteCallAnalyticsJob_RequestSyntax"></a>

```
{
   "CallAnalyticsJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCallAnalyticsJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CallAnalyticsJobName](#API_DeleteCallAnalyticsJob_RequestSyntax) **   <a name="transcribe-DeleteCallAnalyticsJob-request-CallAnalyticsJobName"></a>
The name of the Call Analytics job you want to delete. Job names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Elements
<a name="API_DeleteCallAnalyticsJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCallAnalyticsJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteCallAnalyticsJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/DeleteCallAnalyticsJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/DeleteCallAnalyticsJob) 