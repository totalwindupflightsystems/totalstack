---
id: "@specs/aws/appmesh/docs/API_GatewayRouteRef"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GatewayRouteRef"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GatewayRouteRef

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GatewayRouteRef
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GatewayRouteRef
<a name="API_GatewayRouteRef"></a>

An object that represents a gateway route returned by a list operation.

## Contents
<a name="API_GatewayRouteRef_Contents"></a>

 ** arn **   <a name="appmesh-Type-GatewayRouteRef-arn"></a>
The full Amazon Resource Name (ARN) for the gateway route.  
Type: String  
Required: Yes

 ** createdAt **   <a name="appmesh-Type-GatewayRouteRef-createdAt"></a>
The Unix epoch timestamp in seconds for when the resource was created.  
Type: Timestamp  
Required: Yes

 ** gatewayRouteName **   <a name="appmesh-Type-GatewayRouteRef-gatewayRouteName"></a>
The name of the gateway route.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** lastUpdatedAt **   <a name="appmesh-Type-GatewayRouteRef-lastUpdatedAt"></a>
The Unix epoch timestamp in seconds for when the resource was last updated.  
Type: Timestamp  
Required: Yes

 ** meshName **   <a name="appmesh-Type-GatewayRouteRef-meshName"></a>
The name of the service mesh that the resource resides in.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** meshOwner **   <a name="appmesh-Type-GatewayRouteRef-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Type: String  
Length Constraints: Fixed length of 12.  
Required: Yes

 ** resourceOwner **   <a name="appmesh-Type-GatewayRouteRef-resourceOwner"></a>
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it's the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Type: String  
Length Constraints: Fixed length of 12.  
Required: Yes

 ** version **   <a name="appmesh-Type-GatewayRouteRef-version"></a>
The version of the resource. Resources are created at version 1, and this version is incremented each time that they're updated.  
Type: Long  
Required: Yes

 ** virtualGatewayName **   <a name="appmesh-Type-GatewayRouteRef-virtualGatewayName"></a>
The virtual gateway that the gateway route is associated with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_GatewayRouteRef_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GatewayRouteRef) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GatewayRouteRef) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GatewayRouteRef) 