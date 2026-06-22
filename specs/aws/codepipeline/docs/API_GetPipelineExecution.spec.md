---
id: "@specs/aws/codepipeline/docs/API_GetPipelineExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPipelineExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GetPipelineExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GetPipelineExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPipelineExecution
<a name="API_GetPipelineExecution"></a>

Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.

## Request Syntax
<a name="API_GetPipelineExecution_RequestSyntax"></a>

```
{
   "pipelineExecutionId": "{{string}}",
   "pipelineName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPipelineExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineExecutionId](#API_GetPipelineExecution_RequestSyntax) **   <a name="CodePipeline-GetPipelineExecution-request-pipelineExecutionId"></a>
The ID of the pipeline execution about which you want to get execution details.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** [pipelineName](#API_GetPipelineExecution_RequestSyntax) **   <a name="CodePipeline-GetPipelineExecution-request-pipelineName"></a>
The name of the pipeline about which you want to get execution details.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: Yes

## Response Syntax
<a name="API_GetPipelineExecution_ResponseSyntax"></a>

```
{
   "pipelineExecution": { 
      "artifactRevisions": [ 
         { 
            "created": number,
            "name": "string",
            "revisionChangeIdentifier": "string",
            "revisionId": "string",
            "revisionSummary": "string",
            "revisionUrl": "string"
         }
      ],
      "executionMode": "string",
      "executionType": "string",
      "pipelineExecutionId": "string",
      "pipelineName": "string",
      "pipelineVersion": number,
      "rollbackMetadata": { 
         "rollbackTargetPipelineExecutionId": "string"
      },
      "status": "string",
      "statusSummary": "string",
      "trigger": { 
         "triggerDetail": "string",
         "triggerType": "string"
      },
      "variables": [ 
         { 
            "name": "string",
            "resolvedValue": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetPipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [pipelineExecution](#API_GetPipelineExecution_ResponseSyntax) **   <a name="CodePipeline-GetPipelineExecution-response-pipelineExecution"></a>
Represents information about the execution of a pipeline.  
Type: [PipelineExecution](API_PipelineExecution.md) object

## Errors
<a name="API_GetPipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** PipelineExecutionNotFoundException **   
The pipeline execution was specified in an invalid format or cannot be found, or an execution ID does not belong to the specified pipeline.   
HTTP Status Code: 400

 ** PipelineNotFoundException **   
The pipeline was specified in an invalid format or cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_GetPipelineExecution_Examples"></a>

### Example
<a name="API_GetPipelineExecution_Example_1"></a>

This example illustrates one usage of GetPipelineExecution.

#### Sample Request
<a name="API_GetPipelineExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 27
X-Amz-Target: CodePipeline_20150709.GetPipelineExecution
X-Amz-Date: 20160707T171559Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
   "pipelineExecutionId": "42ee4d10-e4de-a37c-82b7-36c11EXAMPLE",
   "pipelineName": "MyFirstPipeline"
}
```

#### Sample Response
<a name="API_GetPipelineExecution_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 318

{
    "pipelineExecution": {
        "artifactRevisions": [
            {
                "created": 1427298837.7689769,
		"name": "MyApp",
                "revisionChangeIdentifier": "1427298921.3976923",
                "revisionId": "7636d59f3c461cEXAMPLE8417dbc6371",
                "revisionSummary": "Updating the application for feature 12-4820",
                "revisionUrl": "https://api.github.com/repos/anycompany/MyApp/git/commits/7636d59f3c461cEXAMPLE8417dbc6371"
            }
        ],
        "pipelineExecutionId": "3137f7cb-7cf7-039j-s83l-d7eu3EXAMPLE",
        "pipelineName": "MyFirstPipeline",
        "pipelineVersion": 2,
        "status": "Succeeded"
    }
}
```

## See Also
<a name="API_GetPipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/GetPipelineExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GetPipelineExecution) 