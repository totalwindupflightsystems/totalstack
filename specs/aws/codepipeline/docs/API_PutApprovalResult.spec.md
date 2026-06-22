---
id: "@specs/aws/codepipeline/docs/API_PutApprovalResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutApprovalResult"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# PutApprovalResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_PutApprovalResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutApprovalResult
<a name="API_PutApprovalResult"></a>

Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.

## Request Syntax
<a name="API_PutApprovalResult_RequestSyntax"></a>

```
{
   "actionName": "{{string}}",
   "pipelineName": "{{string}}",
   "result": { 
      "status": "{{string}}",
      "summary": "{{string}}"
   },
   "stageName": "{{string}}",
   "token": "{{string}}"
}
```

## Request Parameters
<a name="API_PutApprovalResult_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actionName](#API_PutApprovalResult_RequestSyntax) **   <a name="CodePipeline-PutApprovalResult-request-actionName"></a>
The name of the action for which approval is requested.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [pipelineName](#API_PutApprovalResult_RequestSyntax) **   <a name="CodePipeline-PutApprovalResult-request-pipelineName"></a>
The name of the pipeline that contains the action.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [result](#API_PutApprovalResult_RequestSyntax) **   <a name="CodePipeline-PutApprovalResult-request-result"></a>
Represents information about the result of the approval request.  
Type: [ApprovalResult](API_ApprovalResult.md) object  
Required: Yes

 ** [stageName](#API_PutApprovalResult_RequestSyntax) **   <a name="CodePipeline-PutApprovalResult-request-stageName"></a>
The name of the stage that contains the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

 ** [token](#API_PutApprovalResult_RequestSyntax) **   <a name="CodePipeline-PutApprovalResult-request-token"></a>
The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the [GetPipelineState](API_GetPipelineState.md) action. It is used to validate that the approval request corresponding to this token is still valid.  
For a pipeline where the execution mode is set to PARALLEL, the token required to approve/reject an approval request as detailed above is not available. Instead, use the `externalExecutionId` in the response output from the [ListActionExecutions](API_ListActionExecutions.md) action as the token in the approval request.
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

## Response Syntax
<a name="API_PutApprovalResult_ResponseSyntax"></a>

```
{
   "approvedAt": number
}
```

## Response Elements
<a name="API_PutApprovalResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvedAt](#API_PutApprovalResult_ResponseSyntax) **   <a name="CodePipeline-PutApprovalResult-response-approvedAt"></a>
The timestamp showing when the approval or rejection was submitted.  
Type: Timestamp

## Errors
<a name="API_PutApprovalResult_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActionNotFoundException **   
The specified action cannot be found.  
HTTP Status Code: 400

 ** ApprovalAlreadyCompletedException **   
The approval action has already been approved or rejected.  
HTTP Status Code: 400

 ** InvalidApprovalTokenException **   
The approval request already received a response or has expired.  
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
<a name="API_PutApprovalResult_Examples"></a>

### Example
<a name="API_PutApprovalResult_Example_1"></a>

This example illustrates one usage of PutApprovalResult.

#### Sample Request
<a name="API_PutApprovalResult_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 173
X-Amz-Target: CodePipeline_20150709.PutApprovalResult
X-Amz-Date: 20151030T230047Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151030/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "actionName": "MyApprovalAction",
   "pipelineName": "MyFirstPipeline",
   "result": { 
      "status": "Approved",
      "summary": "Latest changes meet the bar. Ship it!"
   },
   "stageName": "MyApprovalStage",
   "token": "1a2b3c4d-573f-4ea7-a67E-XAMPLETOKEN"
}
```

#### Sample Response
<a name="API_PutApprovalResult_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 24

{
   "approvedAt": 1466137312.204
}
```

## See Also
<a name="API_PutApprovalResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/PutApprovalResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/PutApprovalResult) 