---
id: "@specs/aws/appmesh/docs/API_GrpcRouteMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GrpcRouteMetadata"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# GrpcRouteMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_GrpcRouteMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GrpcRouteMetadata
<a name="API_GrpcRouteMetadata"></a>

An object that represents the match metadata for the route.

## Contents
<a name="API_GrpcRouteMetadata_Contents"></a>

 ** name **   <a name="appmesh-Type-GrpcRouteMetadata-name"></a>
The name of the route.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Required: Yes

 ** invert **   <a name="appmesh-Type-GrpcRouteMetadata-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.  
Type: Boolean  
Required: No

 ** match **   <a name="appmesh-Type-GrpcRouteMetadata-match"></a>
An object that represents the data to match from the request.  
Type: [GrpcRouteMetadataMatchMethod](API_GrpcRouteMetadataMatchMethod.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_GrpcRouteMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcRouteMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcRouteMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcRouteMetadata) 