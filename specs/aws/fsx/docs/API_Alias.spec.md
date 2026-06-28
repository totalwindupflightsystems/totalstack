---
id: "@specs/aws/fsx/docs/API_Alias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Alias"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# Alias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_Alias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Alias
<a name="API_Alias"></a>

A DNS alias that is associated with the file system. You can use a DNS alias to access a file system using user-defined DNS names, in addition to the default DNS name that Amazon FSx assigns to the file system. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) in the *FSx for Windows File Server User Guide*.

## Contents
<a name="API_Alias_Contents"></a>

 ** Lifecycle **   <a name="FSx-Type-Alias-Lifecycle"></a>
Describes the state of the DNS alias.  
+ AVAILABLE - The DNS alias is associated with an Amazon FSx file system.
+ CREATING - Amazon FSx is creating the DNS alias and associating it with the file system.
+ CREATE\_FAILED - Amazon FSx was unable to associate the DNS alias with the file system.
+ DELETING - Amazon FSx is disassociating the DNS alias from the file system and deleting it.
+ DELETE\_FAILED - Amazon FSx was unable to disassociate the DNS alias from the file system.
Type: String  
Valid Values: `AVAILABLE | CREATING | DELETING | CREATE_FAILED | DELETE_FAILED`   
Required: No

 ** Name **   <a name="FSx-Type-Alias-Name"></a>
The name of the DNS alias. The alias name has to meet the following requirements:  
+ Formatted as a fully-qualified domain name (FQDN), `hostname.domain`, for example, `accounting.example.com`.
+ Can contain alphanumeric characters, the underscore (\_), and the hyphen (-).
+ Cannot start or end with a hyphen.
+ Can start with a numeric.
For DNS names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 253.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,253}$`   
Required: No

## See Also
<a name="API_Alias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/Alias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/Alias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/Alias) 