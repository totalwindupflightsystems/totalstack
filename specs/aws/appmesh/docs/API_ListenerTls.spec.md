---
id: "@specs/aws/appmesh/docs/API_ListenerTls"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListenerTls"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListenerTls

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListenerTls
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListenerTls
<a name="API_ListenerTls"></a>

An object that represents the Transport Layer Security (TLS) properties for a listener.

## Contents
<a name="API_ListenerTls_Contents"></a>

 ** certificate **   <a name="appmesh-Type-ListenerTls-certificate"></a>
A reference to an object that represents a listener's Transport Layer Security (TLS) certificate.  
Type: [ListenerTlsCertificate](API_ListenerTlsCertificate.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** mode **   <a name="appmesh-Type-ListenerTls-mode"></a>
Specify one of the following modes.  
+  ****STRICT – Listener only accepts connections with TLS enabled. 
+  ****PERMISSIVE – Listener accepts connections with or without TLS enabled.
+  ****DISABLED – Listener only accepts connections without TLS. 
Type: String  
Valid Values: `STRICT | PERMISSIVE | DISABLED`   
Required: Yes

 ** validation **   <a name="appmesh-Type-ListenerTls-validation"></a>
A reference to an object that represents a listener's Transport Layer Security (TLS) validation context.  
Type: [ListenerTlsValidationContext](API_ListenerTlsValidationContext.md) object  
Required: No

## See Also
<a name="API_ListenerTls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListenerTls) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListenerTls) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListenerTls) 