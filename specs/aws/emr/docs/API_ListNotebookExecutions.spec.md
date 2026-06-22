---
id: "@specs/aws/emr/docs/API_ListNotebookExecutions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListNotebookExecutions"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListNotebookExecutions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListNotebookExecutions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListNotebookExecutions
<a name="API_ListNotebookExecutions"></a>

Provides summaries of all notebook executions. You can filter the list based on multiple criteria such as status, time range, and editor id. Returns a maximum of 50 notebook executions and a marker to track the paging of a longer notebook execution list across multiple `ListNotebookExecutions` calls.

## Request Syntax
<a name="API_ListNotebookExecutions_RequestSyntax"></a>

```
{
   "EditorId": "{{string}}",
   "ExecutionEngineId": "{{string}}",
   "From": {{number}},
   "Marker": "{{string}}",
   "Status": "{{string}}",
   "To": {{number}}
}
```

## Request Parameters
<a name="API_ListNotebookExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EditorId](#API_ListNotebookExecutions_RequestSyntax) **   <a name="EMR-ListNotebookExecutions-request-EditorId"></a>
The unique ID of the editor associated with the notebook execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [ExecutionEngineId](#API_ListNotebookExecutions_RequestSyntax) **   <a name="EMR-ListNotebookExecutions-request-ExecutionEngineId"></a>
The unique ID of the execution engine.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [From](#API_ListNotebookExecutions_RequestSyntax) **   <a name="EMR-ListNotebookExecutions-request-From"></a>
The beginning of time range filter for listing notebook executions. The default is the timestamp of 30 days ago.  
Type: Timestamp  
Required: No

 ** [Marker](#API_ListNotebookExecutions_RequestSyntax) **   <a name="EMR-ListNotebookExecutions-request-Marker"></a>
The pagination token, returned by a previous `ListNotebookExecutions` call, that indicates the start of the list for this `ListNotebookExecutions` call.  
Type: String  
Required: No

 ** [Status](#API_ListNotebookExecutions_RequestSyntax) **   <a name="EMR-ListNotebookExecutions-request-Status"></a>
The status filter for listing notebook executions.  
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

 ** [To](#API_ListNotebookExecutions_RequestSyntax) **   <a name="EMR-ListNotebookExecutions-request-To"></a>
The end of time range filter for listing notebook executions. The default is the current timestamp.  
Type: Timestamp  
Required: No

## Response Syntax
<a name="API_ListNotebookExecutions_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "NotebookExecutions": [ 
      { 
         "EditorId": "string",
         "EndTime": number,
         "ExecutionEngineId": "string",
         "NotebookExecutionId": "string",
         "NotebookExecutionName": "string",
         "NotebookS3Location": { 
            "Bucket": "string",
            "Key": "string"
         },
         "StartTime": number,
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotebookExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListNotebookExecutions_ResponseSyntax) **   <a name="EMR-ListNotebookExecutions-response-Marker"></a>
A pagination token that a subsequent `ListNotebookExecutions` can use to determine the next set of results to retrieve.  
Type: String

 ** [NotebookExecutions](#API_ListNotebookExecutions_ResponseSyntax) **   <a name="EMR-ListNotebookExecutions-response-NotebookExecutions"></a>
A list of notebook executions.  
Type: Array of [NotebookExecutionSummary](API_NotebookExecutionSummary.md) objects

## Errors
<a name="API_ListNotebookExecutions_Errors"></a>

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
<a name="API_ListNotebookExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListNotebookExecutions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListNotebookExecutions) 