---
id: "@specs/aws/appmesh/docs/API_Backend"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Backend"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# Backend

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_Backend
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Backend
<a name="API_Backend"></a>

An object that represents the backends that a virtual node is expected to send outbound traffic to.

## Contents
<a name="API_Backend_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** virtualService **   <a name="appmesh-Type-Backend-virtualService"></a>
Specifies a virtual service to use as a backend.   
Type: [VirtualServiceBackend](API_VirtualServiceBackend.md) object  
Required: No

## See Also
<a name="API_Backend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/Backend) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/Backend) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/Backend) 