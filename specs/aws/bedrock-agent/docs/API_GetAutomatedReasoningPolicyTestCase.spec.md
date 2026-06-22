---
id: "@specs/aws/bedrock-agent/docs/API_GetAutomatedReasoningPolicyTestCase"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAutomatedReasoningPolicyTestCase"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAutomatedReasoningPolicyTestCase

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetAutomatedReasoningPolicyTestCase
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAutomatedReasoningPolicyTestCase
<a name="API_GetAutomatedReasoningPolicyTestCase"></a>

Retrieves details about a specific Automated Reasoning policy test.

## Request Syntax
<a name="API_GetAutomatedReasoningPolicyTestCase_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/test-cases/{{testCaseId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutomatedReasoningPolicyTestCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyArn](#API_GetAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyTestCase-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

 ** [testCaseId](#API_GetAutomatedReasoningPolicyTestCase_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyTestCase-request-uri-testCaseId"></a>
The unique identifier of the test to retrieve.  
Length Constraints: Minimum length of 0. Maximum length of 12.  
Pattern: `[0-9A-Z]{12}`   
Required: Yes

## Request Body
<a name="API_GetAutomatedReasoningPolicyTestCase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutomatedReasoningPolicyTestCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policyArn": "string",
   "testCase": { 
      "confidenceThreshold": number,
      "createdAt": "string",
      "expectedAggregatedFindingsResult": "string",
      "guardContent": "string",
      "queryContent": "string",
      "testCaseId": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_GetAutomatedReasoningPolicyTestCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyArn](#API_GetAutomatedReasoningPolicyTestCase_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyTestCase-response-policyArn"></a>
The Amazon Resource Name (ARN) of the policy that contains the test.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

 ** [testCase](#API_GetAutomatedReasoningPolicyTestCase_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyTestCase-response-testCase"></a>
The test details including the content, query, expected result, and metadata.  
Type: [AutomatedReasoningPolicyTestCase](API_AutomatedReasoningPolicyTestCase.md) object

## Errors
<a name="API_GetAutomatedReasoningPolicyTestCase_Errors"></a>

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
<a name="API_GetAutomatedReasoningPolicyTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyTestCase) 