---
id: "@specs/aws/fsx/docs/API_DeleteFileSystemWindowsConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFileSystemWindowsConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteFileSystemWindowsConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteFileSystemWindowsConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFileSystemWindowsConfiguration
<a name="API_DeleteFileSystemWindowsConfiguration"></a>

The configuration object for the Microsoft Windows file system used in the `DeleteFileSystem` operation.

## Contents
<a name="API_DeleteFileSystemWindowsConfiguration_Contents"></a>

 ** FinalBackupTags **   <a name="FSx-Type-DeleteFileSystemWindowsConfiguration-FinalBackupTags"></a>
A set of tags for your final backup.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** SkipFinalBackup **   <a name="FSx-Type-DeleteFileSystemWindowsConfiguration-SkipFinalBackup"></a>
By default, Amazon FSx for Windows takes a final backup on your behalf when the `DeleteFileSystem` operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip this backup, use this flag to do so.  
Type: Boolean  
Required: No

## See Also
<a name="API_DeleteFileSystemWindowsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileSystemWindowsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileSystemWindowsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileSystemWindowsConfiguration) 