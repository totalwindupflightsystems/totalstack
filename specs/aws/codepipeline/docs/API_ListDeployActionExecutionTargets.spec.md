---
id: "@specs/aws/codepipeline/docs/API_ListDeployActionExecutionTargets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDeployActionExecutionTargets"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListDeployActionExecutionTargets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListDeployActionExecutionTargets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDeployActionExecutionTargets
<a name="API_ListDeployActionExecutionTargets"></a>

Lists the targets for the deploy action.

## Request Syntax
<a name="API_ListDeployActionExecutionTargets_RequestSyntax"></a>

```
{
   "actionExecutionId": "{{string}}",
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "pipelineName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDeployActionExecutionTargets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actionExecutionId](#API_ListDeployActionExecutionTargets_RequestSyntax) **   <a name="CodePipeline-ListDeployActionExecutionTargets-request-actionExecutionId"></a>
The execution ID for the deploy action.  
Type: String  
Required: Yes

 ** [filters](#API_ListDeployActionExecutionTargets_RequestSyntax) **   <a name="CodePipeline-ListDeployActionExecutionTargets-request-filters"></a>
Filters the targets for a specified deploy action.  
Type: Array of [TargetFilter](API_TargetFilter.md) objects  
Required: No

 ** [maxResults](#API_ListDeployActionExecutionTargets_RequestSyntax) **   <a name="CodePipeline-ListDeployActionExecutionTargets-request-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListDeployActionExecutionTargets_RequestSyntax) **   <a name="CodePipeline-ListDeployActionExecutionTargets-request-nextToken"></a>
An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [pipelineName](#API_ListDeployActionExecutionTargets_RequestSyntax) **   <a name="CodePipeline-ListDeployActionExecutionTargets-request-pipelineName"></a>
The name of the pipeline with the deploy action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

## Response Syntax
<a name="API_ListDeployActionExecutionTargets_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "targets": [ 
      { 
         "endTime": number,
         "events": [ 
            { 
               "context": { 
                  "message": "string",
                  "ssmCommandId": "string"
               },
               "endTime": number,
               "name": "string",
               "startTime": number,
               "status": "string"
            }
         ],
         "startTime": number,
         "status": "string",
         "targetId": "string",
         "targetType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDeployActionExecutionTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDeployActionExecutionTargets_ResponseSyntax) **   <a name="CodePipeline-ListDeployActionExecutionTargets-response-nextToken"></a>
An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [targets](#API_ListDeployActionExecutionTargets_ResponseSyntax) **   <a name="CodePipeline-ListDeployActionExecutionTargets-response-targets"></a>
The targets for the deploy action.  
Type: Array of [DeployActionExecutionTarget](API_DeployActionExecutionTarget.md) objects

## Errors
<a name="API_ListDeployActionExecutionTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActionExecutionNotFoundException **   
The action execution was not found.  
HTTP Status Code: 400

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
<a name="API_ListDeployActionExecutionTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListDeployActionExecutionTargets) 