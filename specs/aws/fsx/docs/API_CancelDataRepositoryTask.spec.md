---
id: "@specs/aws/fsx/docs/API_CancelDataRepositoryTask"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelDataRepositoryTask"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CancelDataRepositoryTask

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CancelDataRepositoryTask
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelDataRepositoryTask
<a name="API_CancelDataRepositoryTask"></a>

Cancels an existing Amazon FSx for Lustre data repository task if that task is in either the `PENDING` or `EXECUTING` state. When you cancel an export task, Amazon FSx does the following.
+ Any files that FSx has already exported are not reverted.
+ FSx continues to export any files that are in-flight when the cancel operation is received.
+ FSx does not export any files that have not yet been exported.

For a release task, Amazon FSx will stop releasing files upon cancellation. Any files that have already been released will remain in the released state.

## Request Syntax
<a name="API_CancelDataRepositoryTask_RequestSyntax"></a>

```
{
   "TaskId": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelDataRepositoryTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskId](#API_CancelDataRepositoryTask_RequestSyntax) **   <a name="FSx-CancelDataRepositoryTask-request-TaskId"></a>
Specifies the data repository task to cancel.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(task-[0-9a-f]{17,})$`   
Required: Yes

## Response Syntax
<a name="API_CancelDataRepositoryTask_ResponseSyntax"></a>

```
{
   "Lifecycle": "string",
   "TaskId": "string"
}
```

## Response Elements
<a name="API_CancelDataRepositoryTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Lifecycle](#API_CancelDataRepositoryTask_ResponseSyntax) **   <a name="FSx-CancelDataRepositoryTask-response-Lifecycle"></a>
The lifecycle status of the data repository task, as follows:  
+  `PENDING` - Amazon FSx has not started the task.
+  `EXECUTING` - Amazon FSx is processing the task.
+  `FAILED` - Amazon FSx was not able to complete the task. For example, there may be files the task failed to process. The [DataRepositoryTaskFailureDetails](API_DataRepositoryTaskFailureDetails.md) property provides more information about task failures.
+  `SUCCEEDED` - FSx completed the task successfully.
+  `CANCELED` - Amazon FSx canceled the task and it did not complete.
+  `CANCELING` - FSx is in process of canceling the task.
Type: String  
Valid Values: `PENDING | EXECUTING | FAILED | SUCCEEDED | CANCELED | CANCELING` 

 ** [TaskId](#API_CancelDataRepositoryTask_ResponseSyntax) **   <a name="FSx-CancelDataRepositoryTask-response-TaskId"></a>
The ID of the task being canceled.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(task-[0-9a-f]{17,})$` 

## Errors
<a name="API_CancelDataRepositoryTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** DataRepositoryTaskEnded **   
The data repository task could not be canceled because the task has already ended.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** DataRepositoryTaskNotFound **   
The data repository task or tasks you specified could not be found.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## Examples
<a name="API_CancelDataRepositoryTask_Examples"></a>

### Cancel a Data Repository Task
<a name="API_CancelDataRepositoryTask_Example_1"></a>

The following request cancels a specific data repository task by using the TaskId request parameter.

#### Sample Request
<a name="API_CancelDataRepositoryTask_Example_1_Request"></a>

```
POST /2015-02-01/cancel-data-repository-task HTTP/1.1 

{    
    "TaskId": ["task-0123456789abcdef0"]
}
```

#### Sample Response
<a name="API_CancelDataRepositoryTask_Example_1_Response"></a>

```
HTTP/1.1 200 success
x-amzn-RequestId: 12345678-1234-abcd-5678-0123456789abc

{
    "Status": "CANCELING",
    "TaskId": "task-0123456789abcdef0"
}
```

## See Also
<a name="API_CancelDataRepositoryTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CancelDataRepositoryTask) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CancelDataRepositoryTask) 