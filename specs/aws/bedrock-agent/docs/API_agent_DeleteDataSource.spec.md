---
id: "@specs/aws/bedrock-agent/docs/API_agent_DeleteDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDataSource"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_DeleteDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDataSource
<a name="API_agent_DeleteDataSource"></a>

Deletes a data source from a knowledge base.

## Request Syntax
<a name="API_agent_DeleteDataSource_RequestSyntax"></a>

```
DELETE /knowledgebases/{{knowledgeBaseId}}/datasources/{{dataSourceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeleteDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dataSourceId](#API_agent_DeleteDataSource_RequestSyntax) **   <a name="bedrock-agent_DeleteDataSource-request-uri-dataSourceId"></a>
The unique identifier of the data source to delete.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [knowledgeBaseId](#API_agent_DeleteDataSource_RequestSyntax) **   <a name="bedrock-agent_DeleteDataSource-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base from which to delete the data source.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_DeleteDataSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeleteDataSource_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "dataSourceId": "string",
   "knowledgeBaseId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_agent_DeleteDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [dataSourceId](#API_agent_DeleteDataSource_ResponseSyntax) **   <a name="bedrock-agent_DeleteDataSource-response-dataSourceId"></a>
The unique identifier of the data source that was deleted.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [knowledgeBaseId](#API_agent_DeleteDataSource_ResponseSyntax) **   <a name="bedrock-agent_DeleteDataSource-response-knowledgeBaseId"></a>
The unique identifier of the knowledge base to which the data source that was deleted belonged.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [status](#API_agent_DeleteDataSource_ResponseSyntax) **   <a name="bedrock-agent_DeleteDataSource-response-status"></a>
The status of the data source.  
Type: String  
Valid Values: `AVAILABLE | DELETING | DELETE_UNSUCCESSFUL | CREATING | UPDATING | FAILED` 

## Errors
<a name="API_agent_DeleteDataSource_Errors"></a>

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
<a name="API_agent_DeleteDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteDataSource) 