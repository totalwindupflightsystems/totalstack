---
id: "@specs/aws/quicksight/docs/API_ListActionConnectors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListActionConnectors"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListActionConnectors

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListActionConnectors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListActionConnectors
<a name="API_ListActionConnectors"></a>

Lists all action connectors in the specified AWS account. Returns summary information for each connector including its name, type, creation time, and status.

## Request Syntax
<a name="API_ListActionConnectors_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/action-connectors?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListActionConnectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListActionConnectors_RequestSyntax) **   <a name="QS-ListActionConnectors-request-uri-AwsAccountId"></a>
The AWS account ID for which to list action connectors.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListActionConnectors_RequestSyntax) **   <a name="QS-ListActionConnectors-request-uri-MaxResults"></a>
The maximum number of action connectors to return in a single response. Valid range is 1 to 100.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListActionConnectors_RequestSyntax) **   <a name="QS-ListActionConnectors-request-uri-NextToken"></a>
A pagination token to retrieve the next set of results. Use the token returned from a previous call to continue listing action connectors.

## Request Body
<a name="API_ListActionConnectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListActionConnectors_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "ActionConnectorSummaries": [ 
      { 
         "ActionConnectorId": "string",
         "Arn": "string",
         "CreatedTime": number,
         "Error": { 
            "Message": "string",
            "Type": "string"
         },
         "LastUpdatedTime": number,
         "Name": "string",
         "Status": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListActionConnectors_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListActionConnectors_ResponseSyntax) **   <a name="QS-ListActionConnectors-response-Status"></a>
The HTTP status code of the request.

The following data is returned in JSON format by the service.

 ** [ActionConnectorSummaries](#API_ListActionConnectors_ResponseSyntax) **   <a name="QS-ListActionConnectors-response-ActionConnectorSummaries"></a>
A list of action connector summaries containing basic information about each connector.  
Type: Array of [ActionConnectorSummary](API_ActionConnectorSummary.md) objects

 ** [NextToken](#API_ListActionConnectors_ResponseSyntax) **   <a name="QS-ListActionConnectors-response-NextToken"></a>
A pagination token to retrieve the next set of results. If null, there are no more results to retrieve.  
Type: String

 ** [RequestId](#API_ListActionConnectors_ResponseSyntax) **   <a name="QS-ListActionConnectors-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListActionConnectors_Errors"></a>

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

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListActionConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListActionConnectors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListActionConnectors) 