---
id: "@specs/aws/codepipeline/docs/API_ListRuleExecutions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRuleExecutions"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListRuleExecutions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListRuleExecutions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRuleExecutions
<a name="API_ListRuleExecutions"></a>

Lists the rule executions that have occurred in a pipeline configured for conditions with rules.

## Request Syntax
<a name="API_ListRuleExecutions_RequestSyntax"></a>

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
<a name="API_ListRuleExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_ListRuleExecutions_RequestSyntax) **   <a name="CodePipeline-ListRuleExecutions-request-filter"></a>
Input information used to filter rule execution history.  
Type: [RuleExecutionFilter](API_RuleExecutionFilter.md) object  
Required: No

 ** [maxResults](#API_ListRuleExecutions_RequestSyntax) **   <a name="CodePipeline-ListRuleExecutions-request-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListRuleExecutions_RequestSyntax) **   <a name="CodePipeline-ListRuleExecutions-request-nextToken"></a>
The token that was returned from the previous `ListRuleExecutions` call, which can be used to return the next set of rule executions in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [pipelineName](#API_ListRuleExecutions_RequestSyntax) **   <a name="CodePipeline-ListRuleExecutions-request-pipelineName"></a>
The name of the pipeline for which you want to get execution summary information.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Syntax
<a name="API_ListRuleExecutions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "ruleExecutionDetails": [ 
      { 
         "input": { 
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
            "region": "string",
            "resolvedConfiguration": { 
               "string" : "string" 
            },
            "roleArn": "string",
            "ruleTypeId": { 
               "category": "string",
               "owner": "string",
               "provider": "string",
               "version": "string"
            }
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
               "externalExecutionUrl": "string"
            }
         },
         "pipelineExecutionId": "string",
         "pipelineVersion": number,
         "ruleExecutionId": "string",
         "ruleName": "string",
         "stageName": "string",
         "startTime": number,
         "status": "string",
         "updatedBy": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRuleExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRuleExecutions_ResponseSyntax) **   <a name="CodePipeline-ListRuleExecutions-response-nextToken"></a>
A token that can be used in the next `ListRuleExecutions` call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [ruleExecutionDetails](#API_ListRuleExecutions_ResponseSyntax) **   <a name="CodePipeline-ListRuleExecutions-response-ruleExecutionDetails"></a>
Details about the output for listing rule executions.  
Type: Array of [RuleExecutionDetail](API_RuleExecutionDetail.md) objects

## Errors
<a name="API_ListRuleExecutions_Errors"></a>

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
<a name="API_ListRuleExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListRuleExecutions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListRuleExecutions) 