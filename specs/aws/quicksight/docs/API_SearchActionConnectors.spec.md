---
id: "@specs/aws/quicksight/docs/API_SearchActionConnectors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchActionConnectors"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchActionConnectors

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchActionConnectors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchActionConnectors
<a name="API_SearchActionConnectors"></a>

Searches for action connectors in the specified AWS account using filters. You can search by connector name, type, or user permissions.

## Request Syntax
<a name="API_SearchActionConnectors_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/search/action-connectors?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_SearchActionConnectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchActionConnectors_RequestSyntax) **   <a name="QS-SearchActionConnectors-request-uri-AwsAccountId"></a>
The AWS account ID in which to search for action connectors.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_SearchActionConnectors_RequestSyntax) **   <a name="QS-SearchActionConnectors-request-uri-MaxResults"></a>
The maximum number of action connectors to return in a single response. Valid range is 1 to 100.  
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [NextToken](#API_SearchActionConnectors_RequestSyntax) **   <a name="QS-SearchActionConnectors-request-uri-NextToken"></a>
A pagination token to retrieve the next set of results. Use the token returned from a previous call to continue searching.

## Request Body
<a name="API_SearchActionConnectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchActionConnectors_RequestSyntax) **   <a name="QS-SearchActionConnectors-request-Filters"></a>
The search filters to apply. You can filter by connector name, type, or user permissions. Maximum of one filter is supported.  
Type: Array of [ActionConnectorSearchFilter](API_ActionConnectorSearchFilter.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_SearchActionConnectors_ResponseSyntax"></a>

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
<a name="API_SearchActionConnectors_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchActionConnectors_ResponseSyntax) **   <a name="QS-SearchActionConnectors-response-Status"></a>
The HTTP status code of the request.

The following data is returned in JSON format by the service.

 ** [ActionConnectorSummaries](#API_SearchActionConnectors_ResponseSyntax) **   <a name="QS-SearchActionConnectors-response-ActionConnectorSummaries"></a>
A list of action connector summaries that match the search criteria.  
Type: Array of [ActionConnectorSummary](API_ActionConnectorSummary.md) objects

 ** [NextToken](#API_SearchActionConnectors_ResponseSyntax) **   <a name="QS-SearchActionConnectors-response-NextToken"></a>
A pagination token to retrieve the next set of results. If null, there are no more results to retrieve.  
Type: String

 ** [RequestId](#API_SearchActionConnectors_ResponseSyntax) **   <a name="QS-SearchActionConnectors-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchActionConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_SearchActionConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchActionConnectors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchActionConnectors) 