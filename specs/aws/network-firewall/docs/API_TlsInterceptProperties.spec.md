---
id: "@specs/aws/network-firewall/docs/API_TlsInterceptProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TlsInterceptProperties"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TlsInterceptProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TlsInterceptProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TlsInterceptProperties
<a name="API_TlsInterceptProperties"></a>

TLS decryption on traffic to filter on attributes in the HTTP header. 

## Contents
<a name="API_TlsInterceptProperties_Contents"></a>

 ** PcaArn **   <a name="networkfirewall-Type-TlsInterceptProperties-PcaArn"></a>
Private Certificate Authority (PCA) used to issue private TLS certificates so that the proxy can present PCA-signed certificates which applications trust through the same root, establishing a secure and consistent trust model for encrypted communication.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** TlsInterceptMode **   <a name="networkfirewall-Type-TlsInterceptProperties-TlsInterceptMode"></a>
Specifies whether to enable or disable TLS Intercept Mode.   
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_TlsInterceptProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TlsInterceptProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TlsInterceptProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TlsInterceptProperties) 