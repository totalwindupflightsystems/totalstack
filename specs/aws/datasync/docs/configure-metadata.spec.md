---
id: "@specs/aws/datasync/docs/configure-metadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring how to handle files, objects, and metadata"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Configuring how to handle files, objects, and metadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/configure-metadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring how to handle files, objects, and metadata
<a name="configure-metadata"></a>

You can configure how AWS DataSync handles your files, objects, and their associated metadata when transferring between locations.

For example, with recurring transfers, you might want to overwrite files in your destination with changes in the source to keep the locations in sync. You can copy properties such as POSIX permissions for files and folders, tags associated with objects, and access control lists (ACLs).

## Transfer mode options
<a name="task-option-transfer-mode"></a>

You can configure whether DataSync transfers only the data (including metadata) that's changed following an initial copy or all data every time you run the task. If you're planning on recurring transfers, you might only want to transfer what's changed since your previous task execution.


| Option in console | Option in API | Description | 
| --- | --- | --- | 
| **Transfer only data that has changed** | [TransferMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode) set to `CHANGED` | After your initial full transfer, DataSync copies only the data and metadata that differs between the source and destination location. | 
| **Transfer all data** | [TransferMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode) set to `ALL` | DataSync copies everything in the source to the destination without comparing differences between the locations.  | 

## File and object handling options
<a name="task-option-file-object-handling"></a>

You can control some aspects of how DataSync treats your files or objects in the destination location. For example, DataSync can delete files in the destination that aren't in the source.


| Option in console | Option in API | Description | 
| --- | --- | --- | 
| **Keep deleted files** | [PreserveDeletedFiles](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-PreserveDeletedFiles) | Specifies whether DataSync maintains files or objects in the destination location that don't exist in the source.<br />If you configure your task to delete objects from your Amazon S3 bucket, you might incur minimum storage duration charges for certain storage classes. For detailed information, see [Storage class considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes). You can't configure your task to delete data in the destination and also [transfer all data](#task-option-transfer-mode). When you transfer all data, DataSync doesn't scan your destination location and doesn't know what to delete.  | 
| **Overwrite files** | [OverwriteMode](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-OverwriteMode) | Specifies whether DataSync modifies data in the destination location when the source data or metadata has changed. If you don't configure your task to overwrite data, the destination data isn't overwritten even if the source data differs.<br />If your task overwrites objects, you might incur additional charges for certain storage classes (for example, for retrieval or early deletion). For detailed information, see [Storage class considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes). | 

## Metadata handling options
<a name="task-option-metadata-handling"></a>

DataSync can preserve file and object metadata during a transfer. The metadata that DataSync can preserve depends on the storage systems involved and whether those systems use a similar metadata structure.

Before configuring your task, make sure that you understand how DataSync handles [metadata](metadata-copied.md) and [special files](special-files-copied.md) when transferring between your source and destination locations.

**Important**  
DataSync supports transfers to and from certain third-party cloud storage systems, such as Google Cloud Storage and IBM Cloud Object Storage, which handle system metadata in a way that is not fully S3-compatible. For these transfers, DataSync attempts to copy metadata attributes such as `ContentType`, `ContentEncoding`, `ContentLanguage`, and `CacheControl` on a best-effort basis. If the destination storage system does not apply these attributes, they will be ignored during task verification.


| Option in console | Option in API | Description | 
| --- | --- | --- | 
| **Copy ownership** | [Gid](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-Gid) and [Uid](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-Uid) | Specifies whether DataSync copies POSIX file and folder ownership, such as the group ID of the file's owners and the user ID of the file's owner. | 
| **Copy permissions** | [PosixPermissions](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-PosixPermissions) | Specifies whether DataSync copies POSIX permissions for files and folders from the source to the destination. | 
| Copy timestamps | [Atime](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-Atime) and [Mtime](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-Mtime) | Specifies whether DataSync copies the timestamp metadata from the source to the destination. Required when you need to run a task more than once. | 
| Copy object tags | [ObjectTags](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-ObjectTags) | Specifies whether DataSync preserves the tags associated with your objects when transferring between object storage systems. | 
| Copy ownership, DACLs, and SACLs | [SecurityDescriptorCopyFlags ](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-SecurityDescriptorCopyFlags) set to OWNER\_DACL\_SACL | DataSync copies the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html) | 
| Copy ownership and DACLs | [SecurityDescriptorCopyFlags ](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-SecurityDescriptorCopyFlags) set to OWNER\_DACL | DataSync copies the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html)<br />DataSync won't copy SACLs when you choose this option. | 
| Do not copy ownership or ACLs | [SecurityDescriptorCopyFlags ](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-SecurityDescriptorCopyFlags) set to NONE | DataSync doesn't copy any ownership or permissions data. The objects that DataSync writes to your destination location are owned by the user whose credentials are provided for DataSync to access the destination. Destination object permissions are determined based on the permissions configured on the destination server. | 

## Configuring file, object, and metadata handling options
<a name="configure-file-metadata-options"></a>

You can configure how DataSync handles files, objects, and metadata when creating, editing, or starting your transfer task.

### Using the DataSync console
<a name="configure-metadata-console"></a>

The following instructions describe how to configure file, object, and metadata handling options when creating a task.

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. For **Transfer mode**, choose one of the following options:
   + **Transfer only data that has changed**
   + **Transfer all data**

   For more information about these options, see [Transfer mode options](#task-option-transfer-mode).

1. Select **Keep deleted files** if you want DataSync to maintain files or objects in the destination location that don't exist in the source.

   If you don't choose this option and your task deletes objects from your Amazon S3 bucket, you might incur minimum storage duration charges for certain storage classes. For detailed information, see [Storage class considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes).
**Warning**  
You can't deselect this option and enable **Transfer all data**. When you transfer all data, DataSync doesn't scan your destination location and doesn't know what to delete.

1. Select **Overwrite files** if you want DataSync to modify data in the destination location when the source data or metadata has changed.

   If your task overwrites objects, you might incur additional charges for certain storage classes (for example, for retrieval or early deletion). For detailed information, see [Storage class considerations with Amazon S3 transfers](create-s3-location.md#using-storage-classes).

   If you don't choose this option, the destination data isn't overwritten even if the source data differs.

1. Under **Transfer options**, select how you want DataSync to handle metadata. For more information about the options, see [Metadata handling options](#task-option-metadata-handling).
**Important**  
The options you see in the console depend on your task's source and destination locations. You might have to expand **Additional settings** to see some of these options.
   + **Copy ownership**
   + **Copy permissions**
   + **Copy timestamps**
   + **Copy object tags**
   + **Copy ownership, DACLs, and SACLs**
   + **Copy ownership and DACLs**
   + **Do not copy ownership or ACLs**

### Using the DataSync API
<a name="configure-file-metadata-options-api"></a>

You can configure file, object, and metadata handling options by using the `Options` parameter with any of the following operations:
+ [CreateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html)
+ [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html)
+ [UpdateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html)