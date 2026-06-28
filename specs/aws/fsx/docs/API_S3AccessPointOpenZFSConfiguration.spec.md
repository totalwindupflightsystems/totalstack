---
id: "@specs/aws/fsx/docs/API_S3AccessPointOpenZFSConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3AccessPointOpenZFSConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# S3AccessPointOpenZFSConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_S3AccessPointOpenZFSConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3AccessPointOpenZFSConfiguration
<a name="API_S3AccessPointOpenZFSConfiguration"></a>

Describes the FSx for OpenZFS attachment configuration of an S3 access point attachment.

## Contents
<a name="API_S3AccessPointOpenZFSConfiguration_Contents"></a>

 ** FileSystemIdentity **   <a name="FSx-Type-S3AccessPointOpenZFSConfiguration-FileSystemIdentity"></a>
The file system identity used to authorize file access requests made using the S3 access point.  
Type: [OpenZFSFileSystemIdentity](API_OpenZFSFileSystemIdentity.md) object  
Required: No

 ** VolumeId **   <a name="FSx-Type-S3AccessPointOpenZFSConfiguration-VolumeId"></a>
The ID of the FSx for OpenZFS volume that the S3 access point is attached to.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: No

## See Also
<a name="API_S3AccessPointOpenZFSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3AccessPointOpenZFSConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3AccessPointOpenZFSConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3AccessPointOpenZFSConfiguration) 