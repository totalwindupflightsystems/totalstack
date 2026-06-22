---
id: "@specs/aws/bedrock/docs/API_agent_StopIngestionJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StopIngestionJob"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# StopIngestionJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_StopIngestionJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StopIngestionJob
<a name="API_agent_StopIngestionJob"></a>

Stops a currently running data ingestion job. You can send a `StartIngestionJob` request again to ingest the rest of your data when you are ready.

## Request Syntax
<a name="API_agent_StopIngestionJob_RequestSyntax"></a>

```
POST /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}}/ingestionjobs/{{ingestionJobId}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_StopIngestionJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_StopIngestionJob_RequestSyntax) **   <a name="bedrock-agent_StopIngestionJob-request-uri-dataSourceId"></a>
The unique identifier of the data source for the data ingestion job you want to stop.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [ingestionJobId](#API_agent_StopIngestionJob_RequestSyntax) **   <a name="bedrock-agent_StopIngestionJob-request-uri-ingestionJobId"></a>
The unique identifier of the data ingestion job you want to stop.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_StopIngestionJob_RequestSyntax) **   <a name="bedrock-agent_StopIngestionJob-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base for the data ingestion job you want to stop.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_StopIngestionJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_StopIngestionJob_ResponseSyntax"></a>

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
<a name="API_agent_StopIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [ingestionJob](#API_agent_StopIngestionJob_ResponseSyntax) **   <a name="bedrock-agent_StopIngestionJob-response-ingestionJob"></a>
Contains information about the stopped data ingestion job.  
Type: [IngestionJob](API_agent_IngestionJob.md) object

## Errors
<a name="API_agent_StopIngestionJob_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_StopIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/StopIngestionJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/StopIngestionJob) 