---
id: "@specs/aws/bedrock-agent/docs/API_BatchDeleteAdvancedPromptOptimizationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDeleteAdvancedPromptOptimizationJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# BatchDeleteAdvancedPromptOptimizationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_BatchDeleteAdvancedPromptOptimizationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDeleteAdvancedPromptOptimizationJob
<a name="API_BatchDeleteAdvancedPromptOptimizationJob"></a>

Deletes one or more advanced prompt optimization jobs.

## Request Syntax
<a name="API_BatchDeleteAdvancedPromptOptimizationJob_RequestSyntax"></a>

```
POST /advanced-prompt-optimization-job/batch-delete HTTP/1.1
Content-type: application/json

{
   "jobIdentifiers": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteAdvancedPromptOptimizationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeleteAdvancedPromptOptimizationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobIdentifiers](#API_BatchDeleteAdvancedPromptOptimizationJob_RequestSyntax) **   <a name="bedrock-BatchDeleteAdvancedPromptOptimizationJob-request-jobIdentifiers"></a>
A list of ARNs or IDs of the advanced prompt optimization jobs to delete.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `((arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:advanced-prompt-optimization-job/)?[a-z0-9]{12})`   
Required: Yes

## Response Syntax
<a name="API_BatchDeleteAdvancedPromptOptimizationJob_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "advancedPromptOptimizationJobs": [ 
      { 
         "jobIdentifier": "string",
         "jobStatus": "string"
      }
   ],
   "errors": [ 
      { 
         "code": "string",
         "jobIdentifier": "string",
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteAdvancedPromptOptimizationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [advancedPromptOptimizationJobs](#API_BatchDeleteAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-BatchDeleteAdvancedPromptOptimizationJob-response-advancedPromptOptimizationJobs"></a>
A list of jobs that were successfully deleted.  
Type: Array of [BatchDeleteAdvancedPromptOptimizationJobItem](API_BatchDeleteAdvancedPromptOptimizationJobItem.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [errors](#API_BatchDeleteAdvancedPromptOptimizationJob_ResponseSyntax) **   <a name="bedrock-BatchDeleteAdvancedPromptOptimizationJob-response-errors"></a>
A list of errors for jobs that could not be deleted.  
Type: Array of [BatchDeleteAdvancedPromptOptimizationJobError](API_BatchDeleteAdvancedPromptOptimizationJobError.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_BatchDeleteAdvancedPromptOptimizationJob_Errors"></a>

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
<a name="API_BatchDeleteAdvancedPromptOptimizationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/BatchDeleteAdvancedPromptOptimizationJob) 