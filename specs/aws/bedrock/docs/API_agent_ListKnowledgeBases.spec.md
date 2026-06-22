---
id: "@specs/aws/bedrock/docs/API_agent_ListKnowledgeBases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListKnowledgeBases"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListKnowledgeBases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_ListKnowledgeBases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListKnowledgeBases
<a name="API_agent_ListKnowledgeBases"></a>

Lists the knowledge bases in an account. The list also includesinformation about each knowledge base.

## Request Syntax
<a name="API_agent_ListKnowledgeBases_RequestSyntax"></a>

```
POST /knowledgebases/ HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_ListKnowledgeBases_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent_ListKnowledgeBases_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_agent_ListKnowledgeBases_RequestSyntax) **   <a name="bedrock-agent_ListKnowledgeBases-request-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_agent_ListKnowledgeBases_RequestSyntax) **   <a name="bedrock-agent_ListKnowledgeBases-request-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

## Response Syntax
<a name="API_agent_ListKnowledgeBases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "knowledgeBaseSummaries": [ 
      { 
         "description": "string",
         "knowledgeBaseId": "string",
         "name": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent_ListKnowledgeBases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBaseSummaries](#API_agent_ListKnowledgeBases_ResponseSyntax) **   <a name="bedrock-agent_ListKnowledgeBases-response-knowledgeBaseSummaries"></a>
A list of knowledge bases with information about each knowledge base.  
Type: Array of [KnowledgeBaseSummary](API_agent_KnowledgeBaseSummary.md) objects

 ** [nextToken](#API_agent_ListKnowledgeBases_ResponseSyntax) **   <a name="bedrock-agent_ListKnowledgeBases-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent_ListKnowledgeBases_Errors"></a>

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
<a name="API_agent_ListKnowledgeBases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListKnowledgeBases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListKnowledgeBases) 