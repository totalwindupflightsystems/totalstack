---
id: "@specs/aws/appmesh/docs/API_GrpcGatewayRoute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GrpcGatewayRoute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GrpcGatewayRoute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GrpcGatewayRoute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GrpcGatewayRoute
<a name="API_GrpcGatewayRoute"></a>

An object that represents a gRPC gateway route.

## Contents
<a name="API_GrpcGatewayRoute_Contents"></a>

 ** action **   <a name="appmesh-Type-GrpcGatewayRoute-action"></a>
An object that represents the action to take if a match is determined.  
Type: [GrpcGatewayRouteAction](API_GrpcGatewayRouteAction.md) object  
Required: Yes

 ** match **   <a name="appmesh-Type-GrpcGatewayRoute-match"></a>
An object that represents the criteria for determining a request match.  
Type: [GrpcGatewayRouteMatch](API_GrpcGatewayRouteMatch.md) object  
Required: Yes

## See Also
<a name="API_GrpcGatewayRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcGatewayRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcGatewayRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcGatewayRoute) 