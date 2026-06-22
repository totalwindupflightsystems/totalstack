---
id: "@specs/aws/bedrock-agent/docs/API_BatchDeleteEvaluationJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDeleteEvaluationJob"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# BatchDeleteEvaluationJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_BatchDeleteEvaluationJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDeleteEvaluationJob
<a name="API_BatchDeleteEvaluationJob"></a>

Deletes a batch of evaluation jobs. An evaluation job can only be deleted if it has following status `FAILED`, `COMPLETED`, and `STOPPED`. You can request up to 25 model evaluation jobs be deleted in a single request.

## Request Syntax
<a name="API_BatchDeleteEvaluationJob_RequestSyntax"></a>

```
POST /evaluation-jobs/batch-delete HTTP/1.1
Content-type: application/json

{
   "jobIdentifiers": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteEvaluationJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeleteEvaluationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobIdentifiers](#API_BatchDeleteEvaluationJob_RequestSyntax) **   <a name="bedrock-BatchDeleteEvaluationJob-request-jobIdentifiers"></a>
A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Length Constraints: Minimum length of 0. Maximum length of 1011.  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:evaluation-job/[a-z0-9]{12})`   
Required: Yes

## Response Syntax
<a name="API_BatchDeleteEvaluationJob_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "errors": [ 
      { 
         "code": "string",
         "jobIdentifier": "string",
         "message": "string"
      }
   ],
   "evaluationJobs": [ 
      { 
         "jobIdentifier": "string",
         "jobStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteEvaluationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchDeleteEvaluationJob_ResponseSyntax) **   <a name="bedrock-BatchDeleteEvaluationJob-response-errors"></a>
A JSON object containing the HTTP status codes and the ARNs of evaluation jobs that failed to be deleted.  
Type: Array of [BatchDeleteEvaluationJobError](API_BatchDeleteEvaluationJobError.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [evaluationJobs](#API_BatchDeleteEvaluationJob_ResponseSyntax) **   <a name="bedrock-BatchDeleteEvaluationJob-response-evaluationJobs"></a>
The list of evaluation jobs for deletion.  
Type: Array of [BatchDeleteEvaluationJobItem](API_BatchDeleteEvaluationJobItem.md) objects

## Errors
<a name="API_BatchDeleteEvaluationJob_Errors"></a>

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

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteEvaluationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/BatchDeleteEvaluationJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/BatchDeleteEvaluationJob) 