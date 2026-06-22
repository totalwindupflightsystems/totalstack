---
id: "@specs/aws/eks/docs/API_EtcdPlacementRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EtcdPlacementRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# EtcdPlacementRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_EtcdPlacementRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EtcdPlacementRequest
<a name="API_EtcdPlacementRequest"></a>

The placement configuration for the etcd instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_EtcdPlacementRequest_Contents"></a>

 ** spreadLevel **   <a name="AmazonEKS-Type-EtcdPlacementRequest-spreadLevel"></a>
Optional parameter to specify the placement group spread level for etcd instances. If not provided, Amazon EKS will deploy etcd instances without a placement group.  
Type: String  
Valid Values: `host | rack`   
Required: No

## See Also
<a name="API_EtcdPlacementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/EtcdPlacementRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/EtcdPlacementRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/EtcdPlacementRequest) 