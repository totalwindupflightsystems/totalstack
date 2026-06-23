---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayTlsValidationContextTrust"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayTlsValidationContextTrust"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayTlsValidationContextTrust

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayTlsValidationContextTrust
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayTlsValidationContextTrust
<a name="API_VirtualGatewayTlsValidationContextTrust"></a>

An object that represents a Transport Layer Security (TLS) validation context trust.

## Contents
<a name="API_VirtualGatewayTlsValidationContextTrust_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** acm **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextTrust-acm"></a>
A reference to an object that represents a Transport Layer Security (TLS) validation context trust for an AWS Certificate Manager certificate.  
Type: [VirtualGatewayTlsValidationContextAcmTrust](API_VirtualGatewayTlsValidationContextAcmTrust.md) object  
Required: No

 ** file **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextTrust-file"></a>
An object that represents a Transport Layer Security (TLS) validation context trust for a local file.  
Type: [VirtualGatewayTlsValidationContextFileTrust](API_VirtualGatewayTlsValidationContextFileTrust.md) object  
Required: No

 ** sds **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextTrust-sds"></a>
A reference to an object that represents a virtual gateway's Transport Layer Security (TLS) Secret Discovery Service validation context trust.  
Type: [VirtualGatewayTlsValidationContextSdsTrust](API_VirtualGatewayTlsValidationContextSdsTrust.md) object  
Required: No

## See Also
<a name="API_VirtualGatewayTlsValidationContextTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayTlsValidationContextTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayTlsValidationContextTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayTlsValidationContextTrust) 