---
id: "@specs/aws/eks/docs/API_VpcConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VpcConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# VpcConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_VpcConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VpcConfigResponse
<a name="API_VpcConfigResponse"></a>

An object representing an Amazon EKS cluster VPC configuration response.

## Contents
<a name="API_VpcConfigResponse_Contents"></a>

 ** clusterSecurityGroupId **   <a name="AmazonEKS-Type-VpcConfigResponse-clusterSecurityGroupId"></a>
The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control-plane-to-data-plane communication.  
Type: String  
Required: No

 ** controlPlaneEgressMode **   <a name="AmazonEKS-Type-VpcConfigResponse-controlPlaneEgressMode"></a>
The current control plane egress routing mode for the cluster. If the cluster is set to `AWS_MANAGED`, Amazon EKS manages the egress path from the control plane. If the cluster is set to `CUSTOMER_ROUTED`, you manage the egress path from the control plane in your VPC subnets.  
 [Learn more about control plane egress routing in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-egress.html)   
Type: String  
Valid Values: `AWS_MANAGED | CUSTOMER_ROUTED | CUSTOMER_ISOLATED`   
Required: No

 ** endpointPrivateAccess **   <a name="AmazonEKS-Type-VpcConfigResponse-endpointPrivateAccess"></a>
This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster's VPC use the private VPC endpoint instead of traversing the internet. If this value is disabled and you have nodes or AWS Fargate pods in the cluster, then ensure that `publicAccessCidrs` includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.  
Type: Boolean  
Required: No

 ** endpointPublicAccess **   <a name="AmazonEKS-Type-VpcConfigResponse-endpointPublicAccess"></a>
Whether the public API server endpoint is enabled.  
Type: Boolean  
Required: No

 ** publicAccessCidrs **   <a name="AmazonEKS-Type-VpcConfigResponse-publicAccessCidrs"></a>
The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is `0.0.0.0/0` and additionally `::/0` for dual-stack `IPv6` clusters. If you've disabled private endpoint access, make sure that you specify the necessary CIDR blocks for every node and AWS Fargate `Pod` in the cluster. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.  
Note that the public endpoints are dual-stack for only `IPv6` clusters that are made after October 2024. You can't add `IPv6` CIDR blocks to `IPv4` clusters or `IPv6` clusters that were made before October 2024.  
Type: Array of strings  
Required: No

 ** securityGroupIds **   <a name="AmazonEKS-Type-VpcConfigResponse-securityGroupIds"></a>
The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane.  
Type: Array of strings  
Required: No

 ** subnetIds **   <a name="AmazonEKS-Type-VpcConfigResponse-subnetIds"></a>
The subnets associated with your cluster.  
Type: Array of strings  
Required: No

 ** vpcId **   <a name="AmazonEKS-Type-VpcConfigResponse-vpcId"></a>
The VPC associated with your cluster.  
Type: String  
Required: No

## See Also
<a name="API_VpcConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/VpcConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/VpcConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/VpcConfigResponse) 