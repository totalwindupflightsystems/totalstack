---
id: "@specs/aws/appmesh/docs/API_GrpcGatewayRouteMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GrpcGatewayRouteMetadata"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GrpcGatewayRouteMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GrpcGatewayRouteMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GrpcGatewayRouteMetadata
<a name="API_GrpcGatewayRouteMetadata"></a>

An object representing the metadata of the gateway route.

## Contents
<a name="API_GrpcGatewayRouteMetadata_Contents"></a>

 ** name **   <a name="appmesh-Type-GrpcGatewayRouteMetadata-name"></a>
A name for the gateway route metadata.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** invert **   <a name="appmesh-Type-GrpcGatewayRouteMetadata-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.  
Type: Boolean  
Required: No

 ** match **   <a name="appmesh-Type-GrpcGatewayRouteMetadata-match"></a>
The criteria for determining a metadata match.  
Type: [GrpcMetadataMatchMethod](API_GrpcMetadataMatchMethod.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_GrpcGatewayRouteMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcGatewayRouteMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcGatewayRouteMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcGatewayRouteMetadata) 