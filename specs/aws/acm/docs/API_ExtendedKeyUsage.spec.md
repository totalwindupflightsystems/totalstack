---
id: "@specs/aws/acm/docs/API_ExtendedKeyUsage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExtendedKeyUsage"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# ExtendedKeyUsage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_ExtendedKeyUsage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExtendedKeyUsage
<a name="API_ExtendedKeyUsage"></a>

The Extended Key Usage X.509 v3 extension defines one or more purposes for which the public key can be used. This is in addition to or in place of the basic purposes specified by the Key Usage extension. 

## Contents
<a name="API_ExtendedKeyUsage_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Name **   <a name="ACM-Type-ExtendedKeyUsage-Name"></a>
The name of an Extended Key Usage value.  
Type: String  
Valid Values: `TLS_WEB_SERVER_AUTHENTICATION | TLS_WEB_CLIENT_AUTHENTICATION | CODE_SIGNING | EMAIL_PROTECTION | TIME_STAMPING | OCSP_SIGNING | IPSEC_END_SYSTEM | IPSEC_TUNNEL | IPSEC_USER | ANY | NONE | CUSTOM`   
Required: No

 ** OID **   <a name="ACM-Type-ExtendedKeyUsage-OID"></a>
An object identifier (OID) for the extension value. OIDs are strings of numbers separated by periods. The following OIDs are defined in RFC 3280 and RFC 5280.   
+  `1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)` 
+  `1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)` 
+  `1.3.6.1.5.5.7.3.3 (CODE_SIGNING)` 
+  `1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)` 
+  `1.3.6.1.5.5.7.3.8 (TIME_STAMPING)` 
+  `1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)` 
+  `1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)` 
+  `1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)` 
+  `1.3.6.1.5.5.7.3.7 (IPSEC_USER)` 
Type: String  
Required: No

## See Also
<a name="API_ExtendedKeyUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ExtendedKeyUsage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ExtendedKeyUsage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ExtendedKeyUsage) 