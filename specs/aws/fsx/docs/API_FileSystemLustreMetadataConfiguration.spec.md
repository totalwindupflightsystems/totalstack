---
id: "@specs/aws/fsx/docs/API_FileSystemLustreMetadataConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileSystemLustreMetadataConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileSystemLustreMetadataConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileSystemLustreMetadataConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileSystemLustreMetadataConfiguration
<a name="API_FileSystemLustreMetadataConfiguration"></a>

The Lustre metadata performance configuration of an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type. The configuration enables the file system to support increasing metadata performance.

## Contents
<a name="API_FileSystemLustreMetadataConfiguration_Contents"></a>

 ** Mode **   <a name="FSx-Type-FileSystemLustreMetadataConfiguration-Mode"></a>
The metadata configuration mode for provisioning Metadata IOPS for the file system.  
+ In AUTOMATIC mode (supported only on SSD file systems), FSx for Lustre automatically provisions and scales the number of Metadata IOPS on your file system based on your file system storage capacity.
+ In USER\_PROVISIONED mode, you can choose to specify the number of Metadata IOPS to provision for your file system.
Type: String  
Valid Values: `AUTOMATIC | USER_PROVISIONED`   
Required: Yes

 ** Iops **   <a name="FSx-Type-FileSystemLustreMetadataConfiguration-Iops"></a>
The number of Metadata IOPS provisioned for the file system.  
+ For SSD file systems, valid values are `1500`, `3000`, `6000`, `12000`, and multiples of `12000` up to a maximum of `192000`.
+ For Intelligent-Tiering file systems, valid values are `6000` and `12000`.
Type: Integer  
Valid Range: Minimum value of 1500. Maximum value of 192000.  
Required: No

## See Also
<a name="API_FileSystemLustreMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileSystemLustreMetadataConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileSystemLustreMetadataConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileSystemLustreMetadataConfiguration) 