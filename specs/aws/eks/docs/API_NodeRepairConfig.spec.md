---
id: "@specs/aws/eks/docs/API_NodeRepairConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodeRepairConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# NodeRepairConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_NodeRepairConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodeRepairConfig
<a name="API_NodeRepairConfig"></a>

The node auto repair configuration for the node group.

## Contents
<a name="API_NodeRepairConfig_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-NodeRepairConfig-enabled"></a>
Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default.  
Type: Boolean  
Required: No

 ** maxParallelNodesRepairedCount **   <a name="AmazonEKS-Type-NodeRepairConfig-maxParallelNodesRepairedCount"></a>
Specify the maximum number of nodes that can be repaired concurrently or in parallel, expressed as a count of unhealthy nodes. This gives you finer-grained control over the pace of node replacements. When using this, you cannot also set `maxParallelNodesRepairedPercentage` at the same time.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** maxParallelNodesRepairedPercentage **   <a name="AmazonEKS-Type-NodeRepairConfig-maxParallelNodesRepairedPercentage"></a>
Specify the maximum number of nodes that can be repaired concurrently or in parallel, expressed as a percentage of unhealthy nodes. This gives you finer-grained control over the pace of node replacements. When using this, you cannot also set `maxParallelNodesRepairedCount` at the same time.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** maxUnhealthyNodeThresholdCount **   <a name="AmazonEKS-Type-NodeRepairConfig-maxUnhealthyNodeThresholdCount"></a>
Specify a count threshold of unhealthy nodes, above which node auto repair actions will stop. When using this, you cannot also set `maxUnhealthyNodeThresholdPercentage` at the same time.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** maxUnhealthyNodeThresholdPercentage **   <a name="AmazonEKS-Type-NodeRepairConfig-maxUnhealthyNodeThresholdPercentage"></a>
Specify a percentage threshold of unhealthy nodes, above which node auto repair actions will stop. When using this, you cannot also set `maxUnhealthyNodeThresholdCount` at the same time.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** nodeRepairConfigOverrides **   <a name="AmazonEKS-Type-NodeRepairConfig-nodeRepairConfigOverrides"></a>
Specify granular overrides for specific repair actions. These overrides control the repair action and the repair delay time before a node is considered eligible for repair. If you use this, you must specify all the values.  
Type: Array of [NodeRepairConfigOverrides](API_NodeRepairConfigOverrides.md) objects  
Required: No

## See Also
<a name="API_NodeRepairConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/NodeRepairConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/NodeRepairConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/NodeRepairConfig) 