---
id: "@specs/aws/appmesh/docs/API_PortMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PortMapping"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# PortMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_PortMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PortMapping
<a name="API_PortMapping"></a>

An object that represents a port mapping.

## Contents
<a name="API_PortMapping_Contents"></a>

 ** port **   <a name="appmesh-Type-PortMapping-port"></a>
The port used for the port mapping.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: Yes

 ** protocol **   <a name="appmesh-Type-PortMapping-protocol"></a>
The protocol used for the port mapping. Specify one protocol.  
Type: String  
Valid Values: `http | tcp | http2 | grpc`   
Required: Yes

## See Also
<a name="API_PortMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/PortMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/PortMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/PortMapping) 