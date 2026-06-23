---
id: "@specs/aws/appmesh/docs/API_HttpGatewayRouteMatch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpGatewayRouteMatch"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpGatewayRouteMatch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpGatewayRouteMatch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpGatewayRouteMatch
<a name="API_HttpGatewayRouteMatch"></a>

An object that represents the criteria for determining a request match.

## Contents
<a name="API_HttpGatewayRouteMatch_Contents"></a>

 ** headers **   <a name="appmesh-Type-HttpGatewayRouteMatch-headers"></a>
The client request headers to match on.  
Type: Array of [HttpGatewayRouteHeader](API_HttpGatewayRouteHeader.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** hostname **   <a name="appmesh-Type-HttpGatewayRouteMatch-hostname"></a>
The host name to match on.  
Type: [GatewayRouteHostnameMatch](API_GatewayRouteHostnameMatch.md) object  
Required: No

 ** method **   <a name="appmesh-Type-HttpGatewayRouteMatch-method"></a>
The method to match on.  
Type: String  
Valid Values: `GET | HEAD | POST | PUT | DELETE | CONNECT | OPTIONS | TRACE | PATCH`   
Required: No

 ** path **   <a name="appmesh-Type-HttpGatewayRouteMatch-path"></a>
The path to match on.  
Type: [HttpPathMatch](API_HttpPathMatch.md) object  
Required: No

 ** port **   <a name="appmesh-Type-HttpGatewayRouteMatch-port"></a>
The port number to match on.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** prefix **   <a name="appmesh-Type-HttpGatewayRouteMatch-prefix"></a>
Specifies the path to match requests with. This parameter must always start with `/`, which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is `my-service.local` and you want the route to match requests to `my-service.local/metrics`, your prefix should be `/metrics`.  
Type: String  
Required: No

 ** queryParameters **   <a name="appmesh-Type-HttpGatewayRouteMatch-queryParameters"></a>
The query parameter to match on.  
Type: Array of [HttpQueryParameter](API_HttpQueryParameter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

## See Also
<a name="API_HttpGatewayRouteMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpGatewayRouteMatch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpGatewayRouteMatch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpGatewayRouteMatch) 