---
id: "@specs/aws/bedrock-agent/docs/API_agent_ListKnowledgeBaseDocuments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListKnowledgeBaseDocuments"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListKnowledgeBaseDocuments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_ListKnowledgeBaseDocuments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListKnowledgeBaseDocuments
<a name="API_agent_ListKnowledgeBaseDocuments"></a>

Retrieves all the documents contained in a data source that is connected to a knowledge base. For more information, see [Ingest changes directly into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_ListKnowledgeBaseDocuments_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/documents HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_ListKnowledgeBaseDocuments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_ListKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_ListKnowledgeBaseDocuments-request-uri-dataSourceId"></a>
The unique identifier of the data source that contains the documents.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_ListKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_ListKnowledgeBaseDocuments-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that is connected to the data source.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_ListKnowledgeBaseDocuments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_agent_ListKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_ListKnowledgeBaseDocuments-request-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_agent_ListKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_ListKnowledgeBaseDocuments-request-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

## Response Syntax
<a name="API_agent_ListKnowledgeBaseDocuments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "documentDetails": [ 
      { 
         "dataSourceId": "string",
         "identifier": { 
            "custom": { 
               "id": "string"
            },
            "dataSourceType": "string",
            "s3": { 
               "uri": "string"
            }
         },
         "knowledgeBaseId": "string",
         "status": "string",
         "statusReason": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent_ListKnowledgeBaseDocuments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentDetails](#API_agent_ListKnowledgeBaseDocuments_ResponseSyntax) **   <a name="bedrock-agent_ListKnowledgeBaseDocuments-response-documentDetails"></a>
A list of objects, each of which contains information about the documents that were retrieved.  
Type: Array of [KnowledgeBaseDocumentDetail](API_agent_KnowledgeBaseDocumentDetail.md) objects

 ** [nextToken](#API_agent_ListKnowledgeBaseDocuments_ResponseSyntax) **   <a name="bedrock-agent_ListKnowledgeBaseDocuments-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String

## Errors
<a name="API_agent_ListKnowledgeBaseDocuments_Errors"></a>

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

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 402

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_ListKnowledgeBaseDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListKnowledgeBaseDocuments) 