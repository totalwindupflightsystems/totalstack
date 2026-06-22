---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetKnowledgeBaseDocuments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetKnowledgeBaseDocuments"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetKnowledgeBaseDocuments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetKnowledgeBaseDocuments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetKnowledgeBaseDocuments
<a name="API_agent_GetKnowledgeBaseDocuments"></a>

Retrieves specific documents from a data source that is connected to a knowledge base. For more information, see [Ingest changes directly into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_GetKnowledgeBaseDocuments_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/documents/getDocuments HTTP/1.1
Content-type: application/json

{
   "documentIdentifiers": [ 
      { 
         "custom": { 
            "id": "{{string}}"
         },
         "dataSourceType": "{{string}}",
         "s3": { 
            "uri": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_agent_GetKnowledgeBaseDocuments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_GetKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_GetKnowledgeBaseDocuments-request-uri-dataSourceId"></a>
The unique identifier of the data source that contains the documents.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_GetKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_GetKnowledgeBaseDocuments-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that is connected to the data source.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_GetKnowledgeBaseDocuments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [documentIdentifiers](#API_agent_GetKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_GetKnowledgeBaseDocuments-request-documentIdentifiers"></a>
A list of objects, each of which contains information to identify a document for which to retrieve information.  
Type: Array of [DocumentIdentifier](API_agent_DocumentIdentifier.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

## Response Syntax
<a name="API_agent_GetKnowledgeBaseDocuments_ResponseSyntax"></a>

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
   ]
}
```

## Response Elements
<a name="API_agent_GetKnowledgeBaseDocuments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentDetails](#API_agent_GetKnowledgeBaseDocuments_ResponseSyntax) **   <a name="bedrock-agent_GetKnowledgeBaseDocuments-response-documentDetails"></a>
A list of objects, each of which contains information about the documents that were retrieved.  
Type: Array of [KnowledgeBaseDocumentDetail](API_agent_KnowledgeBaseDocumentDetail.md) objects

## Errors
<a name="API_agent_GetKnowledgeBaseDocuments_Errors"></a>

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
<a name="API_agent_GetKnowledgeBaseDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetKnowledgeBaseDocuments) 