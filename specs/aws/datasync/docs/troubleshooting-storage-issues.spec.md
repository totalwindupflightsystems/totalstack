---
id: "@specs/aws/datasync/docs/troubleshooting-storage-issues"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Troubleshooting location issues"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Troubleshooting location issues

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/troubleshooting-storage-issues
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Troubleshooting issues with DataSync locations
<a name="troubleshooting-storage-issues"></a>

Use the following information to help you troubleshoot issues with AWS DataSync locations. Some of these issues can include:
+ Permissions and mount errors with NFS locations
+ File ownership issues
+ Problems accessing SMB locations that use Kerberos authentication
+ Permission and access issues with object storage, such as Amazon S3 and Microsoft Azure Blob locations

## My task failed with an NFS permissions denied error
<a name="task-permission-denied"></a>

You can get a "permissions denied" error message if you configure your NFS file server with `root_squash` or `all_squash` and your files don't all have read access.

**Action to take**  
To fix this issue, configure your NFS export with `no_root_squash` or make sure that the permissions for all of the files that you want to transfer allow read access for all users.

For DataSync to access directories, you must also enable all-execute access. To make sure that the directory can be mounted, first connect to any computer that has the same network configuration as your agent. Then run the following CLI command:

`mount -t nfs -o nfsvers=<{{your-nfs-server-version}}> <{{your-nfs-server-name}}>:<{{nfs-export-path-you-specified}}> <{{new-test-folder-on-your-computer}}>`

If the issue still isn't resolved, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).

## My task failed with an NFS mount error
<a name="onpremise-location-stuck-mounting"></a>

You might see the following error when running a DataSync task that involves an NFS file server location:

Task failed to access location loc-1111222233334444a: x40016: mount.nfs: Connection timed out

**Actions to take**  
Do the following until the error is resolved.

1. Make sure that the NFS file server and export that you specify in your DataSync location are valid. If they aren't, delete your location and task, then create a new location and task that use a valid NFS file server and export. For more information, see [Using the DataSync console](create-nfs-location.md#create-nfs-location-console).

1. Check your firewall configuration between your agent and NFS file server. For more information, see [Network requirements for on-premises, self-managed, and other cloud storage](datasync-network.md#on-premises-network-requirements).

1. Make sure that your agent can access the NFS file server and mount the export. For more information, see [Providing DataSync access to NFS file servers](create-nfs-location.md#accessing-nfs).

1. If you still see the error, open a support channel with Support. For more information, see [I don't know what's going on with my agent. Can someone help me?](troubleshooting-datasync-agents.md#enable-support-access).

## My task failed with an Amazon EFS mount error
<a name="troubleshoot-efs-mount-target"></a>

You might see the following error when running a DataSync task that involves an Amazon EFS location:

Task failed to access location loc-1111222233334444a: x40016: Failed to connect to EFS mount target with IP: 10.10.1.0.

This can happen if the Amazon EFS file system's mount path that you configure with your location gets updated or deleted. DataSync isn't aware of these changes in the file system. 

**Action to take**  
Delete your location and task and [create a new Amazon EFS location](create-efs-location.md#create-efs-location-how-to) with the new mount path.

## File ownership isn't maintained with NFS transfer
<a name="nfs-id-mapping"></a>

After your transfer, you might notice that the files in your DataSync destination location have different user IDs (UIDs) or group IDs (GIDs) than the same files in your source location. For example, the files in your destination might have a UID of `65534`, `99`, or `nobody`.

This can happen if a file system involved in your transfer uses NFS version 4 ID mapping, a feature that DataSync doesn't support.

**Action to take**  
You have a couple options to work around this issue:
+ Create a new location for the file system that uses NFS version 3 instead of version 4.
+ Disable NFS version 4 ID mapping on the file system.

Retry the transfer. Either option should resolve the issue.

## My task can't access an SMB location that uses Kerberos
<a name="task-fails-smb-location-kerberos"></a>

DataSync errors with SMB locations that use [Kerberos authentication](create-smb-location.md#configuring-smb-kerberos-authentication) are typically related to mismatches between your location and Kerberos configurations. There also might be a network issue.

**Failed to access location**  
The following error indicates that there might be configuration issues with your SMB location or Kerberos setup:  

```
Task failed to access location
```
**Verify the following**:  
+ The SMB file server that you specify for your location is a domain name. For Kerberos, you can't specify the file server's IP address.
+ The Kerberos principal that you specify for your location matches the principal that you use to create the Kerberos key table (keytab) file. Principal names are case sensitive.
+ The Kerberos principal's mapped user password hasn't changed since you created the keytab file. If the password changes (because of password rotation or some other reason), your task execution might fail with the following error:

  Task failed to access location loc-1111222233334444a: x40015: kinit: Preauthentication failed while getting initial credentials

**Can't contact KDC realm**  
The following error indicates a networking issue:  

```
kinit: Cannot contact any KDC for realm 'MYDOMAIN.ORG' while getting initial credentials"
```
**Verify the following**:  
+ The Kerberos configuration file (`krb5.conf`) that you provided DataSync has the correct information about your Kerberos realm. For an example `krb5.conf` file, see [Kerberos authentication prerequisites](create-smb-location.md#configuring-smb-kerberos-prerequisites).
+ The Kerberos Key Distribution Center (KDC) server port is open. The KDC port is typically TCP port 88.
+ The DNS configuration on your network.

## My task failed with an input/output error
<a name="sync-io-error"></a>

You can get an input/output error message if your storage system fails I/O requests from the DataSync agent. Common reasons for this include a server disk failure, changes to your firewall configuration, or a network router failure.

If the error involves an NFS file server or Hadoop Distributed File System (HDFS) cluster, use the following steps to resolve the error.

**Actions to take (NFS)**  
First, check your NFS file server's logs and metrics to determine if the problem started on the NFS server. If yes, resolve that issue.

Next, check that your network configuration hasn't changed. To check if the NFS file server is configured correctly and that DataSync can access it, do the following:

1. Set up another NFS client on the same network subnet as the agent.

1. Mount your share on that client.

1. Validate that the client can read and write to the share successfully.

**Actions to take (HDFS)**  
Do the following until you resolve the error:

1. Make sure that your HDFS cluster allows your DataSync agent to communicate with the cluster's NameNode and DataNode ports.

   In most clusters, you can find the port numbers that the cluster uses in the following configuration files:
   + To find the NameNode port, look in the `core-site.xml` file under the `fs.default` or `fs.default.name` property (depending on the Hadoop distribution).
   + To find the DataNode port, look in the `hdfs-site.xml` file under the `dfs.datanode.address` property.

1. In your `hdfs-site.xml` file, verify that your `dfs.data.transfer.protection` property has only one value. For example:

   ```
   <property>
      <name>dfs.data.transfer.protection</name>
      <value>privacy</value>
   </property>
   ```

## Error: `FsS3UnableToConnectToEndpoint`
<a name="troubleshoot-fss3unabletoconnecttoendpoint"></a>

DataSync can't connect to your [Amazon S3 location](create-s3-location.md). This could mean the location's S3 bucket isn't reachable or the location isn't configured correctly.

Do the following until you resolve the issue:
+ Check if DataSync can [access your S3 bucket](create-s3-location.md#create-s3-location-access).
+ Make your sure location is configured correctly by using the DataSync console or [DescribeLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationS3.html) operation.

## Error: `FsS3HeadBucketFailed`
<a name="troubleshoot-fss3headbucketfailed"></a>

DataSync can't access the S3 bucket that you're transferring to or from. Check if DataSync has permission to access the bucket by using the Amazon S3 [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html) operation. If you need to adjust your permissions, see [Providing DataSync access to S3 buckets](create-s3-location.md#create-s3-location-access).

## Task fails with an `Unable to list Azure Blobs on the volume root` error
<a name="troubleshoot-azure-blob-storage-list-volume-root"></a>

If your DataSync transfer task fails with an `Unable to list Azure Blobs on the volume root` error, there might be an issue with your shared access signature (SAS) token or your Azure storage account's network.

**Actions to take**  
Try the following and run your task again until you fix the issue:
+ Make sure that your [SAS token](creating-azure-blob-location.md#azure-blob-sas-tokens) has the right permissions to access your Microsoft Azure Blob Storage.
+ If you're running your DataSync agent in Azure, configure your storage account to allow access from the virtual network where your agent resides.
+ If you're running your agent on Amazon EC2, configure your Azure storage firewall to allow access from the agent's public IP address.

For information on how to configure your Azure storage account's network, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).

## Error: `FsAzureBlobVolRootListBlobsFailed`
<a name="troubleshoot-fsazureblobvolrootlistblobsfailed"></a>

The shared access signature (SAS) token that DataSync uses to access your Microsoft Azure Blob Storage doesn't have the List permission.

To resolve the issue, [update your location](creating-azure-blob-location.md#azure-blob-update-location) with a token that has the List permission and try running your task again.

## Error: `SrcLocHitAccess`
<a name="troubleshoot-srclochitaccess"></a>

DataSync can't access your source location. Check that DataSync has permission to access the location and try running your task again.

## Error: `SyncTaskErrorLocationNotAdded`
<a name="troubleshoot-synctaskerrorlocationnotadded"></a>

DataSync can't access your location. Check that DataSync has permission to access the location and try running your task again.

## Error: `S3 location creation failed with (InvalidRequestException) when calling the CreateLocationS3 operation`
<a name="troubleshoot-403-error"></a>

This error could be related to IAM permissions, Amazon S3 bucket policies, AWS KMS permissions or other permission issues. If you get this error, use the following information to troubleshoot:
+ [Troubleshoot access denied (403 Forbidden) errors in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshoot-403-errors.html) in the *Amazon Simple Storage Service User Guide*
+ [How do I troubleshoot 403 Access Denied errors from Amazon S3?](https://repost.aws/knowledge-center/s3-troubleshoot-403) on AWS re:Post

## Task with S3 source location fails with `HeadObject` or `GetObjectTagging` error
<a name="troubleshoot-getobjecttagging"></a>

**Errors related to `HeadObject` or `GetObjectTagging`**  
If you're transferring objects with specific version IDs from an S3 bucket, you might see an error related to `HeadObject` or `GetObjectTagging`. For example, here's an error related to `GetObjectTagging`:

```
[WARN] Failed to read metadata for file {{/picture1.png}} (versionId: {{111111}}): S3 Get Object Tagging Failed
[ERROR] S3 Exception: op=GetObjectTagging {{photos/picture1.png}}, code=403, type=15, exception=AccessDenied, 
msg=Access Denied req-hdrs: content-type=application/xml, x-amz-api-version=2006-03-01 rsp-hdrs: content-type=application/xml, 
date=Wed, 07 Feb 2024 20:16:14 GMT, server=AmazonS3, transfer-encoding=chunked, 
x-amz-id-2=IOWQ4fDEXAMPLEQM+ey7N9WgVhSnQ6JEXAMPLEZb7hSQDASK+Jd1vEXAMPLEa3Km, x-amz-request-id=79104EXAMPLEB723
```

If you see either of these errors, validate that the IAM role that DataSync uses to access your S3 source location has the following permissions:
+ `s3:GetObjectVersion`
+ `s3:GetObjectVersionTagging`

If you need to update your role with these permissions, see [Creating an IAM role for DataSync to access your Amazon S3 location](create-s3-location.md#create-role-manually).