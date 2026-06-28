---
id: "@specs/aws/fsx/docs/API_SelfManagedActiveDirectoryConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SelfManagedActiveDirectoryConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# SelfManagedActiveDirectoryConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_SelfManagedActiveDirectoryConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SelfManagedActiveDirectoryConfiguration
<a name="API_SelfManagedActiveDirectoryConfiguration"></a>

The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an FSx for ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory. For more information, see [ Using Amazon FSx for Windows with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html) or [Managing FSx for ONTAP SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html).

## Contents
<a name="API_SelfManagedActiveDirectoryConfiguration_Contents"></a>

 ** DnsIps **   <a name="FSx-Type-SelfManagedActiveDirectoryConfiguration-DnsIps"></a>
A list of IP addresses of DNS servers or domain controllers in the self-managed AD directory. FSx for ONTAP SVMs support up to three IP addresses, FSx for Windows supports up to two.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 3 items.  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: Yes

 ** DomainName **   <a name="FSx-Type-SelfManagedActiveDirectoryConfiguration-DomainName"></a>
The fully qualified domain name of the self-managed AD directory, such as `corp.example.com`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: Yes

 ** DomainJoinServiceAccountSecret **   <a name="FSx-Type-SelfManagedActiveDirectoryConfiguration-DomainJoinServiceAccountSecret"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret containing the self-managed Active Directory domain join service account credentials. When provided, Amazon FSx uses the credentials stored in this secret to join the file system to your self-managed Active Directory domain.  
The secret must contain two key-value pairs:  
+  `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME` - The username for the service account
+  `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD` - The password for the service account
For more information, see [ Using Amazon FSx for Windows with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-manage-prereqs.html) or [ Using Amazon FSx for ONTAP with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/self-manage-prereqs.html).  
Type: String  
Length Constraints: Minimum length of 64. Maximum length of 1024.  
Pattern: `^arn:[^:]{1,63}:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`   
Required: No

 ** FileSystemAdministratorsGroup **   <a name="FSx-Type-SelfManagedActiveDirectoryConfiguration-FileSystemAdministratorsGroup"></a>
(Optional) The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, setting audit controls (audit ACLs) on files and folders, and administering the file system remotely by using the FSx Remote PowerShell. The group that you specify must already exist in your domain. If you don't provide one, your AD domain's Domain Admins group is used.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`   
Required: No

 ** OrganizationalUnitDistinguishedName **   <a name="FSx-Type-SelfManagedActiveDirectoryConfiguration-OrganizationalUnitDistinguishedName"></a>
(Optional) The fully qualified distinguished name of the organizational unit within your self-managed AD directory. Amazon FSx only accepts OU as the direct parent of the file system. An example is `OU=FSx,DC=yourdomain,DC=corp,DC=com`. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253). If none is provided, the FSx file system is created in the default location of your self-managed AD directory.   
Only Organizational Unit (OU) objects can be the direct parent of the file system that you're creating.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,2000}$`   
Required: No

 ** Password **   <a name="FSx-Type-SelfManagedActiveDirectoryConfiguration-Password"></a>
The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^.{1,256}$`   
Required: No

 ** UserName **   <a name="FSx-Type-SelfManagedActiveDirectoryConfiguration-UserName"></a>
The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain. This account must have the permission to join computers to the domain in the organizational unit provided in `OrganizationalUnitDistinguishedName`, or in the default location of your AD domain.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`   
Required: No

## See Also
<a name="API_SelfManagedActiveDirectoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SelfManagedActiveDirectoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SelfManagedActiveDirectoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SelfManagedActiveDirectoryConfiguration) 