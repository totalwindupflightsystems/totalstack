---
id: "@specs/aws/quicksight/docs/API_ListFlows"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFlows"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListFlows

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListFlows
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFlows
<a name="API_ListFlows"></a>

Lists flows in an AWS account.

## Request Syntax
<a name="API_ListFlows_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/flows?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFlows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListFlows_RequestSyntax) **   <a name="QS-ListFlows-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the flow list that you are getting.  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: Yes

 ** [MaxResults](#API_ListFlows_RequestSyntax) **   <a name="QS-ListFlows-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListFlows_RequestSyntax) **   <a name="QS-ListFlows-request-uri-NextToken"></a>
The token to request the next set of results, or null if you want to retrieve the first set.

## Request Body
<a name="API_ListFlows_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFlows_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "FlowSummaryList": [ 
      { 
         "Arn": "string",
         "CreatedBy": "string",
         "CreatedTime": number,
         "Description": "string",
         "FlowId": "string",
         "LastPublishedAt": number,
         "LastPublishedBy": "string",
         "LastUpdatedBy": "string",
         "LastUpdatedTime": number,
         "Name": "string",
         "PublishState": "string",
         "RunCount": number,
         "UserCount": number
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListFlows_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListFlows_ResponseSyntax) **   <a name="QS-ListFlows-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [FlowSummaryList](#API_ListFlows_ResponseSyntax) **   <a name="QS-ListFlows-response-FlowSummaryList"></a>
A structure that contains all of the flows in your AWS account. This structure provides basic information about the flows.  
Type: Array of [FlowSummary](API_FlowSummary.md) objects

 ** [NextToken](#API_ListFlows_ResponseSyntax) **   <a name="QS-ListFlows-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListFlows_ResponseSyntax) **   <a name="QS-ListFlows-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListFlows_Errors"></a>

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
<a name="API_ListFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListFlows) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListFlows) 