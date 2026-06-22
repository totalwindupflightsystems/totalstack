---
id: "@specs/aws/bedrock/docs/API_agent-runtime_GetDocumentContent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDocumentContent"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetDocumentContent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent-runtime_GetDocumentContent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDocumentContent
<a name="API_agent-runtime_GetDocumentContent"></a>

Retrieves the content of an ingested document from a knowledge base. Returns a pre-signed URL for secure document access.

## Request Syntax
<a name="API_agent-runtime_GetDocumentContent_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/documents/{{documentId}}/content HTTP/1.1
Content-type: application/json

{
   "outputFormat": "{{string}}",
   "userContext": { 
      "userId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_GetDocumentContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent-runtime_GetDocumentContent_RequestSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-request-uri-dataSourceId"></a>
The unique identifier of the data source that contains the document.  
Length Constraints: Minimum length of 0. Maximum length of 10.  
Pattern: `[0-9a-zA-Z]+`   
Required: Yes

 ** [documentId](#API_agent-runtime_GetDocumentContent_RequestSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-request-uri-documentId"></a>
The unique identifier of the document to retrieve content for.  
Length Constraints: Minimum length of 1. Maximum length of 1825.  
Pattern: `\P{C}*`   
Required: Yes

 ** [knowledgeBaseId](#API_agent-runtime_GetDocumentContent_RequestSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base that contains the document.  
Length Constraints: Minimum length of 10. Maximum length of 2048.  
Pattern: `[0-9a-zA-Z]{10}$|^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:knowledge-base/[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent-runtime_GetDocumentContent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [outputFormat](#API_agent-runtime_GetDocumentContent_RequestSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-request-outputFormat"></a>
The output format for the document content. `RAW` returns the original file. `EXTRACTED` returns parsed text as JSON. Defaults to `RAW`.  
Type: String  
Valid Values: `RAW | EXTRACTED`   
Required: No

 ** [userContext](#API_agent-runtime_GetDocumentContent_RequestSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-request-userContext"></a>
Contains information about the user making the request. This is used for access control filtering to ensure that results only include documents the user is authorized to access.  
Type: [UserContext](API_agent-runtime_UserContext.md) object  
Required: No

## Response Syntax
<a name="API_agent-runtime_GetDocumentContent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "documentContentLength": number,
   "mimeType": "string",
   "presignedUrl": "string"
}
```

## Response Elements
<a name="API_agent-runtime_GetDocumentContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentContentLength](#API_agent-runtime_GetDocumentContent_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-response-documentContentLength"></a>
The size of the document content in bytes available at the pre-signed URL.  
Type: Long

 ** [mimeType](#API_agent-runtime_GetDocumentContent_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-response-mimeType"></a>
The MIME type of the document content. For `RAW` format, this is the original file type (for example, `application/pdf`). For `EXTRACTED` format, this is always `application/json`.  
Type: String

 ** [presignedUrl](#API_agent-runtime_GetDocumentContent_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetDocumentContent-response-presignedUrl"></a>
A pre-signed URL for downloading the document content. The URL expires after 5 minutes.  
Type: String

## Errors
<a name="API_agent-runtime_GetDocumentContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_GetDocumentContent_Examples"></a>

### Retrieve the original document content
<a name="API_agent-runtime_GetDocumentContent_Example_1"></a>

The following example retrieves the original (raw) content of a document from a knowledge base. The response includes a pre-signed URL that you can use to download the document.

#### Sample Request
<a name="API_agent-runtime_GetDocumentContent_Example_1_Request"></a>

```
POST /knowledgebases/KB12345678/datasources/DS12345678/documents/DOC12345678/content HTTP/1.1
Content-type: application/json

{
    "outputFormat": "RAW"
}
```

## See Also
<a name="API_agent-runtime_GetDocumentContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GetDocumentContent) 