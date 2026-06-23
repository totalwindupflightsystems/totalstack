---
id: "@specs/aws/appmesh/docs/API_HttpRoute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpRoute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpRoute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpRoute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpRoute
<a name="API_HttpRoute"></a>

An object that represents an HTTP or HTTP/2 route type.

## Contents
<a name="API_HttpRoute_Contents"></a>

 ** action **   <a name="appmesh-Type-HttpRoute-action"></a>
An object that represents the action to take if a match is determined.  
Type: [HttpRouteAction](API_HttpRouteAction.md) object  
Required: Yes

 ** match **   <a name="appmesh-Type-HttpRoute-match"></a>
An object that represents the criteria for determining a request match.  
Type: [HttpRouteMatch](API_HttpRouteMatch.md) object  
Required: Yes

 ** retryPolicy **   <a name="appmesh-Type-HttpRoute-retryPolicy"></a>
An object that represents a retry policy.  
Type: [HttpRetryPolicy](API_HttpRetryPolicy.md) object  
Required: No

 ** timeout **   <a name="appmesh-Type-HttpRoute-timeout"></a>
An object that represents types of timeouts.   
Type: [HttpTimeout](API_HttpTimeout.md) object  
Required: No

## See Also
<a name="API_HttpRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpRoute) 