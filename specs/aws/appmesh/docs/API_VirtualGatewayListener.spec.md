---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayListener"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayListener"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayListener

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayListener
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayListener
<a name="API_VirtualGatewayListener"></a>

An object that represents a listener for a virtual gateway.

## Contents
<a name="API_VirtualGatewayListener_Contents"></a>

 ** portMapping **   <a name="appmesh-Type-VirtualGatewayListener-portMapping"></a>
The port mapping information for the listener.  
Type: [VirtualGatewayPortMapping](API_VirtualGatewayPortMapping.md) object  
Required: Yes

 ** connectionPool **   <a name="appmesh-Type-VirtualGatewayListener-connectionPool"></a>
The connection pool information for the virtual gateway listener.  
Type: [VirtualGatewayConnectionPool](API_VirtualGatewayConnectionPool.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** healthCheck **   <a name="appmesh-Type-VirtualGatewayListener-healthCheck"></a>
The health check information for the listener.  
Type: [VirtualGatewayHealthCheckPolicy](API_VirtualGatewayHealthCheckPolicy.md) object  
Required: No

 ** tls **   <a name="appmesh-Type-VirtualGatewayListener-tls"></a>
A reference to an object that represents the Transport Layer Security (TLS) properties for the listener.  
Type: [VirtualGatewayListenerTls](API_VirtualGatewayListenerTls.md) object  
Required: No

## See Also
<a name="API_VirtualGatewayListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayListener) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayListener) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayListener) 