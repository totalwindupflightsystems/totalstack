---
id: "@specs/aws/fsx/docs/API_DataRepositoryTask"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataRepositoryTask"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DataRepositoryTask

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DataRepositoryTask
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataRepositoryTask
<a name="API_DataRepositoryTask"></a>

A description of the data repository task.
+ You use import and export data repository tasks to perform bulk transfer operations between an Amazon FSx for Lustre file system and a linked data repository.
+ You use release data repository tasks to release files that have been exported to a linked S3 bucket from your Amazon FSx for Lustre file system.
+ An Amazon File Cache resource uses a task to automatically release files from the cache.

To learn more about data repository tasks, see [Data Repository Tasks](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repository-tasks.html). 

## Contents
<a name="API_DataRepositoryTask_Contents"></a>

 ** CreationTime **   <a name="FSx-Type-DataRepositoryTask-CreationTime"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.  
Type: Timestamp  
Required: Yes

 ** Lifecycle **   <a name="FSx-Type-DataRepositoryTask-Lifecycle"></a>
The lifecycle status of the data repository task, as follows:  
+  `PENDING` - The task has not started.
+  `EXECUTING` - The task is in process.
+  `FAILED` - The task was not able to be completed. For example, there may be files the task failed to process. The [DataRepositoryTaskFailureDetails](API_DataRepositoryTaskFailureDetails.md) property provides more information about task failures.
+  `SUCCEEDED` - The task has completed successfully.
+  `CANCELED` - The task was canceled and it did not complete.
+  `CANCELING` - The task is in process of being canceled.
You cannot delete an FSx for Lustre file system if there are data repository tasks for the file system in the `PENDING` or `EXECUTING` states. Please retry when the data repository task is finished (with a status of `CANCELED`, `SUCCEEDED`, or `FAILED`). You can use the DescribeDataRepositoryTask action to monitor the task status. Contact the FSx team if you need to delete your file system immediately.
Type: String  
Valid Values: `PENDING | EXECUTING | FAILED | SUCCEEDED | CANCELED | CANCELING`   
Required: Yes

 ** TaskId **   <a name="FSx-Type-DataRepositoryTask-TaskId"></a>
The system-generated, unique 17-digit ID of the data repository task.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(task-[0-9a-f]{17,})$`   
Required: Yes

 ** Type **   <a name="FSx-Type-DataRepositoryTask-Type"></a>
The type of data repository task.  
+  `EXPORT_TO_REPOSITORY` tasks export from your Amazon FSx for Lustre file system to a linked data repository.
+  `IMPORT_METADATA_FROM_REPOSITORY` tasks import metadata changes from a linked S3 bucket to your Amazon FSx for Lustre file system.
+  `RELEASE_DATA_FROM_FILESYSTEM` tasks release files in your Amazon FSx for Lustre file system that have been exported to a linked S3 bucket and that meet your specified release criteria.
+  `AUTO_RELEASE_DATA` tasks automatically release files from an Amazon File Cache resource.
Type: String  
Valid Values: `EXPORT_TO_REPOSITORY | IMPORT_METADATA_FROM_REPOSITORY | RELEASE_DATA_FROM_FILESYSTEM | AUTO_RELEASE_DATA`   
Required: Yes

 ** CapacityToRelease **   <a name="FSx-Type-DataRepositoryTask-CapacityToRelease"></a>
Specifies the amount of data to release, in GiB, by an Amazon File Cache AUTO\_RELEASE\_DATA task that automatically releases files from the cache.  
Type: Long  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** EndTime **   <a name="FSx-Type-DataRepositoryTask-EndTime"></a>
The time the system completed processing the task, populated after the task is complete.  
Type: Timestamp  
Required: No

 ** FailureDetails **   <a name="FSx-Type-DataRepositoryTask-FailureDetails"></a>
Failure message describing why the task failed, it is populated only when `Lifecycle` is set to `FAILED`.  
Type: [DataRepositoryTaskFailureDetails](API_DataRepositoryTaskFailureDetails.md) object  
Required: No

 ** FileCacheId **   <a name="FSx-Type-DataRepositoryTask-FileCacheId"></a>
The system-generated, unique ID of the cache.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fc-[0-9a-f]{8,})$`   
Required: No

 ** FileSystemId **   <a name="FSx-Type-DataRepositoryTask-FileSystemId"></a>
The globally unique ID of the file system.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: No

 ** Paths **   <a name="FSx-Type-DataRepositoryTask-Paths"></a>
An array of paths that specify the data for the data repository task to process. For example, in an EXPORT\_TO\_REPOSITORY task, the paths specify which data to export to the linked data repository.  
(Default) If `Paths` is not specified, Amazon FSx uses the file system root directory.  
Type: Array of strings  
Array Members: Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{0,4096}$`   
Required: No

 ** ReleaseConfiguration **   <a name="FSx-Type-DataRepositoryTask-ReleaseConfiguration"></a>
The configuration that specifies the last accessed time criteria for files that will be released from an Amazon FSx for Lustre file system.  
Type: [ReleaseConfiguration](API_ReleaseConfiguration.md) object  
Required: No

 ** Report **   <a name="FSx-Type-DataRepositoryTask-Report"></a>
Provides a report detailing the data repository task results of the files processed that match the criteria specified in the report `Scope` parameter. FSx delivers the report to the file system's linked data repository in Amazon S3, using the path specified in the report `Path` parameter. You can specify whether or not a report gets generated for a task using the `Enabled` parameter.  
Type: [CompletionReport](API_CompletionReport.md) object  
Required: No

 ** ResourceARN **   <a name="FSx-Type-DataRepositoryTask-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** StartTime **   <a name="FSx-Type-DataRepositoryTask-StartTime"></a>
The time the system began processing the task.  
Type: Timestamp  
Required: No

 ** Status **   <a name="FSx-Type-DataRepositoryTask-Status"></a>
Provides the status of the number of files that the task has processed successfully and failed to process.  
Type: [DataRepositoryTaskStatus](API_DataRepositoryTaskStatus.md) object  
Required: No

 ** Tags **   <a name="FSx-Type-DataRepositoryTask-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## See Also
<a name="API_DataRepositoryTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DataRepositoryTask) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DataRepositoryTask) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DataRepositoryTask) 