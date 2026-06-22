---
id: "@specs/aws/eks/docs/API_NodegroupUpdateConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodegroupUpdateConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# NodegroupUpdateConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_NodegroupUpdateConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodegroupUpdateConfig
<a name="API_NodegroupUpdateConfig"></a>

The node group update configuration. An Amazon EKS managed node group updates by replacing nodes with new nodes of newer AMI versions in parallel. You choose the *maximum unavailable* and the *update strategy*.

## Contents
<a name="API_NodegroupUpdateConfig_Contents"></a>

 ** maxUnavailable **   <a name="AmazonEKS-Type-NodegroupUpdateConfig-maxUnavailable"></a>
The maximum number of nodes unavailable at once during a version update. Nodes are updated in parallel. This value or `maxUnavailablePercentage` is required to have a value.The maximum number is 100.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** maxUnavailablePercentage **   <a name="AmazonEKS-Type-NodegroupUpdateConfig-maxUnavailablePercentage"></a>
The maximum percentage of nodes unavailable during a version update. This percentage of nodes are updated in parallel, up to 100 nodes at once. This value or `maxUnavailable` is required to have a value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** updateStrategy **   <a name="AmazonEKS-Type-NodegroupUpdateConfig-updateStrategy"></a>
The configuration for the behavior to follow during a node group version update of this managed node group. You choose between two possible strategies for replacing nodes during an [https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion.html) action.  
An Amazon EKS managed node group updates by replacing nodes with new nodes of newer AMI versions in parallel. The *update strategy* changes the managed node update behavior of the managed node group for each quantity. The *default* strategy has guardrails to protect you from misconfiguration and launches the new instances first, before terminating the old instances. The *minimal* strategy removes the guardrails and terminates the old instances before launching the new instances. This minimal strategy is useful in scenarios where you are constrained to resources or costs (for example, with hardware accelerators such as GPUs).  
Type: String  
Valid Values: `DEFAULT | MINIMAL`   
Required: No

## See Also
<a name="API_NodegroupUpdateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/NodegroupUpdateConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/NodegroupUpdateConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/NodegroupUpdateConfig) 