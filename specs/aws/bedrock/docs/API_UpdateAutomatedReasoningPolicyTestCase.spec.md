---
id: "@specs/aws/bedrock/docs/API_UpdateAutomatedReasoningPolicyTestCase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAutomatedReasoningPolicyTestCase"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# UpdateAutomatedReasoningPolicyTestCase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_UpdateAutomatedReasoningPolicyTestCase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAutomatedReasoningPolicyTestCase
<a name="API_UpdateAutomatedReasoningPolicyTestCase"></a>

Updates an existing Automated Reasoning policy test. You can modify the content, query, expected result, and confidence threshold.

## Request Syntax
<a name="API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax"></a>

```
PATCH /automated-reasoning-policies/{{policyArn}}/test-cases/{{testCaseId}} HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "confidenceThreshold": {{number}},
   "expectedAggregatedFindingsResult": "{{string}}",
   "guardContent": "{{string}}",
   "lastUpdatedAt": "{{string}}",
   "queryContent": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAutomatedReasoningPolicyTestCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyArn](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

 ** [testCaseId](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-uri-testCaseId"></a>
The unique identifier of the test to update.  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `[0-9A-Z]{12}`   
Required: Yes

## Request Body
<a name="API_UpdateAutomatedReasoningPolicyTestCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-clientRequestToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9]([-a-zA-Z0-9]{0,254}[a-zA-Z0-9])?`   
Required: No

 ** [confidenceThreshold](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-confidenceThreshold"></a>
The updated minimum confidence level for logic validation. If null is provided, the threshold will be removed.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** [expectedAggregatedFindingsResult](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-expectedAggregatedFindingsResult"></a>
The updated expected result of the Automated Reasoning check.  
Type: String  
Valid Values: `VALID | INVALID | SATISFIABLE | IMPOSSIBLE | TRANSLATION_AMBIGUOUS | TOO_COMPLEX | NO_TRANSLATION`   
Required: Yes

 ** [guardContent](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-guardContent"></a>
The updated content to be validated by the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

 ** [lastUpdatedAt](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-lastUpdatedAt"></a>
The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.  
Type: Timestamp  
Required: Yes

 ** [queryContent](#API_UpdateAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-request-queryContent"></a>
The updated input query or prompt that generated the content.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

## Response Syntax
<a name="API_UpdateAutomatedReasoningPolicyTestCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyArn": "string",
   "testCaseId": "string"
}
```

## Response Elements
<a name="API_UpdateAutomatedReasoningPolicyTestCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyArn](#API_UpdateAutomatedReasoningPolicyTestCase_ResponseSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-response-policyArn"></a>
The Amazon Resource Name (ARN) of the policy that contains the updated test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [testCaseId](#API_UpdateAutomatedReasoningPolicyTestCase_ResponseSyntax) **   <a name="bedrock-UpdateAutomatedReasoningPolicyTestCase-response-testCaseId"></a>
The unique identifier of the updated test.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `[0-9A-Z]{12}` 

## Errors
<a name="API_UpdateAutomatedReasoningPolicyTestCase_Errors"></a>

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
<a name="API_UpdateAutomatedReasoningPolicyTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/UpdateAutomatedReasoningPolicyTestCase) 