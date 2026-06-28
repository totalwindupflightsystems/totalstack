---
id: "@specs/aws/fsx/docs/API_SvmActiveDirectoryConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SvmActiveDirectoryConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# SvmActiveDirectoryConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_SvmActiveDirectoryConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SvmActiveDirectoryConfiguration
<a name="API_SvmActiveDirectoryConfiguration"></a>

Describes the Microsoft Active Directory (AD) directory configuration to which the FSx for ONTAP storage virtual machine (SVM) is joined. Note that account credentials are not returned in the response payload.

## Contents
<a name="API_SvmActiveDirectoryConfiguration_Contents"></a>

 ** NetBiosName **   <a name="FSx-Type-SvmActiveDirectoryConfiguration-NetBiosName"></a>
The NetBIOS name of the AD computer object to which the SVM is joined.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 15.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: No

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-SvmActiveDirectoryConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.  
Type: [SelfManagedActiveDirectoryAttributes](API_SelfManagedActiveDirectoryAttributes.md) object  
Required: No

## See Also
<a name="API_SvmActiveDirectoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SvmActiveDirectoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SvmActiveDirectoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SvmActiveDirectoryConfiguration) 