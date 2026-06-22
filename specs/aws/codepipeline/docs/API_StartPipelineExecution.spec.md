---
id: "@specs/aws/codepipeline/docs/API_StartPipelineExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartPipelineExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# StartPipelineExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_StartPipelineExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartPipelineExecution
<a name="API_StartPipelineExecution"></a>

Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.

## Request Syntax
<a name="API_StartPipelineExecution_RequestSyntax"></a>

```
{
   "clientRequestToken": "{{string}}",
   "name": "{{string}}",
   "sourceRevisions": [ 
      { 
         "actionName": "{{string}}",
         "revisionType": "{{string}}",
         "revisionValue": "{{string}}"
      }
   ],
   "variables": [ 
      { 
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartPipelineExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_StartPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StartPipelineExecution-request-clientRequestToken"></a>
The system-generated unique ID used to identify a unique execution request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [name](#API_StartPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StartPipelineExecution-request-name"></a>
The name of the pipeline to start.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [sourceRevisions](#API_StartPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StartPipelineExecution-request-sourceRevisions"></a>
A list that allows you to specify, or override, the source revision for a pipeline execution that's being started. A source revision is the version with all the changes to your application code, or source artifact, for the pipeline execution.  
Type: Array of [SourceRevisionOverride](API_SourceRevisionOverride.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** [variables](#API_StartPipelineExecution_RequestSyntax) **   <a name="CodePipeline-StartPipelineExecution-request-variables"></a>
A list that overrides pipeline variables for a pipeline execution that's being started. Variable names must match `[A-Za-z0-9@\-_]+`, and the values can be anything except an empty string.  
Type: Array of [PipelineVariable](API_PipelineVariable.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_StartPipelineExecution_ResponseSyntax"></a>

```
{
   "pipelineExecutionId": "string"
}
```

## Response Elements
<a name="API_StartPipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineExecutionId](#API_StartPipelineExecution_ResponseSyntax) **   <a name="CodePipeline-StartPipelineExecution-response-pipelineExecutionId"></a>
The unique system-generated ID of the pipeline execution that was started.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors
<a name="API_StartPipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentPipelineExecutionsLimitExceededException **   
The pipeline has reached the limit for concurrent pipeline executions.  
HTTP Status Code: 400

 ** ConflictException **   
Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.  
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_StartPipelineExecution_Examples"></a>

### Example
<a name="API_StartPipelineExecution_Example_1"></a>

This example illustrates one usage of StartPipelineExecution.

#### Sample Request
<a name="API_StartPipelineExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 27
X-Amz-Target: CodePipeline_20150709.StartPipelineExecution
X-Amz-Date: 20160707T172713Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "name": "MyFirstPipeline"
}
```

#### Sample Response
<a name="API_StartPipelineExecution_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 62

{
  "pipelineExecutionId": "3137f7cb-7cf7-EXAMPLE"
}
```

## See Also
<a name="API_StartPipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/StartPipelineExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StartPipelineExecution) 