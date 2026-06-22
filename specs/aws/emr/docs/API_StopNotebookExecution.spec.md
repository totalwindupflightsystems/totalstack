---
id: "@specs/aws/emr/docs/API_StopNotebookExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StopNotebookExecution"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StopNotebookExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StopNotebookExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StopNotebookExecution
<a name="API_StopNotebookExecution"></a>

Stops a notebook execution.

## Request Syntax
<a name="API_StopNotebookExecution_RequestSyntax"></a>

```
{
   "NotebookExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopNotebookExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookExecutionId](#API_StopNotebookExecution_RequestSyntax) **   <a name="EMR-StopNotebookExecution-request-NotebookExecutionId"></a>
The unique identifier of the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Elements
<a name="API_StopNotebookExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopNotebookExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_StopNotebookExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/StopNotebookExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StopNotebookExecution) 