---
id: "@specs/aws/appmesh/docs/API_HttpGatewayRoute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpGatewayRoute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpGatewayRoute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpGatewayRoute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpGatewayRoute
<a name="API_HttpGatewayRoute"></a>

An object that represents an HTTP gateway route.

## Contents
<a name="API_HttpGatewayRoute_Contents"></a>

 ** action **   <a name="appmesh-Type-HttpGatewayRoute-action"></a>
An object that represents the action to take if a match is determined.  
Type: [HttpGatewayRouteAction](API_HttpGatewayRouteAction.md) object  
Required: Yes

 ** match **   <a name="appmesh-Type-HttpGatewayRoute-match"></a>
An object that represents the criteria for determining a request match.  
Type: [HttpGatewayRouteMatch](API_HttpGatewayRouteMatch.md) object  
Required: Yes

## See Also
<a name="API_HttpGatewayRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpGatewayRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpGatewayRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpGatewayRoute) 