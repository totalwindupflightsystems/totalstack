---
id: "@specs/aws/appmesh/docs/API_HttpRouteMatch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpRouteMatch"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpRouteMatch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpRouteMatch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpRouteMatch
<a name="API_HttpRouteMatch"></a>

An object that represents the requirements for a route to match HTTP requests for a virtual router.

## Contents
<a name="API_HttpRouteMatch_Contents"></a>

 ** headers **   <a name="appmesh-Type-HttpRouteMatch-headers"></a>
The client request headers to match on.  
Type: Array of [HttpRouteHeader](API_HttpRouteHeader.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** method **   <a name="appmesh-Type-HttpRouteMatch-method"></a>
The client request method to match on. Specify only one.  
Type: String  
Valid Values: `GET | HEAD | POST | PUT | DELETE | CONNECT | OPTIONS | TRACE | PATCH`   
Required: No

 ** path **   <a name="appmesh-Type-HttpRouteMatch-path"></a>
The client request path to match on.  
Type: [HttpPathMatch](API_HttpPathMatch.md) object  
Required: No

 ** port **   <a name="appmesh-Type-HttpRouteMatch-port"></a>
The port number to match on.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** prefix **   <a name="appmesh-Type-HttpRouteMatch-prefix"></a>
Specifies the path to match requests with. This parameter must always start with `/`, which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is `my-service.local` and you want the route to match requests to `my-service.local/metrics`, your prefix should be `/metrics`.  
Type: String  
Required: No

 ** queryParameters **   <a name="appmesh-Type-HttpRouteMatch-queryParameters"></a>
The client request query parameters to match on.  
Type: Array of [HttpQueryParameter](API_HttpQueryParameter.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** scheme **   <a name="appmesh-Type-HttpRouteMatch-scheme"></a>
The client request scheme to match on. Specify only one. Applicable only for HTTP2 routes.  
Type: String  
Valid Values: `http | https`   
Required: No

## See Also
<a name="API_HttpRouteMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpRouteMatch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpRouteMatch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpRouteMatch) 