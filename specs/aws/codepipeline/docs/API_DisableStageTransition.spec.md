---
id: "@specs/aws/codepipeline/docs/API_DisableStageTransition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisableStageTransition"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# DisableStageTransition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_DisableStageTransition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisableStageTransition
<a name="API_DisableStageTransition"></a>

Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.

## Request Syntax
<a name="API_DisableStageTransition_RequestSyntax"></a>

```
{
   "pipelineName": "{{string}}",
   "reason": "{{string}}",
   "stageName": "{{string}}",
   "transitionType": "{{string}}"
}
```

## Request Parameters
<a name="API_DisableStageTransition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineName](#API_DisableStageTransition_RequestSyntax) **   <a name="CodePipeline-DisableStageTransition-request-pipelineName"></a>
The name of the pipeline in which you want to disable the flow of artifacts from one stage to another.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [reason](#API_DisableStageTransition_RequestSyntax) **   <a name="CodePipeline-DisableStageTransition-request-reason"></a>
The reason given to the user that a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Pattern: `[a-zA-Z0-9!@ \(\)\.\*\?\-]+`   
Required: Yes

 ** [stageName](#API_DisableStageTransition_RequestSyntax) **   <a name="CodePipeline-DisableStageTransition-request-stageName"></a>
The name of the stage where you want to disable the inbound or outbound transition of artifacts.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [transitionType](#API_DisableStageTransition_RequestSyntax) **   <a name="CodePipeline-DisableStageTransition-request-transitionType"></a>
Specifies whether artifacts are prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they have been processed by the actions in that stage (outbound).  
Type: String  
Valid Values: `Inbound | Outbound`   
Required: Yes

## Response Elements
<a name="API_DisableStageTransition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisableStageTransition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** StageNotFoundException **   
The stage was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_DisableStageTransition_Examples"></a>

### Example
<a name="API_DisableStageTransition_Example_1"></a>

This example illustrates one usage of DisableStageTransition.

#### Sample Request
<a name="API_DisableStageTransition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 108
X-Amz-Target: CodePipeline_20150709.DisableStageTransition
X-Amz-Date: 20160707T182043Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "reason": "An example reason",
  "pipelineName": "MyFirstPipeline",
  "stageName": "Staging",
  "transitionType": "Inbound"
}
```

#### Sample Response
<a name="API_DisableStageTransition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 0
```

## See Also
<a name="API_DisableStageTransition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/DisableStageTransition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/DisableStageTransition) 