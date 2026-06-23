---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayListenerTlsSdsCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayListenerTlsSdsCertificate"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayListenerTlsSdsCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayListenerTlsSdsCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayListenerTlsSdsCertificate
<a name="API_VirtualGatewayListenerTlsSdsCertificate"></a>

An object that represents the virtual gateway's listener's Secret Discovery Service certificate.The proxy must be configured with a local SDS provider via a Unix Domain Socket. See App Mesh[TLS documentation](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) for more info. 

## Contents
<a name="API_VirtualGatewayListenerTlsSdsCertificate_Contents"></a>

 ** secretName **   <a name="appmesh-Type-VirtualGatewayListenerTlsSdsCertificate-secretName"></a>
A reference to an object that represents the name of the secret secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.  
Type: String  
Required: Yes

## See Also
<a name="API_VirtualGatewayListenerTlsSdsCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayListenerTlsSdsCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayListenerTlsSdsCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayListenerTlsSdsCertificate) 