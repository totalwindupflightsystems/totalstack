---
id: "@specs/aws/eks/docs/API_ControlPlaneScalingConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ControlPlaneScalingConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ControlPlaneScalingConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ControlPlaneScalingConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ControlPlaneScalingConfig
<a name="API_ControlPlaneScalingConfig"></a>

The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.

## Contents
<a name="API_ControlPlaneScalingConfig_Contents"></a>

 ** tier **   <a name="AmazonEKS-Type-ControlPlaneScalingConfig-tier"></a>
The control plane scaling tier configuration. Available options are `standard`, `tier-xl`, `tier-2xl`, `tier-4xl, or tier-8xl`. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.  
Type: String  
Valid Values: `standard | tier-xl | tier-2xl | tier-4xl | tier-8xl`   
Required: No

## See Also
<a name="API_ControlPlaneScalingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ControlPlaneScalingConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ControlPlaneScalingConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ControlPlaneScalingConfig) 