---
id: "@specs/aws/bedrock-agent/docs/API_CreateAutomatedReasoningPolicyTestCase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAutomatedReasoningPolicyTestCase"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateAutomatedReasoningPolicyTestCase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_CreateAutomatedReasoningPolicyTestCase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAutomatedReasoningPolicyTestCase
<a name="API_CreateAutomatedReasoningPolicyTestCase"></a>

Creates a test for an Automated Reasoning policy. Tests validate that your policy works as expected by providing sample inputs and expected outcomes. Use tests to verify policy behavior before deploying to production.

## Request Syntax
<a name="API_CreateAutomatedReasoningPolicyTestCase_RequestSyntax"></a>

```
POST /automated-reasoning-policies/{{policyArn}}/test-cases HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "confidenceThreshold": {{number}},
   "expectedAggregatedFindingsResult": "{{string}}",
   "guardContent": "{{string}}",
   "queryContent": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAutomatedReasoningPolicyTestCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyArn](#API_CreateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create the test.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_CreateAutomatedReasoningPolicyTestCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [confidenceThreshold](#API_CreateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-request-confidenceThreshold"></a>
The minimum confidence level for logic validation. Content that meets the threshold is considered a high-confidence finding that can be validated.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** [expectedAggregatedFindingsResult](#API_CreateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-request-expectedAggregatedFindingsResult"></a>
The expected result of the Automated Reasoning check. Valid values include: , TOO\_COMPLEX, and NO\_TRANSLATIONS.  
+  `VALID` - The claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false. In other words, there are no alternative answers that are true that contradict the claims.
+  `INVALID` - The claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exists different claims that are consistent with the premises and Automated Reasoning policy.
+  `SATISFIABLE` - The claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.
+  `IMPOSSIBLE` - Automated Reasoning can’t make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.
+  `TRANSLATION_AMBIGUOUS` - Detected an ambiguity in the translation meant it would be unsound to continue with validity checking. Additional context or follow-up questions might be needed to get translation to succeed.
+  `TOO_COMPLEX` - The input contains too much information for Automated Reasoning to process within its latency limits.
+  `NO_TRANSLATIONS` - Identifies that some or all of the input prompt wasn't translated into logic. This can happen if the input isn't relevant to the Automated Reasoning policy, or if the policy doesn't have variables to model relevant input. If Automated Reasoning can't translate anything, you get a single `NO_TRANSLATIONS` finding. You might also see a `NO_TRANSLATIONS` (along with other findings) if some part of the validation isn't translated.
Type: String  
Valid Values: `VALID | INVALID | SATISFIABLE | IMPOSSIBLE | TRANSLATION_AMBIGUOUS | TOO_COMPLEX | NO_TRANSLATION`   
Required: Yes

 ** [guardContent](#API_CreateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-request-guardContent"></a>
The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

 ** [queryContent](#API_CreateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-request-queryContent"></a>
The input query or prompt that generated the content. This provides context for the validation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

## Response Syntax
<a name="API_CreateAutomatedReasoningPolicyTestCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyArn": "string",
   "testCaseId": "string"
}
```

## Response Elements
<a name="API_CreateAutomatedReasoningPolicyTestCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyArn](#API_CreateAutomatedReasoningPolicyTestCase_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-response-policyArn"></a>
The Amazon Resource Name (ARN) of the policy for which the test was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [testCaseId](#API_CreateAutomatedReasoningPolicyTestCase_ResponseSyntax) **   <a name="bedrock-CreateAutomatedReasoningPolicyTestCase-response-testCaseId"></a>
The unique identifier of the created test.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `[0-9A-Z]{12}` 

## Errors
<a name="API_CreateAutomatedReasoningPolicyTestCase_Errors"></a>

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
<a name="API_CreateAutomatedReasoningPolicyTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CreateAutomatedReasoningPolicyTestCase) 