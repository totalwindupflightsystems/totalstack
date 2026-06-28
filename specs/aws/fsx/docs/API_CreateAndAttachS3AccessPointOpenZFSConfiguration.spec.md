---
id: "@specs/aws/fsx/docs/API_CreateAndAttachS3AccessPointOpenZFSConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAndAttachS3AccessPointOpenZFSConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateAndAttachS3AccessPointOpenZFSConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateAndAttachS3AccessPointOpenZFSConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAndAttachS3AccessPointOpenZFSConfiguration
<a name="API_CreateAndAttachS3AccessPointOpenZFSConfiguration"></a>

Specifies the FSx for OpenZFS volume that the S3 access point will be attached to, and the file system user identity.

## Contents
<a name="API_CreateAndAttachS3AccessPointOpenZFSConfiguration_Contents"></a>

 ** FileSystemIdentity **   <a name="FSx-Type-CreateAndAttachS3AccessPointOpenZFSConfiguration-FileSystemIdentity"></a>
Specifies the file system user identity to use for authorizing file read and write requests that are made using this S3 access point.  
Type: [OpenZFSFileSystemIdentity](API_OpenZFSFileSystemIdentity.md) object  
Required: Yes

 ** VolumeId **   <a name="FSx-Type-CreateAndAttachS3AccessPointOpenZFSConfiguration-VolumeId"></a>
The ID of the FSx for OpenZFS volume to which you want the S3 access point attached.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: Yes

## See Also
<a name="API_CreateAndAttachS3AccessPointOpenZFSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateAndAttachS3AccessPointOpenZFSConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateAndAttachS3AccessPointOpenZFSConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateAndAttachS3AccessPointOpenZFSConfiguration) 