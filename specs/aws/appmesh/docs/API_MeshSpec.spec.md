---
id: "@specs/aws/appmesh/docs/API_MeshSpec"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MeshSpec"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# MeshSpec

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_MeshSpec
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MeshSpec
<a name="API_MeshSpec"></a>

An object that represents the specification of a service mesh.

## Contents
<a name="API_MeshSpec_Contents"></a>

 ** egressFilter **   <a name="appmesh-Type-MeshSpec-egressFilter"></a>
The egress filter rules for the service mesh.  
Type: [EgressFilter](API_EgressFilter.md) object  
Required: No

 ** serviceDiscovery **   <a name="appmesh-Type-MeshSpec-serviceDiscovery"></a>
An object that represents the service discovery information for a service mesh.  
Type: [MeshServiceDiscovery](API_MeshServiceDiscovery.md) object  
Required: No

## See Also
<a name="API_MeshSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/MeshSpec) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/MeshSpec) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/MeshSpec) 