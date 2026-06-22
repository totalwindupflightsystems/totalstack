---
id: "@specs/aws/eks/docs/API_ControlPlanePlacementRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ControlPlanePlacementRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ControlPlanePlacementRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ControlPlanePlacementRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ControlPlanePlacementRequest
<a name="API_ControlPlanePlacementRequest"></a>

The placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_ControlPlanePlacementRequest_Contents"></a>

 ** groupName **   <a name="AmazonEKS-Type-ControlPlanePlacementRequest-groupName"></a>
The name of the placement group for the Kubernetes control plane instances. This setting can't be changed after cluster creation.   
Type: String  
Required: No

 ** spreadLevel **   <a name="AmazonEKS-Type-ControlPlanePlacementRequest-spreadLevel"></a>
Optional parameter to specify the placement group spread level for control plane instances. If not provided, Amazon EKS will deploy control plane instances without a placement group.  
Type: String  
Valid Values: `host | rack`   
Required: No

## See Also
<a name="API_ControlPlanePlacementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ControlPlanePlacementRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ControlPlanePlacementRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ControlPlanePlacementRequest) 