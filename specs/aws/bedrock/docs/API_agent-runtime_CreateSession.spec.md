---
id: "@specs/aws/bedrock/docs/API_agent-runtime_CreateSession"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSession"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateSession

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent-runtime_CreateSession
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSession
<a name="API_agent-runtime_CreateSession"></a>

Creates a session to temporarily store conversations for generative AI (GenAI) applications built with open-source frameworks such as LangGraph and LlamaIndex. Sessions enable you to save the state of conversations at checkpoints, with the added security and infrastructure of AWS. For more information, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

By default, Amazon Bedrock uses AWS-managed keys for session encryption, including session metadata, or you can use your own KMS key. For more information, see [Amazon Bedrock session encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html).

**Note**  
 You use a session to store state and conversation history for generative AI applications built with open-source frameworks. For Amazon Bedrock Agents, the service automatically manages conversation context and associates them with the agent-specific sessionId you specify in the [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) API operation. 

Related APIs:
+  [ListSessions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html) 
+  [GetSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html) 
+  [EndSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html) 
+  [DeleteSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteSession.html) 

## Request Syntax
<a name="API_agent-runtime_CreateSession_RequestSyntax"></a>

```
PUT /sessions/ HTTP/1.1
Content-type: application/json

{
   "encryptionKeyArn": "{{string}}",
   "sessionMetadata": { 
      "{{string}}" : "{{string}}" 
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_CreateSession_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent-runtime_CreateSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionKeyArn](#API_agent-runtime_CreateSession_RequestSyntax) **   <a name="bedrock-agent-runtime_CreateSession-request-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to use to encrypt the session data. The user or role creating the session must have permission to use the key. For more information, see [Amazon Bedrock session encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [sessionMetadata](#API_agent-runtime_CreateSession_RequestSyntax) **   <a name="bedrock-agent-runtime_CreateSession-request-sessionMetadata"></a>
A map of key-value pairs containing attributes to be persisted across the session. For example, the user's ID, their language preference, and the type of device they are using.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.  
Required: No

 ** [tags](#API_agent-runtime_CreateSession_RequestSyntax) **   <a name="bedrock-agent-runtime_CreateSession-request-tags"></a>
Specify the key-value pairs for the tags that you want to attach to the session.  
Type: String to string map  
Map Entries: Maximum number of 200 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_agent-runtime_CreateSession_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "createdAt": "string",
   "sessionArn": "string",
   "sessionId": "string",
   "sessionStatus": "string"
}
```

## Response Elements
<a name="API_agent-runtime_CreateSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_agent-runtime_CreateSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_CreateSession-response-createdAt"></a>
The timestamp for when the session was created.  
Type: Timestamp

 ** [sessionArn](#API_agent-runtime_CreateSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_CreateSession-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the created session.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [sessionId](#API_agent-runtime_CreateSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_CreateSession-response-sessionId"></a>
The unique identifier for the session.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [sessionStatus](#API_agent-runtime_CreateSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_CreateSession-response-sessionStatus"></a>
The current status of the session.  
Type: String  
Valid Values: `ACTIVE | EXPIRED | ENDED` 

## Errors
<a name="API_agent-runtime_CreateSession_Errors"></a>

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
<a name="API_agent-runtime_CreateSession_Examples"></a>

### Example request
<a name="API_agent-runtime_CreateSession_Example_1"></a>

This example illustrates one usage of CreateSession.

```
PUT bedrock-agent-runtime.us-east-1.amazonaws.com/sessions/ HTTP/1.1
Content-type: application/json

{
    "encryptionKeyArn": "key Amazon Resource Name (ARN)",
    "sessionMetadata": {
        "deviceType": "mobile",
        "language": "english"
    },
    "tags": {
        "Environment": "Production",
        "Project": "Demo"
    }
}
```

## See Also
<a name="API_agent-runtime_CreateSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/CreateSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/CreateSession) 