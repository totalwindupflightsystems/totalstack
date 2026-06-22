---
id: "@specs/aws/bedrock-agent/docs/API_ListEvaluationJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListEvaluationJobs"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListEvaluationJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListEvaluationJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListEvaluationJobs
<a name="API_ListEvaluationJobs"></a>

Lists all existing evaluation jobs.

## Request Syntax
<a name="API_ListEvaluationJobs_RequestSyntax"></a>

```
GET /evaluation-jobs?applicationTypeEquals={{applicationTypeEquals}}&creationTimeAfter={{creationTimeAfter}}&creationTimeBefore={{creationTimeBefore}}&maxResults={{maxResults}}&nameContains={{nameContains}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&statusEquals={{statusEquals}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEvaluationJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationTypeEquals](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-applicationTypeEquals"></a>
A filter to only list evaluation jobs that are either model evaluations or knowledge base evaluations.  
Valid Values: `ModelEvaluation | RagEvaluation` 

 ** [creationTimeAfter](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-creationTimeAfter"></a>
A filter to only list evaluation jobs created after a specified time.

 ** [creationTimeBefore](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-creationTimeBefore"></a>
A filter to only list evaluation jobs created before a specified time.

 ** [maxResults](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-maxResults"></a>
The maximum number of results to return.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nameContains](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-nameContains"></a>
A filter to only list evaluation jobs that contain a specified string in the job name.  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-z0-9](-*[a-z0-9]){0,62}` 

 ** [nextToken](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-nextToken"></a>
Continuation token from the previous response, for Amazon Bedrock to list the next set of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-sortBy"></a>
Specifies a creation time to sort the list of evaluation jobs by when they were created.  
Valid Values: `CreationTime` 

 ** [sortOrder](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-sortOrder"></a>
Specifies whether to sort the list of evaluation jobs by either ascending or descending order.  
Valid Values: `Ascending | Descending` 

 ** [statusEquals](#API_ListEvaluationJobs_RequestSyntax) **   <a name="bedrock-ListEvaluationJobs-request-uri-statusEquals"></a>
A filter to only list evaluation jobs that are of a certain status.  
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting` 

## Request Body
<a name="API_ListEvaluationJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEvaluationJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobSummaries": [ 
      { 
         "applicationType": "string",
         "creationTime": "string",
         "customMetricsEvaluatorModelIdentifiers": [ "string" ],
         "evaluationTaskTypes": [ "string" ],
         "evaluatorModelIdentifiers": [ "string" ],
         "inferenceConfigSummary": { 
            "modelConfigSummary": { 
               "bedrockModelIdentifiers": [ "string" ],
               "precomputedInferenceSourceIdentifiers": [ "string" ]
            },
            "ragConfigSummary": { 
               "bedrockKnowledgeBaseIdentifiers": [ "string" ],
               "precomputedRagSourceIdentifiers": [ "string" ]
            }
         },
         "jobArn": "string",
         "jobName": "string",
         "jobType": "string",
         "modelIdentifiers": [ "string" ],
         "ragIdentifiers": [ "string" ],
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEvaluationJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobSummaries](#API_ListEvaluationJobs_ResponseSyntax) **   <a name="bedrock-ListEvaluationJobs-response-jobSummaries"></a>
A list of summaries of the evaluation jobs.  
Type: Array of [EvaluationSummary](API_EvaluationSummary.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [nextToken](#API_ListEvaluationJobs_ResponseSyntax) **   <a name="bedrock-ListEvaluationJobs-response-nextToken"></a>
Continuation token from the previous response, for Amazon Bedrock to list the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListEvaluationJobs_Errors"></a>

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
<a name="API_ListEvaluationJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListEvaluationJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListEvaluationJobs) 