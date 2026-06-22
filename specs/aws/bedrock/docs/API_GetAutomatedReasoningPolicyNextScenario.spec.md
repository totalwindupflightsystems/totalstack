---
id: "@specs/aws/bedrock/docs/API_GetAutomatedReasoningPolicyNextScenario"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAutomatedReasoningPolicyNextScenario"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# GetAutomatedReasoningPolicyNextScenario

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_GetAutomatedReasoningPolicyNextScenario
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAutomatedReasoningPolicyNextScenario
<a name="API_GetAutomatedReasoningPolicyNextScenario"></a>

Retrieves the next test scenario for validating an Automated Reasoning policy. This is used during the interactive policy refinement process to test policy behavior.

## Request Syntax
<a name="API_GetAutomatedReasoningPolicyNextScenario_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}}/scenarios HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutomatedReasoningPolicyNextScenario_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowId](#API_GetAutomatedReasoningPolicyNextScenario_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyNextScenario-request-uri-buildWorkflowId"></a>
The unique identifier of the build workflow associated with the test scenarios.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [policyArn](#API_GetAutomatedReasoningPolicyNextScenario_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyNextScenario-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy for which you want to get the next test scenario.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_GetAutomatedReasoningPolicyNextScenario_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutomatedReasoningPolicyNextScenario_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyArn": "string",
   "scenario": { 
      "alternateExpression": "string",
      "expectedResult": "string",
      "expression": "string",
      "ruleIds": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetAutomatedReasoningPolicyNextScenario_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyArn](#API_GetAutomatedReasoningPolicyNextScenario_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyNextScenario-response-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [scenario](#API_GetAutomatedReasoningPolicyNextScenario_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyNextScenario-response-scenario"></a>
The next test scenario to validate, including the test expression and expected results.  
Type: [AutomatedReasoningPolicyScenario](API_AutomatedReasoningPolicyScenario.md) object

## Errors
<a name="API_GetAutomatedReasoningPolicyNextScenario_Errors"></a>

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
<a name="API_GetAutomatedReasoningPolicyNextScenario_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyNextScenario) 