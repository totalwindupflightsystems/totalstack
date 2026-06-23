---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayTlsValidationContext"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayTlsValidationContext"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayTlsValidationContext

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayTlsValidationContext
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayTlsValidationContext
<a name="API_VirtualGatewayTlsValidationContext"></a>

An object that represents a Transport Layer Security (TLS) validation context.

## Contents
<a name="API_VirtualGatewayTlsValidationContext_Contents"></a>

 ** trust **   <a name="appmesh-Type-VirtualGatewayTlsValidationContext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.  
Type: [VirtualGatewayTlsValidationContextTrust](API_VirtualGatewayTlsValidationContextTrust.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** subjectAlternativeNames **   <a name="appmesh-Type-VirtualGatewayTlsValidationContext-subjectAlternativeNames"></a>
A reference to an object that represents the SANs for a virtual gateway's listener's Transport Layer Security (TLS) validation context.  
Type: [SubjectAlternativeNames](API_SubjectAlternativeNames.md) object  
Required: No

## See Also
<a name="API_VirtualGatewayTlsValidationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayTlsValidationContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayTlsValidationContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayTlsValidationContext) 