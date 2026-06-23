---
id: "@specs/aws/appmesh/docs/API_GatewayRouteTarget"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GatewayRouteTarget"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GatewayRouteTarget

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GatewayRouteTarget
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GatewayRouteTarget
<a name="API_GatewayRouteTarget"></a>

An object that represents a gateway route target.

## Contents
<a name="API_GatewayRouteTarget_Contents"></a>

 ** virtualService **   <a name="appmesh-Type-GatewayRouteTarget-virtualService"></a>
An object that represents a virtual service gateway route target.  
Type: [GatewayRouteVirtualService](API_GatewayRouteVirtualService.md) object  
Required: Yes

 ** port **   <a name="appmesh-Type-GatewayRouteTarget-port"></a>
The port number of the gateway route target.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

## See Also
<a name="API_GatewayRouteTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GatewayRouteTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GatewayRouteTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GatewayRouteTarget) 