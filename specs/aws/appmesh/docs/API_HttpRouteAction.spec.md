---
id: "@specs/aws/appmesh/docs/API_HttpRouteAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpRouteAction"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpRouteAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpRouteAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpRouteAction
<a name="API_HttpRouteAction"></a>

An object that represents the action to take if a match is determined.

## Contents
<a name="API_HttpRouteAction_Contents"></a>

 ** weightedTargets **   <a name="appmesh-Type-HttpRouteAction-weightedTargets"></a>
An object that represents the targets that traffic is routed to when a request matches the route.  
Type: Array of [WeightedTarget](API_WeightedTarget.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

## See Also
<a name="API_HttpRouteAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpRouteAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpRouteAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpRouteAction) 