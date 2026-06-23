---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayData"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayData
<a name="API_VirtualGatewayData"></a>

An object that represents a virtual gateway returned by a describe operation.

## Contents
<a name="API_VirtualGatewayData_Contents"></a>

 ** meshName **   <a name="appmesh-Type-VirtualGatewayData-meshName"></a>
The name of the service mesh that the virtual gateway resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** metadata **   <a name="appmesh-Type-VirtualGatewayData-metadata"></a>
An object that represents metadata for a resource.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object  
Required: Yes

 ** spec **   <a name="appmesh-Type-VirtualGatewayData-spec"></a>
The specifications of the virtual gateway.  
Type: [VirtualGatewaySpec](API_VirtualGatewaySpec.md) object  
Required: Yes

 ** status **   <a name="appmesh-Type-VirtualGatewayData-status"></a>
The current status of the virtual gateway.  
Type: [VirtualGatewayStatus](API_VirtualGatewayStatus.md) object  
Required: Yes

 ** virtualGatewayName **   <a name="appmesh-Type-VirtualGatewayData-virtualGatewayName"></a>
The name of the virtual gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_VirtualGatewayData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayData) 