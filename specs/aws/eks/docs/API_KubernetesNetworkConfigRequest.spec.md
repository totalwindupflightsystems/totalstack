---
id: "@specs/aws/eks/docs/API_KubernetesNetworkConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KubernetesNetworkConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# KubernetesNetworkConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_KubernetesNetworkConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KubernetesNetworkConfigRequest
<a name="API_KubernetesNetworkConfigRequest"></a>

The Kubernetes network configuration for the cluster.

## Contents
<a name="API_KubernetesNetworkConfigRequest_Contents"></a>

 ** elasticLoadBalancing **   <a name="AmazonEKS-Type-KubernetesNetworkConfigRequest-elasticLoadBalancing"></a>
Request to enable or disable the load balancing capability on your EKS Auto Mode cluster. For more information, see EKS Auto Mode load balancing capability in the *Amazon EKS User Guide*.  
Type: [ElasticLoadBalancing](API_ElasticLoadBalancing.md) object  
Required: No

 ** ipFamily **   <a name="AmazonEKS-Type-KubernetesNetworkConfigRequest-ipFamily"></a>
Specify which IP family is used to assign Kubernetes pod and service IP addresses. If you don't specify a value, `ipv4` is used by default. You can only specify an IP family when you create a cluster and can't change this value once the cluster is created. If you specify `ipv6`, the VPC and subnets that you specify for cluster creation must have both `IPv4` and `IPv6` CIDR blocks assigned to them. You can't specify `ipv6` for clusters in China Regions.  
You can only specify `ipv6` for `1.21` and later clusters that use version `1.10.1` or later of the Amazon VPC CNI add-on. If you specify `ipv6`, then ensure that your VPC meets the requirements listed in the considerations listed in [Assigning IPv6 addresses to pods and services](https://docs.aws.amazon.com/eks/latest/userguide/cni-ipv6.html) in the *Amazon EKS User Guide*. Kubernetes assigns services `IPv6` addresses from the unique local address range `(fc00::/7)`. You can't specify a custom `IPv6` CIDR block. Pod addresses are assigned from the subnet's `IPv6` CIDR.  
Type: String  
Valid Values: `ipv4 | ipv6`   
Required: No

 ** serviceIpv4Cidr **   <a name="AmazonEKS-Type-KubernetesNetworkConfigRequest-serviceIpv4Cidr"></a>
Don't specify a value if you select `ipv6` for **ipFamily**. The CIDR block to assign Kubernetes service IP addresses from. If you don't specify a block, Kubernetes assigns addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks. We recommend that you specify a block that does not overlap with resources in other networks that are peered or connected to your VPC. The block must meet the following requirements:  
+ Within one of the following private IP address blocks: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`.
+ Doesn't overlap with any CIDR block assigned to the VPC that you selected for VPC.
+ Between `/24` and `/12`.
You can only specify a custom CIDR block when you create a cluster. You can't change this value after the cluster is created.
Type: String  
Required: No

## See Also
<a name="API_KubernetesNetworkConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/KubernetesNetworkConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/KubernetesNetworkConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/KubernetesNetworkConfigRequest) 