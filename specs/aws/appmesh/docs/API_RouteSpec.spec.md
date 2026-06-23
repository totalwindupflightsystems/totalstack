---
id: "@specs/aws/appmesh/docs/API_RouteSpec"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RouteSpec"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# RouteSpec

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_RouteSpec
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RouteSpec
<a name="API_RouteSpec"></a>

An object that represents a route specification. Specify one route type.

## Contents
<a name="API_RouteSpec_Contents"></a>

 ** grpcRoute **   <a name="appmesh-Type-RouteSpec-grpcRoute"></a>
An object that represents the specification of a gRPC route.  
Type: [GrpcRoute](API_GrpcRoute.md) object  
Required: No

 ** http2Route **   <a name="appmesh-Type-RouteSpec-http2Route"></a>
An object that represents the specification of an HTTP/2 route.  
Type: [HttpRoute](API_HttpRoute.md) object  
Required: No

 ** httpRoute **   <a name="appmesh-Type-RouteSpec-httpRoute"></a>
An object that represents the specification of an HTTP route.  
Type: [HttpRoute](API_HttpRoute.md) object  
Required: No

 ** priority **   <a name="appmesh-Type-RouteSpec-priority"></a>
The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000.  
Required: No

 ** tcpRoute **   <a name="appmesh-Type-RouteSpec-tcpRoute"></a>
An object that represents the specification of a TCP route.  
Type: [TcpRoute](API_TcpRoute.md) object  
Required: No

## See Also
<a name="API_RouteSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/RouteSpec) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/RouteSpec) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/RouteSpec) 