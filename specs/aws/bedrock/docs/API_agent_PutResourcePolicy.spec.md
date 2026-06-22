---
id: "@specs/aws/bedrock/docs/API_agent_PutResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutResourcePolicy"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# PutResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_PutResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutResourcePolicy
<a name="API_agent_PutResourcePolicy"></a>

Associates a resource policy with a knowledge base. A resource policy allows other AWS accounts to access the knowledge base. For more information, see [Cross-account access for knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-cross-account.html).

## Request Syntax
<a name="API_agent_PutResourcePolicy_RequestSyntax"></a>

```
PUT /resourcepolicy/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "expectedRevisionId": "{{string}}",
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_PutResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_agent_PutResourcePolicy_RequestSyntax) **   <a name="bedrock-agent_PutResourcePolicy-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the knowledge base to attach the resource policy to.  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+`   
Required: Yes

## Request Body
<a name="API_agent_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expectedRevisionId](#API_agent_PutResourcePolicy_RequestSyntax) **   <a name="bedrock-agent_PutResourcePolicy-request-expectedRevisionId"></a>
The expected revision identifier of the resource policy. Use this to prevent conflicts when multiple users update the same policy concurrently. Specify the `revisionId` from the most recent `GetResourcePolicy` or `PutResourcePolicy` response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** [policy](#API_agent_PutResourcePolicy_RequestSyntax) **   <a name="bedrock-agent_PutResourcePolicy-request-policy"></a>
The JSON-formatted resource policy to associate with the knowledge base.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20480.  
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`   
Required: Yes

## Response Syntax
<a name="API_agent_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "resourceArn": "string",
   "revisionId": "string"
}
```

## Response Elements
<a name="API_agent_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceArn](#API_agent_PutResourcePolicy_ResponseSyntax) **   <a name="bedrock-agent_PutResourcePolicy-response-resourceArn"></a>
The ARN of the knowledge base that the resource policy was attached to.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:knowledge-base/[0-9a-zA-Z]+` 

 ** [revisionId](#API_agent_PutResourcePolicy_ResponseSyntax) **   <a name="bedrock-agent_PutResourcePolicy-response-revisionId"></a>
The revision identifier of the resource policy. Use this value in the `expectedRevisionId` field of a subsequent `PutResourcePolicy` or `DeleteResourcePolicy` request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_agent_PutResourcePolicy_Errors"></a>

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
<a name="API_agent_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/PutResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PutResourcePolicy) 