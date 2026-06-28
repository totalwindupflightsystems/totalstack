---
id: "@specs/aws/quicksight/docs/API_CreateRefreshSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateRefreshSchedule"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateRefreshSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateRefreshSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateRefreshSchedule
<a name="API_CreateRefreshSchedule"></a>

Creates a refresh schedule for a dataset. You can create up to 5 different schedules for a single dataset.

## Request Syntax
<a name="API_CreateRefreshSchedule_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}}/refresh-schedules HTTP/1.1
Content-type: application/json

{
   "Schedule": { 
      "Arn": "{{string}}",
      "RefreshType": "{{string}}",
      "ScheduleFrequency": { 
         "Interval": "{{string}}",
         "RefreshOnDay": { 
            "DayOfMonth": "{{string}}",
            "DayOfWeek": "{{string}}"
         },
         "TimeOfTheDay": "{{string}}",
         "Timezone": "{{string}}"
      },
      "ScheduleId": "{{string}}",
      "StartAfterDateTime": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateRefreshSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateRefreshSchedule_RequestSyntax) **   <a name="QS-CreateRefreshSchedule-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DataSetId](#API_CreateRefreshSchedule_RequestSyntax) **   <a name="QS-CreateRefreshSchedule-request-uri-DataSetId"></a>
The ID of the dataset.  
Required: Yes

## Request Body
<a name="API_CreateRefreshSchedule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Schedule](#API_CreateRefreshSchedule_RequestSyntax) **   <a name="QS-CreateRefreshSchedule-request-Schedule"></a>
The refresh schedule.  
Type: [RefreshSchedule](API_RefreshSchedule.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateRefreshSchedule_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "RequestId": "string",
   "ScheduleId": "string"
}
```

## Response Elements
<a name="API_CreateRefreshSchedule_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateRefreshSchedule_ResponseSyntax) **   <a name="QS-CreateRefreshSchedule-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateRefreshSchedule_ResponseSyntax) **   <a name="QS-CreateRefreshSchedule-response-Arn"></a>
The Amazon Resource Name (ARN) for the refresh schedule.  
Type: String

 ** [RequestId](#API_CreateRefreshSchedule_ResponseSyntax) **   <a name="QS-CreateRefreshSchedule-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [ScheduleId](#API_CreateRefreshSchedule_ResponseSyntax) **   <a name="QS-CreateRefreshSchedule-response-ScheduleId"></a>
The ID of the refresh schedule.  
Type: String

## Errors
<a name="API_CreateRefreshSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateRefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateRefreshSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateRefreshSchedule) 