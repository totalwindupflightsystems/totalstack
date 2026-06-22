---
id: "@specs/aws/bedrock-agent/docs/API_agent_DeleteKnowledgeBaseDocuments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteKnowledgeBaseDocuments"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteKnowledgeBaseDocuments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_DeleteKnowledgeBaseDocuments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteKnowledgeBaseDocuments
<a name="API_agent_DeleteKnowledgeBaseDocuments"></a>

Deletes documents from a data source and syncs the changes to the knowledge base that is connected to it. For more information, see [Ingest changes directly into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_DeleteKnowledgeBaseDocuments_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/documents/deleteDocuments HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
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
<a name="API_agent_DeleteKnowledgeBaseDocuments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_DeleteKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBaseDocuments-request-uri-dataSourceId"></a>
The unique identifier of the data source that contains the documents.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_DeleteKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBaseDocuments-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that is connected to the data source.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_DeleteKnowledgeBaseDocuments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_DeleteKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBaseDocuments-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [documentIdentifiers](#API_agent_DeleteKnowledgeBaseDocuments_RequestSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBaseDocuments-request-documentIdentifiers"></a>
A list of objects, each of which contains information to identify a document to delete.  
Type: Array of [DocumentIdentifier](API_agent_DocumentIdentifier.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

## Response Syntax
<a name="API_agent_DeleteKnowledgeBaseDocuments_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_agent_DeleteKnowledgeBaseDocuments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [documentDetails](#API_agent_DeleteKnowledgeBaseDocuments_ResponseSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBaseDocuments-response-documentDetails"></a>
A list of objects, each of which contains information about the documents that were deleted.  
Type: Array of [KnowledgeBaseDocumentDetail](API_agent_KnowledgeBaseDocumentDetail.md) objects

## Errors
<a name="API_agent_DeleteKnowledgeBaseDocuments_Errors"></a>

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
<a name="API_agent_DeleteKnowledgeBaseDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteKnowledgeBaseDocuments) 