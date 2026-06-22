---
id: "@specs/aws/eks/docs/API_OutpostConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OutpostConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# OutpostConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_OutpostConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OutpostConfigRequest
<a name="API_OutpostConfigRequest"></a>

The configuration of your local Amazon EKS cluster on an AWS Outpost. Before creating a cluster on an Outpost, review [Creating a local cluster on an Outpost](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-create.html) in the *Amazon EKS User Guide*. This API isn't available for Amazon EKS clusters on the AWS cloud.

## Contents
<a name="API_OutpostConfigRequest_Contents"></a>

 ** controlPlaneInstanceType **   <a name="AmazonEKS-Type-OutpostConfigRequest-controlPlaneInstanceType"></a>
The Amazon EC2 instance type for the Kubernetes control plane instances of your local Amazon EKS cluster on AWS Outposts. This instance type applies to all control plane instances and cannot be changed after cluster creation.  
For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.  
   
Type: String  
Required: Yes

 ** outpostArns **   <a name="AmazonEKS-Type-OutpostConfigRequest-outpostArns"></a>
The ARN of the Outpost that you want to use for your local Amazon EKS cluster on Outposts. Only a single Outpost ARN is supported.  
Type: Array of strings  
Required: Yes

 ** controlPlanePlacement **   <a name="AmazonEKS-Type-OutpostConfigRequest-controlPlanePlacement"></a>
An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.  
Type: [ControlPlanePlacementRequest](API_ControlPlanePlacementRequest.md) object  
Required: No

 ** etcdInstanceType **   <a name="AmazonEKS-Type-OutpostConfigRequest-etcdInstanceType"></a>
The Amazon EC2 instance type for etcd instances of your local Amazon EKS cluster on AWS Outposts. This instance type applies to all etcd instances and cannot be changed after cluster creation.  
Type: String  
Required: No

 ** etcdPlacement **   <a name="AmazonEKS-Type-OutpostConfigRequest-etcdPlacement"></a>
An object representing the placement configuration for the etcd instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.  
Type: [EtcdPlacementRequest](API_EtcdPlacementRequest.md) object  
Required: No

## See Also
<a name="API_OutpostConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/OutpostConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/OutpostConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/OutpostConfigRequest) 