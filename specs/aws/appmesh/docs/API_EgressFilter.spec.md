---
id: "@specs/aws/appmesh/docs/API_EgressFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EgressFilter"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# EgressFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_EgressFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EgressFilter
<a name="API_EgressFilter"></a>

An object that represents the egress filter rules for a service mesh.

## Contents
<a name="API_EgressFilter_Contents"></a>

 ** type **   <a name="appmesh-Type-EgressFilter-type"></a>
The egress filter type. By default, the type is `DROP_ALL`, which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to `*.amazonaws.com` for AWS API calls). You can set the egress filter type to `ALLOW_ALL` to allow egress to any endpoint inside or outside of the service mesh.  
If you specify any backends on a virtual node when using `ALLOW_ALL`, you must specifiy all egress for that virtual node as backends. Otherwise, `ALLOW_ALL` will no longer work for that virtual node.
Type: String  
Valid Values: `ALLOW_ALL | DROP_ALL`   
Required: Yes

## See Also
<a name="API_EgressFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/EgressFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/EgressFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/EgressFilter) 