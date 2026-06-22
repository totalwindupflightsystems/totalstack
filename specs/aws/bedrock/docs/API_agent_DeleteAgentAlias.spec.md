---
id: "@specs/aws/bedrock/docs/API_agent_DeleteAgentAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAgentAlias"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeleteAgentAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_DeleteAgentAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAgentAlias
<a name="API_agent_DeleteAgentAlias"></a>

Deletes an alias of an agent.

## Request Syntax
<a name="API_agent_DeleteAgentAlias_RequestSyntax"></a>

```
DELETE /agents/{{agentId}}/agentaliases/{{agentAliasId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeleteAgentAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentAliasId](#API_agent_DeleteAgentAlias_RequestSyntax) **   <a name="bedrock-agent_DeleteAgentAlias-request-uri-agentAliasId"></a>
The unique identifier of the alias to delete.  
Length Constraints: Fixed length of 10.  
Pattern: `(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [agentId](#API_agent_DeleteAgentAlias_RequestSyntax) **   <a name="bedrock-agent_DeleteAgentAlias-request-uri-agentId"></a>
The unique identifier of the agent that the alias belongs to.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_DeleteAgentAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeleteAgentAlias_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "agentAliasId": "string",
   "agentAliasStatus": "string",
   "agentId": "string"
}
```

## Response Elements
<a name="API_agent_DeleteAgentAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agentAliasId](#API_agent_DeleteAgentAlias_ResponseSyntax) **   <a name="bedrock-agent_DeleteAgentAlias-response-agentAliasId"></a>
The unique identifier of the alias that was deleted.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `(\bTSTALIASID\b|[0-9a-zA-Z]+)` 

 ** [agentAliasStatus](#API_agent_DeleteAgentAlias_ResponseSyntax) **   <a name="bedrock-agent_DeleteAgentAlias-response-agentAliasStatus"></a>
The status of the alias.  
Type: String  
Valid Values: `CREATING | PREPARED | FAILED | UPDATING | DELETING | DISSOCIATED` 

 ** [agentId](#API_agent_DeleteAgentAlias_ResponseSyntax) **   <a name="bedrock-agent_DeleteAgentAlias-response-agentId"></a>
The unique identifier of the agent that the alias belongs to.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

## Errors
<a name="API_agent_DeleteAgentAlias_Errors"></a>

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

## Examples
<a name="API_agent_DeleteAgentAlias_Examples"></a>

### Example request
<a name="API_agent_DeleteAgentAlias_Example_1"></a>

This example illustrates one usage of DeleteAgentAlias.

```
DELETE /agents/ABCDEFGHIJ/agentaliases/ABCDEFGHIJ/ HTTP/1.1
```

## See Also
<a name="API_agent_DeleteAgentAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteAgentAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteAgentAlias) 