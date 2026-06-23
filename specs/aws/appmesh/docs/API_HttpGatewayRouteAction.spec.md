---
id: "@specs/aws/appmesh/docs/API_HttpGatewayRouteAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpGatewayRouteAction"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpGatewayRouteAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpGatewayRouteAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpGatewayRouteAction
<a name="API_HttpGatewayRouteAction"></a>

An object that represents the action to take if a match is determined.

## Contents
<a name="API_HttpGatewayRouteAction_Contents"></a>

 ** target **   <a name="appmesh-Type-HttpGatewayRouteAction-target"></a>
An object that represents the target that traffic is routed to when a request matches the gateway route.  
Type: [GatewayRouteTarget](API_GatewayRouteTarget.md) object  
Required: Yes

 ** rewrite **   <a name="appmesh-Type-HttpGatewayRouteAction-rewrite"></a>
The gateway route action to rewrite.  
Type: [HttpGatewayRouteRewrite](API_HttpGatewayRouteRewrite.md) object  
Required: No

## See Also
<a name="API_HttpGatewayRouteAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpGatewayRouteAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpGatewayRouteAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpGatewayRouteAction) 