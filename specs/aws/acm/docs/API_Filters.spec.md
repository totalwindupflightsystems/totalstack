---
id: "@specs/aws/acm/docs/API_Filters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Filters"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# Filters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_Filters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Filters
<a name="API_Filters"></a>

This structure can be used in the [ListCertificates](API_ListCertificates.md) action to filter the output of the certificate list. 

## Contents
<a name="API_Filters_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** exportOption **   <a name="ACM-Type-Filters-exportOption"></a>
Specify `ENABLED` or `DISABLED` to identify certificates that can be exported.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** extendedKeyUsage **   <a name="ACM-Type-Filters-extendedKeyUsage"></a>
Specify one or more [ExtendedKeyUsage](API_ExtendedKeyUsage.md) extension values.  
Type: Array of strings  
Valid Values: `TLS_WEB_SERVER_AUTHENTICATION | TLS_WEB_CLIENT_AUTHENTICATION | CODE_SIGNING | EMAIL_PROTECTION | TIME_STAMPING | OCSP_SIGNING | IPSEC_END_SYSTEM | IPSEC_TUNNEL | IPSEC_USER | ANY | NONE | CUSTOM`   
Required: No

 ** keyTypes **   <a name="ACM-Type-Filters-keyTypes"></a>
Specify one or more algorithms that can be used to generate key pairs.  
Default filtering returns only `RSA_1024` and `RSA_2048` certificates that have at least one domain. To return other certificate types, provide the desired type signatures in a comma-separated list. For example, `"keyTypes": ["RSA_2048","RSA_4096"]` returns both `RSA_2048` and `RSA_4096` certificates.  
Type: Array of strings  
Valid Values: `RSA_1024 | RSA_2048 | RSA_3072 | RSA_4096 | EC_prime256v1 | EC_secp384r1 | EC_secp521r1`   
Required: No

 ** keyUsage **   <a name="ACM-Type-Filters-keyUsage"></a>
Specify one or more [KeyUsage](API_KeyUsage.md) extension values.  
Type: Array of strings  
Valid Values: `DIGITAL_SIGNATURE | NON_REPUDIATION | KEY_ENCIPHERMENT | DATA_ENCIPHERMENT | KEY_AGREEMENT | CERTIFICATE_SIGNING | CRL_SIGNING | ENCIPHER_ONLY | DECIPHER_ONLY | ANY | CUSTOM`   
Required: No

 ** managedBy **   <a name="ACM-Type-Filters-managedBy"></a>
Identifies the AWS service that manages the certificate issued by ACM.  
Type: String  
Valid Values: `CLOUDFRONT`   
Required: No

## See Also
<a name="API_Filters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/Filters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/Filters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/Filters) 