---
id: "@specs/aws/network-firewall/docs/API_ServerCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServerCertificate"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ServerCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ServerCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServerCertificate
<a name="API_ServerCertificate"></a>

Any AWS Certificate Manager (ACM) Secure Sockets Layer/Transport Layer Security (SSL/TLS) server certificate that's associated with a [ServerCertificateConfiguration](API_ServerCertificateConfiguration.md). Used in a [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md) for inspection of inbound traffic to your firewall. You must request or import a SSL/TLS certificate into ACM for each domain Network Firewall needs to decrypt and inspect. AWS Network Firewall uses the SSL/TLS certificates to decrypt specified inbound SSL/TLS traffic going to your firewall. For information about working with certificates in AWS Certificate Manager, see [Request a public certificate ](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) or [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the * AWS Certificate Manager User Guide*.

## Contents
<a name="API_ServerCertificate_Contents"></a>

 ** ResourceArn **   <a name="networkfirewall-Type-ServerCertificate-ResourceArn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager SSL/TLS server certificate that's used for inbound SSL/TLS inspection.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

## See Also
<a name="API_ServerCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ServerCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ServerCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ServerCertificate) 