---
id: "@specs/aws/eks/docs/API_OutpostConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OutpostConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# OutpostConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_OutpostConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OutpostConfigResponse
<a name="API_OutpostConfigResponse"></a>

An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This API isn't available for Amazon EKS clusters on the AWS cloud.

## Contents
<a name="API_OutpostConfigResponse_Contents"></a>

 ** controlPlaneInstanceType **   <a name="AmazonEKS-Type-OutpostConfigResponse-controlPlaneInstanceType"></a>
The Amazon EC2 instance type for the Kubernetes control plane instances of your local Amazon EKS cluster on AWS Outposts. The instance type is the same for all control plane instances.  
Type: String  
Required: Yes

 ** outpostArns **   <a name="AmazonEKS-Type-OutpostConfigResponse-outpostArns"></a>
The ARN of the Outpost that you specified for use with your local Amazon EKS cluster on Outposts.  
Type: Array of strings  
Required: Yes

 ** controlPlanePlacement **   <a name="AmazonEKS-Type-OutpostConfigResponse-controlPlanePlacement"></a>
An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.  
Type: [ControlPlanePlacementResponse](API_ControlPlanePlacementResponse.md) object  
Required: No

 ** etcdInstanceType **   <a name="AmazonEKS-Type-OutpostConfigResponse-etcdInstanceType"></a>
The Amazon EC2 instance type for etcd instances of your local Amazon EKS cluster on AWS Outposts. The instance type is the same for all etcd instances.  
Type: String  
Required: No

 ** etcdPlacement **   <a name="AmazonEKS-Type-OutpostConfigResponse-etcdPlacement"></a>
An object representing the placement configuration for the etcd instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.  
Type: [EtcdPlacementResponse](API_EtcdPlacementResponse.md) object  
Required: No

## See Also
<a name="API_OutpostConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/OutpostConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/OutpostConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/OutpostConfigResponse) 