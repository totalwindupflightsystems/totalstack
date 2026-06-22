---
id: "@specs/aws/emr/docs/API_NotebookExecutionSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NotebookExecutionSummary"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# NotebookExecutionSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_NotebookExecutionSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NotebookExecutionSummary
<a name="API_NotebookExecutionSummary"></a>

Details for a notebook execution. The details include information such as the unique ID and status of the notebook execution.

## Contents
<a name="API_NotebookExecutionSummary_Contents"></a>

 ** EditorId **   <a name="EMR-Type-NotebookExecutionSummary-EditorId"></a>
The unique identifier of the editor associated with the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** EndTime **   <a name="EMR-Type-NotebookExecutionSummary-EndTime"></a>
The timestamp when notebook execution started.  
Type: Timestamp  
Required: No

 ** ExecutionEngineId **   <a name="EMR-Type-NotebookExecutionSummary-ExecutionEngineId"></a>
The unique ID of the execution engine for the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookExecutionId **   <a name="EMR-Type-NotebookExecutionSummary-NotebookExecutionId"></a>
The unique identifier of the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookExecutionName **   <a name="EMR-Type-NotebookExecutionSummary-NotebookExecutionName"></a>
The name of the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** NotebookS3Location **   <a name="EMR-Type-NotebookExecutionSummary-NotebookS3Location"></a>
The Amazon S3 location that stores the notebook execution input.  
Type: [NotebookS3LocationForOutput](API_NotebookS3LocationForOutput.md) object  
Required: No

 ** StartTime **   <a name="EMR-Type-NotebookExecutionSummary-StartTime"></a>
The timestamp when notebook execution started.  
Type: Timestamp  
Required: No

 ** Status **   <a name="EMR-Type-NotebookExecutionSummary-Status"></a>
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

## See Also
<a name="API_NotebookExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/NotebookExecutionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/NotebookExecutionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/NotebookExecutionSummary) 