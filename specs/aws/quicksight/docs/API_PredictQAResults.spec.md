---
id: "@specs/aws/quicksight/docs/API_PredictQAResults"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PredictQAResults"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# PredictQAResults

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_PredictQAResults
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PredictQAResults
<a name="API_PredictQAResults"></a>

Predicts existing visuals or generates new visuals to answer a given query.

This API uses [trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation.html) to ensure that an end user is authenticated and receives the embed URL that is specific to that user. The IAM Identity Center application that the user has logged into needs to have [trusted Identity Propagation enabled for Quick](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.html) with the scope value set to `quicksight:read`. Before you use this action, make sure that you have configured the relevant Quick resource and permissions.

We recommend enabling the `QSearchStatus` API to unlock the full potential of `PredictQnA`. When `QSearchStatus` is enabled, it first checks the specified dashboard for any existing visuals that match the question. If no matching visuals are found, `PredictQnA` uses generative Q&A to provide an answer. To update the `QSearchStatus`, see [UpdateQuickSightQSearchConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateQuickSightQSearchConfiguration.html).

## Request Syntax
<a name="API_PredictQAResults_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/qa/predict HTTP/1.1
Content-type: application/json

{
   "IncludeGeneratedAnswer": "{{string}}",
   "IncludeQuickSightQIndex": "{{string}}",
   "MaxTopicsToConsider": {{number}},
   "QueryText": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PredictQAResults_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_PredictQAResults_RequestSyntax) **   <a name="QS-PredictQAResults-request-uri-AwsAccountId"></a>
The ID of the AWS account that the user wants to execute Predict QA results in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_PredictQAResults_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueryText](#API_PredictQAResults_RequestSyntax) **   <a name="QS-PredictQAResults-request-QueryText"></a>
The query text to be used to predict QA results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** [IncludeGeneratedAnswer](#API_PredictQAResults_RequestSyntax) **   <a name="QS-PredictQAResults-request-IncludeGeneratedAnswer"></a>
Indicates whether generated answers are included or excluded.  
Type: String  
Valid Values: `INCLUDE | EXCLUDE`   
Required: No

 ** [IncludeQuickSightQIndex](#API_PredictQAResults_RequestSyntax) **   <a name="QS-PredictQAResults-request-IncludeQuickSightQIndex"></a>
Indicates whether Q indicies are included or excluded.  
Type: String  
Valid Values: `INCLUDE | EXCLUDE`   
Required: No

 ** [MaxTopicsToConsider](#API_PredictQAResults_RequestSyntax) **   <a name="QS-PredictQAResults-request-MaxTopicsToConsider"></a>
The number of maximum topics to be considered to predict QA results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 4.  
Required: No

## Response Syntax
<a name="API_PredictQAResults_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AdditionalResults": [ 
      { 
         "DashboardVisual": { 
            "DashboardId": "string",
            "DashboardName": "string",
            "DashboardUrl": "string",
            "SheetId": "string",
            "SheetName": "string",
            "VisualId": "string",
            "VisualSubtitle": "string",
            "VisualTitle": "string"
         },
         "GeneratedAnswer": { 
            "AnswerId": "string",
            "AnswerStatus": "string",
            "QuestionId": "string",
            "QuestionText": "string",
            "QuestionUrl": "string",
            "Restatement": "string",
            "TopicId": "string",
            "TopicName": "string"
         },
         "ResultType": "string"
      }
   ],
   "PrimaryResult": { 
      "DashboardVisual": { 
         "DashboardId": "string",
         "DashboardName": "string",
         "DashboardUrl": "string",
         "SheetId": "string",
         "SheetName": "string",
         "VisualId": "string",
         "VisualSubtitle": "string",
         "VisualTitle": "string"
      },
      "GeneratedAnswer": { 
         "AnswerId": "string",
         "AnswerStatus": "string",
         "QuestionId": "string",
         "QuestionText": "string",
         "QuestionUrl": "string",
         "Restatement": "string",
         "TopicId": "string",
         "TopicName": "string"
      },
      "ResultType": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_PredictQAResults_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_PredictQAResults_ResponseSyntax) **   <a name="QS-PredictQAResults-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AdditionalResults](#API_PredictQAResults_ResponseSyntax) **   <a name="QS-PredictQAResults-response-AdditionalResults"></a>
Additional visual responses.  
Type: Array of [QAResult](API_QAResult.md) objects

 ** [PrimaryResult](#API_PredictQAResults_ResponseSyntax) **   <a name="QS-PredictQAResults-response-PrimaryResult"></a>
The primary visual response.  
Type: [QAResult](API_QAResult.md) object

 ** [RequestId](#API_PredictQAResults_ResponseSyntax) **   <a name="QS-PredictQAResults-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_PredictQAResults_Errors"></a>

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

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_PredictQAResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/PredictQAResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PredictQAResults) 