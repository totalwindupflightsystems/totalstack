---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayTlsValidationContextSdsTrust"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayTlsValidationContextSdsTrust"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayTlsValidationContextSdsTrust

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayTlsValidationContextSdsTrust
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayTlsValidationContextSdsTrust
<a name="API_VirtualGatewayTlsValidationContextSdsTrust"></a>

An object that represents a virtual gateway's listener's Transport Layer Security (TLS) Secret Discovery Service validation context trust. The proxy must be configured with a local SDS provider via a Unix Domain Socket. See App Mesh [TLS documentation](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) for more info.

## Contents
<a name="API_VirtualGatewayTlsValidationContextSdsTrust_Contents"></a>

 ** secretName **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextSdsTrust-secretName"></a>
A reference to an object that represents the name of the secret for a virtual gateway's Transport Layer Security (TLS) Secret Discovery Service validation context trust.  
Type: String  
Required: Yes

## See Also
<a name="API_VirtualGatewayTlsValidationContextSdsTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayTlsValidationContextSdsTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayTlsValidationContextSdsTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayTlsValidationContextSdsTrust) 