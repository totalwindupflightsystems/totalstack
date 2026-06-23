---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayClientTlsCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayClientTlsCertificate"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayClientTlsCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayClientTlsCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayClientTlsCertificate
<a name="API_VirtualGatewayClientTlsCertificate"></a>

An object that represents the virtual gateway's client's Transport Layer Security (TLS) certificate.

## Contents
<a name="API_VirtualGatewayClientTlsCertificate_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** file **   <a name="appmesh-Type-VirtualGatewayClientTlsCertificate-file"></a>
An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [ Transport Layer Security (TLS) ](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html).  
Type: [VirtualGatewayListenerTlsFileCertificate](API_VirtualGatewayListenerTlsFileCertificate.md) object  
Required: No

 ** sds **   <a name="appmesh-Type-VirtualGatewayClientTlsCertificate-sds"></a>
A reference to an object that represents a virtual gateway's client's Secret Discovery Service certificate.  
Type: [VirtualGatewayListenerTlsSdsCertificate](API_VirtualGatewayListenerTlsSdsCertificate.md) object  
Required: No

## See Also
<a name="API_VirtualGatewayClientTlsCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayClientTlsCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayClientTlsCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayClientTlsCertificate) 