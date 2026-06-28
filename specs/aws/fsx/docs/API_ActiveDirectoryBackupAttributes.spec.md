---
id: "@specs/aws/fsx/docs/API_ActiveDirectoryBackupAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActiveDirectoryBackupAttributes"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# ActiveDirectoryBackupAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_ActiveDirectoryBackupAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActiveDirectoryBackupAttributes
<a name="API_ActiveDirectoryBackupAttributes"></a>

The Microsoft Active Directory attributes of the Amazon FSx for Windows File Server file system.

## Contents
<a name="API_ActiveDirectoryBackupAttributes_Contents"></a>

 ** ActiveDirectoryId **   <a name="FSx-Type-ActiveDirectoryBackupAttributes-ActiveDirectoryId"></a>
The ID of the AWS Managed Microsoft Active Directory instance to which the file system is joined.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** DomainName **   <a name="FSx-Type-ActiveDirectoryBackupAttributes-DomainName"></a>
The fully qualified domain name of the self-managed Active Directory directory.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,255}$`   
Required: No

 ** ResourceARN **   <a name="FSx-Type-ActiveDirectoryBackupAttributes-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

## See Also
<a name="API_ActiveDirectoryBackupAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/ActiveDirectoryBackupAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/ActiveDirectoryBackupAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/ActiveDirectoryBackupAttributes) 