---
id: "@specs/aws/fsx/docs/API_CreateOpenZFSOriginSnapshotConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateOpenZFSOriginSnapshotConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateOpenZFSOriginSnapshotConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateOpenZFSOriginSnapshotConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateOpenZFSOriginSnapshotConfiguration
<a name="API_CreateOpenZFSOriginSnapshotConfiguration"></a>

The snapshot configuration to use when creating an Amazon FSx for OpenZFS volume from a snapshot. 

## Contents
<a name="API_CreateOpenZFSOriginSnapshotConfiguration_Contents"></a>

 ** CopyStrategy **   <a name="FSx-Type-CreateOpenZFSOriginSnapshotConfiguration-CopyStrategy"></a>
Specifies the strategy used when copying data from the snapshot to the new volume.   
+  `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesn't consume disk throughput. However, the origin snapshot can't be deleted if there is a volume using its copied data.
+  `FULL_COPY` - Copies all data from the snapshot to the new volume.

  Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.
The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html).
Type: String  
Valid Values: `CLONE | FULL_COPY | INCREMENTAL_COPY`   
Required: Yes

 ** SnapshotARN **   <a name="FSx-Type-CreateOpenZFSOriginSnapshotConfiguration-SnapshotARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: Yes

## See Also
<a name="API_CreateOpenZFSOriginSnapshotConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateOpenZFSOriginSnapshotConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateOpenZFSOriginSnapshotConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateOpenZFSOriginSnapshotConfiguration) 