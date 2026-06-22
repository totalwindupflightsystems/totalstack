---
id: "@specs/aws/bedrock/docs/API_DeleteAutomatedReasoningPolicyBuildWorkflow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAutomatedReasoningPolicyBuildWorkflow"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeleteAutomatedReasoningPolicyBuildWorkflow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_DeleteAutomatedReasoningPolicyBuildWorkflow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAutomatedReasoningPolicyBuildWorkflow
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow"></a>

Deletes an Automated Reasoning policy build workflow and its associated artifacts. This permanently removes the workflow history and any generated assets.

## Request Syntax
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow_RequestSyntax"></a>

```
DELETE /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}}?updatedAt={{lastUpdatedAt}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowId](#API_DeleteAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-DeleteAutomatedReasoningPolicyBuildWorkflow-request-uri-buildWorkflowId"></a>
The unique identifier of the build workflow to delete.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [lastUpdatedAt](#API_DeleteAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-DeleteAutomatedReasoningPolicyBuildWorkflow-request-uri-lastUpdatedAt"></a>
The timestamp when the build workflow was last updated. This is used for optimistic concurrency control to prevent accidental deletion of workflows that have been modified.  
Required: Yes

 ** [policyArn](#API_DeleteAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-DeleteAutomatedReasoningPolicyBuildWorkflow-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to delete.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow_Errors"></a>

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
<a name="API_DeleteAutomatedReasoningPolicyBuildWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteAutomatedReasoningPolicyBuildWorkflow) 