---
id: "@specs/aws/appmesh/docs/API_ResourceMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResourceMetadata"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# ResourceMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_ResourceMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResourceMetadata
<a name="API_ResourceMetadata"></a>

An object that represents metadata for a resource.

## Contents
<a name="API_ResourceMetadata_Contents"></a>

 ** arn **   <a name="appmesh-Type-ResourceMetadata-arn"></a>
The full Amazon Resource Name (ARN) for the resource.  
Type: String  
Required: Yes

 ** createdAt **   <a name="appmesh-Type-ResourceMetadata-createdAt"></a>
The Unix epoch timestamp in seconds for when the resource was created.  
Type: Timestamp  
Required: Yes

 ** lastUpdatedAt **   <a name="appmesh-Type-ResourceMetadata-lastUpdatedAt"></a>
The Unix epoch timestamp in seconds for when the resource was last updated.  
Type: Timestamp  
Required: Yes

 ** meshOwner **   <a name="appmesh-Type-ResourceMetadata-meshOwner"></a>
The AWS IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Type: String  
Length Constraints: Fixed length of 12.  
Required: Yes

 ** resourceOwner **   <a name="appmesh-Type-ResourceMetadata-resourceOwner"></a>
The AWS IAM account ID of the resource owner. If the account ID is not your own, then it's the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html).  
Type: String  
Length Constraints: Fixed length of 12.  
Required: Yes

 ** uid **   <a name="appmesh-Type-ResourceMetadata-uid"></a>
The unique identifier for the resource.  
Type: String  
Required: Yes

 ** version **   <a name="appmesh-Type-ResourceMetadata-version"></a>
The version of the resource. Resources are created at version 1, and this version is incremented each time that they're updated.  
Type: Long  
Required: Yes

## See Also
<a name="API_ResourceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ResourceMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ResourceMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ResourceMetadata) 