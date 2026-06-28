---
id: "@specs/aws/quicksight/docs/API_SearchTopics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchTopics"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchTopics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchTopics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchTopics
<a name="API_SearchTopics"></a>

Searches for any Q topic that exists in an Quick account.

## Request Syntax
<a name="API_SearchTopics_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/topics HTTP/1.1
Content-type: application/json

{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchTopics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchTopics_RequestSyntax) **   <a name="QS-SearchTopics-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the topic that you want to find.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_SearchTopics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchTopics_RequestSyntax) **   <a name="QS-SearchTopics-request-Filters"></a>
The filters that you want to use to search for the topic.  
Type: Array of [TopicSearchFilter](API_TopicSearchFilter.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [MaxResults](#API_SearchTopics_RequestSyntax) **   <a name="QS-SearchTopics-request-MaxResults"></a>
The maximum number of results to be returned per request.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_SearchTopics_RequestSyntax) **   <a name="QS-SearchTopics-request-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String  
Required: No

## Response Syntax
<a name="API_SearchTopics_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "TopicSummaryList": [ 
      { 
         "Arn": "string",
         "Name": "string",
         "TopicId": "string",
         "UserExperienceVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchTopics_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchTopics_ResponseSyntax) **   <a name="QS-SearchTopics-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchTopics_ResponseSyntax) **   <a name="QS-SearchTopics-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_SearchTopics_ResponseSyntax) **   <a name="QS-SearchTopics-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TopicSummaryList](#API_SearchTopics_ResponseSyntax) **   <a name="QS-SearchTopics-response-TopicSummaryList"></a>
A list of topic summaries that is returned by the search topic request.  
Type: Array of [TopicSummary](API_TopicSummary.md) objects

## Errors
<a name="API_SearchTopics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

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

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_SearchTopics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchTopics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchTopics) 