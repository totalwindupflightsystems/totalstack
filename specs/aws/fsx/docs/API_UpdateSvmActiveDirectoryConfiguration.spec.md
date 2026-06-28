---
id: "@specs/aws/fsx/docs/API_UpdateSvmActiveDirectoryConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSvmActiveDirectoryConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateSvmActiveDirectoryConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateSvmActiveDirectoryConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSvmActiveDirectoryConfiguration
<a name="API_UpdateSvmActiveDirectoryConfiguration"></a>

Specifies updates to an FSx for ONTAP storage virtual machine's (SVM) Microsoft Active Directory (AD) configuration. Note that account credentials are not returned in the response payload.

## Contents
<a name="API_UpdateSvmActiveDirectoryConfiguration_Contents"></a>

 ** NetBiosName **   <a name="FSx-Type-UpdateSvmActiveDirectoryConfiguration-NetBiosName"></a>
Specifies an updated NetBIOS name of the AD computer object `NetBiosName` to which an SVM is joined.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 15.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: No

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-UpdateSvmActiveDirectoryConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
Specifies changes you are making to the self-managed Microsoft Active Directory configuration to which an FSx for Windows File Server file system or an FSx for ONTAP SVM is joined.  
Type: [SelfManagedActiveDirectoryConfigurationUpdates](API_SelfManagedActiveDirectoryConfigurationUpdates.md) object  
Required: No

## See Also
<a name="API_UpdateSvmActiveDirectoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateSvmActiveDirectoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateSvmActiveDirectoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateSvmActiveDirectoryConfiguration) 