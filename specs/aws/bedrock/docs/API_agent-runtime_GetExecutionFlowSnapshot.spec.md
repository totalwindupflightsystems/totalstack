---
id: "@specs/aws/bedrock/docs/API_agent-runtime_GetExecutionFlowSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetExecutionFlowSnapshot"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetExecutionFlowSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent-runtime_GetExecutionFlowSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetExecutionFlowSnapshot
<a name="API_agent-runtime_GetExecutionFlowSnapshot"></a>

Retrieves the flow definition snapshot used for a flow execution. The snapshot represents the flow metadata and definition as it existed at the time the execution was started. Note that even if the flow is edited after an execution starts, the snapshot connected to the execution remains unchanged.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Request Syntax
<a name="API_agent-runtime_GetExecutionFlowSnapshot_RequestSyntax"></a>

```
GET /flows/{{flowIdentifier}}/aliases/{{flowAliasIdentifier}}/executions/{{executionIdentifier}}/flowsnapshot HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_GetExecutionFlowSnapshot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [executionIdentifier](#API_agent-runtime_GetExecutionFlowSnapshot_RequestSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-request-uri-executionIdentifier"></a>
The unique identifier of the flow execution.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})`   
Required: Yes

 ** [flowAliasIdentifier](#API_agent-runtime_GetExecutionFlowSnapshot_RequestSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-request-uri-flowAliasIdentifier"></a>
The unique identifier of the flow alias used for the flow execution.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [flowIdentifier](#API_agent-runtime_GetExecutionFlowSnapshot_RequestSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_GetExecutionFlowSnapshot_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_GetExecutionFlowSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "customerEncryptionKeyArn": "string",
   "definition": "string",
   "executionRoleArn": "string",
   "flowAliasIdentifier": "string",
   "flowIdentifier": "string",
   "flowVersion": "string"
}
```

## Response Elements
<a name="API_agent-runtime_GetExecutionFlowSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customerEncryptionKeyArn](#API_agent-runtime_GetExecutionFlowSnapshot_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-response-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed AWS KMS key that's used to encrypt the flow snapshot.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [definition](#API_agent-runtime_GetExecutionFlowSnapshot_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-response-definition"></a>
The flow definition used for the flow execution, including the nodes, connections, and configuration at the time when the execution started.  
The definition returns as a string that follows the structure of a [FlowDefinition](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_FlowDefinition.html) object.  
Type: String

 ** [executionRoleArn](#API_agent-runtime_GetExecutionFlowSnapshot_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-response-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that's used by the flow execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+` 

 ** [flowAliasIdentifier](#API_agent-runtime_GetExecutionFlowSnapshot_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-response-flowAliasIdentifier"></a>
The unique identifier of the flow alias used for the flow execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)` 

 ** [flowIdentifier](#API_agent-runtime_GetExecutionFlowSnapshot_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-response-flowIdentifier"></a>
The unique identifier of the flow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})` 

 ** [flowVersion](#API_agent-runtime_GetExecutionFlowSnapshot_ResponseSyntax) **   <a name="bedrock-agent-runtime_GetExecutionFlowSnapshot-response-flowVersion"></a>
The version of the flow used for the flow execution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})` 

## Errors
<a name="API_agent-runtime_GetExecutionFlowSnapshot_Errors"></a>

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

## See Also
<a name="API_agent-runtime_GetExecutionFlowSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GetExecutionFlowSnapshot) 