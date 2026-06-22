---
id: "@specs/aws/bedrock/docs/API_ListAdvancedPromptOptimizationJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAdvancedPromptOptimizationJobs"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# ListAdvancedPromptOptimizationJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_ListAdvancedPromptOptimizationJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAdvancedPromptOptimizationJobs
<a name="API_ListAdvancedPromptOptimizationJobs"></a>

Lists the advanced prompt optimization jobs in your account.

## Request Syntax
<a name="API_ListAdvancedPromptOptimizationJobs_RequestSyntax"></a>

```
GET /advanced-prompt-optimization-jobs?maxResults={{maxResults}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAdvancedPromptOptimizationJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAdvancedPromptOptimizationJobs_RequestSyntax) **   <a name="bedrock-ListAdvancedPromptOptimizationJobs-request-uri-maxResults"></a>
The maximum number of results to return.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAdvancedPromptOptimizationJobs_RequestSyntax) **   <a name="bedrock-ListAdvancedPromptOptimizationJobs-request-uri-nextToken"></a>
A token to get the next page of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListAdvancedPromptOptimizationJobs_RequestSyntax) **   <a name="bedrock-ListAdvancedPromptOptimizationJobs-request-uri-sortBy"></a>
The field to sort the results by.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListAdvancedPromptOptimizationJobs_RequestSyntax) **   <a name="bedrock-ListAdvancedPromptOptimizationJobs-request-uri-sortOrder"></a>
The sort order for the results.  
Valid Values: `Ascending | Descending` 

## Request Body
<a name="API_ListAdvancedPromptOptimizationJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAdvancedPromptOptimizationJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobSummaries": [ 
      { 
         "creationTime": "string",
         "jobArn": "string",
         "jobName": "string",
         "jobStatus": "string",
         "lastModifiedTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAdvancedPromptOptimizationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobSummaries](#API_ListAdvancedPromptOptimizationJobs_ResponseSyntax) **   <a name="bedrock-ListAdvancedPromptOptimizationJobs-response-jobSummaries"></a>
A list of advanced prompt optimization job summaries.  
Type: Array of [AdvancedPromptOptimizationJobSummary](API_AdvancedPromptOptimizationJobSummary.md) objects

 ** [nextToken](#API_ListAdvancedPromptOptimizationJobs_ResponseSyntax) **   <a name="bedrock-ListAdvancedPromptOptimizationJobs-response-nextToken"></a>
A token to get the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListAdvancedPromptOptimizationJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_ListAdvancedPromptOptimizationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListAdvancedPromptOptimizationJobs) 