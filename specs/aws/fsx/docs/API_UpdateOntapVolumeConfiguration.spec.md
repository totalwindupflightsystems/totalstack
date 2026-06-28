---
id: "@specs/aws/fsx/docs/API_UpdateOntapVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateOntapVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateOntapVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateOntapVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateOntapVolumeConfiguration
<a name="API_UpdateOntapVolumeConfiguration"></a>

Used to specify changes to the ONTAP configuration for the volume you are updating.

## Contents
<a name="API_UpdateOntapVolumeConfiguration_Contents"></a>

 ** CopyTagsToBackups **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-CopyTagsToBackups"></a>
A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If it's set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.  
Type: Boolean  
Required: No

 ** JunctionPath **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-JunctionPath"></a>
Specifies the location in the SVM's namespace where the volume is mounted. The `JunctionPath` must have a leading forward slash, such as `/vol3`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: No

 ** SecurityStyle **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-SecurityStyle"></a>
The security style for the volume, which can be `UNIX`, `NTFS`, or `MIXED`.  
Type: String  
Valid Values: `UNIX | NTFS | MIXED`   
Required: No

 ** SizeInBytes **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-SizeInBytes"></a>
The configured size of the volume, in bytes.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 22517998000000000.  
Required: No

 ** SizeInMegabytes **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-SizeInMegabytes"></a>
Specifies the size of the volume in megabytes.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** SnaplockConfiguration **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-SnaplockConfiguration"></a>
The configuration object for updating the SnapLock configuration of an FSx for ONTAP SnapLock volume.   
Type: [UpdateSnaplockConfiguration](API_UpdateSnaplockConfiguration.md) object  
Required: No

 ** SnapshotPolicy **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-SnapshotPolicy"></a>
Specifies the snapshot policy for the volume. There are three built-in snapshot policies:  
+  `default`: This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.
+  `default-1weekly`: This policy is the same as the `default` policy except that it only retains one snapshot from the weekly schedule.
+  `none`: This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.
You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.  
For more information, see [Snapshot policies](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies) in the *Amazon FSx for NetApp ONTAP User Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** StorageEfficiencyEnabled **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-StorageEfficiencyEnabled"></a>
Default is `false`. Set to true to enable the deduplication, compression, and compaction storage efficiency features on the volume.  
Type: Boolean  
Required: No

 ** TieringPolicy **   <a name="FSx-Type-UpdateOntapVolumeConfiguration-TieringPolicy"></a>
Update the volume's data tiering policy.  
Type: [TieringPolicy](API_TieringPolicy.md) object  
Required: No

## See Also
<a name="API_UpdateOntapVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateOntapVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateOntapVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateOntapVolumeConfiguration) 