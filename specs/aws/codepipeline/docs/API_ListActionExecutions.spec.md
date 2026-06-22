---
id: "@specs/aws/codepipeline/docs/API_ListActionExecutions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListActionExecutions"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListActionExecutions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListActionExecutions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListActionExecutions
<a name="API_ListActionExecutions"></a>

Lists the action executions that have occurred in a pipeline.

## Request Syntax
<a name="API_ListActionExecutions_RequestSyntax"></a>

```
{
   "filter": { 
      "latestInPipelineExecution": { 
         "pipelineExecutionId": "{{string}}",
         "startTimeRange": "{{string}}"
      },
      "pipelineExecutionId": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pipelineName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListActionExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_ListActionExecutions_RequestSyntax) **   <a name="CodePipeline-ListActionExecutions-request-filter"></a>
Input information used to filter action execution history.  
Type: [ActionExecutionFilter](API_ActionExecutionFilter.md) object  
Required: No

 ** [maxResults](#API_ListActionExecutions_RequestSyntax) **   <a name="CodePipeline-ListActionExecutions-request-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Action execution history is retained for up to 12 months, based on action execution start times. Default value is 100.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListActionExecutions_RequestSyntax) **   <a name="CodePipeline-ListActionExecutions-request-nextToken"></a>
The token that was returned from the previous `ListActionExecutions` call, which can be used to return the next set of action executions in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [pipelineName](#API_ListActionExecutions_RequestSyntax) **   <a name="CodePipeline-ListActionExecutions-request-pipelineName"></a>
 The name of the pipeline for which you want to list action execution history.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Syntax
<a name="API_ListActionExecutions_ResponseSyntax"></a>

```
{
   "actionExecutionDetails": [ 
      { 
         "actionExecutionId": "string",
         "actionName": "string",
         "input": { 
            "actionTypeId": { 
               "category": "string",
               "owner": "string",
               "provider": "string",
               "version": "string"
            },
            "configuration": { 
               "string" : "string" 
            },
            "inputArtifacts": [ 
               { 
                  "name": "string",
                  "s3location": { 
                     "bucket": "string",
                     "key": "string"
                  }
               }
            ],
            "namespace": "string",
            "region": "string",
            "resolvedConfiguration": { 
               "string" : "string" 
            },
            "roleArn": "string"
         },
         "lastUpdateTime": number,
         "output": { 
            "executionResult": { 
               "errorDetails": { 
                  "code": "string",
                  "message": "string"
               },
               "externalExecutionId": "string",
               "externalExecutionSummary": "string",
               "externalExecutionUrl": "string",
               "logStreamARN": "string"
            },
            "outputArtifacts": [ 
               { 
                  "name": "string",
                  "s3location": { 
                     "bucket": "string",
                     "key": "string"
                  }
               }
            ],
            "outputVariables": { 
               "string" : "string" 
            }
         },
         "pipelineExecutionId": "string",
         "pipelineVersion": number,
         "stageName": "string",
         "startTime": number,
         "status": "string",
         "updatedBy": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListActionExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionExecutionDetails](#API_ListActionExecutions_ResponseSyntax) **   <a name="CodePipeline-ListActionExecutions-response-actionExecutionDetails"></a>
The details for a list of recent executions, such as action execution ID.  
Type: Array of [ActionExecutionDetail](API_ActionExecutionDetail.md) objects

 ** [nextToken](#API_ListActionExecutions_ResponseSyntax) **   <a name="CodePipeline-ListActionExecutions-response-nextToken"></a>
If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent `ListActionExecutions` call to return the next set of action executions in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListActionExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **   
The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.  
HTTP Status Code: 400

 ** PipelineExecutionNotFoundException **   
The pipeline execution was specified in an invalid format or cannot be found, or an execution ID does not belong to the specified pipeline.   
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_ListActionExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListActionExecutions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListActionExecutions) 