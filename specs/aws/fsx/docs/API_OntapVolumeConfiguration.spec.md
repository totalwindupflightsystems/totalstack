---
id: "@specs/aws/fsx/docs/API_OntapVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OntapVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OntapVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OntapVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OntapVolumeConfiguration
<a name="API_OntapVolumeConfiguration"></a>

The configuration of an Amazon FSx for NetApp ONTAP volume.

## Contents
<a name="API_OntapVolumeConfiguration_Contents"></a>

 ** AggregateConfiguration **   <a name="FSx-Type-OntapVolumeConfiguration-AggregateConfiguration"></a>
This structure specifies configuration options for a volume’s storage aggregate or aggregates.  
Type: [AggregateConfiguration](API_AggregateConfiguration.md) object  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-OntapVolumeConfiguration-CopyTagsToBackups"></a>
A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If it's set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.  
Type: Boolean  
Required: No

 ** FlexCacheEndpointType **   <a name="FSx-Type-OntapVolumeConfiguration-FlexCacheEndpointType"></a>
Specifies the FlexCache endpoint type of the volume. Valid values are the following:  
+  `NONE` specifies that the volume doesn't have a FlexCache configuration. `NONE` is the default.
+  `ORIGIN` specifies that the volume is the origin volume for a FlexCache volume.
+  `CACHE` specifies that the volume is a FlexCache volume.
Type: String  
Valid Values: `NONE | ORIGIN | CACHE`   
Required: No

 ** JunctionPath **   <a name="FSx-Type-OntapVolumeConfiguration-JunctionPath"></a>
Specifies the directory that network-attached storage (NAS) clients use to mount the volume, along with the storage virtual machine (SVM) Domain Name System (DNS) name or IP address. You can create a `JunctionPath` directly below a parent volume junction or on a directory within a volume. A `JunctionPath` for a volume named `vol3` might be `/vol1/vol2/vol3`, or `/vol1/dir2/vol3`, or even `/dir1/dir2/vol3`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: No

 ** OntapVolumeType **   <a name="FSx-Type-OntapVolumeConfiguration-OntapVolumeType"></a>
Specifies the type of volume. Valid values are the following:  
+  `RW` specifies a read/write volume. `RW` is the default.
+  `DP` specifies a data-protection volume. You can protect data by replicating it to data-protection mirror copies. If a disaster occurs, you can use these data-protection mirror copies to recover data.
+  `LS` specifies a load-sharing mirror volume. A load-sharing mirror reduces the network traffic to a FlexVol volume by providing additional read-only access to clients.
Type: String  
Valid Values: `RW | DP | LS`   
Required: No

 ** SecurityStyle **   <a name="FSx-Type-OntapVolumeConfiguration-SecurityStyle"></a>
The security style for the volume, which can be `UNIX`, `NTFS`, or `MIXED`.  
Type: String  
Valid Values: `UNIX | NTFS | MIXED`   
Required: No

 ** SizeInBytes **   <a name="FSx-Type-OntapVolumeConfiguration-SizeInBytes"></a>
The configured size of the volume, in bytes.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 22517998000000000.  
Required: No

 ** SizeInMegabytes **   <a name="FSx-Type-OntapVolumeConfiguration-SizeInMegabytes"></a>
The configured size of the volume, in megabytes (MBs).  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** SnaplockConfiguration **   <a name="FSx-Type-OntapVolumeConfiguration-SnaplockConfiguration"></a>
The SnapLock configuration object for an FSx for ONTAP SnapLock volume.   
Type: [SnaplockConfiguration](API_SnaplockConfiguration.md) object  
Required: No

 ** SnapshotPolicy **   <a name="FSx-Type-OntapVolumeConfiguration-SnapshotPolicy"></a>
Specifies the snapshot policy for the volume. There are three built-in snapshot policies:  
+  `default`: This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
+  `default-1weekly`: This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
+  `none`: This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.
You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.  
For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the Amazon FSx for NetApp ONTAP User Guide.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** StorageEfficiencyEnabled **   <a name="FSx-Type-OntapVolumeConfiguration-StorageEfficiencyEnabled"></a>
The volume's storage efficiency setting.  
Type: Boolean  
Required: No

 ** StorageVirtualMachineId **   <a name="FSx-Type-OntapVolumeConfiguration-StorageVirtualMachineId"></a>
The ID of the volume's storage virtual machine.  
Type: String  
Length Constraints: Fixed length of 21.  
Pattern: `^(svm-[0-9a-f]{17,})$`   
Required: No

 ** StorageVirtualMachineRoot **   <a name="FSx-Type-OntapVolumeConfiguration-StorageVirtualMachineRoot"></a>
A Boolean flag indicating whether this volume is the root volume for its storage virtual machine (SVM). Only one volume on an SVM can be the root volume. This value defaults to `false`. If this value is `true`, then this is the SVM root volume.  
This flag is useful when you're deleting an SVM, because you must first delete all non-root volumes. This flag, when set to `false`, helps you identify which volumes to delete before you can delete the SVM.  
Type: Boolean  
Required: No

 ** TieringPolicy **   <a name="FSx-Type-OntapVolumeConfiguration-TieringPolicy"></a>
The volume's `TieringPolicy` setting.  
Type: [TieringPolicy](API_TieringPolicy.md) object  
Required: No

 ** UUID **   <a name="FSx-Type-OntapVolumeConfiguration-UUID"></a>
The volume's universally unique identifier (UUID).  
Type: String  
Length Constraints: Maximum length of 36.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`   
Required: No

 ** VolumeStyle **   <a name="FSx-Type-OntapVolumeConfiguration-VolumeStyle"></a>
Use to specify the style of an ONTAP volume. For more information about FlexVols and FlexGroups, see [Volume types](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-types.html) in Amazon FSx for NetApp ONTAP User Guide.  
Type: String  
Valid Values: `FLEXVOL | FLEXGROUP`   
Required: No

## See Also
<a name="API_OntapVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OntapVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OntapVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OntapVolumeConfiguration) 