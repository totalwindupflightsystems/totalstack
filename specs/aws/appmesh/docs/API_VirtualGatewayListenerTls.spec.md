---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayListenerTls"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayListenerTls"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayListenerTls

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayListenerTls
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayListenerTls
<a name="API_VirtualGatewayListenerTls"></a>

An object that represents the Transport Layer Security (TLS) properties for a listener.

## Contents
<a name="API_VirtualGatewayListenerTls_Contents"></a>

 ** certificate **   <a name="appmesh-Type-VirtualGatewayListenerTls-certificate"></a>
An object that represents a Transport Layer Security (TLS) certificate.  
Type: [VirtualGatewayListenerTlsCertificate](API_VirtualGatewayListenerTlsCertificate.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** mode **   <a name="appmesh-Type-VirtualGatewayListenerTls-mode"></a>
Specify one of the following modes.  
+  ****STRICT – Listener only accepts connections with TLS enabled. 
+  ****PERMISSIVE – Listener accepts connections with or without TLS enabled.
+  ****DISABLED – Listener only accepts connections without TLS. 
Type: String  
Valid Values: `STRICT | PERMISSIVE | DISABLED`   
Required: Yes

 ** validation **   <a name="appmesh-Type-VirtualGatewayListenerTls-validation"></a>
A reference to an object that represents a virtual gateway's listener's Transport Layer Security (TLS) validation context.  
Type: [VirtualGatewayListenerTlsValidationContext](API_VirtualGatewayListenerTlsValidationContext.md) object  
Required: No

## See Also
<a name="API_VirtualGatewayListenerTls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayListenerTls) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayListenerTls) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayListenerTls) 