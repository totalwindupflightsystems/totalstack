---
id: "@specs/aws/quicksight/docs/API_StartAutomationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartAutomationJob"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# StartAutomationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_StartAutomationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartAutomationJob
<a name="API_StartAutomationJob"></a>

Starts a new job for a specified automation. The job runs the automation with the provided input payload.

## Request Syntax
<a name="API_StartAutomationJob_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/automation-groups/{{AutomationGroupId}}/automations/{{AutomationId}}/jobs HTTP/1.1
Content-type: application/json

{
   "InputPayload": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartAutomationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AutomationGroupId](#API_StartAutomationJob_RequestSyntax) **   <a name="QS-StartAutomationJob-request-uri-AutomationGroupId"></a>
The ID of the automation group that contains the automation to run.  
Pattern: `[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}`   
Required: Yes

 ** [AutomationId](#API_StartAutomationJob_RequestSyntax) **   <a name="QS-StartAutomationJob-request-uri-AutomationId"></a>
The ID of the automation to run.  
Pattern: `[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}`   
Required: Yes

 ** [AwsAccountId](#API_StartAutomationJob_RequestSyntax) **   <a name="QS-StartAutomationJob-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the automation.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_StartAutomationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InputPayload](#API_StartAutomationJob_RequestSyntax) **   <a name="QS-StartAutomationJob-request-InputPayload"></a>
The input payload for the automation job, provided as a JSON string.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 7000000.  
Pattern: `[\s\S]*[{\[].*[}\]]\s*`   
Required: No

## Response Syntax
<a name="API_StartAutomationJob_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "JobId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_StartAutomationJob_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_StartAutomationJob_ResponseSyntax) **   <a name="QS-StartAutomationJob-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_StartAutomationJob_ResponseSyntax) **   <a name="QS-StartAutomationJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the automation job.  
Type: String

 ** [JobId](#API_StartAutomationJob_ResponseSyntax) **   <a name="QS-StartAutomationJob-response-JobId"></a>
The ID of the automation job that was started.  
Type: String  
Pattern: `[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}` 

 ** [RequestId](#API_StartAutomationJob_ResponseSyntax) **   <a name="QS-StartAutomationJob-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_StartAutomationJob_Errors"></a>

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
<a name="API_StartAutomationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/StartAutomationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StartAutomationJob) 