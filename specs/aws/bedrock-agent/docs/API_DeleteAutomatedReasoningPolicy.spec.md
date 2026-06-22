---
id: "@specs/aws/bedrock-agent/docs/API_DeleteAutomatedReasoningPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAutomatedReasoningPolicy"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteAutomatedReasoningPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_DeleteAutomatedReasoningPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAutomatedReasoningPolicy
<a name="API_DeleteAutomatedReasoningPolicy"></a>

Deletes an Automated Reasoning policy or policy version. This operation is idempotent. If you delete a policy more than once, each call succeeds. Deleting a policy removes it permanently and cannot be undone.

## Request Syntax
<a name="API_DeleteAutomatedReasoningPolicy_RequestSyntax"></a>

```
DELETE /automated-reasoning-policies/{{policyArn}}?force={{force}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAutomatedReasoningPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [force](#API_DeleteAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-DeleteAutomatedReasoningPolicy-request-uri-force"></a>
Specifies whether to force delete the automated reasoning policy even if it has active resources. When `false`, Amazon Bedrock validates if all artifacts have been deleted (e.g. policy version, test case, test result) for a policy before deletion. When `true`, Amazon Bedrock will delete the policy and all its artifacts without validation. Default is `false`. 

 ** [policyArn](#API_DeleteAutomatedReasoningPolicy_RequestSyntax) **   <a name="bedrock-DeleteAutomatedReasoningPolicy-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy to delete.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_DeleteAutomatedReasoningPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAutomatedReasoningPolicy_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteAutomatedReasoningPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteAutomatedReasoningPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceInUseException **   
Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.  
HTTP Status Code: 400

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
<a name="API_DeleteAutomatedReasoningPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicy) 