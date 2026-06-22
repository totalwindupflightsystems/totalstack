---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_EndSession"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EndSession"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# EndSession

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_EndSession
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EndSession
<a name="API_agent-runtime_EndSession"></a>

Ends the session. After you end a session, you can still access its content but you can’t add to it. To delete the session and it's content, you use the DeleteSession API operation. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

## Request Syntax
<a name="API_agent-runtime_EndSession_RequestSyntax"></a>

```
PATCH /sessions/{{sessionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_EndSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sessionIdentifier](#API_agent-runtime_EndSession_RequestSyntax) **   <a name="bedrock-agent-runtime_EndSession-request-uri-sessionIdentifier"></a>
The unique identifier for the session to end. You can specify either the session's `sessionId` or its Amazon Resource Name (ARN).  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_EndSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_EndSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sessionArn": "string",
   "sessionId": "string",
   "sessionStatus": "string"
}
```

## Response Elements
<a name="API_agent-runtime_EndSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sessionArn](#API_agent-runtime_EndSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_EndSession-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the session you ended.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [sessionId](#API_agent-runtime_EndSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_EndSession-response-sessionId"></a>
The unique identifier of the session you ended.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [sessionStatus](#API_agent-runtime_EndSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_EndSession-response-sessionStatus"></a>
The current status of the session you ended.  
Type: String  
Valid Values: `ACTIVE | EXPIRED | ENDED` 

## Errors
<a name="API_agent-runtime_EndSession_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_EndSession_Examples"></a>

### Example request
<a name="API_agent-runtime_EndSession_Example_1"></a>

This example illustrates one usage of EndSession.

```
PATCH bedrock-agent-runtime.us-east-1.amazonaws.com/sessions/12345abc-1234-abcd-1234-abcdef123456/ HTTP/1.1
```

## See Also
<a name="API_agent-runtime_EndSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/EndSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/EndSession) 