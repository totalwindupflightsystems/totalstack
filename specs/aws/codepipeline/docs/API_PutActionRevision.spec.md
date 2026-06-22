---
id: "@specs/aws/codepipeline/docs/API_PutActionRevision"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutActionRevision"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PutActionRevision

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PutActionRevision
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutActionRevision
<a name="API_PutActionRevision"></a>

Provides information to CodePipeline about new revisions to a source.

## Request Syntax
<a name="API_PutActionRevision_RequestSyntax"></a>

```
{
   "actionName": "{{string}}",
   "actionRevision": { 
      "created": {{number}},
      "revisionChangeId": "{{string}}",
      "revisionId": "{{string}}"
   },
   "pipelineName": "{{string}}",
   "stageName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutActionRevision_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actionName](#API_PutActionRevision_RequestSyntax) **   <a name="CodePipeline-PutActionRevision-request-actionName"></a>
The name of the action that processes the revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [actionRevision](#API_PutActionRevision_RequestSyntax) **   <a name="CodePipeline-PutActionRevision-request-actionRevision"></a>
Represents information about the version (or revision) of an action.  
Type: [ActionRevision](API_ActionRevision.md) object  
Required: Yes

 ** [pipelineName](#API_PutActionRevision_RequestSyntax) **   <a name="CodePipeline-PutActionRevision-request-pipelineName"></a>
The name of the pipeline that starts processing the revision to the source.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [stageName](#API_PutActionRevision_RequestSyntax) **   <a name="CodePipeline-PutActionRevision-request-stageName"></a>
The name of the stage that contains the action that acts on the revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Syntax
<a name="API_PutActionRevision_ResponseSyntax"></a>

```
{
   "newRevision": boolean,
   "pipelineExecutionId": "string"
}
```

## Response Elements
<a name="API_PutActionRevision_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [newRevision](#API_PutActionRevision_ResponseSyntax) **   <a name="CodePipeline-PutActionRevision-response-newRevision"></a>
Indicates whether the artifact revision was previously used in an execution of the specified pipeline.  
Type: Boolean

 ** [pipelineExecutionId](#API_PutActionRevision_ResponseSyntax) **   <a name="CodePipeline-PutActionRevision-response-pipelineExecutionId"></a>
The ID of the current workflow state of the pipeline.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors
<a name="API_PutActionRevision_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActionNotFoundException **   
The specified action cannot be found.  
HTTP Status Code: 400

 ** ConcurrentPipelineExecutionsLimitExceededException **   
The pipeline has reached the limit for concurrent pipeline executions.  
HTTP Status Code: 400

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
<a name="API_PutActionRevision_Examples"></a>

### Example
<a name="API_PutActionRevision_Example_1"></a>

This example illustrates one usage of PutActionRevision.

#### Sample Request
<a name="API_PutActionRevision_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 173
X-Amz-Target: CodePipeline_20150709.PutActionRevision
X-Amz-Date: 20151030T230047Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151030/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "actionName": "Source",
   "actionRevision": { 
      "created": 1446726163.571,
	  "revisionChangeId": "3fdd7b9196697a096d5af1d649e26a4a",
      "revisionId": "HYGp7zmwbCPPwo234xsCEM7d6ToeAqIl"
   },
   "pipelineName": "MyFirstPipeline",
   "stageName": "Staging"
}
```

#### Sample Response
<a name="API_PutActionRevision_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 1830

{
   "newRevision": true,
   "pipelineExecutionId": "42ee4d10-e4de-a37c-82b7-36c11EXAMPLE"
}
```

## See Also
<a name="API_PutActionRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/PutActionRevision) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PutActionRevision) 