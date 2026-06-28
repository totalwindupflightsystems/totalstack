---
id: "@specs/aws/fsx/docs/API_DeleteVolumeOntapConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteVolumeOntapConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteVolumeOntapConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteVolumeOntapConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteVolumeOntapConfiguration
<a name="API_DeleteVolumeOntapConfiguration"></a>

Use to specify skipping a final backup, adding tags to a final backup, or bypassing the retention period of an FSx for ONTAP SnapLock Enterprise volume when deleting an FSx for ONTAP volume. 

## Contents
<a name="API_DeleteVolumeOntapConfiguration_Contents"></a>

 ** BypassSnaplockEnterpriseRetention **   <a name="FSx-Type-DeleteVolumeOntapConfiguration-BypassSnaplockEnterpriseRetention"></a>
Setting this to `true` allows a SnapLock administrator to delete an FSx for ONTAP SnapLock Enterprise volume with unexpired write once, read many (WORM) files. The IAM permission `fsx:BypassSnaplockEnterpriseRetention` is also required to delete SnapLock Enterprise volumes with unexpired WORM files. The default value is `false`.   
For more information, see [ Deleting a SnapLock volume](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-delete-volume.html).   
Type: Boolean  
Required: No

 ** FinalBackupTags **   <a name="FSx-Type-DeleteVolumeOntapConfiguration-FinalBackupTags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** SkipFinalBackup **   <a name="FSx-Type-DeleteVolumeOntapConfiguration-SkipFinalBackup"></a>
Set to true if you want to skip taking a final backup of the volume you are deleting.  
Type: Boolean  
Required: No

## See Also
<a name="API_DeleteVolumeOntapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteVolumeOntapConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteVolumeOntapConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteVolumeOntapConfiguration) 