---
id: "@specs/aws/appmesh/docs/API_HttpGatewayRouteRewrite"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpGatewayRouteRewrite"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpGatewayRouteRewrite

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpGatewayRouteRewrite
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpGatewayRouteRewrite
<a name="API_HttpGatewayRouteRewrite"></a>

An object representing the gateway route to rewrite.

## Contents
<a name="API_HttpGatewayRouteRewrite_Contents"></a>

 ** hostname **   <a name="appmesh-Type-HttpGatewayRouteRewrite-hostname"></a>
The host name to rewrite.  
Type: [GatewayRouteHostnameRewrite](API_GatewayRouteHostnameRewrite.md) object  
Required: No

 ** path **   <a name="appmesh-Type-HttpGatewayRouteRewrite-path"></a>
The path to rewrite.  
Type: [HttpGatewayRoutePathRewrite](API_HttpGatewayRoutePathRewrite.md) object  
Required: No

 ** prefix **   <a name="appmesh-Type-HttpGatewayRouteRewrite-prefix"></a>
The specified beginning characters to rewrite.  
Type: [HttpGatewayRoutePrefixRewrite](API_HttpGatewayRoutePrefixRewrite.md) object  
Required: No

## See Also
<a name="API_HttpGatewayRouteRewrite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpGatewayRouteRewrite) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpGatewayRouteRewrite) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpGatewayRouteRewrite) 