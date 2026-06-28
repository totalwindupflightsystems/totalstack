---
id: "@specs/aws/fsx/docs/API_DeleteFileSystemLustreConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFileSystemLustreConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteFileSystemLustreConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteFileSystemLustreConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFileSystemLustreConfiguration
<a name="API_DeleteFileSystemLustreConfiguration"></a>

The configuration object for the Amazon FSx for Lustre file system being deleted in the `DeleteFileSystem` operation.

## Contents
<a name="API_DeleteFileSystemLustreConfiguration_Contents"></a>

 ** FinalBackupTags **   <a name="FSx-Type-DeleteFileSystemLustreConfiguration-FinalBackupTags"></a>
Use if `SkipFinalBackup` is set to `false`, and you want to apply an array of tags to the final backup. If you have set the file system property `CopyTagsToBackups` to true, and you specify one or more `FinalBackupTags` when deleting a file system, Amazon FSx will not copy any existing file system tags to the backup.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** SkipFinalBackup **   <a name="FSx-Type-DeleteFileSystemLustreConfiguration-SkipFinalBackup"></a>
Set `SkipFinalBackup` to false if you want to take a final backup of the file system you are deleting. By default, Amazon FSx will not take a final backup on your behalf when the `DeleteFileSystem` operation is invoked. (Default = true)  
The `fsx:CreateBackup` permission is required if you set `SkipFinalBackup` to `false` in order to delete the file system and take a final backup.
Type: Boolean  
Required: No

## See Also
<a name="API_DeleteFileSystemLustreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileSystemLustreConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileSystemLustreConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileSystemLustreConfiguration) 