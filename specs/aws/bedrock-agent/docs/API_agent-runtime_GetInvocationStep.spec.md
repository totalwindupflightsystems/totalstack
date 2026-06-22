---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_GetInvocationStep"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetInvocationStep"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetInvocationStep

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_GetInvocationStep
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetInvocationStep
<a name="API_agent-runtime_GetInvocationStep"></a>

Retrieves the details of a specific invocation step within an invocation in a session. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

## Request Syntax
<a name="API_agent-runtime_GetInvocationStep_RequestSyntax"></a>

```
POST /sessions/{{sessionIdentifier}}/invocationSteps/{{invocationStepId}} HTTP/1.1
Content-type: application/json

{
   "invocationIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent-runtime_GetInvocationStep_RequestParameters"></a>

The request uses the following URI parameters.

 ** [invocationStepId](#API_agent-runtime_GetInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_GetInvocationStep-request-uri-invocationStepId"></a>
The unique identifier (in UUID format) for the specific invocation step to retrieve.  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

 ** [sessionIdentifier](#API_agent-runtime_GetInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_GetInvocationStep-request-uri-sessionIdentifier"></a>
The unique identifier for the invocation step's associated session. You can specify either the session's `sessionId` or its Amazon Resource Name (ARN).  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_GetInvocationStep_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [invocationIdentifier](#API_agent-runtime_GetInvocationStep_RequestSyntax) **   <a name="bedrock-agent-runtime_GetInvocationStep-request-invocationIdentifier"></a>
The unique identifier for the invocation in UUID format.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

## Response Syntax
<a name="API_agent-runtime_GetInvocationStep_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "invocationStep": { 
      "invocationId": "string",
      "invocationStepId": "string",
      "invocationStepTime": "string",
      "payload": { ... },
      "sessionId": "string"
   }
}
```

## Response Elements
<a name="API_agent-runtime_GetInvocationStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invocationStep](#API_agent-runtime_GetInvocationStep_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetInvocationStep-response-invocationStep"></a>
The complete details of the requested invocation step.  
Type: [InvocationStep](API_agent-runtime_InvocationStep.md) object

## Errors
<a name="API_agent-runtime_GetInvocationStep_Errors"></a>

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
<a name="API_agent-runtime_GetInvocationStep_Examples"></a>

### Example request
<a name="API_agent-runtime_GetInvocationStep_Example_1"></a>

This example illustrates one usage of GetInvocationStep.

```
POST bedrock-agent-runtime.us-east-1.amazonaws.com/sessions/12345abc-1234-abcd-1234-abcdef123456/invocationSteps/11111111-2222-3333-4444-555555555555 HTTP/1.1
Content-type: application/json

{
   "invocationIdentifier": "abc-1234-abcd-1234-abcdef123456"
}
```

## See Also
<a name="API_agent-runtime_GetInvocationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GetInvocationStep) 