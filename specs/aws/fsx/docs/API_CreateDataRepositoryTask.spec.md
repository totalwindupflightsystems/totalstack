---
id: "@specs/aws/fsx/docs/API_CreateDataRepositoryTask"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDataRepositoryTask"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateDataRepositoryTask

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateDataRepositoryTask
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDataRepositoryTask
<a name="API_CreateDataRepositoryTask"></a>

Creates an Amazon FSx for Lustre data repository task. A `CreateDataRepositoryTask` operation will fail if a data repository is not linked to the FSx file system.

You use import and export data repository tasks to perform bulk operations between your FSx for Lustre file system and its linked data repositories. An example of a data repository task is exporting any data and metadata changes, including POSIX metadata, to files, directories, and symbolic links (symlinks) from your FSx file system to a linked data repository.

You use release data repository tasks to release data from your file system for files that are exported to S3. The metadata of released files remains on the file system so users or applications can still access released files by reading the files again, which will restore data from Amazon S3 to the FSx for Lustre file system.

To learn more about data repository tasks, see [Data Repository Tasks](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repository-tasks.html). To learn more about linking a data repository to your file system, see [Linking your file system to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html).

## Request Syntax
<a name="API_CreateDataRepositoryTask_RequestSyntax"></a>

```
{
   "CapacityToRelease": {{number}},
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "Paths": [ "{{string}}" ],
   "ReleaseConfiguration": { 
      "DurationSinceLastAccess": { 
         "Unit": "{{string}}",
         "Value": {{number}}
      }
   },
   "Report": { 
      "Enabled": {{boolean}},
      "Format": "{{string}}",
      "Path": "{{string}}",
      "Scope": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDataRepositoryTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CapacityToRelease](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-CapacityToRelease"></a>
Specifies the amount of data to release, in GiB, by an Amazon File Cache `AUTO_RELEASE_DATA` task that automatically releases files from the cache.  
Type: Long  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [ClientRequestToken](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

 ** [Paths](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-Paths"></a>
A list of paths for the data repository task to use when the task is processed. If a path that you provide isn't valid, the task fails. If you don't provide paths, the default behavior is to export all files to S3 (for export tasks), import all files from S3 (for import tasks), or release all exported files that meet the last accessed time criteria (for release tasks).  
+ For export tasks, the list contains paths on the FSx for Lustre file system from which the files are exported to the Amazon S3 bucket. The default path is the file system root directory. The paths you provide need to be relative to the mount point of the file system. If the mount point is `/mnt/fsx` and `/mnt/fsx/path1` is a directory or file on the file system you want to export, then the path to provide is `path1`.
+ For import tasks, the list contains paths in the Amazon S3 bucket from which POSIX metadata changes are imported to the FSx for Lustre file system. The path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix` (where `prefix` is optional).
+ For release tasks, the list contains directory or file paths on the FSx for Lustre file system from which to release exported files. If a directory is specified, files within the directory are released. If a file path is specified, only that file is released. To release all exported files in the file system, specify a forward slash (/) as the path.
**Note**  
A file must also meet the last accessed time criteria specified in [ReleaseConfiguration](API_ReleaseConfiguration.md) for the file to be released.
Type: Array of strings  
Array Members: Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{0,4096}$`   
Required: No

 ** [ReleaseConfiguration](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-ReleaseConfiguration"></a>
The configuration that specifies the last accessed time criteria for files that will be released from an Amazon FSx for Lustre file system.  
Type: [ReleaseConfiguration](API_ReleaseConfiguration.md) object  
Required: No

 ** [Report](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-Report"></a>
Defines whether or not Amazon FSx provides a CompletionReport once the task has completed. A CompletionReport provides a detailed report on the files that Amazon FSx processed that meet the criteria specified by the `Scope` parameter. For more information, see [Working with Task Completion Reports](https://docs.aws.amazon.com/fsx/latest/LustreGuide/task-completion-report.html).  
Type: [CompletionReport](API_CompletionReport.md) object  
Required: Yes

 ** [Tags](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** [Type](#API_CreateDataRepositoryTask_RequestSyntax) **   <a name="FSx-CreateDataRepositoryTask-request-Type"></a>
Specifies the type of data repository task to create.  
+  `EXPORT_TO_REPOSITORY` tasks export from your Amazon FSx for Lustre file system to a linked data repository.
+  `IMPORT_METADATA_FROM_REPOSITORY` tasks import metadata changes from a linked S3 bucket to your Amazon FSx for Lustre file system.
+  `RELEASE_DATA_FROM_FILESYSTEM` tasks release files in your Amazon FSx for Lustre file system that have been exported to a linked S3 bucket and that meet your specified release criteria.
+  `AUTO_RELEASE_DATA` tasks automatically release files from an Amazon File Cache resource.
Type: String  
Valid Values: `EXPORT_TO_REPOSITORY | IMPORT_METADATA_FROM_REPOSITORY | RELEASE_DATA_FROM_FILESYSTEM | AUTO_RELEASE_DATA`   
Required: Yes

## Response Syntax
<a name="API_CreateDataRepositoryTask_ResponseSyntax"></a>

```
{
   "DataRepositoryTask": { 
      "CapacityToRelease": number,
      "CreationTime": number,
      "EndTime": number,
      "FailureDetails": { 
         "Message": "string"
      },
      "FileCacheId": "string",
      "FileSystemId": "string",
      "Lifecycle": "string",
      "Paths": [ "string" ],
      "ReleaseConfiguration": { 
         "DurationSinceLastAccess": { 
            "Unit": "string",
            "Value": number
         }
      },
      "Report": { 
         "Enabled": boolean,
         "Format": "string",
         "Path": "string",
         "Scope": "string"
      },
      "ResourceARN": "string",
      "StartTime": number,
      "Status": { 
         "FailedCount": number,
         "LastUpdatedTime": number,
         "ReleasedCapacity": number,
         "SucceededCount": number,
         "TotalCount": number
      },
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "TaskId": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_CreateDataRepositoryTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataRepositoryTask](#API_CreateDataRepositoryTask_ResponseSyntax) **   <a name="FSx-CreateDataRepositoryTask-response-DataRepositoryTask"></a>
The description of the data repository task that you just created.  
Type: [DataRepositoryTask](API_DataRepositoryTask.md) object

## Errors
<a name="API_CreateDataRepositoryTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** DataRepositoryTaskExecuting **   
An existing data repository task is currently executing on the file system. Wait until the existing task has completed, then create the new task.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **   
No Amazon FSx file systems were found based upon supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## Examples
<a name="API_CreateDataRepositoryTask_Examples"></a>

### Create a Data Repository Task
<a name="API_CreateDataRepositoryTask_Example_1"></a>

The following request creates an `EXPORT_TO_REPOSITORY` data repository task for the specified file system.

#### Sample Request
<a name="API_CreateDataRepositoryTask_Example_1_Request"></a>

```
POST /2015-02-01/create-data-repository-task HTTP/1.1 
Host: fsx.us-east-1.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{
    "FileSystemId": "fs-0123456789abcdef0",
    "Type": "EXPORT_TO_REPOSITORY",
    "Paths": ["path1", "path2/file1"],
    "Report": {
        "Enabled":true,
        "Path":"s3://amzn-s3-demo-bucket/FSxLustre20191118T225838Z/myreports",
        "Format":"REPORT_CSV_20191124",
        "Scope":"FAILED_FILES_ONLY"
    },
        
}
```

#### Sample Response
<a name="API_CreateDataRepositoryTask_Example_1_Response"></a>

```
HTTP/1.1 200 success
x-amzn-RequestId: c3616af3-33fa-40ad-ae0d-d3895a2c3a1f

{
    "Task": {
        "TaskId": "task-0123456789abcdef1",
        "TaskType": "EXPORT_TO_REPOSITORY",
        "Lifecycle": "PENDING",
        "FileSystemId": "fs-0123456789abcdef0",
        "Paths": ["path1", "path2/file1"],
        "TaskReport": {
            "Path":"s3://amzn-s3-demo-bucket/FSxLustre20191118T225838Z/myreports",
            "Format":"REPORT_CSV_20191124",
            "Enabled":true,
            "Scope":"FAILED_FILES_ONLY"
        },
        "Tags": [],
        "CreationTime": "2018-12-17T18:18:18.000Z",
        "ClientRequestToken": "10192019-drt-12",
        "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:task:task-123f8cd8e330c1321"
    }
}
```

## See Also
<a name="API_CreateDataRepositoryTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateDataRepositoryTask) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateDataRepositoryTask) 