---
id: "@specs/aws/appmesh/docs/API_VirtualRouterData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualRouterData"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualRouterData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualRouterData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualRouterData
<a name="API_VirtualRouterData"></a>

An object that represents a virtual router returned by a describe operation.

## Contents
<a name="API_VirtualRouterData_Contents"></a>

 ** meshName **   <a name="appmesh-Type-VirtualRouterData-meshName"></a>
The name of the service mesh that the virtual router resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** metadata **   <a name="appmesh-Type-VirtualRouterData-metadata"></a>
The associated metadata for the virtual router.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object  
Required: Yes

 ** spec **   <a name="appmesh-Type-VirtualRouterData-spec"></a>
The specifications of the virtual router.  
Type: [VirtualRouterSpec](API_VirtualRouterSpec.md) object  
Required: Yes

 ** status **   <a name="appmesh-Type-VirtualRouterData-status"></a>
The current status of the virtual router.  
Type: [VirtualRouterStatus](API_VirtualRouterStatus.md) object  
Required: Yes

 ** virtualRouterName **   <a name="appmesh-Type-VirtualRouterData-virtualRouterName"></a>
The name of the virtual router.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_VirtualRouterData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualRouterData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualRouterData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualRouterData) 