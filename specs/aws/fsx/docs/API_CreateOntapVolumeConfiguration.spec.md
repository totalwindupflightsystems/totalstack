---
id: "@specs/aws/fsx/docs/API_CreateOntapVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateOntapVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateOntapVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateOntapVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateOntapVolumeConfiguration
<a name="API_CreateOntapVolumeConfiguration"></a>

Specifies the configuration of the ONTAP volume that you are creating.

## Contents
<a name="API_CreateOntapVolumeConfiguration_Contents"></a>

 ** StorageVirtualMachineId **   <a name="FSx-Type-CreateOntapVolumeConfiguration-StorageVirtualMachineId"></a>
Specifies the ONTAP SVM in which to create the volume.  
Type: String  
Length Constraints: Fixed length of 21.  
Pattern: `^(svm-[0-9a-f]{17,})$`   
Required: Yes

 ** AggregateConfiguration **   <a name="FSx-Type-CreateOntapVolumeConfiguration-AggregateConfiguration"></a>
Use to specify configuration options for a volume’s storage aggregate or aggregates.  
Type: [CreateAggregateConfiguration](API_CreateAggregateConfiguration.md) object  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-CreateOntapVolumeConfiguration-CopyTagsToBackups"></a>
A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If it's set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.  
Type: Boolean  
Required: No

 ** JunctionPath **   <a name="FSx-Type-CreateOntapVolumeConfiguration-JunctionPath"></a>
Specifies the location in the SVM's namespace where the volume is mounted. This parameter is required. The `JunctionPath` must have a leading forward slash, such as `/vol3`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: No

 ** OntapVolumeType **   <a name="FSx-Type-CreateOntapVolumeConfiguration-OntapVolumeType"></a>
Specifies the type of volume you are creating. Valid values are the following:  
+  `RW` specifies a read/write volume. `RW` is the default.
+  `DP` specifies a data-protection volume. A `DP` volume is read-only and can be used as the destination of a NetApp SnapMirror relationship.
For more information, see [Volume types](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-types) in the Amazon FSx for NetApp ONTAP User Guide.  
Type: String  
Valid Values: `RW | DP`   
Required: No

 ** SecurityStyle **   <a name="FSx-Type-CreateOntapVolumeConfiguration-SecurityStyle"></a>
Specifies the security style for the volume. If a volume's security style is not specified, it is automatically set to the root volume's security style. The security style determines the type of permissions that FSx for ONTAP uses to control data access. Specify one of the following values:  
+  `UNIX` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account. 
+  `NTFS` if the file system is managed by a Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Windows user as the service account.
+  `MIXED` This is an advanced setting. For more information, see the topic [What the security styles and their effects are](https://docs.netapp.com/us-en/ontap/nfs-admin/security-styles-their-effects-concept.html) in the NetApp Documentation Center.
For more information, see [Volume security style](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-security-style) in the FSx for ONTAP User Guide.  
Type: String  
Valid Values: `UNIX | NTFS | MIXED`   
Required: No

 ** SizeInBytes **   <a name="FSx-Type-CreateOntapVolumeConfiguration-SizeInBytes"></a>
Specifies the configured size of the volume, in bytes.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 22517998000000000.  
Required: No

 ** SizeInMegabytes **   <a name="FSx-Type-CreateOntapVolumeConfiguration-SizeInMegabytes"></a>
 *This member has been deprecated.*   
Use `SizeInBytes` instead. Specifies the size of the volume, in megabytes (MB), that you are creating.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** SnaplockConfiguration **   <a name="FSx-Type-CreateOntapVolumeConfiguration-SnaplockConfiguration"></a>
Specifies the SnapLock configuration for an FSx for ONTAP volume.   
Type: [CreateSnaplockConfiguration](API_CreateSnaplockConfiguration.md) object  
Required: No

 ** SnapshotPolicy **   <a name="FSx-Type-CreateOntapVolumeConfiguration-SnapshotPolicy"></a>
Specifies the snapshot policy for the volume. There are three built-in snapshot policies:  
+  `default`: This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
+  `default-1weekly`: This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
+  `none`: This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.
You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.  
For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the Amazon FSx for NetApp ONTAP User Guide.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** StorageEfficiencyEnabled **   <a name="FSx-Type-CreateOntapVolumeConfiguration-StorageEfficiencyEnabled"></a>
Set to true to enable deduplication, compression, and compaction storage efficiency features on the volume, or set to false to disable them.  
 `StorageEfficiencyEnabled` is required when creating a `RW` volume (`OntapVolumeType` set to `RW`).  
Type: Boolean  
Required: No

 ** TieringPolicy **   <a name="FSx-Type-CreateOntapVolumeConfiguration-TieringPolicy"></a>
Describes the data tiering policy for an ONTAP volume. When enabled, Amazon FSx for ONTAP's intelligent tiering automatically transitions a volume's data between the file system's primary storage and capacity pool storage based on your access patterns.  
Valid tiering policies are the following:  
+  `SNAPSHOT_ONLY` - (Default value) moves cold snapshots to the capacity pool storage tier.
+  `AUTO` - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.
+  `ALL` - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.
+  `NONE` - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.
Type: [TieringPolicy](API_TieringPolicy.md) object  
Required: No

 ** VolumeStyle **   <a name="FSx-Type-CreateOntapVolumeConfiguration-VolumeStyle"></a>
Use to specify the style of an ONTAP volume. FSx for ONTAP offers two styles of volumes that you can use for different purposes, FlexVol and FlexGroup volumes. For more information, see [Volume styles](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-styles) in the Amazon FSx for NetApp ONTAP User Guide.  
Type: String  
Valid Values: `FLEXVOL | FLEXGROUP`   
Required: No

## See Also
<a name="API_CreateOntapVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateOntapVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateOntapVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateOntapVolumeConfiguration) 