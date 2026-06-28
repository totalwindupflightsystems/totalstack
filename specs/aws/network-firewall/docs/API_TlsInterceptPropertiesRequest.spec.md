---
id: "@specs/aws/network-firewall/docs/API_TlsInterceptPropertiesRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TlsInterceptPropertiesRequest"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TlsInterceptPropertiesRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TlsInterceptPropertiesRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TlsInterceptPropertiesRequest
<a name="API_TlsInterceptPropertiesRequest"></a>

This data type is used specifically for the [CreateProxy](API_CreateProxy.md) and [UpdateProxy](API_UpdateProxy.md) APIs.

TLS decryption on traffic to filter on attributes in the HTTP header. 

## Contents
<a name="API_TlsInterceptPropertiesRequest_Contents"></a>

 ** PcaArn **   <a name="networkfirewall-Type-TlsInterceptPropertiesRequest-PcaArn"></a>
Private Certificate Authority (PCA) used to issue private TLS certificates so that the proxy can present PCA-signed certificates which applications trust through the same root, establishing a secure and consistent trust model for encrypted communication.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** TlsInterceptMode **   <a name="networkfirewall-Type-TlsInterceptPropertiesRequest-TlsInterceptMode"></a>
Specifies whether to enable or disable TLS Intercept Mode.   
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_TlsInterceptPropertiesRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TlsInterceptPropertiesRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TlsInterceptPropertiesRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TlsInterceptPropertiesRequest) 