---
id: "@specs/aws/appmesh/docs/API_GrpcGatewayRouteMatch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GrpcGatewayRouteMatch"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GrpcGatewayRouteMatch

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GrpcGatewayRouteMatch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GrpcGatewayRouteMatch
<a name="API_GrpcGatewayRouteMatch"></a>

An object that represents the criteria for determining a request match.

## Contents
<a name="API_GrpcGatewayRouteMatch_Contents"></a>

 ** hostname **   <a name="appmesh-Type-GrpcGatewayRouteMatch-hostname"></a>
The gateway route host name to be matched on.  
Type: [GatewayRouteHostnameMatch](API_GatewayRouteHostnameMatch.md) object  
Required: No

 ** metadata **   <a name="appmesh-Type-GrpcGatewayRouteMatch-metadata"></a>
The gateway route metadata to be matched on.  
Type: Array of [GrpcGatewayRouteMetadata](API_GrpcGatewayRouteMetadata.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** port **   <a name="appmesh-Type-GrpcGatewayRouteMatch-port"></a>
The gateway route port to be matched on.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65535.  
Required: No

 ** serviceName **   <a name="appmesh-Type-GrpcGatewayRouteMatch-serviceName"></a>
The fully qualified domain name for the service to match from the request.  
Type: String  
Required: No

## See Also
<a name="API_GrpcGatewayRouteMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcGatewayRouteMatch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcGatewayRouteMatch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcGatewayRouteMatch) 