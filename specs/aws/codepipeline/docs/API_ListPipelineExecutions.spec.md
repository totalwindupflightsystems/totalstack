---
id: "@specs/aws/codepipeline/docs/API_ListPipelineExecutions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListPipelineExecutions"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListPipelineExecutions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListPipelineExecutions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListPipelineExecutions
<a name="API_ListPipelineExecutions"></a>

Gets a summary of the most recent executions for a pipeline.

**Note**  
When applying the filter for pipeline executions that have succeeded in the stage, the operation returns all executions in the current pipeline version beginning on February 1, 2024.

## Request Syntax
<a name="API_ListPipelineExecutions_RequestSyntax"></a>

```
{
   "filter": { 
      "succeededInStage": { 
         "stageName": "{{string}}"
      }
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pipelineName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelineExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_ListPipelineExecutions_RequestSyntax) **   <a name="CodePipeline-ListPipelineExecutions-request-filter"></a>
The pipeline execution to filter on.  
Type: [PipelineExecutionFilter](API_PipelineExecutionFilter.md) object  
Required: No

 ** [maxResults](#API_ListPipelineExecutions_RequestSyntax) **   <a name="CodePipeline-ListPipelineExecutions-request-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListPipelineExecutions_RequestSyntax) **   <a name="CodePipeline-ListPipelineExecutions-request-nextToken"></a>
The token that was returned from the previous `ListPipelineExecutions` call, which can be used to return the next set of pipeline executions in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [pipelineName](#API_ListPipelineExecutions_RequestSyntax) **   <a name="CodePipeline-ListPipelineExecutions-request-pipelineName"></a>
The name of the pipeline for which you want to get execution summary information.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Syntax
<a name="API_ListPipelineExecutions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "pipelineExecutionSummaries": [ 
      { 
         "executionMode": "string",
         "executionType": "string",
         "lastUpdateTime": number,
         "pipelineExecutionId": "string",
         "rollbackMetadata": { 
            "rollbackTargetPipelineExecutionId": "string"
         },
         "sourceRevisions": [ 
            { 
               "actionName": "string",
               "revisionId": "string",
               "revisionSummary": "string",
               "revisionUrl": "string"
            }
         ],
         "startTime": number,
         "status": "string",
         "statusSummary": "string",
         "stopTrigger": { 
            "reason": "string"
         },
         "trigger": { 
            "triggerDetail": "string",
            "triggerType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelineExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPipelineExecutions_ResponseSyntax) **   <a name="CodePipeline-ListPipelineExecutions-response-nextToken"></a>
A token that can be used in the next `ListPipelineExecutions` call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [pipelineExecutionSummaries](#API_ListPipelineExecutions_ResponseSyntax) **   <a name="CodePipeline-ListPipelineExecutions-response-pipelineExecutionSummaries"></a>
A list of executions in the history of a pipeline.  
Type: Array of [PipelineExecutionSummary](API_PipelineExecutionSummary.md) objects

## Errors
<a name="API_ListPipelineExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **   
The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.  
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_ListPipelineExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListPipelineExecutions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListPipelineExecutions) 