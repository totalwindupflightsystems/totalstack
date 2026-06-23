---
id: "@specs/aws/appmesh/docs/API_GrpcRoute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GrpcRoute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GrpcRoute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GrpcRoute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GrpcRoute
<a name="API_GrpcRoute"></a>

An object that represents a gRPC route type.

## Contents
<a name="API_GrpcRoute_Contents"></a>

 ** action **   <a name="appmesh-Type-GrpcRoute-action"></a>
An object that represents the action to take if a match is determined.  
Type: [GrpcRouteAction](API_GrpcRouteAction.md) object  
Required: Yes

 ** match **   <a name="appmesh-Type-GrpcRoute-match"></a>
An object that represents the criteria for determining a request match.  
Type: [GrpcRouteMatch](API_GrpcRouteMatch.md) object  
Required: Yes

 ** retryPolicy **   <a name="appmesh-Type-GrpcRoute-retryPolicy"></a>
An object that represents a retry policy.  
Type: [GrpcRetryPolicy](API_GrpcRetryPolicy.md) object  
Required: No

 ** timeout **   <a name="appmesh-Type-GrpcRoute-timeout"></a>
An object that represents types of timeouts.   
Type: [GrpcTimeout](API_GrpcTimeout.md) object  
Required: No

## See Also
<a name="API_GrpcRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcRoute) 