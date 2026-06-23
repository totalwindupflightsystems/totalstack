---
id: "@specs/aws/appmesh/docs/API_MeshData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MeshData"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# MeshData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_MeshData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MeshData
<a name="API_MeshData"></a>

An object that represents a service mesh returned by a describe operation.

## Contents
<a name="API_MeshData_Contents"></a>

 ** meshName **   <a name="appmesh-Type-MeshData-meshName"></a>
The name of the service mesh.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** metadata **   <a name="appmesh-Type-MeshData-metadata"></a>
The associated metadata for the service mesh.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object  
Required: Yes

 ** spec **   <a name="appmesh-Type-MeshData-spec"></a>
The associated specification for the service mesh.  
Type: [MeshSpec](API_MeshSpec.md) object  
Required: Yes

 ** status **   <a name="appmesh-Type-MeshData-status"></a>
The status of the service mesh.  
Type: [MeshStatus](API_MeshStatus.md) object  
Required: Yes

## See Also
<a name="API_MeshData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/MeshData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/MeshData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/MeshData) 