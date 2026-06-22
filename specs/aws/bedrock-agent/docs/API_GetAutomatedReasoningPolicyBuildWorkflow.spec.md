---
id: "@specs/aws/bedrock-agent/docs/API_GetAutomatedReasoningPolicyBuildWorkflow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAutomatedReasoningPolicyBuildWorkflow"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAutomatedReasoningPolicyBuildWorkflow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetAutomatedReasoningPolicyBuildWorkflow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAutomatedReasoningPolicyBuildWorkflow
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow"></a>

Retrieves detailed information about an Automated Reasoning policy build workflow, including its status, configuration, and metadata.

## Request Syntax
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowId](#API_GetAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-request-uri-buildWorkflowId"></a>
The unique identifier of the build workflow to retrieve.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [policyArn](#API_GetAutomatedReasoningPolicyBuildWorkflow_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to retrieve.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "buildWorkflowId": "string",
   "buildWorkflowType": "string",
   "createdAt": "string",
   "documentContentType": "string",
   "documentDescription": "string",
   "documentName": "string",
   "policyArn": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildWorkflowId](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-buildWorkflowId"></a>
The unique identifier of the build workflow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}` 

 ** [buildWorkflowType](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-buildWorkflowType"></a>
The type of build workflow being executed (e.g., DOCUMENT\_INGESTION, POLICY\_REPAIR).  
Type: String  
Valid Values: `INGEST_CONTENT | REFINE_POLICY | IMPORT_POLICY | GENERATE_FIDELITY_REPORT | GENERATE_POLICY_SCENARIOS | RESOLVE_POLICY_AMBIGUITIES | ITERATIVELY_REFINE_POLICY` 

 ** [createdAt](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-createdAt"></a>
The timestamp when the build workflow was created.  
Type: Timestamp

 ** [documentContentType](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-documentContentType"></a>
The content type of the source document (e.g., text/plain, application/pdf).  
Type: String  
Valid Values: `pdf | txt` 

 ** [documentDescription](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-documentDescription"></a>
A detailed description of the document's content and how it should be used in the policy generation process.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4000.

 ** [documentName](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-documentName"></a>
The name of the source document used in the build workflow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [policyArn](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [status](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-status"></a>
The current status of the build workflow (e.g., RUNNING, COMPLETED, FAILED, CANCELLED).  
Type: String  
Valid Values: `SCHEDULED | CANCEL_REQUESTED | PREPROCESSING | BUILDING | TESTING | COMPLETED | FAILED | CANCELLED` 

 ** [updatedAt](#API_GetAutomatedReasoningPolicyBuildWorkflow_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflow-response-updatedAt"></a>
The timestamp when the build workflow was last updated.  
Type: Timestamp

## Errors
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow_Errors"></a>

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
<a name="API_GetAutomatedReasoningPolicyBuildWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflow) 