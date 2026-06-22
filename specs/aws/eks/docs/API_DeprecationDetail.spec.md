---
id: "@specs/aws/eks/docs/API_DeprecationDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeprecationDetail"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DeprecationDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DeprecationDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeprecationDetail
<a name="API_DeprecationDetail"></a>

The summary information about deprecated resource usage for an insight check in the `UPGRADE_READINESS` category.

## Contents
<a name="API_DeprecationDetail_Contents"></a>

 ** clientStats **   <a name="AmazonEKS-Type-DeprecationDetail-clientStats"></a>
Details about Kubernetes clients using the deprecated resources.  
Type: Array of [ClientStat](API_ClientStat.md) objects  
Required: No

 ** replacedWith **   <a name="AmazonEKS-Type-DeprecationDetail-replacedWith"></a>
The newer version of the resource to migrate to if applicable.   
Type: String  
Required: No

 ** startServingReplacementVersion **   <a name="AmazonEKS-Type-DeprecationDetail-startServingReplacementVersion"></a>
The version of the software where the newer resource version became available to migrate to if applicable.  
Type: String  
Required: No

 ** stopServingVersion **   <a name="AmazonEKS-Type-DeprecationDetail-stopServingVersion"></a>
The version of the software where the deprecated resource version will stop being served.  
Type: String  
Required: No

 ** usage **   <a name="AmazonEKS-Type-DeprecationDetail-usage"></a>
The deprecated version of the resource.  
Type: String  
Required: No

## See Also
<a name="API_DeprecationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DeprecationDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DeprecationDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DeprecationDetail) 