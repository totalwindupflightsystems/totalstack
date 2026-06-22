---
id: "@specs/aws/bedrock-agent/docs/API_CancelAutomatedReasoningPolicyBuildWorkflow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelAutomatedReasoningPolicyBuildWorkflow"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CancelAutomatedReasoningPolicyBuildWorkflow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CancelAutomatedReasoningPolicyBuildWorkflow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelAutomatedReasoningPolicyBuildWorkflow
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow"></a>

Cancels a running Automated Reasoning policy build workflow. This stops the policy generation process and prevents further processing of the source documents.

## Request Syntax
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow_RequestSyntax"></a>

```
POST /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowId](#API_CancelAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-CancelAutomatedReasoningPolicyBuildWorkflow-request-uri-buildWorkflowId"></a>
The unique identifier of the build workflow to cancel. You can get this ID from the StartAutomatedReasoningPolicyBuildWorkflow response or by listing build workflows.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [policyArn](#API_CancelAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-CancelAutomatedReasoningPolicyBuildWorkflow-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to cancel.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow_Errors"></a>

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
<a name="API_CancelAutomatedReasoningPolicyBuildWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CancelAutomatedReasoningPolicyBuildWorkflow) 