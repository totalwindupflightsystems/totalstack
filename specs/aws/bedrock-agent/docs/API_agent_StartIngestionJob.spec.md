---
id: "@specs/aws/bedrock-agent/docs/API_agent_StartIngestionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartIngestionJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# StartIngestionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_StartIngestionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartIngestionJob
<a name="API_agent_StartIngestionJob"></a>

Begins a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.

## Request Syntax
<a name="API_agent_StartIngestionJob_RequestSyntax"></a>

```
PUT /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/ingestionjobs/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_StartIngestionJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_StartIngestionJob_RequestSyntax) **   <a name="bedrock-agent_StartIngestionJob-request-uri-dataSourceId"></a>
The unique identifier of the data source you want to ingest into your knowledge base.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_StartIngestionJob_RequestSyntax) **   <a name="bedrock-agent_StartIngestionJob-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base for the data ingestion job.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_StartIngestionJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_StartIngestionJob_RequestSyntax) **   <a name="bedrock-agent_StartIngestionJob-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_agent_StartIngestionJob_RequestSyntax) **   <a name="bedrock-agent_StartIngestionJob-request-description"></a>
A description of the data ingestion job.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## Response Syntax
<a name="API_agent_StartIngestionJob_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_agent_StartIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [ingestionJob](#API_agent_StartIngestionJob_ResponseSyntax) **   <a name="bedrock-agent_StartIngestionJob-response-ingestionJob"></a>
Contains information about the data ingestion job.  
Type: [IngestionJob](API_agent_IngestionJob.md) object

## Errors
<a name="API_agent_StartIngestionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
There was a conflict performing an operation.  
HTTP Status Code: 409

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
<a name="API_agent_StartIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/StartIngestionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/StartIngestionJob) 