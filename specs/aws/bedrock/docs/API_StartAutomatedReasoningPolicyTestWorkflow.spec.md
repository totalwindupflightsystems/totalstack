---
id: "@specs/aws/bedrock/docs/API_StartAutomatedReasoningPolicyTestWorkflow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartAutomatedReasoningPolicyTestWorkflow"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# StartAutomatedReasoningPolicyTestWorkflow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_StartAutomatedReasoningPolicyTestWorkflow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartAutomatedReasoningPolicyTestWorkflow
<a name="API_StartAutomatedReasoningPolicyTestWorkflow"></a>

Initiates a test workflow to validate Automated Reasoning policy tests. The workflow executes the specified tests against the policy and generates validation results.

## Request Syntax
<a name="API_StartAutomatedReasoningPolicyTestWorkflow_RequestSyntax"></a>

```
POST /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}}/test-workflows HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "testCaseIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_StartAutomatedReasoningPolicyTestWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowId](#API_StartAutomatedReasoningPolicyTestWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyTestWorkflow-request-uri-buildWorkflowId"></a>
The build workflow identifier. The build workflow must show a `COMPLETED` status before running tests.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [policyArn](#API_StartAutomatedReasoningPolicyTestWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyTestWorkflow-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy to test.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_StartAutomatedReasoningPolicyTestWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_StartAutomatedReasoningPolicyTestWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyTestWorkflow-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [testCaseIds](#API_StartAutomatedReasoningPolicyTestWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyTestWorkflow-request-testCaseIds"></a>
The list of test identifiers to run. If not provided, all tests for the policy are run.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `[0-9A-Z]{12}`   
Required: No

## Response Syntax
<a name="API_StartAutomatedReasoningPolicyTestWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyArn": "string"
}
```

## Response Elements
<a name="API_StartAutomatedReasoningPolicyTestWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyArn](#API_StartAutomatedReasoningPolicyTestWorkflow_ResponseSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyTestWorkflow-response-policyArn"></a>
The Amazon Resource Name (ARN) of the policy for which the test workflow was started.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

## Errors
<a name="API_StartAutomatedReasoningPolicyTestWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

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
<a name="API_StartAutomatedReasoningPolicyTestWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/StartAutomatedReasoningPolicyTestWorkflow) 