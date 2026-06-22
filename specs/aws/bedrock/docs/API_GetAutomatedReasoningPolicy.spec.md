---
id: "@specs/aws/bedrock/docs/API_GetAutomatedReasoningPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAutomatedReasoningPolicy"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetAutomatedReasoningPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetAutomatedReasoningPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAutomatedReasoningPolicy
<a name="API_GetAutomatedReasoningPolicy"></a>

Retrieves details about an Automated Reasoning policy or policy version. Returns information including the policy definition, metadata, and timestamps.

## Request Syntax
<a name="API_GetAutomatedReasoningPolicy_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutomatedReasoningPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyArn](#API_GetAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy to retrieve. Can be either the unversioned ARN for the draft policy or an ARN for a specific policy version.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_GetAutomatedReasoningPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutomatedReasoningPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "definitionHash": "string",
   "description": "string",
   "kmsKeyArn": "string",
   "name": "string",
   "policyArn": "string",
   "policyId": "string",
   "updatedAt": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_GetAutomatedReasoningPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-createdAt"></a>
The timestamp when the policy was created.  
Type: Timestamp

 ** [definitionHash](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-definitionHash"></a>
The hash of the policy definition used as a concurrency token.  
Type: String  
Length Constraints: Fixed length of 128.  
Pattern: `[0-9a-z]{128}` 

 ** [description](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-description"></a>
The description of the policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+` 

 ** [kmsKeyArn](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the automated reasoning policy and its associated artifacts. If a AWS KMS key is not provided during the initial CreateAutomatedReasoningPolicyRequest, the kmsKeyArn won't be included in the GetAutomatedReasoningPolicyResponse.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-name"></a>
The name of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+` 

 ** [policyArn](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-policyArn"></a>
The Amazon Resource Name (ARN) of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [policyId](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-policyId"></a>
The unique identifier of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[a-z0-9]{12}` 

 ** [updatedAt](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-updatedAt"></a>
The timestamp when the policy was last updated.  
Type: Timestamp

 ** [version](#API_GetAutomatedReasoningPolicy_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicy-response-version"></a>
The version of the policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `([1-9][0-9]{0,11})` 

## Errors
<a name="API_GetAutomatedReasoningPolicy_Errors"></a>

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
HTTP Status Code: 400

## See Also
<a name="API_GetAutomatedReasoningPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAutomatedReasoningPolicy) 