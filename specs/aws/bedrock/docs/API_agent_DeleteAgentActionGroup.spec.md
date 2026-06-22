---
id: "@specs/aws/bedrock/docs/API_agent_DeleteAgentActionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAgentActionGroup"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeleteAgentActionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_DeleteAgentActionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAgentActionGroup
<a name="API_agent_DeleteAgentActionGroup"></a>

Deletes an action group in an agent.

## Request Syntax
<a name="API_agent_DeleteAgentActionGroup_RequestSyntax"></a>

```
DELETE /agents/{{agentId}}/agentversions/{{agentVersion}}/actiongroups/{{actionGroupId}}/?skipResourceInUseCheck={{skipResourceInUseCheck}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeleteAgentActionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionGroupId](#API_agent_DeleteAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_DeleteAgentActionGroup-request-uri-actionGroupId"></a>
The unique identifier of the action group to delete.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentId](#API_agent_DeleteAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_DeleteAgentActionGroup-request-uri-agentId"></a>
The unique identifier of the agent that the action group belongs to.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** [agentVersion](#API_agent_DeleteAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_DeleteAgentActionGroup-request-uri-agentVersion"></a>
The version of the agent that the action group belongs to.  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT`   
Required: Yes

 ** [skipResourceInUseCheck](#API_agent_DeleteAgentActionGroup_RequestSyntax) **   <a name="bedrock-agent_DeleteAgentActionGroup-request-uri-skipResourceInUseCheck"></a>
By default, this value is `false` and deletion is stopped if the resource is in use. If you set it to `true`, the resource will be deleted even if the resource is in use.

## Request Body
<a name="API_agent_DeleteAgentActionGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeleteAgentActionGroup_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_agent_DeleteAgentActionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_agent_DeleteAgentActionGroup_Errors"></a>

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

## Examples
<a name="API_agent_DeleteAgentActionGroup_Examples"></a>

### Example request
<a name="API_agent_DeleteAgentActionGroup_Example_1"></a>

This example illustrates one usage of DeleteAgentActionGroup.

```
DELETE /agents/ABCDEFGHIJ/agentversions/1/actiongroups/ABCDEFGHIJ/ HTTP/1.1
```

## See Also
<a name="API_agent_DeleteAgentActionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteAgentActionGroup) 