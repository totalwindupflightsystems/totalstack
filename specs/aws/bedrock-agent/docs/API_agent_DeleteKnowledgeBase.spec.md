---
id: "@specs/aws/bedrock-agent/docs/API_agent_DeleteKnowledgeBase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteKnowledgeBase"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteKnowledgeBase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_DeleteKnowledgeBase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteKnowledgeBase
<a name="API_agent_DeleteKnowledgeBase"></a>

Deletes a knowledge base. Before deleting a knowledge base, you should disassociate the knowledge base from any agents that it is associated with by making a [DisassociateAgentKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DisassociateAgentKnowledgeBase.html) request.

## Request Syntax
<a name="API_agent_DeleteKnowledgeBase_RequestSyntax"></a>

```
DELETE /knowledgebases/{{knowledgeBaseId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeleteKnowledgeBase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_agent_DeleteKnowledgeBase_RequestSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBase-request-uri-knowledgeBaseId"></a>
The unique identifier of the knowledge base to delete.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_DeleteKnowledgeBase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeleteKnowledgeBase_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "knowledgeBaseId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_agent_DeleteKnowledgeBase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [knowledgeBaseId](#API_agent_DeleteKnowledgeBase_ResponseSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBase-response-knowledgeBaseId"></a>
The unique identifier of the knowledge base that was deleted.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [status](#API_agent_DeleteKnowledgeBase_ResponseSyntax) **   <a name="bedrock-agent_DeleteKnowledgeBase-response-status"></a>
The status of the knowledge base and whether it has been successfully deleted.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | FAILED | DELETE_UNSUCCESSFUL | UPDATE_UNSUCCESSFUL` 

## Errors
<a name="API_agent_DeleteKnowledgeBase_Errors"></a>

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
<a name="API_agent_DeleteKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteKnowledgeBase) 