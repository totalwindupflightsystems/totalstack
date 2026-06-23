---
id: "@specs/aws/appmesh/docs/API_TcpRouteAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TcpRouteAction"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# TcpRouteAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_TcpRouteAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TcpRouteAction
<a name="API_TcpRouteAction"></a>

An object that represents the action to take if a match is determined.

## Contents
<a name="API_TcpRouteAction_Contents"></a>

 ** weightedTargets **   <a name="appmesh-Type-TcpRouteAction-weightedTargets"></a>
An object that represents the targets that traffic is routed to when a request matches the route.  
Type: Array of [WeightedTarget](API_WeightedTarget.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

## See Also
<a name="API_TcpRouteAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/TcpRouteAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/TcpRouteAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/TcpRouteAction) 