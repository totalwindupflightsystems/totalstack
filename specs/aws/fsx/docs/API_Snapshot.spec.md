---
id: "@specs/aws/fsx/docs/API_Snapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Snapshot"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# Snapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_Snapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Snapshot
<a name="API_Snapshot"></a>

A snapshot of an Amazon FSx for OpenZFS volume.

## Contents
<a name="API_Snapshot_Contents"></a>

 ** AdministrativeActions **   <a name="FSx-Type-Snapshot-AdministrativeActions"></a>
A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system.  
Type: Array of [AdministrativeAction](API_AdministrativeAction.md) objects  
Array Members: Maximum number of 50 items.  
Required: No

 ** CreationTime **   <a name="FSx-Type-Snapshot-CreationTime"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.  
Type: Timestamp  
Required: No

 ** Lifecycle **   <a name="FSx-Type-Snapshot-Lifecycle"></a>
The lifecycle status of the snapshot.  
+  `PENDING` - Amazon FSx hasn't started creating the snapshot.
+  `CREATING` - Amazon FSx is creating the snapshot.
+  `DELETING` - Amazon FSx is deleting the snapshot.
+  `AVAILABLE` - The snapshot is fully available.
Type: String  
Valid Values: `PENDING | CREATING | DELETING | AVAILABLE`   
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-Snapshot-LifecycleTransitionReason"></a>
Describes why a resource lifecycle state changed.  
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object  
Required: No

 ** Name **   <a name="FSx-Type-Snapshot-Name"></a>
The name of the snapshot.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 203.  
Pattern: `^[a-zA-Z0-9_:.-]{1,203}$`   
Required: No

 ** ResourceARN **   <a name="FSx-Type-Snapshot-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** SnapshotId **   <a name="FSx-Type-Snapshot-SnapshotId"></a>
The ID of the snapshot.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 28.  
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`   
Required: No

 ** Tags **   <a name="FSx-Type-Snapshot-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** VolumeId **   <a name="FSx-Type-Snapshot-VolumeId"></a>
The ID of the volume that the snapshot is of.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: No

## See Also
<a name="API_Snapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/Snapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/Snapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/Snapshot) 