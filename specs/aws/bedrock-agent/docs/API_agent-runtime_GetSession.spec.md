---
id: "@specs/aws/bedrock-agent/docs/API_agent-runtime_GetSession"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSession"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetSession

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent-runtime_GetSession
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSession
<a name="API_agent-runtime_GetSession"></a>

Retrieves details about a specific session. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

## Request Syntax
<a name="API_agent-runtime_GetSession_RequestSyntax"></a>

```
GET /sessions/{{sessionIdentifier}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_GetSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sessionIdentifier](#API_agent-runtime_GetSession_RequestSyntax) **   <a name="bedrock-agent-runtime_GetSession-request-uri-sessionIdentifier"></a>
A unique identifier for the session to retrieve. You can specify either the session's `sessionId` or its Amazon Resource Name (ARN).  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_GetSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_GetSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "encryptionKeyArn": "string",
   "lastUpdatedAt": "string",
   "sessionArn": "string",
   "sessionId": "string",
   "sessionMetadata": { 
      "string" : "string" 
   },
   "sessionStatus": "string"
}
```

## Response Elements
<a name="API_agent-runtime_GetSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_agent-runtime_GetSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetSession-response-createdAt"></a>
The timestamp for when the session was created.  
Type: Timestamp

 ** [encryptionKeyArn](#API_agent-runtime_GetSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetSession-response-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the session data. For more information, see [Amazon Bedrock session encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [lastUpdatedAt](#API_agent-runtime_GetSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetSession-response-lastUpdatedAt"></a>
The timestamp for when the session was last modified.  
Type: Timestamp

 ** [sessionArn](#API_agent-runtime_GetSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetSession-response-sessionArn"></a>
The Amazon Resource Name (ARN) of the session.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [sessionId](#API_agent-runtime_GetSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetSession-response-sessionId"></a>
The unique identifier for the session in UUID format.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [sessionMetadata](#API_agent-runtime_GetSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetSession-response-sessionMetadata"></a>
A map of key-value pairs containing attributes persisted across the session.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Value Length Constraints: Minimum length of 0. Maximum length of 5000.

 ** [sessionStatus](#API_agent-runtime_GetSession_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetSession-response-sessionStatus"></a>
The current status of the session.  
Type: String  
Valid Values: `ACTIVE | EXPIRED | ENDED` 

## Errors
<a name="API_agent-runtime_GetSession_Errors"></a>

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
<a name="API_agent-runtime_GetSession_Examples"></a>

### Example request
<a name="API_agent-runtime_GetSession_Example_1"></a>

This example illustrates one usage of GetSession.

```
GET bedrock-agent-runtime.us-east-1.amazonaws.com/sessions/12345abc-1234-abcd-1234-abcdef123456/ HTTP/1.1
```

## See Also
<a name="API_agent-runtime_GetSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GetSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GetSession) 