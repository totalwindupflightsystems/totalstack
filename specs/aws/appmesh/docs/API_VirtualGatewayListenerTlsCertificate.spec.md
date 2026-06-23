---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayListenerTlsCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayListenerTlsCertificate"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayListenerTlsCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayListenerTlsCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayListenerTlsCertificate
<a name="API_VirtualGatewayListenerTlsCertificate"></a>

An object that represents a listener's Transport Layer Security (TLS) certificate.

## Contents
<a name="API_VirtualGatewayListenerTlsCertificate_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** acm **   <a name="appmesh-Type-VirtualGatewayListenerTlsCertificate-acm"></a>
A reference to an object that represents an AWS Certificate Manager certificate.  
Type: [VirtualGatewayListenerTlsAcmCertificate](API_VirtualGatewayListenerTlsAcmCertificate.md) object  
Required: No

 ** file **   <a name="appmesh-Type-VirtualGatewayListenerTlsCertificate-file"></a>
A reference to an object that represents a local file certificate.  
Type: [VirtualGatewayListenerTlsFileCertificate](API_VirtualGatewayListenerTlsFileCertificate.md) object  
Required: No

 ** sds **   <a name="appmesh-Type-VirtualGatewayListenerTlsCertificate-sds"></a>
A reference to an object that represents a virtual gateway's listener's Secret Discovery Service certificate.  
Type: [VirtualGatewayListenerTlsSdsCertificate](API_VirtualGatewayListenerTlsSdsCertificate.md) object  
Required: No

## See Also
<a name="API_VirtualGatewayListenerTlsCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayListenerTlsCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayListenerTlsCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayListenerTlsCertificate) 