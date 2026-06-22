---
id: "@specs/aws/bedrock/docs/API_agent_PrepareAgent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PrepareAgent"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# PrepareAgent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_PrepareAgent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PrepareAgent
<a name="API_agent_PrepareAgent"></a>

Creates a `DRAFT` version of the agent that can be used for internal testing.

## Request Syntax
<a name="API_agent_PrepareAgent_RequestSyntax"></a>

```
POST /agents/{{agentId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_PrepareAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_agent_PrepareAgent_RequestSyntax) **   <a name="bedrock-agent_PrepareAgent-request-uri-agentId"></a>
The unique identifier of the agent for which to create a `DRAFT` version.  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

## Request Body
<a name="API_agent_PrepareAgent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_PrepareAgent_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "agentId": "string",
   "agentStatus": "string",
   "agentVersion": "string",
   "preparedAt": "string"
}
```

## Response Elements
<a name="API_agent_PrepareAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [agentId](#API_agent_PrepareAgent_ResponseSyntax) **   <a name="bedrock-agent_PrepareAgent-response-agentId"></a>
The unique identifier of the agent for which the `DRAFT` version was created.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [agentStatus](#API_agent_PrepareAgent_ResponseSyntax) **   <a name="bedrock-agent_PrepareAgent-response-agentStatus"></a>
The status of the `DRAFT` version and whether it is ready for use.  
Type: String  
Valid Values: `CREATING | PREPARING | PREPARED | NOT_PREPARED | DELETING | FAILED | VERSIONING | UPDATING` 

 ** [agentVersion](#API_agent_PrepareAgent_ResponseSyntax) **   <a name="bedrock-agent_PrepareAgent-response-agentVersion"></a>
The version of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})` 

 ** [preparedAt](#API_agent_PrepareAgent_ResponseSyntax) **   <a name="bedrock-agent_PrepareAgent-response-preparedAt"></a>
The time at which the `DRAFT` version of the agent was last prepared.  
Type: Timestamp

## Errors
<a name="API_agent_PrepareAgent_Errors"></a>

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

## Examples
<a name="API_agent_PrepareAgent_Examples"></a>

### Example request
<a name="API_agent_PrepareAgent_Example_1"></a>

This example illustrates one usage of PrepareAgent.

```
POST /agents/ABCDEFGHIJ/ HTTP/1.1
```

## See Also
<a name="API_agent_PrepareAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/PrepareAgent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PrepareAgent) 