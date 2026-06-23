---
id: "@specs/aws/appmesh/docs/API_VirtualServiceBackend"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualServiceBackend"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualServiceBackend

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualServiceBackend
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualServiceBackend
<a name="API_VirtualServiceBackend"></a>

An object that represents a virtual service backend for a virtual node.

## Contents
<a name="API_VirtualServiceBackend_Contents"></a>

 ** virtualServiceName **   <a name="appmesh-Type-VirtualServiceBackend-virtualServiceName"></a>
The name of the virtual service that is acting as a virtual node backend.  
App Mesh doesn't validate the existence of those virtual services specified in backends. This is to prevent a cyclic dependency between virtual nodes and virtual services creation. Make sure the virtual service name is correct. The virtual service can be created afterwards if it doesn't already exist. 
Type: String  
Required: Yes

 ** clientPolicy **   <a name="appmesh-Type-VirtualServiceBackend-clientPolicy"></a>
A reference to an object that represents the client policy for a backend.  
Type: [ClientPolicy](API_ClientPolicy.md) object  
Required: No

## See Also
<a name="API_VirtualServiceBackend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualServiceBackend) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualServiceBackend) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualServiceBackend) 