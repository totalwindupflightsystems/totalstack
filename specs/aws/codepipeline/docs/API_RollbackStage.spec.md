---
id: "@specs/aws/codepipeline/docs/API_RollbackStage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RollbackStage"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RollbackStage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RollbackStage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RollbackStage
<a name="API_RollbackStage"></a>

Rolls back a stage execution.

## Request Syntax
<a name="API_RollbackStage_RequestSyntax"></a>

```
{
   "pipelineName": "{{string}}",
   "stageName": "{{string}}",
   "targetPipelineExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_RollbackStage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineName](#API_RollbackStage_RequestSyntax) **   <a name="CodePipeline-RollbackStage-request-pipelineName"></a>
The name of the pipeline for which the stage will be rolled back.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [stageName](#API_RollbackStage_RequestSyntax) **   <a name="CodePipeline-RollbackStage-request-stageName"></a>
The name of the stage in the pipeline to be rolled back.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [targetPipelineExecutionId](#API_RollbackStage_RequestSyntax) **   <a name="CodePipeline-RollbackStage-request-targetPipelineExecutionId"></a>
The pipeline execution ID for the stage to be rolled back to.   
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

## Response Syntax
<a name="API_RollbackStage_ResponseSyntax"></a>

```
{
   "pipelineExecutionId": "string"
}
```

## Response Elements
<a name="API_RollbackStage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineExecutionId](#API_RollbackStage_ResponseSyntax) **   <a name="CodePipeline-RollbackStage-response-pipelineExecutionId"></a>
The execution ID of the pipeline execution for the stage that has been rolled back.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors
<a name="API_RollbackStage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.  
HTTP Status Code: 400

 ** PipelineExecutionNotFoundException **   
The pipeline execution was specified in an invalid format or cannot be found, or an execution ID does not belong to the specified pipeline.   
HTTP Status Code: 400

 ** PipelineExecutionOutdatedException **   
The specified pipeline execution is outdated and cannot be used as a target pipeline execution for rollback.  
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** StageNotFoundException **   
The stage was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** UnableToRollbackStageException **   
Unable to roll back the stage. The cause might be if the pipeline version has changed since the target pipeline execution was deployed, the stage is currently running, or an incorrect target pipeline execution ID was provided.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_RollbackStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/RollbackStage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RollbackStage) 