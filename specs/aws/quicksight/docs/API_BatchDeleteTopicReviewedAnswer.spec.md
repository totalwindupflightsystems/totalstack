---
id: "@specs/aws/quicksight/docs/API_BatchDeleteTopicReviewedAnswer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDeleteTopicReviewedAnswer"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# BatchDeleteTopicReviewedAnswer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_BatchDeleteTopicReviewedAnswer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDeleteTopicReviewedAnswer
<a name="API_BatchDeleteTopicReviewedAnswer"></a>

Deletes reviewed answers for Q Topic.

## Request Syntax
<a name="API_BatchDeleteTopicReviewedAnswer_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/topics/{{TopicId}}/batch-delete-reviewed-answers HTTP/1.1
Content-type: application/json

{
   "AnswerIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteTopicReviewedAnswer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_BatchDeleteTopicReviewedAnswer_RequestSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-request-uri-AwsAccountId"></a>
The ID of the AWS account that you want to delete a reviewed answers in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TopicId](#API_BatchDeleteTopicReviewedAnswer_RequestSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-request-uri-TopicId"></a>
The ID for the topic reviewed answer that you want to delete. This ID is unique per AWS Region for each AWS account.  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: Yes

## Request Body
<a name="API_BatchDeleteTopicReviewedAnswer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AnswerIds](#API_BatchDeleteTopicReviewedAnswer_RequestSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-request-AnswerIds"></a>
The Answer IDs of the Answers to be deleted.  
Type: Array of strings  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: No

## Response Syntax
<a name="API_BatchDeleteTopicReviewedAnswer_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "InvalidAnswers": [ 
      { 
         "AnswerId": "string",
         "Error": "string"
      }
   ],
   "RequestId": "string",
   "SucceededAnswers": [ 
      { 
         "AnswerId": "string"
      }
   ],
   "TopicArn": "string",
   "TopicId": "string"
}
```

## Response Elements
<a name="API_BatchDeleteTopicReviewedAnswer_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_BatchDeleteTopicReviewedAnswer_ResponseSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [InvalidAnswers](#API_BatchDeleteTopicReviewedAnswer_ResponseSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-response-InvalidAnswers"></a>
The definition of Answers that are invalid and not deleted.  
Type: Array of [InvalidTopicReviewedAnswer](API_InvalidTopicReviewedAnswer.md) objects

 ** [RequestId](#API_BatchDeleteTopicReviewedAnswer_ResponseSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [SucceededAnswers](#API_BatchDeleteTopicReviewedAnswer_ResponseSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-response-SucceededAnswers"></a>
The definition of Answers that are successfully deleted.  
Type: Array of [SucceededTopicReviewedAnswer](API_SucceededTopicReviewedAnswer.md) objects

 ** [TopicArn](#API_BatchDeleteTopicReviewedAnswer_ResponseSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-response-TopicArn"></a>
The Amazon Resource Name (ARN) of the topic.  
Type: String

 ** [TopicId](#API_BatchDeleteTopicReviewedAnswer_ResponseSyntax) **   <a name="QS-BatchDeleteTopicReviewedAnswer-response-TopicId"></a>
The ID of the topic reviewed answer that you want to delete. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$` 

## Errors
<a name="API_BatchDeleteTopicReviewedAnswer_Errors"></a>

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
<a name="API_BatchDeleteTopicReviewedAnswer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchDeleteTopicReviewedAnswer) 