---
id: "@specs/aws/fsx/docs/API_OntapWindowsFileSystemUser"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OntapWindowsFileSystemUser"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OntapWindowsFileSystemUser

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OntapWindowsFileSystemUser
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OntapWindowsFileSystemUser
<a name="API_OntapWindowsFileSystemUser"></a>

The FSx for ONTAP Windows file system user that is used for authorizing all file access requests that are made using the S3 access point.

## Contents
<a name="API_OntapWindowsFileSystemUser_Contents"></a>

 ** Name **   <a name="FSx-Type-OntapWindowsFileSystemUser-Name"></a>
The name of the Windows user. The name can be up to 256 characters long and supports Active Directory users.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`   
Required: Yes

## See Also
<a name="API_OntapWindowsFileSystemUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OntapWindowsFileSystemUser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OntapWindowsFileSystemUser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OntapWindowsFileSystemUser) 