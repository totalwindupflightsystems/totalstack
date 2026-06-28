---
id: "@specs/aws/quicksight/docs/API_DeleteTopicRefreshSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTopicRefreshSchedule"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteTopicRefreshSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteTopicRefreshSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTopicRefreshSchedule
<a name="API_DeleteTopicRefreshSchedule"></a>

Deletes a topic refresh schedule.

## Request Syntax
<a name="API_DeleteTopicRefreshSchedule_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/topics/{{TopicId}}/schedules/{{DatasetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTopicRefreshSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteTopicRefreshSchedule_RequestSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DatasetId](#API_DeleteTopicRefreshSchedule_RequestSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-request-uri-DatasetId"></a>
The ID of the dataset.  
Required: Yes

 ** [TopicId](#API_DeleteTopicRefreshSchedule_RequestSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-request-uri-TopicId"></a>
The ID of the topic that you want to modify. This ID is unique per AWS Region for each AWS account.  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: Yes

## Request Body
<a name="API_DeleteTopicRefreshSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTopicRefreshSchedule_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DatasetArn": "string",
   "RequestId": "string",
   "TopicArn": "string",
   "TopicId": "string"
}
```

## Response Elements
<a name="API_DeleteTopicRefreshSchedule_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteTopicRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DatasetArn](#API_DeleteTopicRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-response-DatasetArn"></a>
The Amazon Resource Name (ARN) of the dataset.  
Type: String

 ** [RequestId](#API_DeleteTopicRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TopicArn](#API_DeleteTopicRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-response-TopicArn"></a>
The Amazon Resource Name (ARN) of the topic.  
Type: String

 ** [TopicId](#API_DeleteTopicRefreshSchedule_ResponseSyntax) **   <a name="QS-DeleteTopicRefreshSchedule-response-TopicId"></a>
The ID of the topic that you want to modify. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$` 

## Errors
<a name="API_DeleteTopicRefreshSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

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

## Examples
<a name="API_DeleteTopicRefreshSchedule_Examples"></a>

### Example
<a name="API_DeleteTopicRefreshSchedule_Example_1"></a>

This example illustrates one usage of DeleteTopicRefreshSchedule.

#### Sample Request
<a name="API_DeleteTopicRefreshSchedule_Example_1_Request"></a>

```
DEL /accounts/{AwsAccountId}/topics/{TopicId}/schedules/{ScheduleId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_DeleteTopicRefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteTopicRefreshSchedule) 