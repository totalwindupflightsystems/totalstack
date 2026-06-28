---
id: "@specs/aws/quicksight/docs/API_ListAnalyses"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAnalyses"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListAnalyses

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListAnalyses
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAnalyses
<a name="API_ListAnalyses"></a>

Lists Amazon Quick Sight analyses that exist in the specified AWS account.

## Request Syntax
<a name="API_ListAnalyses_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/analyses?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAnalyses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListAnalyses_RequestSyntax) **   <a name="QS-ListAnalyses-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the analyses.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListAnalyses_RequestSyntax) **   <a name="QS-ListAnalyses-request-uri-MaxResults"></a>
The maximum number of results to return.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAnalyses_RequestSyntax) **   <a name="QS-ListAnalyses-request-uri-NextToken"></a>
A pagination token that can be used in a subsequent request.

## Request Body
<a name="API_ListAnalyses_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAnalyses_ResponseSyntax"></a>

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
<a name="API_ListAnalyses_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListAnalyses_ResponseSyntax) **   <a name="QS-ListAnalyses-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisSummaryList](#API_ListAnalyses_ResponseSyntax) **   <a name="QS-ListAnalyses-response-AnalysisSummaryList"></a>
Metadata describing each of the analyses that are listed.  
Type: Array of [AnalysisSummary](API_AnalysisSummary.md) objects  
Array Members: Maximum number of 100 items.

 ** [NextToken](#API_ListAnalyses_ResponseSyntax) **   <a name="QS-ListAnalyses-response-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String

 ** [RequestId](#API_ListAnalyses_ResponseSyntax) **   <a name="QS-ListAnalyses-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListAnalyses_Errors"></a>

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
<a name="API_ListAnalyses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListAnalyses) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListAnalyses) 