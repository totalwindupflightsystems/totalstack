---
id: "@specs/aws/eks/docs/API_VpcConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VpcConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# VpcConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_VpcConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VpcConfigRequest
<a name="API_VpcConfigRequest"></a>

An object representing the VPC configuration to use for an Amazon EKS cluster.

## Contents
<a name="API_VpcConfigRequest_Contents"></a>

 ** controlPlaneEgressMode **   <a name="AmazonEKS-Type-VpcConfigRequest-controlPlaneEgressMode"></a>
Specifies the control plane egress routing mode for the cluster. If the cluster is set to `AWS_MANAGED`, Amazon EKS manages the egress path from the control plane and you don't need to configure NAT gateways or other routing infrastructure for control plane traffic. If the cluster is set to `CUSTOMER_ROUTED`, you manage the egress path from the control plane in your VPC subnets. You are responsible for ensuring that the control plane can reach required endpoints such as webhook servers and OIDC providers. The default value is `AWS_MANAGED`. Once set to `CUSTOMER_ROUTED`, this setting cannot be changed back to `AWS_MANAGED` on the same cluster.  
 [Learn more about control plane egress routing in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-egress.html)   
Type: String  
Valid Values: `AWS_MANAGED | CUSTOMER_ROUTED | CUSTOMER_ISOLATED`   
Required: No

 ** endpointPrivateAccess **   <a name="AmazonEKS-Type-VpcConfigRequest-endpointPrivateAccess"></a>
Set this value to `true` to enable private access for your cluster's Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC use the private VPC endpoint. The default value for this parameter is `false`, which disables private access for your Kubernetes API server. If you disable private access and you have nodes or AWS Fargate pods in the cluster, then ensure that `publicAccessCidrs` includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.  
Type: Boolean  
Required: No

 ** endpointPublicAccess **   <a name="AmazonEKS-Type-VpcConfigRequest-endpointPublicAccess"></a>
Set this value to `false` to disable public access to your cluster's Kubernetes API server endpoint. If you disable public access, your cluster's Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is `true`, which enables public access for your Kubernetes API server. The endpoint domain name and IP address family depends on the value of the `ipFamily` for the cluster. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.  
Type: Boolean  
Required: No

 ** publicAccessCidrs **   <a name="AmazonEKS-Type-VpcConfigRequest-publicAccessCidrs"></a>
The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is `0.0.0.0/0` and additionally `::/0` for dual-stack `IPv6` clusters. If you've disabled private endpoint access, make sure that you specify the necessary CIDR blocks for every node and AWS Fargate `Pod` in the cluster. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.  
Note that the public endpoints are dual-stack for only `IPv6` clusters that are made after October 2024. You can't add `IPv6` CIDR blocks to `IPv4` clusters or `IPv6` clusters that were made before October 2024.  
Type: Array of strings  
Required: No

 ** securityGroupIds **   <a name="AmazonEKS-Type-VpcConfigRequest-securityGroupIds"></a>
Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use that allow communication between your nodes and the Kubernetes control plane. If you don't specify any security groups, then familiarize yourself with the difference between Amazon EKS defaults for clusters deployed with Kubernetes. For more information, see [Amazon EKS security group considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the * *Amazon EKS User Guide* *.  
Type: Array of strings  
Required: No

 ** subnetIds **   <a name="AmazonEKS-Type-VpcConfigRequest-subnetIds"></a>
Specify subnets for your Amazon EKS nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your nodes and the Kubernetes control plane.  
Type: Array of strings  
Required: No

## See Also
<a name="API_VpcConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/VpcConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/VpcConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/VpcConfigRequest) 