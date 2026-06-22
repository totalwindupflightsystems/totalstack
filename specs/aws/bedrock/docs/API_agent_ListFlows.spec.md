---
id: "@specs/aws/bedrock/docs/API_agent_ListFlows"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFlows"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListFlows

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_ListFlows
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFlows
<a name="API_agent_ListFlows"></a>

Returns a list of flows and information about each flow. For more information, see [Manage a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_ListFlows_RequestSyntax"></a>

```
GET /flows/?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_ListFlows_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_agent_ListFlows_RequestSyntax) **   <a name="bedrock-agent_ListFlows-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_agent_ListFlows_RequestSyntax) **   <a name="bedrock-agent_ListFlows-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_agent_ListFlows_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_ListFlows_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowSummaries": [ 
      { 
         "arn": "string",
         "createdAt": "string",
         "description": "string",
         "id": "string",
         "name": "string",
         "status": "string",
         "updatedAt": "string",
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent_ListFlows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowSummaries](#API_agent_ListFlows_ResponseSyntax) **   <a name="bedrock-agent_ListFlows-response-flowSummaries"></a>
A list, each member of which contains information about a flow.  
Type: Array of [FlowSummary](API_agent_FlowSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [nextToken](#API_agent_ListFlows_ResponseSyntax) **   <a name="bedrock-agent_ListFlows-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent_ListFlows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_ListFlows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListFlows) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListFlows) 