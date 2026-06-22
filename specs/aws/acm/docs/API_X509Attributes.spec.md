---
id: "@specs/aws/acm/docs/API_X509Attributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS X509Attributes"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# X509Attributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_X509Attributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# X509Attributes
<a name="API_X509Attributes"></a>

Contains X.509 certificate attributes extracted from the certificate.

## Contents
<a name="API_X509Attributes_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ExtendedKeyUsages **   <a name="ACM-Type-X509Attributes-ExtendedKeyUsages"></a>
Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID).   
Type: Array of strings  
Valid Values: `TLS_WEB_SERVER_AUTHENTICATION | TLS_WEB_CLIENT_AUTHENTICATION | CODE_SIGNING | EMAIL_PROTECTION | TIME_STAMPING | OCSP_SIGNING | IPSEC_END_SYSTEM | IPSEC_TUNNEL | IPSEC_USER | ANY | NONE | CUSTOM`   
Required: No

 ** Issuer **   <a name="ACM-Type-X509Attributes-Issuer"></a>
The distinguished name of the certificate issuer.  
Type: [DistinguishedName](API_DistinguishedName.md) object  
Required: No

 ** KeyAlgorithm **   <a name="ACM-Type-X509Attributes-KeyAlgorithm"></a>
The algorithm that was used to generate the public-private key pair.  
Type: String  
Valid Values: `RSA_1024 | RSA_2048 | RSA_3072 | RSA_4096 | EC_prime256v1 | EC_secp384r1 | EC_secp521r1`   
Required: No

 ** KeyUsages **   <a name="ACM-Type-X509Attributes-KeyUsages"></a>
A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL\_SIGNATURE, KEY\_ENCHIPHERMENT, NON\_REPUDIATION, and more.  
Type: Array of strings  
Valid Values: `DIGITAL_SIGNATURE | NON_REPUDIATION | KEY_ENCIPHERMENT | DATA_ENCIPHERMENT | KEY_AGREEMENT | CERTIFICATE_SIGNING | CRL_SIGNING | ENCIPHER_ONLY | DECIPHER_ONLY | ANY | CUSTOM`   
Required: No

 ** NotAfter **   <a name="ACM-Type-X509Attributes-NotAfter"></a>
The time after which the certificate is not valid.  
Type: Timestamp  
Required: No

 ** NotBefore **   <a name="ACM-Type-X509Attributes-NotBefore"></a>
The time before which the certificate is not valid.  
Type: Timestamp  
Required: No

 ** SerialNumber **   <a name="ACM-Type-X509Attributes-SerialNumber"></a>
The serial number assigned by the certificate authority.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 59.  
Pattern: `[0-9a-f]{2}(:[0-9a-f]{2}){1,19}`   
Required: No

 ** Subject **   <a name="ACM-Type-X509Attributes-Subject"></a>
The distinguished name of the certificate subject.  
Type: [DistinguishedName](API_DistinguishedName.md) object  
Required: No

 ** SubjectAlternativeNames **   <a name="ACM-Type-X509Attributes-SubjectAlternativeNames"></a>
One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.   
Type: Array of [GeneralName](API_GeneralName.md) objects  
Required: No

## See Also
<a name="API_X509Attributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/X509Attributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/X509Attributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/X509Attributes) 