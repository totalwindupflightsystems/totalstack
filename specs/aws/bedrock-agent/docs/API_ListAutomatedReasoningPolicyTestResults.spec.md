---
id: "@specs/aws/bedrock-agent/docs/API_ListAutomatedReasoningPolicyTestResults"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAutomatedReasoningPolicyTestResults"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListAutomatedReasoningPolicyTestResults

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListAutomatedReasoningPolicyTestResults
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAutomatedReasoningPolicyTestResults
<a name="API_ListAutomatedReasoningPolicyTestResults"></a>

Lists test results for an Automated Reasoning policy, showing how the policy performed against various test scenarios and validation checks.

## Request Syntax
<a name="API_ListAutomatedReasoningPolicyTestResults_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}}/test-results?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAutomatedReasoningPolicyTestResults_RequestParameters"></a>

The request uses the following URI parameters.

 ** [buildWorkflowId](#API_ListAutomatedReasoningPolicyTestResults_RequestSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestResults-request-uri-buildWorkflowId"></a>
The unique identifier of the build workflow whose test results you want to list.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [maxResults](#API_ListAutomatedReasoningPolicyTestResults_RequestSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestResults-request-uri-maxResults"></a>
The maximum number of test results to return in a single response. Valid range is 1-100.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAutomatedReasoningPolicyTestResults_RequestSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestResults-request-uri-nextToken"></a>
A pagination token from a previous request to continue listing test results from where the previous request left off.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyArn](#API_ListAutomatedReasoningPolicyTestResults_RequestSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestResults-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy whose test results you want to list.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_ListAutomatedReasoningPolicyTestResults_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAutomatedReasoningPolicyTestResults_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "testResults": [ 
      { 
         "aggregatedTestFindingsResult": "string",
         "policyArn": "string",
         "testCase": { 
            "confidenceThreshold": number,
            "createdAt": "string",
            "expectedAggregatedFindingsResult": "string",
            "guardContent": "string",
            "queryContent": "string",
            "testCaseId": "string",
            "updatedAt": "string"
         },
         "testFindings": [ 
            { ... }
         ],
         "testRunResult": "string",
         "testRunStatus": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAutomatedReasoningPolicyTestResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAutomatedReasoningPolicyTestResults_ResponseSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestResults-response-nextToken"></a>
A pagination token to use in subsequent requests to retrieve additional test results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [testResults](#API_ListAutomatedReasoningPolicyTestResults_ResponseSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestResults-response-testResults"></a>
A list of test results, each containing information about how the policy performed on specific test scenarios.  
Type: Array of [AutomatedReasoningPolicyTestResult](API_AutomatedReasoningPolicyTestResult.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5000 items.

## Errors
<a name="API_ListAutomatedReasoningPolicyTestResults_Errors"></a>

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
<a name="API_ListAutomatedReasoningPolicyTestResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestResults) 