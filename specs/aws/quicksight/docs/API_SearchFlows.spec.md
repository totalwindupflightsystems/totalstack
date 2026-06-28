---
id: "@specs/aws/quicksight/docs/API_SearchFlows"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchFlows"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchFlows

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchFlows
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchFlows
<a name="API_SearchFlows"></a>

Search for the flows in an AWS account.

## Request Syntax
<a name="API_SearchFlows_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/flows/searchFlows HTTP/1.1
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
<a name="API_SearchFlows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchFlows_RequestSyntax) **   <a name="QS-SearchFlows-request-uri-AwsAccountId"></a>
The ID of the AWS account where you are searching for flows from.  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: Yes

## Request Body
<a name="API_SearchFlows_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchFlows_RequestSyntax) **   <a name="QS-SearchFlows-request-Filters"></a>
The filters applied to the search when searching for flows in the AWS account.  
Type: Array of [SearchFlowsFilter](API_SearchFlowsFilter.md) objects  
Required: Yes

 ** [MaxResults](#API_SearchFlows_RequestSyntax) **   <a name="QS-SearchFlows-request-MaxResults"></a>
The maximum number of results to be returned per request.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_SearchFlows_RequestSyntax) **   <a name="QS-SearchFlows-request-NextToken"></a>
The token to request the next set of results, or null if you want to retrieve the first set.  
Type: String  
Required: No

## Response Syntax
<a name="API_SearchFlows_ResponseSyntax"></a>

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
<a name="API_SearchFlows_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchFlows_ResponseSyntax) **   <a name="QS-SearchFlows-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [FlowSummaryList](#API_SearchFlows_ResponseSyntax) **   <a name="QS-SearchFlows-response-FlowSummaryList"></a>
The list of flows found against the search.  
Type: Array of [FlowSummary](API_FlowSummary.md) objects

 ** [NextToken](#API_SearchFlows_ResponseSyntax) **   <a name="QS-SearchFlows-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_SearchFlows_ResponseSyntax) **   <a name="QS-SearchFlows-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchFlows_Errors"></a>

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
<a name="API_SearchFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchFlows) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchFlows) 