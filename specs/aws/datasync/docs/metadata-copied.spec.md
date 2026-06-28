---
id: "@specs/aws/datasync/docs/metadata-copied"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding how DataSync handles metadata"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Understanding how DataSync handles metadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/metadata-copied
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding how DataSync handles file and object metadata
<a name="metadata-copied"></a>

AWS DataSync can preserve your file or object metadata during a data transfer. How your metadata gets copied depends on your transfer locations and if those locations use similar types of metadata.

## System-level metadata
<a name="metadata-copied-system-level"></a>

In general, DataSync doesn't copy system-level metadata. For example, when transferring from an SMB file server, the permissions you configured at the file system level aren't copied to the destination storage system.

There are exceptions. When transferring between Amazon S3 and other object storage, DataSync does copy some [system-defined object metadata](#metadata-copied-between-object-s3).

## Metadata copied in Amazon S3 transfers
<a name="metadata-copied-amazon-s3"></a>

The following tables describe what metadata DataSync can copy when a transfer involves an Amazon S3 location.

**Topics**
+ [To Amazon S3](#metadata-copied-to-s3)
+ [Between Amazon S3 and other object storage](#metadata-copied-between-object-s3)
+ [Between Amazon S3 and HDFS](#metadata-copied-between-hdfs-s3)

### To Amazon S3
<a name="metadata-copied-to-s3"></a>


| When copying from one of these locations | To this location | DataSync can copy | 
| --- | --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  | The following as Amazon S3 user metadata:[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)<br />The file metadata stored in Amazon S3 user metadata is interoperable with NFS shares on file gateways using AWS Storage Gateway. A file gateway enables low-latency access from on-premises networks to data that was copied to Amazon S3 by DataSync. This metadata is also interoperable with FSx for Lustre.<br />When DataSync copies objects that contain this metadata back to an NFS server, the file metadata is restored. Restoring metadata requires granting elevated permissions to the NFS server. For more information, see [Configuring AWS DataSync transfers with an NFS file server](create-nfs-location.md). | 

### Between Amazon S3 and other object storage
<a name="metadata-copied-between-object-s3"></a>


<table>
<thead>
  <tr><th>When copying between these locations</th><th>DataSync can copy</th></tr>
</thead>
<tbody>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td rowspan="2">[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)DataSync doesn't copy other object metadata, such as object access control lists (ACLs), prior object versions, or the Last-Modified key.</td></tr>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td></tr>
</tbody>
</table>


### Between Amazon S3 and HDFS
<a name="metadata-copied-between-hdfs-s3"></a>


| When copying between these locations | DataSync can copy | 
| --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  | The following as Amazon S3 user metadata:[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)HDFS uses strings to store file and folder user and group ownership, rather than numeric identifiers, such as UIDs and GIDs. | 

## Metadata copied in NFS transfers
<a name="metadata-copied-nfs"></a>

The following table describes what metadata DataSync can copy between locations that use Network File System (NFS).


| When copying between these locations | DataSync can copy | 
| --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  | 

## Metadata copied in SMB transfers
<a name="metadata-copied-smb"></a>

The following table describes what metadata DataSync can copy between locations that use Server Message Block (SMB).


| When copying between these locations | DataSync can copy | 
| --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  | 

## Metadata copied in other transfer scenarios
<a name="metadata-copied-different"></a>

DataSync handles metadata the following ways when copying between these storage systems (most of which have different metadata structures).


<table>
<thead>
  <tr><th>When copying from one of these locations</th><th>To one of these locations</th><th>DataSync can copy</th></tr>
</thead>
<tbody>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td>[Default POSIX metadata](#POSIX-metadata) for all files and folders on the destination file system or objects in the destination S3 bucket. This approach includes using the default POSIX user ID and group ID values.<br />Windows-based metadata (such as ACLs) is not preserved.</td></tr>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td>[Default POSIX metadata](#POSIX-metadata) on the destination files and folders. This approach includes using the default POSIX user ID and group ID values.</td></tr>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td>The following as user-defined metadata:[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)</td></tr>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td>[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)HDFS stores file and folder user and group ownership as strings rather than numeric identifiers (such as UIDs and GIDs). Default values for UIDs and GIDs are applied on the destination file system. For more information, see [Understanding when and how DataSync applies default POSIX metadata](#POSIX-metadata).</td></tr>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td>File and folder timestamps from the source location. The file or folder owner is set based on the HDFS user or Kerberos principal you specified when creating the [HDFS transfer location](create-hdfs-location.md). The Groups Mapping configuration on the Hadoop cluster determines the group.</td></tr>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td rowspan="2">File and folder timestamps from the source location. Ownership is set based on the Windows user that was specified in DataSync to access the Amazon FSx or SMB share. Permissions are inherited from the parent directory.</td></tr>
  <tr><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html) </td></tr>
</tbody>
</table>


## Understanding when and how DataSync applies default POSIX metadata
<a name="POSIX-metadata"></a>

DataSync applies default POSIX metadata in the following situations:
+ When your transfer's source and destination locations don't have similar metadata structures
+ When metadata is missing from the source location

The following table describes how DataSync applies default POSIX metadata during these types of transfers:


| Source | Destination | File permissions | Folder permissions | UID | GID | 
| --- | --- | --- | --- | --- | --- | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  | 0755 | 0755 | 65534 | 65534 | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  | 0644 | 0755 | 65534 | 65534 | 
|  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html)  | 0644 | 0755 | 65534 | 65534 | 

1 In cases where the objects don't have metadata that was previously applied by DataSync.