---
id: "@specs/aws/fsx/docs/API_CreateSvmActiveDirectoryConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSvmActiveDirectoryConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateSvmActiveDirectoryConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateSvmActiveDirectoryConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSvmActiveDirectoryConfiguration
<a name="API_CreateSvmActiveDirectoryConfiguration"></a>

The configuration that Amazon FSx uses to join the ONTAP storage virtual machine (SVM) to your self-managed (including on-premises) Microsoft Active Directory directory.

## Contents
<a name="API_CreateSvmActiveDirectoryConfiguration_Contents"></a>

 ** NetBiosName **   <a name="FSx-Type-CreateSvmActiveDirectoryConfiguration-NetBiosName"></a>
The NetBIOS name of the Active Directory computer object that will be created for your SVM.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 15.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: Yes

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-CreateSvmActiveDirectoryConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an FSx for ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory. For more information, see [ Using Amazon FSx for Windows with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html) or [Managing FSx for ONTAP SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html).  
Type: [SelfManagedActiveDirectoryConfiguration](API_SelfManagedActiveDirectoryConfiguration.md) object  
Required: No

## See Also
<a name="API_CreateSvmActiveDirectoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateSvmActiveDirectoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateSvmActiveDirectoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateSvmActiveDirectoryConfiguration) 