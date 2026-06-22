---
id: "@specs/aws/bedrock/docs/API_agent_GetIngestionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetIngestionJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetIngestionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_GetIngestionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetIngestionJob
<a name="API_agent_GetIngestionJob"></a>

Gets information about a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.

## Request Syntax
<a name="API_agent_GetIngestionJob_RequestSyntax"></a>

```
GET /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/ingestionjobs/{{ingestionJobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetIngestionJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_GetIngestionJob_RequestSyntax) **   <a name="bedrock-agent_GetIngestionJob-request-uri-dataSourceId"></a>
The unique identifier of the data source for the data ingestion job you want to get information on.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [ingestionJobId](#API_agent_GetIngestionJob_RequestSyntax) **   <a name="bedrock-agent_GetIngestionJob-request-uri-ingestionJobId"></a>
The unique identifier of the data ingestion job you want to get information on.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_GetIngestionJob_RequestSyntax) **   <a name="bedrock-agent_GetIngestionJob-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base for the data ingestion job you want to get information on.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_GetIngestionJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetIngestionJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ingestionJob": { 
      "dataSourceId": "string",
      "description": "string",
      "failureReasons": [ "string" ],
      "ingestionJobId": "string",
      "knowledgeBaseId": "string",
      "startedAt": "string",
      "statistics": { 
         "numberOfDocumentsDeleted": number,
         "numberOfDocumentsFailed": number,
         "numberOfDocumentsScanned": number,
         "numberOfDocumentsSkipped": number,
         "numberOfMetadataDocumentsModified": number,
         "numberOfMetadataDocumentsScanned": number,
         "numberOfModifiedDocumentsIndexed": number,
         "numberOfNewDocumentsIndexed": number
      },
      "status": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_agent_GetIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestionJob](#API_agent_GetIngestionJob_ResponseSyntax) **   <a name="bedrock-agent_GetIngestionJob-response-ingestionJob"></a>
Contains details about the data ingestion job.  
Type: [IngestionJob](API_agent_IngestionJob.md) object

## Errors
<a name="API_agent_GetIngestionJob_Errors"></a>

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
<a name="API_agent_GetIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetIngestionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetIngestionJob) 