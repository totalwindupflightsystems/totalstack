---
id: "@specs/aws/appmesh/docs/API_GatewayRouteSpec"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GatewayRouteSpec"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GatewayRouteSpec

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GatewayRouteSpec
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GatewayRouteSpec
<a name="API_GatewayRouteSpec"></a>

An object that represents a gateway route specification. Specify one gateway route type.

## Contents
<a name="API_GatewayRouteSpec_Contents"></a>

 ** grpcRoute **   <a name="appmesh-Type-GatewayRouteSpec-grpcRoute"></a>
An object that represents the specification of a gRPC gateway route.  
Type: [GrpcGatewayRoute](API_GrpcGatewayRoute.md) object  
Required: No

 ** http2Route **   <a name="appmesh-Type-GatewayRouteSpec-http2Route"></a>
An object that represents the specification of an HTTP/2 gateway route.  
Type: [HttpGatewayRoute](API_HttpGatewayRoute.md) object  
Required: No

 ** httpRoute **   <a name="appmesh-Type-GatewayRouteSpec-httpRoute"></a>
An object that represents the specification of an HTTP gateway route.  
Type: [HttpGatewayRoute](API_HttpGatewayRoute.md) object  
Required: No

 ** priority **   <a name="appmesh-Type-GatewayRouteSpec-priority"></a>
The ordering of the gateway routes spec.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000.  
Required: No

## See Also
<a name="API_GatewayRouteSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GatewayRouteSpec) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GatewayRouteSpec) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GatewayRouteSpec) 