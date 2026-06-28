---
id: "@specs/aws/fsx/docs/API_DeleteFileSystemWindowsResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFileSystemWindowsResponse"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteFileSystemWindowsResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteFileSystemWindowsResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFileSystemWindowsResponse
<a name="API_DeleteFileSystemWindowsResponse"></a>

The response object for the Microsoft Windows file system used in the `DeleteFileSystem` operation.

## Contents
<a name="API_DeleteFileSystemWindowsResponse_Contents"></a>

 ** FinalBackupId **   <a name="FSx-Type-DeleteFileSystemWindowsResponse-FinalBackupId"></a>
The ID of the final backup for this file system.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: No

 ** FinalBackupTags **   <a name="FSx-Type-DeleteFileSystemWindowsResponse-FinalBackupTags"></a>
The set of tags applied to the final backup.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## See Also
<a name="API_DeleteFileSystemWindowsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteFileSystemWindowsResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteFileSystemWindowsResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteFileSystemWindowsResponse) 