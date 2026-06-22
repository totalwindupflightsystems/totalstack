---
id: "@specs/aws/acm/docs/API_X509AttributeFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS X509AttributeFilter"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# X509AttributeFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_X509AttributeFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# X509AttributeFilter
<a name="API_X509AttributeFilter"></a>

Filters certificates by X.509 attributes.

## Contents
<a name="API_X509AttributeFilter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ExtendedKeyUsage **   <a name="ACM-Type-X509AttributeFilter-ExtendedKeyUsage"></a>
Filter by extended key usage.  
Type: String  
Valid Values: `TLS_WEB_SERVER_AUTHENTICATION | TLS_WEB_CLIENT_AUTHENTICATION | CODE_SIGNING | EMAIL_PROTECTION | TIME_STAMPING | OCSP_SIGNING | IPSEC_END_SYSTEM | IPSEC_TUNNEL | IPSEC_USER | ANY | NONE | CUSTOM`   
Required: No

 ** KeyAlgorithm **   <a name="ACM-Type-X509AttributeFilter-KeyAlgorithm"></a>
Filter by key algorithm.  
Type: String  
Valid Values: `RSA_1024 | RSA_2048 | RSA_3072 | RSA_4096 | EC_prime256v1 | EC_secp384r1 | EC_secp521r1`   
Required: No

 ** KeyUsage **   <a name="ACM-Type-X509AttributeFilter-KeyUsage"></a>
Filter by key usage.  
Type: String  
Valid Values: `DIGITAL_SIGNATURE | NON_REPUDIATION | KEY_ENCIPHERMENT | DATA_ENCIPHERMENT | KEY_AGREEMENT | CERTIFICATE_SIGNING | CRL_SIGNING | ENCIPHER_ONLY | DECIPHER_ONLY | ANY | CUSTOM`   
Required: No

 ** NotAfter **   <a name="ACM-Type-X509AttributeFilter-NotAfter"></a>
Filter by certificate expiration date. The start date is inclusive.  
Type: [TimestampRange](API_TimestampRange.md) object  
Required: No

 ** NotBefore **   <a name="ACM-Type-X509AttributeFilter-NotBefore"></a>
Filter by certificate validity start date. The start date is inclusive.  
Type: [TimestampRange](API_TimestampRange.md) object  
Required: No

 ** SerialNumber **   <a name="ACM-Type-X509AttributeFilter-SerialNumber"></a>
Filter by serial number.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 59.  
Pattern: `[0-9a-f]{2}(:[0-9a-f]{2}){1,19}`   
Required: No

 ** Subject **   <a name="ACM-Type-X509AttributeFilter-Subject"></a>
Filter by certificate subject.  
Type: [SubjectFilter](API_SubjectFilter.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** SubjectAlternativeName **   <a name="ACM-Type-X509AttributeFilter-SubjectAlternativeName"></a>
Filter by subject alternative names.  
Type: [SubjectAlternativeNameFilter](API_SubjectAlternativeNameFilter.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_X509AttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/X509AttributeFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/X509AttributeFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/X509AttributeFilter) 