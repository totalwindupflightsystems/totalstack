---
id: "@specs/aws/eks/docs/API_NodeRepairConfigOverrides"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodeRepairConfigOverrides"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# NodeRepairConfigOverrides

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_NodeRepairConfigOverrides
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodeRepairConfigOverrides
<a name="API_NodeRepairConfigOverrides"></a>

Specify granular overrides for specific repair actions. These overrides control the repair action and the repair delay time before a node is considered eligible for repair. If you use this, you must specify all the values.

## Contents
<a name="API_NodeRepairConfigOverrides_Contents"></a>

 ** minRepairWaitTimeMins **   <a name="AmazonEKS-Type-NodeRepairConfigOverrides-minRepairWaitTimeMins"></a>
Specify the minimum time in minutes to wait before attempting to repair a node with this specific `nodeMonitoringCondition` and `nodeUnhealthyReason`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** nodeMonitoringCondition **   <a name="AmazonEKS-Type-NodeRepairConfigOverrides-nodeMonitoringCondition"></a>
Specify an unhealthy condition reported by the node monitoring agent that this override would apply to.  
Type: String  
Required: No

 ** nodeUnhealthyReason **   <a name="AmazonEKS-Type-NodeRepairConfigOverrides-nodeUnhealthyReason"></a>
Specify a reason reported by the node monitoring agent that this override would apply to.  
Type: String  
Required: No

 ** repairAction **   <a name="AmazonEKS-Type-NodeRepairConfigOverrides-repairAction"></a>
Specify the repair action to take for nodes when all of the specified conditions are met.  
Type: String  
Valid Values: `Replace | Reboot | NoAction`   
Required: No

## See Also
<a name="API_NodeRepairConfigOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/NodeRepairConfigOverrides) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/NodeRepairConfigOverrides) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/NodeRepairConfigOverrides) 