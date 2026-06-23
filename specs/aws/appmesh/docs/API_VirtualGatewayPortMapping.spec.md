---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayPortMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayPortMapping"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayPortMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayPortMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayPortMapping
<a name="API_VirtualGatewayPortMapping"></a>

An object that represents a port mapping.

## Contents
<a name="API_VirtualGatewayPortMapping_Contents"></a>

 ** port **   <a name="appmesh-Type-VirtualGatewayPortMapping-port"></a>
The port used for the port mapping. Specify one protocol.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: Yes

 ** protocol **   <a name="appmesh-Type-VirtualGatewayPortMapping-protocol"></a>
The protocol used for the port mapping.  
Type: String  
Valid Values: `http | http2 | grpc`   
Required: Yes

## See Also
<a name="API_VirtualGatewayPortMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayPortMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayPortMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayPortMapping) 