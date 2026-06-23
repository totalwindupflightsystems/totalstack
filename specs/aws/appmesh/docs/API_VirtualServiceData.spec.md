---
id: "@specs/aws/appmesh/docs/API_VirtualServiceData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualServiceData"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualServiceData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualServiceData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualServiceData
<a name="API_VirtualServiceData"></a>

An object that represents a virtual service returned by a describe operation.

## Contents
<a name="API_VirtualServiceData_Contents"></a>

 ** meshName **   <a name="appmesh-Type-VirtualServiceData-meshName"></a>
The name of the service mesh that the virtual service resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** metadata **   <a name="appmesh-Type-VirtualServiceData-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object  
Required: Yes

 ** spec **   <a name="appmesh-Type-VirtualServiceData-spec"></a>
The specifications of the virtual service.  
Type: [VirtualServiceSpec](API_VirtualServiceSpec.md) object  
Required: Yes

 ** status **   <a name="appmesh-Type-VirtualServiceData-status"></a>
The current status of the virtual service.  
Type: [VirtualServiceStatus](API_VirtualServiceStatus.md) object  
Required: Yes

 ** virtualServiceName **   <a name="appmesh-Type-VirtualServiceData-virtualServiceName"></a>
The name of the virtual service.  
Type: String  
Required: Yes

## See Also
<a name="API_VirtualServiceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualServiceData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualServiceData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualServiceData) 