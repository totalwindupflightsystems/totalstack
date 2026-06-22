---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_CreateInvocation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateInvocation"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateInvocation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_CreateInvocation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateInvocation
<a name="API_agent-runtime_CreateInvocation"></a>

Creates a new invocation within a session. An invocation groups the related invocation steps that store the content from a conversation. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

Related APIs
+  [ListInvocations](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html) 
+  [ListSessions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html) 
+  [GetSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html) 

## Request Syntax
<a name="API_agent-runtime_CreateInvocation_RequestSyntax"></a>

```
PUT /sessions/{{sessionIdentifier}}/invocations/ HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "invocationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent-runtime_CreateInvocation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sessionIdentifier](#API_agent-runtime_CreateInvocation_RequestSyntax) **   <a name="bedrock-agent-runtime_CreateInvocation-request-uri-sessionIdentifier"></a>
The unique identifier for the associated session for the invocation. You can specify either the session's `sessionId` or its Amazon Resource Name (ARN).   
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_CreateInvocation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_agent-runtime_CreateInvocation_RequestSyntax) **   <a name="bedrock-agent-runtime_CreateInvocation-request-description"></a>
A description for the interactions in the invocation. For example, "User asking about weather in Seattle".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [invocationId](#API_agent-runtime_CreateInvocation_RequestSyntax) **   <a name="bedrock-agent-runtime_CreateInvocation-request-invocationId"></a>
A unique identifier for the invocation in UUID format.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: No

## Response Syntax
<a name="API_agent-runtime_CreateInvocation_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": "string",
   "invocationId": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_agent-runtime_CreateInvocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_agent-runtime_CreateInvocation_ResponseSyntax) **   <a name="bedrock-agent-runtime_CreateInvocation-response-createdAt"></a>
The timestamp for when the invocation was created.  
Type: Timestamp

 ** [invocationId](#API_agent-runtime_CreateInvocation_ResponseSyntax) **   <a name="bedrock-agent-runtime_CreateInvocation-response-invocationId"></a>
The unique identifier for the invocation.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [sessionId](#API_agent-runtime_CreateInvocation_ResponseSyntax) **   <a name="bedrock-agent-runtime_CreateInvocation-response-sessionId"></a>
The unique identifier for the session associated with the invocation.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

## Errors
<a name="API_agent-runtime_CreateInvocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_CreateInvocation_Examples"></a>

### Request example
<a name="API_agent-runtime_CreateInvocation_Example_1"></a>

This example illustrates one usage of CreateInvocation.

```
PUT bedrock-agent-runtime.us-east-1.amazonaws.com/sessions/12345abc-1234-abcd-1234-abcdef123456/invocations/ HTTP/1.1
Content-type: application/json

{
    "description": "User asking about weather in Seattle",
    "invocationId": "12345abc-1234-abcd-1234-abcdef123456"
}
```

## See Also
<a name="API_agent-runtime_CreateInvocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/CreateInvocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/CreateInvocation) 