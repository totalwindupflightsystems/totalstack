---
id: "@specs/aws/fsx/docs/API_SelfManagedActiveDirectoryAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SelfManagedActiveDirectoryAttributes"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# SelfManagedActiveDirectoryAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_SelfManagedActiveDirectoryAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SelfManagedActiveDirectoryAttributes
<a name="API_SelfManagedActiveDirectoryAttributes"></a>

The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

## Contents
<a name="API_SelfManagedActiveDirectoryAttributes_Contents"></a>

 ** DnsIps **   <a name="FSx-Type-SelfManagedActiveDirectoryAttributes-DnsIps"></a>
A list of IP addresses of DNS servers or domain controllers in the self-managed AD directory. FSx for ONTAP SVMs support up to three IP addresses, FSx for Windows supports up to two.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 3 items.  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: No

 ** DomainJoinServiceAccountSecret **   <a name="FSx-Type-SelfManagedActiveDirectoryAttributes-DomainJoinServiceAccountSecret"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the service account credentials used to join the file system to your self-managed Active Directory domain.  
Type: String  
Length Constraints: Minimum length of 64. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`   
Required: No

 ** DomainName **   <a name="FSx-Type-SelfManagedActiveDirectoryAttributes-DomainName"></a>
The fully qualified domain name of the self-managed AD directory.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: No

 ** FileSystemAdministratorsGroup **   <a name="FSx-Type-SelfManagedActiveDirectoryAttributes-FileSystemAdministratorsGroup"></a>
The name of the domain group whose members have administrative privileges for the FSx file system.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`   
Required: No

 ** OrganizationalUnitDistinguishedName **   <a name="FSx-Type-SelfManagedActiveDirectoryAttributes-OrganizationalUnitDistinguishedName"></a>
The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,2000}$`   
Required: No

 ** UserName **   <a name="FSx-Type-SelfManagedActiveDirectoryAttributes-UserName"></a>
The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`   
Required: No

## See Also
<a name="API_SelfManagedActiveDirectoryAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SelfManagedActiveDirectoryAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SelfManagedActiveDirectoryAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SelfManagedActiveDirectoryAttributes) 