---
id: "@specs/aws/appmesh/docs/API_GatewayRouteData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GatewayRouteData"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GatewayRouteData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GatewayRouteData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GatewayRouteData
<a name="API_GatewayRouteData"></a>

An object that represents a gateway route returned by a describe operation.

## Contents
<a name="API_GatewayRouteData_Contents"></a>

 ** gatewayRouteName **   <a name="appmesh-Type-GatewayRouteData-gatewayRouteName"></a>
The name of the gateway route.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** meshName **   <a name="appmesh-Type-GatewayRouteData-meshName"></a>
The name of the service mesh that the resource resides in.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** metadata **   <a name="appmesh-Type-GatewayRouteData-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object  
Required: Yes

 ** spec **   <a name="appmesh-Type-GatewayRouteData-spec"></a>
The specifications of the gateway route.  
Type: [GatewayRouteSpec](API_GatewayRouteSpec.md) object  
Required: Yes

 ** status **   <a name="appmesh-Type-GatewayRouteData-status"></a>
The status of the gateway route.  
Type: [GatewayRouteStatus](API_GatewayRouteStatus.md) object  
Required: Yes

 ** virtualGatewayName **   <a name="appmesh-Type-GatewayRouteData-virtualGatewayName"></a>
The virtual gateway that the gateway route is associated with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_GatewayRouteData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GatewayRouteData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GatewayRouteData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GatewayRouteData) 