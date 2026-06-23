---
id: "@specs/aws/appmesh/docs/API_ListenerTlsFileCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListenerTlsFileCertificate"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ListenerTlsFileCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ListenerTlsFileCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListenerTlsFileCertificate
<a name="API_ListenerTlsFileCertificate"></a>

An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html#virtual-node-tls-prerequisites).

## Contents
<a name="API_ListenerTlsFileCertificate_Contents"></a>

 ** certificateChain **   <a name="appmesh-Type-ListenerTlsFileCertificate-certificateChain"></a>
The certificate chain for the certificate.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** privateKey **   <a name="appmesh-Type-ListenerTlsFileCertificate-privateKey"></a>
The private key for a certificate stored on the file system of the virtual node that the proxy is running on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_ListenerTlsFileCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListenerTlsFileCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListenerTlsFileCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListenerTlsFileCertificate) 