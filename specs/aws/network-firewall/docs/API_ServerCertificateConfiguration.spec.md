---
id: "@specs/aws/network-firewall/docs/API_ServerCertificateConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServerCertificateConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ServerCertificateConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ServerCertificateConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServerCertificateConfiguration
<a name="API_ServerCertificateConfiguration"></a>

Configures the AWS Certificate Manager certificates and scope that Network Firewall uses to decrypt and re-encrypt traffic using a [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md). You can configure `ServerCertificates` for inbound SSL/TLS inspection, a `CertificateAuthorityArn` for outbound SSL/TLS inspection, or both. For information about working with certificates for TLS inspection, see [ Using SSL/TLS server certficiates with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html) in the * AWS Network Firewall Developer Guide*.

**Note**  
If a server certificate that's associated with your [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md) is revoked, deleted, or expired it can result in client-side TLS errors.

## Contents
<a name="API_ServerCertificateConfiguration_Contents"></a>

 ** CertificateAuthorityArn **   <a name="networkfirewall-Type-ServerCertificateConfiguration-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the imported certificate authority (CA) certificate within AWS Certificate Manager (ACM) to use for outbound SSL/TLS inspection.  
The following limitations apply:  
+ You can use CA certificates that you imported into ACM, but you can't generate CA certificates with ACM.
+ You can't use certificates issued by AWS Private Certificate Authority.
For more information about configuring certificates for outbound inspection, see [Using SSL/TLS certificates with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html) in the * AWS Network Firewall Developer Guide*.   
For information about working with certificates in ACM, see [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the * AWS Certificate Manager User Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** CheckCertificateRevocationStatus **   <a name="networkfirewall-Type-ServerCertificateConfiguration-CheckCertificateRevocationStatus"></a>
When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status. If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a `CertificateAuthorityArn` in [ServerCertificateConfiguration](#API_ServerCertificateConfiguration).  
Type: [CheckCertificateRevocationStatusActions](API_CheckCertificateRevocationStatusActions.md) object  
Required: No

 ** Scopes **   <a name="networkfirewall-Type-ServerCertificateConfiguration-Scopes"></a>
A list of scopes.  
Type: Array of [ServerCertificateScope](API_ServerCertificateScope.md) objects  
Required: No

 ** ServerCertificates **   <a name="networkfirewall-Type-ServerCertificateConfiguration-ServerCertificates"></a>
The list of server certificates to use for inbound SSL/TLS inspection.  
Type: Array of [ServerCertificate](API_ServerCertificate.md) objects  
Required: No

## See Also
<a name="API_ServerCertificateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ServerCertificateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ServerCertificateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ServerCertificateConfiguration) 