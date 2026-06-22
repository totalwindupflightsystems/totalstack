---
id: "@specs/aws/bedrock/docs/API_agent_ListFlowVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFlowVersions"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListFlowVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_ListFlowVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFlowVersions
<a name="API_agent_ListFlowVersions"></a>

Returns a list of information about each flow. For more information, see [Deploy a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_ListFlowVersions_RequestSyntax"></a>

```
GET /flows/{{flowIdentifier}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_ListFlowVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowIdentifier](#API_agent_ListFlowVersions_RequestSyntax) **   <a name="bedrock-agent_ListFlowVersions-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

 ** [maxResults](#API_agent_ListFlowVersions_RequestSyntax) **   <a name="bedrock-agent_ListFlowVersions-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_agent_ListFlowVersions_RequestSyntax) **   <a name="bedrock-agent_ListFlowVersions-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_agent_ListFlowVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_ListFlowVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowVersionSummaries": [ 
      { 
         "arn": "string",
         "createdAt": "string",
         "id": "string",
         "status": "string",
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent_ListFlowVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowVersionSummaries](#API_agent_ListFlowVersions_ResponseSyntax) **   <a name="bedrock-agent_ListFlowVersions-response-flowVersionSummaries"></a>
A list, each member of which contains information about a flow.  
Type: Array of [FlowVersionSummary](API_agent_FlowVersionSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [nextToken](#API_agent_ListFlowVersions_ResponseSyntax) **   <a name="bedrock-agent_ListFlowVersions-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent_ListFlowVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_ListFlowVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListFlowVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListFlowVersions) 