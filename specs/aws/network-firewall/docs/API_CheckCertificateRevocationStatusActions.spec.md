---
id: "@specs/aws/network-firewall/docs/API_CheckCertificateRevocationStatusActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CheckCertificateRevocationStatusActions"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CheckCertificateRevocationStatusActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CheckCertificateRevocationStatusActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CheckCertificateRevocationStatusActions
<a name="API_CheckCertificateRevocationStatusActions"></a>

Defines the actions to take on the SSL/TLS connection if the certificate presented by the server in the connection has a revoked or unknown status.

## Contents
<a name="API_CheckCertificateRevocationStatusActions_Contents"></a>

 ** RevokedStatusAction **   <a name="networkfirewall-Type-CheckCertificateRevocationStatusActions-RevokedStatusAction"></a>
Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has a revoked status.  
+  **PASS** - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
+  **DROP** - Network Firewall closes the connection and drops subsequent packets for that connection.
+  **REJECT** - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. `REJECT` is available only for TCP traffic.
Type: String  
Valid Values: `PASS | DROP | REJECT`   
Required: No

 ** UnknownStatusAction **   <a name="networkfirewall-Type-CheckCertificateRevocationStatusActions-UnknownStatusAction"></a>
Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has an unknown status, or a status that cannot be determined for any other reason, including when the service is unable to connect to the OCSP and CRL endpoints for the certificate.  
+  **PASS** - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
+  **DROP** - Network Firewall closes the connection and drops subsequent packets for that connection.
+  **REJECT** - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. `REJECT` is available only for TCP traffic.
Type: String  
Valid Values: `PASS | DROP | REJECT`   
Required: No

## See Also
<a name="API_CheckCertificateRevocationStatusActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CheckCertificateRevocationStatusActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CheckCertificateRevocationStatusActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CheckCertificateRevocationStatusActions) 