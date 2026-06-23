---
id: "@specs/aws/appmesh/docs/API_TlsValidationContextSdsTrust"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TlsValidationContextSdsTrust"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# TlsValidationContextSdsTrust

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_TlsValidationContextSdsTrust
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TlsValidationContextSdsTrust
<a name="API_TlsValidationContextSdsTrust"></a>

An object that represents a Transport Layer Security (TLS) Secret Discovery Service validation context trust. The proxy must be configured with a local SDS provider via a Unix Domain Socket. See App Mesh [TLS documentation](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) for more info.

## Contents
<a name="API_TlsValidationContextSdsTrust_Contents"></a>

 ** secretName **   <a name="appmesh-Type-TlsValidationContextSdsTrust-secretName"></a>
A reference to an object that represents the name of the secret for a Transport Layer Security (TLS) Secret Discovery Service validation context trust.  
Type: String  
Required: Yes

## See Also
<a name="API_TlsValidationContextSdsTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/TlsValidationContextSdsTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/TlsValidationContextSdsTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/TlsValidationContextSdsTrust) 