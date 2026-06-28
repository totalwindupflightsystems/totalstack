---
id: "@specs/aws/fsx/docs/API_AdministrativeAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AdministrativeAction"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# AdministrativeAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_AdministrativeAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AdministrativeAction
<a name="API_AdministrativeAction"></a>

Describes a specific Amazon FSx administrative action for the current Windows, Lustre, OpenZFS, or ONTAP file system or volume.

## Contents
<a name="API_AdministrativeAction_Contents"></a>

 ** AdministrativeActionType **   <a name="FSx-Type-AdministrativeAction-AdministrativeActionType"></a>
Describes the type of administrative action, as follows:  
+  `FILE_SYSTEM_UPDATE` - A file system update administrative action initiated from the Amazon FSx console, API (`UpdateFileSystem`), or CLI (`update-file-system`).
+  `THROUGHPUT_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file system's throughput capacity has been completed successfully, a `THROUGHPUT_OPTIMIZATION` task starts.

  You can track the storage-optimization progress using the `ProgressPercent` property. When `THROUGHPUT_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED`. For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html) in the *Amazon FSx for Windows File Server User Guide*.
+  `STORAGE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file system's storage capacity has completed successfully, a `STORAGE_OPTIMIZATION` task starts. 
  + For Windows and ONTAP, storage optimization is the process of migrating the file system data to newer larger disks.
  + For Lustre, storage optimization consists of rebalancing the data across the existing and newly added file servers.

  You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED`. For more information, see [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html) in the *Amazon FSx for Windows File Server User Guide*, [Managing storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html) in the *Amazon FSx for Lustre User Guide*, and [Managing storage capacity and provisioned IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-storage-capacity.html) in the *Amazon FSx for NetApp ONTAP User Guide*.
+  `FILE_SYSTEM_ALIAS_ASSOCIATION` - A file system update to associate a new Domain Name System (DNS) alias with the file system. For more information, see [ AssociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AssociateFileSystemAliases.html).
+  `FILE_SYSTEM_ALIAS_DISASSOCIATION` - A file system update to disassociate a DNS alias from the file system. For more information, see [DisassociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DisassociateFileSystemAliases.html).
+  `IOPS_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file system's throughput capacity has been completed successfully, a `IOPS_OPTIMIZATION` task starts.

  You can track the storage-optimization progress using the `ProgressPercent` property. When `IOPS_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED`. For more information, see [Managing provisioned SSD IOPS](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-provisioned-ssd-iops.html) in the Amazon FSx for Windows File Server User Guide.
+  `STORAGE_TYPE_OPTIMIZATION` - After the `FILE_SYSTEM_UPDATE` task to increase a file system's throughput capacity has been completed successfully, a `STORAGE_TYPE_OPTIMIZATION` task starts.

  You can track the storage-optimization progress using the `ProgressPercent` property. When `STORAGE_TYPE_OPTIMIZATION` has been completed successfully, the parent `FILE_SYSTEM_UPDATE` action status changes to `COMPLETED`.
+  `VOLUME_UPDATE` - A volume update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateVolume`), or CLI (`update-volume`).
+  `VOLUME_RESTORE` - An Amazon FSx for OpenZFS volume is returned to the state saved by the specified snapshot, initiated from an API (`RestoreVolumeFromSnapshot`) or CLI (`restore-volume-from-snapshot`).
+  `SNAPSHOT_UPDATE` - A snapshot update to an Amazon FSx for OpenZFS volume initiated from the Amazon FSx console, API (`UpdateSnapshot`), or CLI (`update-snapshot`).
+  `RELEASE_NFS_V3_LOCKS` - Tracks the release of Network File System (NFS) V3 locks on an Amazon FSx for OpenZFS file system.
+  `DOWNLOAD_DATA_FROM_BACKUP` - An FSx for ONTAP backup is being restored to a new volume on a second-generation file system. Once the all the file metadata is loaded onto the volume, you can mount the volume with read-only access. during this process.
+  `VOLUME_INITIALIZE_WITH_SNAPSHOT` - A volume is being created from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CreateVolume`), or CLI (`create-volume`) when using the using the `FULL_COPY` strategy.
+  `VOLUME_UPDATE_WITH_SNAPSHOT` - A volume is being updated from a snapshot on a different FSx for OpenZFS file system. You can initiate this from the Amazon FSx console, API (`CopySnapshotAndUpdateVolume`), or CLI (`copy-snapshot-and-update-volume`).
Type: String  
Valid Values: `FILE_SYSTEM_UPDATE | STORAGE_OPTIMIZATION | FILE_SYSTEM_ALIAS_ASSOCIATION | FILE_SYSTEM_ALIAS_DISASSOCIATION | VOLUME_UPDATE | SNAPSHOT_UPDATE | RELEASE_NFS_V3_LOCKS | VOLUME_RESTORE | THROUGHPUT_OPTIMIZATION | IOPS_OPTIMIZATION | STORAGE_TYPE_OPTIMIZATION | MISCONFIGURED_STATE_RECOVERY | VOLUME_UPDATE_WITH_SNAPSHOT | VOLUME_INITIALIZE_WITH_SNAPSHOT | DOWNLOAD_DATA_FROM_BACKUP`   
Required: No

 ** FailureDetails **   <a name="FSx-Type-AdministrativeAction-FailureDetails"></a>
Provides information about a failed administrative action.  
Type: [AdministrativeActionFailureDetails](API_AdministrativeActionFailureDetails.md) object  
Required: No

 ** Message **   <a name="FSx-Type-AdministrativeAction-Message"></a>
A detailed error message.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** ProgressPercent **   <a name="FSx-Type-AdministrativeAction-ProgressPercent"></a>
The percentage-complete status of a `STORAGE_OPTIMIZATION` or `DOWNLOAD_DATA_FROM_BACKUP` administrative action. Does not apply to any other administrative action type.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** RemainingTransferBytes **   <a name="FSx-Type-AdministrativeAction-RemainingTransferBytes"></a>
The remaining bytes to transfer for the FSx for OpenZFS snapshot that you're copying.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

 ** RequestTime **   <a name="FSx-Type-AdministrativeAction-RequestTime"></a>
The time that the administrative action request was received.  
Type: Timestamp  
Required: No

 ** Status **   <a name="FSx-Type-AdministrativeAction-Status"></a>
The status of the administrative action, as follows:  
+  `FAILED` - Amazon FSx failed to process the administrative action successfully.
+  `IN_PROGRESS` - Amazon FSx is processing the administrative action.
+  `PENDING` - Amazon FSx is waiting to process the administrative action.
+  `COMPLETED` - Amazon FSx has finished processing the administrative task.

  For a backup restore to a second-generation FSx for ONTAP file system, indicates that all data has been downloaded to the volume, and clients now have read-write access to volume.
+  `UPDATED_OPTIMIZING` - For a storage-capacity increase update, Amazon FSx has updated the file system with the new storage capacity, and is now performing the storage-optimization process.
+  `PENDING` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that the file metadata is being downloaded onto the volume. The volume's Lifecycle state is CREATING.
+  `IN_PROGRESS` - For a backup restore to a second-generation FSx for ONTAP file system, indicates that all metadata has been downloaded to the new volume and client can access data with read-only access while Amazon FSx downloads the file data to the volume. Track the progress of this process with the `ProgressPercent` element.
Type: String  
Valid Values: `FAILED | IN_PROGRESS | PENDING | COMPLETED | UPDATED_OPTIMIZING | OPTIMIZING | PAUSED | CANCELLED`   
Required: No

 ** TargetFileSystemValues **   <a name="FSx-Type-AdministrativeAction-TargetFileSystemValues"></a>
The target value for the administration action, provided in the `UpdateFileSystem` operation. Returned for `FILE_SYSTEM_UPDATE` administrative actions.   
Type: [FileSystem](API_FileSystem.md) object  
Required: No

 ** TargetSnapshotValues **   <a name="FSx-Type-AdministrativeAction-TargetSnapshotValues"></a>
A snapshot of an Amazon FSx for OpenZFS volume.  
Type: [Snapshot](API_Snapshot.md) object  
Required: No

 ** TargetVolumeValues **   <a name="FSx-Type-AdministrativeAction-TargetVolumeValues"></a>
Describes an Amazon FSx volume.  
Type: [Volume](API_Volume.md) object  
Required: No

 ** TotalTransferBytes **   <a name="FSx-Type-AdministrativeAction-TotalTransferBytes"></a>
The number of bytes that have transferred for the FSx for OpenZFS snapshot that you're copying.  
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_AdministrativeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/AdministrativeAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/AdministrativeAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/AdministrativeAction) 