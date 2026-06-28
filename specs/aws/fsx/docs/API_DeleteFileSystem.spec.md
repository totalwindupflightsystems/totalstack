---
id: "@specs/aws/fsx/docs/API_DeleteFileSystem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFileSystem"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteFileSystem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteFileSystem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFileSystem
<a name="API_DeleteFileSystem"></a>

Deletes a file system. After deletion, the file system no longer exists, and its data is gone. Any existing automatic backups and snapshots are also deleted.

To delete an Amazon FSx for NetApp ONTAP file system, first delete all the volumes and storage virtual machines (SVMs) on the file system. Then provide a `FileSystemId` value to the `DeleteFileSystem` operation.

Before deleting an Amazon FSx for OpenZFS file system, make sure that there aren't any Amazon S3 access points attached to any volume. For more information on how to list S3 access points that are attached to volumes, see [Listing S3 access point attachments](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-list.html). For more information on how to delete S3 access points, see [Deleting an S3 access point attachment](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/delete-access-point.html).

By default, when you delete an Amazon FSx for Windows File Server file system, a final backup is created upon deletion. This final backup isn't subject to the file system's retention policy, and must be manually deleted.

To delete an Amazon FSx for Lustre file system, first [unmount](https://docs.aws.amazon.com/fsx/latest/LustreGuide/unmounting-fs.html) it from every connected Amazon EC2 instance, then provide a `FileSystemId` value to the `DeleteFileSystem` operation. By default, Amazon FSx will not take a final backup when the `DeleteFileSystem` operation is invoked. On file systems not linked to an Amazon S3 bucket, set `SkipFinalBackup` to `false` to take a final backup of the file system you are deleting. Backups cannot be enabled on S3-linked file systems. To ensure all of your data is written back to S3 before deleting your file system, you can either monitor for the [AgeOfOldestQueuedMessage](https://docs.aws.amazon.com/fsx/latest/LustreGuide/monitoring-cloudwatch.html#auto-import-export-metrics) metric to be zero (if using automatic export) or you can run an [export data repository task](https://docs.aws.amazon.com/fsx/latest/LustreGuide/export-data-repo-task-dra.html). If you have automatic export enabled and want to use an export data repository task, you have to disable automatic export before executing the export data repository task.

The `DeleteFileSystem` operation returns while the file system has the `DELETING` status. You can check the file system deletion status by calling the [DescribeFileSystems](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html) operation, which returns a list of file systems in your account. If you pass the file system ID for a deleted file system, the `DescribeFileSystems` operation returns a `FileSystemNotFound` error.

**Note**  
If a data repository task is in a `PENDING` or `EXECUTING` state, deleting an Amazon FSx for Lustre file system will fail with an HTTP status code 400 (Bad Request).

**Important**  
The data in a deleted file system is also deleted and can't be recovered by any means.

## Request Syntax
<a name="API_DeleteFileSystem_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "LustreConfiguration": { 
      "FinalBackupTags": [ 
         { 
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SkipFinalBackup": {{boolean}}
   },
   "OpenZFSConfiguration": { 
      "FinalBackupTags": [ 
         { 
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Options": [ "{{string}}" ],
      "SkipFinalBackup": {{boolean}}
   },
   "WindowsConfiguration": { 
      "FinalBackupTags": [ 
         { 
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SkipFinalBackup": {{boolean}}
   }
}
```

## Request Parameters
<a name="API_DeleteFileSystem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DeleteFileSystem_RequestSyntax) **   <a name="FSx-DeleteFileSystem-request-ClientRequestToken"></a>
A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This token is automatically filled on your behalf when using the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_DeleteFileSystem_RequestSyntax) **   <a name="FSx-DeleteFileSystem-request-FileSystemId"></a>
The ID of the file system that you want to delete.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

 ** [LustreConfiguration](#API_DeleteFileSystem_RequestSyntax) **   <a name="FSx-DeleteFileSystem-request-LustreConfiguration"></a>
The configuration object for the Amazon FSx for Lustre file system being deleted in the `DeleteFileSystem` operation.  
Type: [DeleteFileSystemLustreConfiguration](API_DeleteFileSystemLustreConfiguration.md) object  
Required: No

 ** [OpenZFSConfiguration](#API_DeleteFileSystem_RequestSyntax) **   <a name="FSx-DeleteFileSystem-request-OpenZFSConfiguration"></a>
The configuration object for the OpenZFS file system used in the `DeleteFileSystem` operation.  
Type: [DeleteFileSystemOpenZFSConfiguration](API_DeleteFileSystemOpenZFSConfiguration.md) object  
Required: No

 ** [WindowsConfiguration](#API_DeleteFileSystem_RequestSyntax) **   <a name="FSx-DeleteFileSystem-request-WindowsConfiguration"></a>
The configuration object for the Microsoft Windows file system used in the `DeleteFileSystem` operation.  
Type: [DeleteFileSystemWindowsConfiguration](API_DeleteFileSystemWindowsConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_DeleteFileSystem_ResponseSyntax"></a>

```
{
   "FileSystemId": "string",
   "Lifecycle": "string",
   "LustreResponse": { 
      "FinalBackupId": "string",
      "FinalBackupTags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   },
   "OpenZFSResponse": { 
      "FinalBackupId": "string",
      "FinalBackupTags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   },
   "WindowsResponse": { 
      "FinalBackupId": "string",
      "FinalBackupTags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DeleteFileSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystemId](#API_DeleteFileSystem_ResponseSyntax) **   <a name="FSx-DeleteFileSystem-response-FileSystemId"></a>
The ID of the file system that's being deleted.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$` 

 ** [Lifecycle](#API_DeleteFileSystem_ResponseSyntax) **   <a name="FSx-DeleteFileSystem-response-Lifecycle"></a>
The file system lifecycle for the deletion request. If the `DeleteFileSystem` operation is successful, this status is `DELETING`.  
Type: String  
Valid Values: `AVAILABLE | CREATING | FAILED | DELETING | MISCONFIGURED | UPDATING | MISCONFIGURED_UNAVAILABLE` 

 ** [LustreResponse](#API_DeleteFileSystem_ResponseSyntax) **   <a name="FSx-DeleteFileSystem-response-LustreResponse"></a>
The response object for the Amazon FSx for Lustre file system being deleted in the `DeleteFileSystem` operation.  
Type: [DeleteFileSystemLustreResponse](API_DeleteFileSystemLustreResponse.md) object

 ** [OpenZFSResponse](#API_DeleteFileSystem_ResponseSyntax) **   <a name="FSx-DeleteFileSystem-response-OpenZFSResponse"></a>
The response object for the OpenZFS file system that's being deleted in the `DeleteFileSystem` operation.  
Type: [DeleteFileSystemOpenZFSResponse](API_DeleteFileSystemOpenZFSResponse.md) object

 ** [WindowsResponse](#API_DeleteFileSystem_ResponseSyntax) **   <a name="FSx-DeleteFileSystem-response-WindowsResponse"></a>
The response object for the Microsoft Windows file system used in the `DeleteFileSystem` operation.  
Type: [DeleteFileSystemWindowsResponse](API_DeleteFileSystemWindowsResponse.md) object

## Errors
<a name="API_DeleteFileSystem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
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

## See Also
<a name="API_DeleteFileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteFileSystem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileSystem) 