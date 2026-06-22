---
id: "@specs/aws/emr/docs/API_NotebookExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NotebookExecution"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# NotebookExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_NotebookExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NotebookExecution
<a name="API_NotebookExecution"></a>

A notebook execution. An execution is a specific instance that an Amazon EMR Notebook is run using the `StartNotebookExecution` action.

## Contents
<a name="API_NotebookExecution_Contents"></a>

 ** Arn **   <a name="EMR-Type-NotebookExecution-Arn"></a>
The Amazon Resource Name (ARN) of the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EditorId **   <a name="EMR-Type-NotebookExecution-EditorId"></a>
The unique identifier of the Amazon EMR Notebook that is used for the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EndTime **   <a name="EMR-Type-NotebookExecution-EndTime"></a>
The timestamp when notebook execution ended.  
Type: Timestamp  
Required: No

 ** EnvironmentVariables **   <a name="EMR-Type-NotebookExecution-EnvironmentVariables"></a>
The environment variables associated with the notebook execution.  
Type: String to string map  
Key Length Constraints: Minimum length of 0. Maximum length of 256.  
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 10280.  
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ExecutionEngine **   <a name="EMR-Type-NotebookExecution-ExecutionEngine"></a>
The execution engine, such as an Amazon EMR cluster, used to run the Amazon EMR notebook and perform the notebook execution.  
Type: [ExecutionEngineConfig](API_ExecutionEngineConfig.md) object  
Required: No

 ** LastStateChangeReason **   <a name="EMR-Type-NotebookExecution-LastStateChangeReason"></a>
The reason for the latest status change of the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookExecutionId **   <a name="EMR-Type-NotebookExecution-NotebookExecutionId"></a>
The unique identifier of a notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookExecutionName **   <a name="EMR-Type-NotebookExecution-NotebookExecutionName"></a>
A name for the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookInstanceSecurityGroupId **   <a name="EMR-Type-NotebookExecution-NotebookInstanceSecurityGroupId"></a>
The unique identifier of the Amazon EC2 security group associated with the Amazon EMR Notebook instance. For more information see [Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html) in the *Amazon EMR Management Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookParams **   <a name="EMR-Type-NotebookExecution-NotebookParams"></a>
Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookS3Location **   <a name="EMR-Type-NotebookExecution-NotebookS3Location"></a>
The Amazon S3 location that stores the notebook execution input.  
Type: [NotebookS3LocationForOutput](API_NotebookS3LocationForOutput.md) object  
Required: No

 ** OutputNotebookFormat **   <a name="EMR-Type-NotebookExecution-OutputNotebookFormat"></a>
The output format for the notebook execution.  
Type: String  
Valid Values: `HTML`   
Required: No

 ** OutputNotebookS3Location **   <a name="EMR-Type-NotebookExecution-OutputNotebookS3Location"></a>
The Amazon S3 location for the notebook execution output.  
Type: [OutputNotebookS3LocationForOutput](API_OutputNotebookS3LocationForOutput.md) object  
Required: No

 ** OutputNotebookURI **   <a name="EMR-Type-NotebookExecution-OutputNotebookURI"></a>
The location of the notebook execution's output file in Amazon S3.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** StartTime **   <a name="EMR-Type-NotebookExecution-StartTime"></a>
The timestamp when notebook execution started.  
Type: Timestamp  
Required: No

 ** Status **   <a name="EMR-Type-NotebookExecution-Status"></a>
The status of the notebook execution.  
+  `START_PENDING` indicates that the cluster has received the execution request but execution has not begun.
+  `STARTING` indicates that the execution is starting on the cluster.
+  `RUNNING` indicates that the execution is being processed by the cluster.
+  `FINISHING` indicates that execution processing is in the final stages.
+  `FINISHED` indicates that the execution has completed without error.
+  `FAILING` indicates that the execution is failing and will not finish successfully.
+  `FAILED` indicates that the execution failed.
+  `STOP_PENDING` indicates that the cluster has received a `StopNotebookExecution` request and the stop is pending.
+  `STOPPING` indicates that the cluster is in the process of stopping the execution as a result of a `StopNotebookExecution` request.
+  `STOPPED` indicates that the execution stopped because of a `StopNotebookExecution` request.
Type: String  
Valid Values: `START_PENDING | STARTING | RUNNING | FINISHING | FINISHED | FAILING | FAILED | STOP_PENDING | STOPPING | STOPPED`   
Required: No

 ** Tags **   <a name="EMR-Type-NotebookExecution-Tags"></a>
A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_NotebookExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/NotebookExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/NotebookExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/NotebookExecution) 