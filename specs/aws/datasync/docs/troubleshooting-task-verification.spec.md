---
id: "@specs/aws/datasync/docs/troubleshooting-task-verification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshooting data verification issues"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Troubleshooting data verification issues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/troubleshooting-task-verification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Troubleshooting data verification issues
<a name="troubleshooting-task-verification"></a>

By default, AWS DataSync [verifies the integrity](how-datasync-transfer-works.md#how-verifying-works) of your data at the end of a transfer. Use the following information to help you diagnose common verification errors and warnings, such as files being modified or deleted before DataSync finishes verifying your data.

With verification issues, many times it helps to review your [CloudWatch logs](configure-logging.md) (or [task reports](task-reports.md)) in addition to the task execution error that you're seeing. DataSync provides JSON-structured logs for Enhanced mode tasks, while Basic mode tasks have unstructured logs.

## There are mismatches between a file's contents
<a name="troubleshooting-mismatch-file-contents"></a>

When your task execution finishes, you see the following error:

```
Transfer and verification completed. Verification detected mismatches. Files with mismatches are listed in Cloud Watch Logs
```

In your CloudWatch logs, you might notice failed verifications for contents that differ between the source and destination locations. This can happen if files are modified during your transfer.

For example, the following logs shows that `file1.txt` has different `mtime`, `srcHash`, and `dstHash` values:

**Basic mode log example**  

```
[NOTICE] Verification failed <> /directory1/directory2/file1.txt
[NOTICE] /directory1/directory2/file1.txt   srcMeta: type=R mode=0755 uid=65534 gid=65534 size=534528 atime=1633100003/684349800 mtime={{1602647222/222919600}} extAttrsHash=0
[NOTICE]   srcHash: {{0c506c26bd1e43bd3ac346734f1a9c16c4ad100d1b43c2903772ca894fd24e44}}
[NOTICE] /directory1/directory2/file1.txt   dstMeta: type=R mode=0755 uid=65534 gid=65534 size=511001 atime=1633100003/684349800 mtime={{1633106855/859227500}} extAttrsHash=0
[NOTICE]   dstHash: {{dbd798929f11a7c0201e97f7a61191a83b4e010a449dfc79fbb8233801067c46}}
```

In DataSync, `mtime` represents the last time a file was written to before [preparation](how-datasync-transfer-works.md#how-datasync-prepares). When verifying transfers, DataSync compares `mtime` values between source and destination locations. A verification failure like this occurs if the `mtime` for a file isn't the same for both locations. The differences between `srcHash` and `dstHash` indicate the file's contents don't match at both locations.

**Actions to take**  
Do the following:

1. Use an epoch time converter to determine whether the source or destination file or object was modified more recently. This can help identify which version is current.

1. To avoid this error again, [schedule your task](task-scheduling.md) to run during a maintenance window when there's no activity at your source and destination.

## There's a mismatch between a file's SMB metadata
<a name="troubleshooting-mismatch-smb-attributes"></a>

When your task execution finishes, you see the following error:

```
Transfer and verification completed. Verification detected mismatches. Files with mismatches are listed in Cloud Watch Logs
```

When transferring between storage systems that support the Server Message Block (SMB) protocol, you might see this error when a file's extended SMB attributes don't match between source and destination.

For example, the following logs show that `file1.txt` has a different `extAttrsHash` value between locations, indicating the file contents are identical but extended attributes weren't set at the destination:

**Basic mode log example**  

```
[NOTICE] Verification failed <> /directory1/directory2/file1.txt
[NOTICE] /directory1/directory2/file1.txt   srcMeta: type=R mode=0755 uid=65534 gid=65534 size=1469752 atime=1631354985/174924200 mtime=1536995541/986211400 extAttrsHash={{2272191894}}
[NOTICE]   srcHash: 38571d42b646ac8f4034b7518636b37dd0899c6fc03cdaa8369be6e81a1a2bb5
[NOTICE] /directory1/directory2/file1.txt   dstMeta: type=R mode=0755 uid=65534 gid=65534 size=1469752 atime=1631354985/174924200 mtime=1536995541/986211400 extAttrsHash={{3051150340}}
[NOTICE]   dstHash: 38571d42b646ac8f4034b7518636b37dd0899c6fc03cdaa8369be6e81a1a2bb5
```

You might also see a related error message about extended attributes:

```
[ERROR] Deferred error: WriteFileExtAttr2 failed to setextattrlist(filename="/directory1/directory2/file1.txt"): Input/output error
```

**Action to take**  
This error typically occurs when there are insufficient permissions to copy access control lists (ACLs) to the destination. To resolve this issue, review the following configuration guides based on your destination type:
+ [Required permissions](create-fsx-location.md#create-fsx-windows-location-permissions) with FSx for Windows File Server file systems
+ [Required permissions](create-ontap-location.md#create-ontap-location-smb) with FSx for ONTAP file systems that use SMB

## Files to transfer are no longer at source location
<a name="source-files-deleted-preparation"></a>

When your task execution finishes, you see the following error:

```
Transfer and verification completed. Selected files transferred except for files skipped due to errors. If no skipped files are listed in Cloud Watch Logs, please contact AWS Support for further assistance.
```

In your logs, you might see errors indicating that files aren't at the source location. This can happen if files (such as `file1.dll` and `file2.dll`) are deleted after [preparation](how-datasync-transfer-works.md#how-datasync-prepares) but before DataSync transfers them:

**Basic mode log example**  

```
[ERROR] Failed to open source file /file1.dll: No such file or directory
[ERROR] Failed to open source file /file2.dll: No such file or directory
```

**Action to take**  
To avoid these situations, [schedule your task](task-scheduling.md) to run when there's no activity at the source location.

For example, you can run your task during a maintenance window when users and applications aren't actively working with that location.

In some cases, you might not see logs associated with this error. If that happens, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## DataSync can't verify destination data
<a name="troubleshooting-cant-verify-destination"></a>

When your task execution finishes, you see the following error:

```
Transfer and verification completed. Verification detected mismatches. Files with mismatches are listed in Cloud Watch Logs
```

In your logs, you might notice that DataSync can't verify certain folders or files in the destination location. These errors can look like this:

**Basic mode log example**  

```
[ERROR] Failed to read metadata for destination file /directory1/directory2/file1.txt: No such file or directory
```

For files, you might see verification failures like this:

**Basic mode log example**  

```
[NOTICE] Verification failed <> /directory1/directory2/file1.txt
[NOTICE] /directory1/directory2/file1.txt   srcMeta: type=R mode=0755 uid=65534 gid=65534 size=61533 atime=1633099987/747713800 mtime=1536995631/894267700 extAttrsHash=232104771
[NOTICE]   srcHash: 1426fe40f669a7d36cca1b5329983df31a9aeff8eb9fe3ac885f26de2f8fff6b
[NOTICE] /directory1/directory2/file1.txt   dstMeta: type=R mode=0755 uid=65534 gid=65534 size=0 atime=0/0 mtime=0/0 extAttrsHash=0
[NOTICE]   dstHash: 0000000000000000000000000000000000000000000000000000000000000000
```

**Action to take**  
These logs indicate that destination data was deleted after the transfer but before verification. (Logs look similar when data is uploaded to a source location during the same time frame.)

To avoid these situations, [schedule your task](task-scheduling.md) to run when there's no activity at the destination location.

For example, you can run your task during a maintenance window when users and applications aren't actively working with that location.

## DataSync can't read object metadata
<a name="troubleshooting-cant-read-object-metadata"></a>

When your task execution finishes, you see the following error:

```
Transfer and verification completed. Selected files transferred except for files skipped due to errors. If no skipped files are listed in Cloud Watch Logs, please contact AWS Support for further assistance.
```

In your logs, you might notice that DataSync can't read `file1.png` because of a failed Amazon S3 `HeadObject` request. [DataSync makes `HeadObject` requests](create-s3-location.md#create-s3-location-s3-requests-made) with S3 locations during task preparation and verification.

**Basic mode log example**  

```
[WARN] Failed to read metadata for file /file1.png: S3 Head Object Failed
```

**Actions to take**  
To fix this issue, verify whether DataSync has the right level of permissions to work with your S3 bucket:
+ Make sure that the IAM role that DataSync uses to access your Amazon S3 locations allows the `s3:GetObject` permission. For more information, see [Required permissions](create-s3-location.md#create-s3-location-required-permissions).
+ If your S3 bucket uses server-side encryption, make sure that DataSync is allowed to access the objects in that bucket. For more information, see [Accessing S3 buckets using server-side encryption](create-s3-location.md#create-s3-location-encryption).

## There's a mismatch in an object's system-defined metadata
<a name="troubleshooting-verification-object-system-metadata"></a>

When your Enhanced mode task execution between S3 buckets finishes, you see the following error:

```
Verification failed due to a difference in metadata
```

You might notice in your logs a mismatch in an object’s Amazon S3 [system-defined metadata](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html#SysMetadata). In this particular example, the source object doesn't have `Content-Type` metadata but the destination object does. This happened because the destination S3 bucket automatically applied `"ContentType": "application/octet-stream"` metadata to the object when DataSync transferred it there.

**Enhanced mode log example**  

```
{
    "Action": "VERIFY",
    "Source": {
        "LocationId": "loc-0b3017fc4ba4a2d8d",
        "RelativePath": "encoding/content-null",
        "Metadata": {
            "Type": "Object",
            "ContentSize": 24,
            "LastModified": "2024-12-23T15:48:15Z",
            "S3": {
                "SystemMetadata": {
                    "ETag": "\"68b9c323bb846841ee491481f576ed4a\""
                },
                "UserMetadata": {},
                "Tags": {}
            }
        }
    },
    "Destination": {
        "LocationId": "loc-abcdef01234567890",
        "RelativePath": "encoding/content-null",
        "Metadata": {
            "Type": "Object",
            "ContentSize": 24,
            "LastModified": "2024-12-23T16:00:03Z",
            "S3": {
                "SystemMetadata": {
                    "{{ContentType}}": "{{application/octet-stream}}",
                    "ETag": "\"68b9c323bb846841ee491481f576ed4a\""
                },
                "UserMetadata": {
                    "file-mtime": "1734968895000"
                },
                "Tags": {}
            }
        }
    },
    "TransferType": "CONTENT_AND_METADATA",
    "ErrorCode": "MetadataDiffers",
    "ErrorDetail": "Verification failed due to a difference in metadata"
}
```

**Action to take**  
To avoid this error, update your source location objects to include the `Content-Type` metadata property.

## Understanding data verification duration
<a name="verifying-status-too-long"></a>

DataSync verification includes an SHA256 checksum on file content and an exact comparison of file metadata between locations. How long verification takes depends on several factors, including the number of files or objects involved, the size of the data in the storage systems, and the performance of these systems.

**Action to take**  
Given the factors that can affect verification time, you shouldn't have to do anything. However, if your task execution seems stuck with a [verifying](run-task.md#understand-task-execution-statuses) status, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).