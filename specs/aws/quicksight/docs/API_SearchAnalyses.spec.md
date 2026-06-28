---
id: "@specs/aws/quicksight/docs/API_SearchAnalyses"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchAnalyses"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchAnalyses

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchAnalyses
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchAnalyses
<a name="API_SearchAnalyses"></a>

Searches for analyses that belong to the user specified in the filter.

**Note**  
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

## Request Syntax
<a name="API_SearchAnalyses_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/analyses HTTP/1.1
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
<a name="API_SearchAnalyses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchAnalyses_RequestSyntax) **   <a name="QS-SearchAnalyses-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the analyses that you're searching for.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_SearchAnalyses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchAnalyses_RequestSyntax) **   <a name="QS-SearchAnalyses-request-Filters"></a>
The structure for the search filters that you want to apply to your search.   
Type: Array of [AnalysisSearchFilter](API_AnalysisSearchFilter.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [MaxResults](#API_SearchAnalyses_RequestSyntax) **   <a name="QS-SearchAnalyses-request-MaxResults"></a>
The maximum number of results to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_SearchAnalyses_RequestSyntax) **   <a name="QS-SearchAnalyses-request-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String  
Required: No

## Response Syntax
<a name="API_SearchAnalyses_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AnalysisSummaryList": [ 
      { 
         "AnalysisId": "string",
         "Arn": "string",
         "CreatedTime": number,
         "LastUpdatedTime": number,
         "Name": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_SearchAnalyses_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchAnalyses_ResponseSyntax) **   <a name="QS-SearchAnalyses-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisSummaryList](#API_SearchAnalyses_ResponseSyntax) **   <a name="QS-SearchAnalyses-response-AnalysisSummaryList"></a>
Metadata describing the analyses that you searched for.  
Type: Array of [AnalysisSummary](API_AnalysisSummary.md) objects  
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_SearchAnalyses_ResponseSyntax) **   <a name="QS-SearchAnalyses-response-NextToken"></a>
A pagination token that can be used in a subsequent request.   
Type: String

 ** [RequestId](#API_SearchAnalyses_ResponseSyntax) **   <a name="QS-SearchAnalyses-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchAnalyses_Errors"></a>

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
<a name="API_SearchAnalyses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchAnalyses) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchAnalyses) 