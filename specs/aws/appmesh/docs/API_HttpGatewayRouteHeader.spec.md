---
id: "@specs/aws/appmesh/docs/API_HttpGatewayRouteHeader"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpGatewayRouteHeader"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# HttpGatewayRouteHeader

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_HttpGatewayRouteHeader
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpGatewayRouteHeader
<a name="API_HttpGatewayRouteHeader"></a>

An object that represents the HTTP header in the gateway route.

## Contents
<a name="API_HttpGatewayRouteHeader_Contents"></a>

 ** name **   <a name="appmesh-Type-HttpGatewayRouteHeader-name"></a>
A name for the HTTP header in the gateway route that will be matched on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** invert **   <a name="appmesh-Type-HttpGatewayRouteHeader-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.  
Type: Boolean  
Required: No

 ** match **   <a name="appmesh-Type-HttpGatewayRouteHeader-match"></a>
An object that represents the method and value to match with the header value sent in a request. Specify one match method.  
Type: [HeaderMatchMethod](API_HeaderMatchMethod.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_HttpGatewayRouteHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpGatewayRouteHeader) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpGatewayRouteHeader) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpGatewayRouteHeader) 