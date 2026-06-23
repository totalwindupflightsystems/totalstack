---
id: "@specs/aws/appmesh/docs/API_RouteData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RouteData"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# RouteData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_RouteData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RouteData
<a name="API_RouteData"></a>

An object that represents a route returned by a describe operation.

## Contents
<a name="API_RouteData_Contents"></a>

 ** meshName **   <a name="appmesh-Type-RouteData-meshName"></a>
The name of the service mesh that the route resides in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** metadata **   <a name="appmesh-Type-RouteData-metadata"></a>
The associated metadata for the route.  
Type: [ResourceMetadata](API_ResourceMetadata.md) object  
Required: Yes

 ** routeName **   <a name="appmesh-Type-RouteData-routeName"></a>
The name of the route.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** spec **   <a name="appmesh-Type-RouteData-spec"></a>
The specifications of the route.  
Type: [RouteSpec](API_RouteSpec.md) object  
Required: Yes

 ** status **   <a name="appmesh-Type-RouteData-status"></a>
The status of the route.  
Type: [RouteStatus](API_RouteStatus.md) object  
Required: Yes

 ** virtualRouterName **   <a name="appmesh-Type-RouteData-virtualRouterName"></a>
The virtual router that the route is associated with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_RouteData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/RouteData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/RouteData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/RouteData) 