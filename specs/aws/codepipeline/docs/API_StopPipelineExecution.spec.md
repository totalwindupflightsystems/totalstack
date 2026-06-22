---
id: "@specs/aws/codepipeline/docs/API_StopPipelineExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StopPipelineExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# StopPipelineExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_StopPipelineExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StopPipelineExecution
<a name="API_StopPipelineExecution"></a>

Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a `Stopping` state. After all in-progress actions are completed or abandoned, the pipeline execution is in a `Stopped` state.

## Request Syntax
<a name="API_StopPipelineExecution_RequestSyntax"></a>

```
{
   "abandon": {{boolean}},
   "pipelineExecutionId": "{{string}}",
   "pipelineName": "{{string}}",
   "reason": "{{string}}"
}
```

## Request Parameters
<a name="API_StopPipelineExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [abandon](#API_StopPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StopPipelineExecution-request-abandon"></a>
Use this option to stop the pipeline execution by abandoning, rather than finishing, in-progress actions.  
This option can lead to failed or out-of-sequence tasks.
Type: Boolean  
Required: No

 ** [pipelineExecutionId](#API_StopPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StopPipelineExecution-request-pipelineExecutionId"></a>
The ID of the pipeline execution to be stopped in the current stage. Use the `GetPipelineState` action to retrieve the current pipelineExecutionId.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** [pipelineName](#API_StopPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StopPipelineExecution-request-pipelineName"></a>
The name of the pipeline to stop.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [reason](#API_StopPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StopPipelineExecution-request-reason"></a>
Use this option to enter comments, such as the reason the pipeline was stopped.  
Type: String  
Length Constraints: Maximum length of 200.  
Required: No

## Response Syntax
<a name="API_StopPipelineExecution_ResponseSyntax"></a>

```
{
   "pipelineExecutionId": "string"
}
```

## Response Elements
<a name="API_StopPipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineExecutionId](#API_StopPipelineExecution_ResponseSyntax) **   <a name="CodePipeline-StopPipelineExecution-response-pipelineExecutionId"></a>
The unique system-generated ID of the pipeline execution that was stopped.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors
<a name="API_StopPipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.  
HTTP Status Code: 400

 ** DuplicatedStopRequestException **   
The pipeline execution is already in a `Stopping` state. If you already chose to stop and wait, you cannot make that request again. You can choose to stop and abandon now, but be aware that this option can lead to failed tasks or out of sequence tasks. If you already chose to stop and abandon, you cannot make that request again.  
HTTP Status Code: 400

 ** PipelineExecutionNotStoppableException **   
Unable to stop the pipeline execution. The execution might already be in a `Stopped` state, or it might no longer be in progress.  
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_StopPipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/StopPipelineExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StopPipelineExecution) 