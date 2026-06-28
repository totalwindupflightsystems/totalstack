---
id: "@specs/aws/fsx/docs/API_Backup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Backup"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# Backup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_Backup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Backup
<a name="API_Backup"></a>

A backup of an Amazon FSx for Windows File Server, Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or Amazon FSx for OpenZFS file system.

## Contents
<a name="API_Backup_Contents"></a>

 ** BackupId **   <a name="FSx-Type-Backup-BackupId"></a>
The ID of the backup.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: Yes

 ** CreationTime **   <a name="FSx-Type-Backup-CreationTime"></a>
The time when a particular backup was created.  
Type: Timestamp  
Required: Yes

 ** FileSystem **   <a name="FSx-Type-Backup-FileSystem"></a>
The metadata of the file system associated with the backup. This metadata is persisted even if the file system is deleted.  
Type: [FileSystem](API_FileSystem.md) object  
Required: Yes

 ** Lifecycle **   <a name="FSx-Type-Backup-Lifecycle"></a>
The lifecycle status of the backup.  
+  `AVAILABLE` - The backup is fully available.
+  `PENDING` - For user-initiated backups on Lustre file systems only; Amazon FSx hasn't started creating the backup.
+  `CREATING` - Amazon FSx is creating the backup.
+  `TRANSFERRING` - For user-initiated backups on Lustre file systems only; Amazon FSx is transferring the backup to Amazon S3.
+  `COPYING` - Amazon FSx is copying the backup.
+  `DELETED` - Amazon FSx deleted the backup and it's no longer available.
+  `FAILED` - Amazon FSx couldn't finish the backup.
Type: String  
Valid Values: `AVAILABLE | CREATING | TRANSFERRING | DELETED | FAILED | PENDING | COPYING`   
Required: Yes

 ** Type **   <a name="FSx-Type-Backup-Type"></a>
The type of the file-system backup.  
Type: String  
Valid Values: `AUTOMATIC | USER_INITIATED | AWS_BACKUP`   
Required: Yes

 ** DirectoryInformation **   <a name="FSx-Type-Backup-DirectoryInformation"></a>
The configuration of the self-managed Microsoft Active Directory directory to which the Windows File Server instance is joined.  
Type: [ActiveDirectoryBackupAttributes](API_ActiveDirectoryBackupAttributes.md) object  
Required: No

 ** FailureDetails **   <a name="FSx-Type-Backup-FailureDetails"></a>
Details explaining any failures that occurred when creating a backup.  
Type: [BackupFailureDetails](API_BackupFailureDetails.md) object  
Required: No

 ** KmsKeyId **   <a name="FSx-Type-Backup-KmsKeyId"></a>
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt the backup of the Amazon FSx file system's data at rest.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^.{1,2048}$`   
Required: No

 ** OwnerId **   <a name="FSx-Type-Backup-OwnerId"></a>
An AWS account ID. This ID is a 12-digit number that you use to construct Amazon Resource Names (ARNs) for resources.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^\d{12}$`   
Required: No

 ** ProgressPercent **   <a name="FSx-Type-Backup-ProgressPercent"></a>
Displays the current percent of progress of an asynchronous task.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** ResourceARN **   <a name="FSx-Type-Backup-ResourceARN"></a>
The Amazon Resource Name (ARN) for the backup resource.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** ResourceType **   <a name="FSx-Type-Backup-ResourceType"></a>
Specifies the resource type that's backed up.  
Type: String  
Valid Values: `FILE_SYSTEM | VOLUME`   
Required: No

 ** SizeInBytes **   <a name="FSx-Type-Backup-SizeInBytes"></a>
 The size of the backup in bytes. This represents the amount of data that the file system would contain if you restore this backup.   
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

 ** SourceBackupId **   <a name="FSx-Type-Backup-SourceBackupId"></a>
The ID of the source backup. Specifies the backup that you are copying.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: No

 ** SourceBackupRegion **   <a name="FSx-Type-Backup-SourceBackupRegion"></a>
The source Region of the backup. Specifies the Region from where this backup is copied.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `^[a-z0-9-]{1,20}$`   
Required: No

 ** Tags **   <a name="FSx-Type-Backup-Tags"></a>
The tags associated with a particular file system.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** Volume **   <a name="FSx-Type-Backup-Volume"></a>
Describes an Amazon FSx volume.  
Type: [Volume](API_Volume.md) object  
Required: No

## See Also
<a name="API_Backup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/Backup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/Backup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/Backup) 