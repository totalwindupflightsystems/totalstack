---
id: "@specs/aws/appmesh/docs/API_TcpRoute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TcpRoute"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# TcpRoute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_TcpRoute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TcpRoute
<a name="API_TcpRoute"></a>

An object that represents a TCP route type.

## Contents
<a name="API_TcpRoute_Contents"></a>

 ** action **   <a name="appmesh-Type-TcpRoute-action"></a>
The action to take if a match is determined.  
Type: [TcpRouteAction](API_TcpRouteAction.md) object  
Required: Yes

 ** match **   <a name="appmesh-Type-TcpRoute-match"></a>
An object that represents the criteria for determining a request match.  
Type: [TcpRouteMatch](API_TcpRouteMatch.md) object  
Required: No

 ** timeout **   <a name="appmesh-Type-TcpRoute-timeout"></a>
An object that represents types of timeouts.   
Type: [TcpTimeout](API_TcpTimeout.md) object  
Required: No

## See Also
<a name="API_TcpRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/TcpRoute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/TcpRoute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/TcpRoute) 