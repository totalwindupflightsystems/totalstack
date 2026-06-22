---
id: "@specs/aws/codepipeline/docs/API_RetryStageExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RetryStageExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RetryStageExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RetryStageExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RetryStageExecution
<a name="API_RetryStageExecution"></a>

You can retry a stage that has failed without having to run a pipeline again from the beginning. You do this by either retrying the failed actions in a stage or by retrying all actions in the stage starting from the first action in the stage. When you retry the failed actions in a stage, all actions that are still in progress continue working, and failed actions are triggered again. When you retry a failed stage from the first action in the stage, the stage cannot have any actions in progress. Before a stage can be retried, it must either have all actions failed or some actions failed and some succeeded.

## Request Syntax
<a name="API_RetryStageExecution_RequestSyntax"></a>

```
{
   "pipelineExecutionId": "{{string}}",
   "pipelineName": "{{string}}",
   "retryMode": "{{string}}",
   "stageName": "{{string}}"
}
```

## Request Parameters
<a name="API_RetryStageExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineExecutionId](#API_RetryStageExecution_RequestSyntax) **   <a name="CodePipeline-RetryStageExecution-request-pipelineExecutionId"></a>
The ID of the pipeline execution in the failed stage to be retried. Use the [GetPipelineState](API_GetPipelineState.md) action to retrieve the current pipelineExecutionId of the failed stage  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** [pipelineName](#API_RetryStageExecution_RequestSyntax) **   <a name="CodePipeline-RetryStageExecution-request-pipelineName"></a>
The name of the pipeline that contains the failed stage.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [retryMode](#API_RetryStageExecution_RequestSyntax) **   <a name="CodePipeline-RetryStageExecution-request-retryMode"></a>
The scope of the retry attempt.  
Type: String  
Valid Values: `FAILED_ACTIONS | ALL_ACTIONS`   
Required: Yes

 ** [stageName](#API_RetryStageExecution_RequestSyntax) **   <a name="CodePipeline-RetryStageExecution-request-stageName"></a>
The name of the failed stage to be retried.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Syntax
<a name="API_RetryStageExecution_ResponseSyntax"></a>

```
{
   "pipelineExecutionId": "string"
}
```

## Response Elements
<a name="API_RetryStageExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineExecutionId](#API_RetryStageExecution_ResponseSyntax) **   <a name="CodePipeline-RetryStageExecution-response-pipelineExecutionId"></a>
The ID of the current workflow execution in the failed stage.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors
<a name="API_RetryStageExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentPipelineExecutionsLimitExceededException **   
The pipeline has reached the limit for concurrent pipeline executions.  
HTTP Status Code: 400

 ** ConflictException **   
Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.  
HTTP Status Code: 400

 ** NotLatestPipelineExecutionException **   
The stage has failed in a later run of the pipeline and the `pipelineExecutionId` associated with the request is out of date.  
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** StageNotFoundException **   
The stage was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** StageNotRetryableException **   
Unable to retry. The pipeline structure or stage state might have changed while actions awaited retry, or the stage contains no failed actions.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_RetryStageExecution_Examples"></a>

### Example
<a name="API_RetryStageExecution_Example_1"></a>

This example illustrates one usage of RetryStageExecution.

#### Sample Request
<a name="API_RetryStageExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 173
X-Amz-Target: CodePipeline_20150709.RetryStageExecution
X-Amz-Date: 20151030T230047Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151030/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pipelineExecutionId": "3137f7cb-7cf7-EXAMPLE",
   "pipelineName": "MyFirstPipeline",
   "retryMode": "FAILED_ACTIONS",
   "stageName": "Staging"
}
```

#### Sample Response
<a name="API_RetryStageExecution_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 30

{
   "pipelineExecutionId": "3137f7cb-7cf7-EXAMPLE"
}
```

## See Also
<a name="API_RetryStageExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/RetryStageExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RetryStageExecution) 