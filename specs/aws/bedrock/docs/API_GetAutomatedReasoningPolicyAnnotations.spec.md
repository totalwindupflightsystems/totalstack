---
id: "@specs/aws/bedrock/docs/API_GetAutomatedReasoningPolicyAnnotations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAutomatedReasoningPolicyAnnotations"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetAutomatedReasoningPolicyAnnotations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetAutomatedReasoningPolicyAnnotations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAutomatedReasoningPolicyAnnotations
<a name="API_GetAutomatedReasoningPolicyAnnotations"></a>

Retrieves the current annotations for an Automated Reasoning policy build workflow. Annotations contain corrections to the rules, variables and types to be applied to the policy.

## Request Syntax
<a name="API_GetAutomatedReasoningPolicyAnnotations_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}}/annotations HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutomatedReasoningPolicyAnnotations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowId](#API_GetAutomatedReasoningPolicyAnnotations_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-request-uri-buildWorkflowId"></a>
The unique identifier of the build workflow whose annotations you want to retrieve.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [policyArn](#API_GetAutomatedReasoningPolicyAnnotations_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to retrieve.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_GetAutomatedReasoningPolicyAnnotations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutomatedReasoningPolicyAnnotations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "annotations": [ 
      { ... }
   ],
   "annotationSetHash": "string",
   "buildWorkflowId": "string",
   "name": "string",
   "policyArn": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetAutomatedReasoningPolicyAnnotations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [annotations](#API_GetAutomatedReasoningPolicyAnnotations_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-response-annotations"></a>
The current set of annotations containing rules, variables, and types extracted from the source documents. These can be modified before finalizing the policy.  
Type: Array of [AutomatedReasoningPolicyAnnotation](API_AutomatedReasoningPolicyAnnotation.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [annotationSetHash](#API_GetAutomatedReasoningPolicyAnnotations_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-response-annotationSetHash"></a>
A hash value representing the current state of the annotations. This is used for optimistic concurrency control when updating annotations.  
Type: String  
Length Constraints: Fixed length of 128.  
Pattern: `[0-9a-z]{128}` 

 ** [buildWorkflowId](#API_GetAutomatedReasoningPolicyAnnotations_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-response-buildWorkflowId"></a>
The unique identifier of the build workflow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}` 

 ** [name](#API_GetAutomatedReasoningPolicyAnnotations_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-response-name"></a>
The name of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_ ]+` 

 ** [policyArn](#API_GetAutomatedReasoningPolicyAnnotations_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-response-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [updatedAt](#API_GetAutomatedReasoningPolicyAnnotations_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyAnnotations-response-updatedAt"></a>
The timestamp when the annotations were last updated.  
Type: Timestamp

## Errors
<a name="API_GetAutomatedReasoningPolicyAnnotations_Errors"></a>

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
<a name="API_GetAutomatedReasoningPolicyAnnotations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyAnnotations) 