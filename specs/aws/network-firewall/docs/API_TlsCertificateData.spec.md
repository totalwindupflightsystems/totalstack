---
id: "@specs/aws/network-firewall/docs/API_TlsCertificateData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TlsCertificateData"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TlsCertificateData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TlsCertificateData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TlsCertificateData
<a name="API_TlsCertificateData"></a>

Contains metadata about an AWS Certificate Manager certificate.

## Contents
<a name="API_TlsCertificateData_Contents"></a>

 ** CertificateArn **   <a name="networkfirewall-Type-TlsCertificateData-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** CertificateSerial **   <a name="networkfirewall-Type-TlsCertificateData-CertificateSerial"></a>
The serial number of the certificate.  
Type: String  
Required: No

 ** Status **   <a name="networkfirewall-Type-TlsCertificateData-Status"></a>
The status of the certificate.  
Type: String  
Required: No

 ** StatusMessage **   <a name="networkfirewall-Type-TlsCertificateData-StatusMessage"></a>
Contains details about the certificate status, including information about certificate errors.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9- ]+$`   
Required: No

## See Also
<a name="API_TlsCertificateData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TlsCertificateData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TlsCertificateData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TlsCertificateData) 