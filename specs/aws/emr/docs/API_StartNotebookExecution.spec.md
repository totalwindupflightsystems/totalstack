---
id: "@specs/aws/emr/docs/API_StartNotebookExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartNotebookExecution"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StartNotebookExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StartNotebookExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartNotebookExecution
<a name="API_StartNotebookExecution"></a>

Starts a notebook execution.

## Request Syntax
<a name="API_StartNotebookExecution_RequestSyntax"></a>

```
{
   "EditorId": "{{string}}",
   "EnvironmentVariables": { 
      "{{string}}" : "{{string}}" 
   },
   "ExecutionEngine": { 
      "ExecutionRoleArn": "{{string}}",
      "Id": "{{string}}",
      "MasterInstanceSecurityGroupId": "{{string}}",
      "Type": "{{string}}"
   },
   "NotebookExecutionName": "{{string}}",
   "NotebookInstanceSecurityGroupId": "{{string}}",
   "NotebookParams": "{{string}}",
   "NotebookS3Location": { 
      "Bucket": "{{string}}",
      "Key": "{{string}}"
   },
   "OutputNotebookFormat": "{{string}}",
   "OutputNotebookS3Location": { 
      "Bucket": "{{string}}",
      "Key": "{{string}}"
   },
   "RelativePath": "{{string}}",
   "ServiceRole": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartNotebookExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EditorId](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-EditorId"></a>
The unique identifier of the Amazon EMR Notebook to use for notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [EnvironmentVariables](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-EnvironmentVariables"></a>
The environment variables associated with the notebook execution.  
Type: String to string map  
Key Length Constraints: Minimum length of 0. Maximum length of 256.  
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 10280.  
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [ExecutionEngine](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-ExecutionEngine"></a>
Specifies the execution engine (cluster) that runs the notebook execution.  
Type: [ExecutionEngineConfig](API_ExecutionEngineConfig.md) object  
Required: Yes

 ** [NotebookExecutionName](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-NotebookExecutionName"></a>
An optional name for the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [NotebookInstanceSecurityGroupId](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-NotebookInstanceSecurityGroupId"></a>
The unique identifier of the Amazon EC2 security group to associate with the Amazon EMR Notebook for this notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [NotebookParams](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-NotebookParams"></a>
Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [NotebookS3Location](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-NotebookS3Location"></a>
The Amazon S3 location for the notebook execution input.  
Type: [NotebookS3LocationFromInput](API_NotebookS3LocationFromInput.md) object  
Required: No

 ** [OutputNotebookFormat](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-OutputNotebookFormat"></a>
The output format for the notebook execution.  
Type: String  
Valid Values: `HTML`   
Required: No

 ** [OutputNotebookS3Location](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-OutputNotebookS3Location"></a>
The Amazon S3 location for the notebook execution output.  
Type: [OutputNotebookS3LocationFromInput](API_OutputNotebookS3LocationFromInput.md) object  
Required: No

 ** [RelativePath](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-RelativePath"></a>
The path and file name of the notebook file for this execution, relative to the path specified for the Amazon EMR Notebook. For example, if you specify a path of `s3://MyBucket/MyNotebooks` when you create an Amazon EMR Notebook for a notebook with an ID of `e-ABCDEFGHIJK1234567890ABCD` (the `EditorID` of this request), and you specify a `RelativePath` of `my_notebook_executions/notebook_execution.ipynb`, the location of the file for the notebook execution is `s3://MyBucket/MyNotebooks/e-ABCDEFGHIJK1234567890ABCD/my_notebook_executions/notebook_execution.ipynb`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [ServiceRole](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-ServiceRole"></a>
The name or ARN of the IAM role that is used as the service role for Amazon EMR (the Amazon EMR role) for the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [Tags](#API_StartNotebookExecution_RequestSyntax) **   <a name="EMR-StartNotebookExecution-request-Tags"></a>
A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_StartNotebookExecution_ResponseSyntax"></a>

```
{
   "NotebookExecutionId": "string"
}
```

## Response Elements
<a name="API_StartNotebookExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NotebookExecutionId](#API_StartNotebookExecution_ResponseSyntax) **   <a name="EMR-StartNotebookExecution-response-NotebookExecutionId"></a>
The unique identifier of the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

## Errors
<a name="API_StartNotebookExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_StartNotebookExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/StartNotebookExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StartNotebookExecution) 