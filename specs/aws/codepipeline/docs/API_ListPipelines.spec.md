---
id: "@specs/aws/codepipeline/docs/API_ListPipelines"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListPipelines"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListPipelines

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListPipelines
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListPipelines
<a name="API_ListPipelines"></a>

Gets a summary of all of the pipelines associated with your account.

## Request Syntax
<a name="API_ListPipelines_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelines_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPipelines_RequestSyntax) **   <a name="CodePipeline-ListPipelines-request-maxResults"></a>
The maximum number of pipelines to return in a single call. To retrieve the remaining pipelines, make another call with the returned nextToken value. The minimum value you can specify is 1. The maximum accepted value is 1000.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [nextToken](#API_ListPipelines_RequestSyntax) **   <a name="CodePipeline-ListPipelines-request-nextToken"></a>
An identifier that was returned from the previous list pipelines call. It can be used to return the next set of pipelines in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## Response Syntax
<a name="API_ListPipelines_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "pipelines": [ 
      { 
         "created": number,
         "executionMode": "string",
         "name": "string",
         "pipelineType": "string",
         "updated": number,
         "version": number
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPipelines_ResponseSyntax) **   <a name="CodePipeline-ListPipelines-response-nextToken"></a>
If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list pipelines call to return the next set of pipelines in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [pipelines](#API_ListPipelines_ResponseSyntax) **   <a name="CodePipeline-ListPipelines-response-pipelines"></a>
The list of pipelines.  
Type: Array of [PipelineSummary](API_PipelineSummary.md) objects

## Errors
<a name="API_ListPipelines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **   
The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_ListPipelines_Examples"></a>

### Example
<a name="API_ListPipelines_Example_1"></a>

This example illustrates one usage of ListPipelines.

#### Sample Request
<a name="API_ListPipelines_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: CodePipeline_20150709.ListPipelines
X-Amz-Date: 20160707T160211Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{}
```

#### Sample Response
<a name="API_ListPipelines_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 668

{
    "pipelines": [
        {
            "updated": 1444681408.094,
            "version": 1,
            "name": "MyFirstPipeline",
            "created": 1444681408.094
        },
        {
            "updated": 1443048299.639,
            "version": 3,
            "name": "MySecondPipeline",
            "created": 1443046290.003
        }
    ]
}
```

## See Also
<a name="API_ListPipelines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListPipelines) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListPipelines) 