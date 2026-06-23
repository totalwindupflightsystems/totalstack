---
id: "@specs/aws/appmesh/docs/API_ListenerTlsValidationContextTrust"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListenerTlsValidationContextTrust"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListenerTlsValidationContextTrust

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListenerTlsValidationContextTrust
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListenerTlsValidationContextTrust
<a name="API_ListenerTlsValidationContextTrust"></a>

An object that represents a listener's Transport Layer Security (TLS) validation context trust.

## Contents
<a name="API_ListenerTlsValidationContextTrust_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** file **   <a name="appmesh-Type-ListenerTlsValidationContextTrust-file"></a>
An object that represents a Transport Layer Security (TLS) validation context trust for a local file.  
Type: [TlsValidationContextFileTrust](API_TlsValidationContextFileTrust.md) object  
Required: No

 ** sds **   <a name="appmesh-Type-ListenerTlsValidationContextTrust-sds"></a>
A reference to an object that represents a listener's Transport Layer Security (TLS) Secret Discovery Service validation context trust.  
Type: [TlsValidationContextSdsTrust](API_TlsValidationContextSdsTrust.md) object  
Required: No

## See Also
<a name="API_ListenerTlsValidationContextTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListenerTlsValidationContextTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListenerTlsValidationContextTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListenerTlsValidationContextTrust) 