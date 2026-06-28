---
id: "@specs/aws/datasync/docs/special-files-copied"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Links and directories copied by DataSync"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Links and directories copied by DataSync

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/special-files-copied
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Links and directories copied by AWS DataSync
<a name="special-files-copied"></a>

AWS DataSync handles hard links, symbolic links, and directories differently depending on the storage locations involved in your transfer.

## Hard links
<a name="special-files-copied-hard-links"></a>

Here's how DataSync handles hard links in some common transfer scenarios:
+ **When transferring between an NFS file server, FSx for Lustre, FSx for OpenZFS, FSx for ONTAP (using NFS), and Amazon EFS**, hard links are preserved.
+ **When transferring to Amazon S3**, each underlying file referenced by a hard link is transferred only once. During incremental transfers, separate objects are created in your S3 bucket. If a hard link is unchanged in Amazon S3, it's correctly restored when transferred to an NFS file server, FSx for Lustre, FSx for OpenZFS, FSx for ONTAP (using NFS), or Amazon EFS file system.
+ **When transferring to Microsoft Azure Blob Storage**, each underlying file referenced by a hard link is transferred only once. During incremental transfers, separate objects are created in your blob storage if there are new references in the source. When transferring from Azure Blob Storage, DataSync transfers hard links as if they are individual files.
+ **When transferring between an SMB file server, FSx for Windows File Server, and FSx for ONTAP (using SMB)**, hard links aren't supported. If DataSync encounters hard links in these situations, the transfer task completes with an error. To learn more, check your CloudWatch logs.
+ **When transferring to HDFS**, hard links aren't supported. CloudWatch logs show these links as skipped.

## Symbolic links
<a name="special-files-copied-symbolic-links"></a>

Here's how DataSync handles symbolic links in some common transfer scenarios:
+ **When transferring between an NFS file server, FSx for Lustre, FSx for OpenZFS, FSx for ONTAP (using NFS), and Amazon EFS**, symbolic links are preserved.
+ **When transferring to Amazon S3**, the link target path is stored in the Amazon S3 object. The link is correctly restored when transferred to an NFS file server, FSx for Lustre, FSx for OpenZFS, FSx for ONTAP, or Amazon EFS file system.
+ **When transferring to Azure Blob Storage**, symbolic links aren't supported. CloudWatch logs show these links as skipped.
+ **When transferring between an SMB file server, FSx for Windows File Server, and FSx for ONTAP (using SMB)**, symbolic links aren't supported. DataSync doesn't transfer a symbolic link itself but instead a file referenced by the symbolic link. To recognize duplicate files and deduplicate them with symbolic links, you must configure deduplication on your destination file system.
+ **When transferring to HDFS**, symbolic links aren't supported. CloudWatch logs show these links as skipped.

## Directories
<a name="special-files-copied-directories"></a>

In general, DataSync preserves directories when transferring between storage systems. This isn’t the case in the following situations:
+ **When transferring to Amazon S3**, directories are represented as empty objects that have prefixes and end with a forward slash (`/`).
+ **When transferring to Azure Blob Storage without a hierarchical namespace**, directories don't exist. What looks like a directory is just part of an object name.