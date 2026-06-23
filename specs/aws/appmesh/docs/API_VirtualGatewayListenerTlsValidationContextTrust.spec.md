---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayListenerTlsValidationContextTrust"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayListenerTlsValidationContextTrust"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayListenerTlsValidationContextTrust

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayListenerTlsValidationContextTrust
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayListenerTlsValidationContextTrust
<a name="API_VirtualGatewayListenerTlsValidationContextTrust"></a>

An object that represents a virtual gateway's listener's Transport Layer Security (TLS) validation context trust.

## Contents
<a name="API_VirtualGatewayListenerTlsValidationContextTrust_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** file **   <a name="appmesh-Type-VirtualGatewayListenerTlsValidationContextTrust-file"></a>
An object that represents a Transport Layer Security (TLS) validation context trust for a local file.  
Type: [VirtualGatewayTlsValidationContextFileTrust](API_VirtualGatewayTlsValidationContextFileTrust.md) object  
Required: No

 ** sds **   <a name="appmesh-Type-VirtualGatewayListenerTlsValidationContextTrust-sds"></a>
A reference to an object that represents a virtual gateway's listener's Transport Layer Security (TLS) Secret Discovery Service validation context trust.  
Type: [VirtualGatewayTlsValidationContextSdsTrust](API_VirtualGatewayTlsValidationContextSdsTrust.md) object  
Required: No

## See Also
<a name="API_VirtualGatewayListenerTlsValidationContextTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayListenerTlsValidationContextTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayListenerTlsValidationContextTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayListenerTlsValidationContextTrust) 