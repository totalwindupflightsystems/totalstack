---
id: "@specs/aws/bedrock-agent/docs/API_ListAutomatedReasoningPolicyTestCases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAutomatedReasoningPolicyTestCases"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListAutomatedReasoningPolicyTestCases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListAutomatedReasoningPolicyTestCases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAutomatedReasoningPolicyTestCases
<a name="API_ListAutomatedReasoningPolicyTestCases"></a>

Lists tests for an Automated Reasoning policy. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListAutomatedReasoningPolicyTestCases_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/test-cases?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAutomatedReasoningPolicyTestCases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAutomatedReasoningPolicyTestCases_RequestSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestCases-request-uri-maxResults"></a>
The maximum number of tests to return in a single call.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAutomatedReasoningPolicyTestCases_RequestSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestCases-request-uri-nextToken"></a>
The pagination token from a previous request to retrieve the next page of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [policyArn](#API_ListAutomatedReasoningPolicyTestCases_RequestSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestCases-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to list tests.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_ListAutomatedReasoningPolicyTestCases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAutomatedReasoningPolicyTestCases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "testCases": [ 
      { 
         "confidenceThreshold": number,
         "createdAt": "string",
         "expectedAggregatedFindingsResult": "string",
         "guardContent": "string",
         "queryContent": "string",
         "testCaseId": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAutomatedReasoningPolicyTestCases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAutomatedReasoningPolicyTestCases_ResponseSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestCases-response-nextToken"></a>
The pagination token to use in a subsequent request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [testCases](#API_ListAutomatedReasoningPolicyTestCases_ResponseSyntax) **   <a name="bedrock-ListAutomatedReasoningPolicyTestCases-response-testCases"></a>
A list of tests for the specified policy.  
Type: Array of [AutomatedReasoningPolicyTestCase](API_AutomatedReasoningPolicyTestCase.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

## Errors
<a name="API_ListAutomatedReasoningPolicyTestCases_Errors"></a>

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
<a name="API_ListAutomatedReasoningPolicyTestCases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListAutomatedReasoningPolicyTestCases) 