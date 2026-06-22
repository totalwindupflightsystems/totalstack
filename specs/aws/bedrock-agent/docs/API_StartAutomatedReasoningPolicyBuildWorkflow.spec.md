---
id: "@specs/aws/bedrock-agent/docs/API_StartAutomatedReasoningPolicyBuildWorkflow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartAutomatedReasoningPolicyBuildWorkflow"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# StartAutomatedReasoningPolicyBuildWorkflow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_StartAutomatedReasoningPolicyBuildWorkflow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartAutomatedReasoningPolicyBuildWorkflow
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow"></a>

Starts a new build workflow for an Automated Reasoning policy. This initiates the process of analyzing source documents and generating policy rules, variables, and types.

## Request Syntax
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow_RequestSyntax"></a>

```
POST /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowType}}/start HTTP/1.1
x-amz-client-token: {{clientRequestToken}}
Content-type: application/json

{
   "policyDefinition": { 
      "rules": [ 
         { 
            "alternateExpression": "{{string}}",
            "expression": "{{string}}",
            "id": "{{string}}"
         }
      ],
      "types": [ 
         { 
            "description": "{{string}}",
            "name": "{{string}}",
            "values": [ 
               { 
                  "description": "{{string}}",
                  "value": "{{string}}"
               }
            ]
         }
      ],
      "variables": [ 
         { 
            "description": "{{string}}",
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "version": "{{string}}"
   },
   "workflowContent": { ... }
}
```

## URI Request Parameters
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowType](#API_StartAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyBuildWorkflow-request-uri-buildWorkflowType"></a>
The type of build workflow to start (e.g., DOCUMENT\_INGESTION for processing new documents, POLICY\_REPAIR for fixing existing policies).  
Valid Values: `INGEST_CONTENT | REFINE_POLICY | IMPORT_POLICY | GENERATE_FIDELITY_REPORT | GENERATE_POLICY_SCENARIOS | RESOLVE_POLICY_AMBIGUITIES | ITERATIVELY_REFINE_POLICY`   
Required: Yes

 ** [clientRequestToken](#API_StartAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyBuildWorkflow-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?` 

 ** [policyArn](#API_StartAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyBuildWorkflow-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to start the build workflow.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policyDefinition](#API_StartAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyBuildWorkflow-request-policyDefinition"></a>
An existing policy definition that serves as the starting point for the build workflow, typically used in policy repair or update scenarios.  
Type: [AutomatedReasoningPolicyDefinition](API_AutomatedReasoningPolicyDefinition.md) object  
Required: No

 ** [workflowContent](#API_StartAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyBuildWorkflow-request-workflowContent"></a>
The actual content to be processed in the build workflow, such as documents to analyze or repair instructions to apply.  
Type: [AutomatedReasoningPolicyWorkflowTypeContent](API_AutomatedReasoningPolicyWorkflowTypeContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## Response Syntax
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "buildWorkflowId": "string",
   "policyArn": "string"
}
```

## Response Elements
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildWorkflowId](#API_StartAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyBuildWorkflow-response-buildWorkflowId"></a>
The unique identifier of the newly started build workflow. Use this ID to track the workflow's progress and retrieve its results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}` 

 ** [policyArn](#API_StartAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-StartAutomatedReasoningPolicyBuildWorkflow-response-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

## Errors
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow_Errors"></a>

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

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_StartAutomatedReasoningPolicyBuildWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/StartAutomatedReasoningPolicyBuildWorkflow) 