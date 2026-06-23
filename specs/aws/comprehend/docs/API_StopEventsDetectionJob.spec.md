---
id: "@specs/aws/comprehend/docs/API_StopEventsDetectionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StopEventsDetectionJob"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# StopEventsDetectionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_StopEventsDetectionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StopEventsDetectionJob
<a name="API_StopEventsDetectionJob"></a>

**Important**  
Service availability notice: Amazon Comprehend topic modeling, event detection, and prompt safety classification features will no longer be available to new customers, effective April 30, 2026. For more information, see [Amazon Comprehend feature availability change](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-availability-change.html). 

Stops an events detection job in progress.

## Request Syntax
<a name="API_StopEventsDetectionJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopEventsDetectionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_StopEventsDetectionJob_RequestSyntax) **   <a name="comprehend-StopEventsDetectionJob-request-JobId"></a>
The identifier of the events detection job to stop.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`   
Required: Yes

## Response Syntax
<a name="API_StopEventsDetectionJob_ResponseSyntax"></a>

```
{
   "JobId": "string",
   "JobStatus": "string"
}
```

## Response Elements
<a name="API_StopEventsDetectionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StopEventsDetectionJob_ResponseSyntax) **   <a name="comprehend-StopEventsDetectionJob-response-JobId"></a>
The identifier of the events detection job to stop.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$` 

 ** [JobStatus](#API_StopEventsDetectionJob_ResponseSyntax) **   <a name="comprehend-StopEventsDetectionJob-response-JobStatus"></a>
The status of the events detection job.  
Type: String  
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED | STOP_REQUESTED | STOPPED` 

## Errors
<a name="API_StopEventsDetectionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** JobNotFoundException **   
The specified job was not found. Check the job ID and try again.  
HTTP Status Code: 400

## See Also
<a name="API_StopEventsDetectionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/StopEventsDetectionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/StopEventsDetectionJob) 