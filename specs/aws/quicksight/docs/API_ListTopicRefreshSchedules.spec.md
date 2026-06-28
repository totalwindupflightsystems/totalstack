---
id: "@specs/aws/quicksight/docs/API_ListTopicRefreshSchedules"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTopicRefreshSchedules"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListTopicRefreshSchedules

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListTopicRefreshSchedules
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTopicRefreshSchedules
<a name="API_ListTopicRefreshSchedules"></a>

Lists all of the refresh schedules for a topic.

## Request Syntax
<a name="API_ListTopicRefreshSchedules_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/topics/{{TopicId}}/schedules HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTopicRefreshSchedules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListTopicRefreshSchedules_RequestSyntax) **   <a name="QS-ListTopicRefreshSchedules-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the topic whose refresh schedule you want described.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TopicId](#API_ListTopicRefreshSchedules_RequestSyntax) **   <a name="QS-ListTopicRefreshSchedules-request-uri-TopicId"></a>
The ID for the topic that you want to describe. This ID is unique per AWS Region for each AWS account.  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: Yes

## Request Body
<a name="API_ListTopicRefreshSchedules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTopicRefreshSchedules_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RefreshSchedules": [ 
      { 
         "DatasetArn": "string",
         "DatasetId": "string",
         "DatasetName": "string",
         "RefreshSchedule": { 
            "BasedOnSpiceSchedule": boolean,
            "IsEnabled": boolean,
            "RepeatAt": "string",
            "StartingAt": number,
            "Timezone": "string",
            "TopicScheduleType": "string"
         }
      }
   ],
   "RequestId": "string",
   "TopicArn": "string",
   "TopicId": "string"
}
```

## Response Elements
<a name="API_ListTopicRefreshSchedules_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListTopicRefreshSchedules_ResponseSyntax) **   <a name="QS-ListTopicRefreshSchedules-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RefreshSchedules](#API_ListTopicRefreshSchedules_ResponseSyntax) **   <a name="QS-ListTopicRefreshSchedules-response-RefreshSchedules"></a>
The list of topic refresh schedules.  
Type: Array of [TopicRefreshScheduleSummary](API_TopicRefreshScheduleSummary.md) objects

 ** [RequestId](#API_ListTopicRefreshSchedules_ResponseSyntax) **   <a name="QS-ListTopicRefreshSchedules-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TopicArn](#API_ListTopicRefreshSchedules_ResponseSyntax) **   <a name="QS-ListTopicRefreshSchedules-response-TopicArn"></a>
The Amazon Resource Name (ARN) of the topic.  
Type: String

 ** [TopicId](#API_ListTopicRefreshSchedules_ResponseSyntax) **   <a name="QS-ListTopicRefreshSchedules-response-TopicId"></a>
The ID for the topic that you want to describe. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$` 

## Errors
<a name="API_ListTopicRefreshSchedules_Errors"></a>

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
<a name="API_ListTopicRefreshSchedules_Examples"></a>

### Example
<a name="API_ListTopicRefreshSchedules_Example_1"></a>

This example illustrates one usage of ListTopicRefreshSchedules.

#### Sample Request
<a name="API_ListTopicRefreshSchedules_Example_1_Request"></a>

```
GET /accounts/{AwsAccountId}/topics/{TopicId}/schedules HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_ListTopicRefreshSchedules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListTopicRefreshSchedules) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListTopicRefreshSchedules) 