---
id: "@specs/aws/fsx/docs/API_OpenZFSPosixFileSystemUser"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenZFSPosixFileSystemUser"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OpenZFSPosixFileSystemUser

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OpenZFSPosixFileSystemUser
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenZFSPosixFileSystemUser
<a name="API_OpenZFSPosixFileSystemUser"></a>

The FSx for OpenZFS file system user that is used for authorizing all file access requests that are made using the S3 access point.

## Contents
<a name="API_OpenZFSPosixFileSystemUser_Contents"></a>

 ** Gid **   <a name="FSx-Type-OpenZFSPosixFileSystemUser-Gid"></a>
The GID of the file system user.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 4294967295.  
Required: Yes

 ** Uid **   <a name="FSx-Type-OpenZFSPosixFileSystemUser-Uid"></a>
The UID of the file system user.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 4294967295.  
Required: Yes

 ** SecondaryGids **   <a name="FSx-Type-OpenZFSPosixFileSystemUser-SecondaryGids"></a>
The list of secondary GIDs for the file system user.   
Type: Array of longs  
Array Members: Maximum number of 15 items.  
Valid Range: Minimum value of 0. Maximum value of 4294967295.  
Required: No

## See Also
<a name="API_OpenZFSPosixFileSystemUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSPosixFileSystemUser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSPosixFileSystemUser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSPosixFileSystemUser) 