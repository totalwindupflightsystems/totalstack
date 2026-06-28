---
id: "@specs/aws/fsx/docs/API_DeleteFileSystemOpenZFSConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFileSystemOpenZFSConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteFileSystemOpenZFSConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteFileSystemOpenZFSConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFileSystemOpenZFSConfiguration
<a name="API_DeleteFileSystemOpenZFSConfiguration"></a>

The configuration object for the Amazon FSx for OpenZFS file system used in the `DeleteFileSystem` operation.

## Contents
<a name="API_DeleteFileSystemOpenZFSConfiguration_Contents"></a>

 ** FinalBackupTags **   <a name="FSx-Type-DeleteFileSystemOpenZFSConfiguration-FinalBackupTags"></a>
A list of tags to apply to the file system's final backup.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** Options **   <a name="FSx-Type-DeleteFileSystemOpenZFSConfiguration-Options"></a>
To delete a file system if there are child volumes present below the root volume, use the string `DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`. If your file system has child volumes and you don't use this option, the delete request will fail.  
Type: Array of strings  
Array Members: Maximum number of 1 item.  
Valid Values: `DELETE_CHILD_VOLUMES_AND_SNAPSHOTS`   
Required: No

 ** SkipFinalBackup **   <a name="FSx-Type-DeleteFileSystemOpenZFSConfiguration-SkipFinalBackup"></a>
By default, Amazon FSx for OpenZFS takes a final backup on your behalf when the `DeleteFileSystem` operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip taking a final backup, set this value to `true`.  
Type: Boolean  
Required: No

## See Also
<a name="API_DeleteFileSystemOpenZFSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileSystemOpenZFSConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileSystemOpenZFSConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileSystemOpenZFSConfiguration) 