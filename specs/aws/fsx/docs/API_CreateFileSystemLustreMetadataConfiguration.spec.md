---
id: "@specs/aws/fsx/docs/API_CreateFileSystemLustreMetadataConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileSystemLustreMetadataConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileSystemLustreMetadataConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileSystemLustreMetadataConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileSystemLustreMetadataConfiguration
<a name="API_CreateFileSystemLustreMetadataConfiguration"></a>

The Lustre metadata performance configuration for the creation of an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type. The configuration uses a Metadata IOPS value to set the maximum rate of metadata disk IOPS supported by the file system.

After creation, the file system supports increasing metadata performance. For more information on Metadata IOPS, see [Lustre metadata performance configuration](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-metadata-performance.html#metadata-configuration) in the *Amazon FSx for Lustre User Guide*.

## Contents
<a name="API_CreateFileSystemLustreMetadataConfiguration_Contents"></a>

 ** Mode **   <a name="FSx-Type-CreateFileSystemLustreMetadataConfiguration-Mode"></a>
The metadata configuration mode for provisioning Metadata IOPS for an FSx for Lustre file system using a `PERSISTENT_2` deployment type.  
+ In AUTOMATIC mode (supported only on SSD file systems), FSx for Lustre automatically provisions and scales the number of Metadata IOPS for your file system based on your file system storage capacity.
+ In USER\_PROVISIONED mode, you specify the number of Metadata IOPS to provision for your file system.
Type: String  
Valid Values: `AUTOMATIC | USER_PROVISIONED`   
Required: Yes

 ** Iops **   <a name="FSx-Type-CreateFileSystemLustreMetadataConfiguration-Iops"></a>
(USER\_PROVISIONED mode only) Specifies the number of Metadata IOPS to provision for the file system. This parameter sets the maximum rate of metadata disk IOPS supported by the file system.  
+ For SSD file systems, valid values are `1500`, `3000`, `6000`, `12000`, and multiples of `12000` up to a maximum of `192000`.
+ For Intelligent-Tiering file systems, valid values are `6000` and `12000`.
 `Iops` doesn’t have a default value. If you're using USER\_PROVISIONED mode, you can choose to specify a valid value. If you're using AUTOMATIC mode, you cannot specify a value because FSx for Lustre automatically sets the value based on your file system storage capacity. 
Type: Integer  
Valid Range: Minimum value of 1500. Maximum value of 192000.  
Required: No

## See Also
<a name="API_CreateFileSystemLustreMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileSystemLustreMetadataConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileSystemLustreMetadataConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileSystemLustreMetadataConfiguration) 