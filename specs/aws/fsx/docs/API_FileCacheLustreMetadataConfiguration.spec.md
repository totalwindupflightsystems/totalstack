---
id: "@specs/aws/fsx/docs/API_FileCacheLustreMetadataConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileCacheLustreMetadataConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileCacheLustreMetadataConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileCacheLustreMetadataConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileCacheLustreMetadataConfiguration
<a name="API_FileCacheLustreMetadataConfiguration"></a>

The configuration for a Lustre MDT (Metadata Target) storage volume. The metadata on Amazon File Cache is managed by a Lustre Metadata Server (MDS) while the actual metadata is persisted on an MDT.

## Contents
<a name="API_FileCacheLustreMetadataConfiguration_Contents"></a>

 ** StorageCapacity **   <a name="FSx-Type-FileCacheLustreMetadataConfiguration-StorageCapacity"></a>
The storage capacity of the Lustre MDT (Metadata Target) storage volume in gibibytes (GiB). The only supported value is `2400` GiB.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: Yes

## See Also
<a name="API_FileCacheLustreMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileCacheLustreMetadataConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileCacheLustreMetadataConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileCacheLustreMetadataConfiguration) 