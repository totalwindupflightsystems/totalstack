---
id: "@specs/aws/appmesh/docs/API_VirtualServiceSpec"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualServiceSpec"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualServiceSpec

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualServiceSpec
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualServiceSpec
<a name="API_VirtualServiceSpec"></a>

An object that represents the specification of a virtual service.

## Contents
<a name="API_VirtualServiceSpec_Contents"></a>

 ** provider **   <a name="appmesh-Type-VirtualServiceSpec-provider"></a>
The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.  
Type: [VirtualServiceProvider](API_VirtualServiceProvider.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_VirtualServiceSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualServiceSpec) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualServiceSpec) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualServiceSpec) 