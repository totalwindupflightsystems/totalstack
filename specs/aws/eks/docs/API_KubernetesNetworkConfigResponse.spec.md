---
id: "@specs/aws/eks/docs/API_KubernetesNetworkConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KubernetesNetworkConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# KubernetesNetworkConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_KubernetesNetworkConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KubernetesNetworkConfigResponse
<a name="API_KubernetesNetworkConfigResponse"></a>

The Kubernetes network configuration for the cluster. The response contains a value for **serviceIpv6Cidr** or **serviceIpv4Cidr**, but not both. 

## Contents
<a name="API_KubernetesNetworkConfigResponse_Contents"></a>

 ** elasticLoadBalancing **   <a name="AmazonEKS-Type-KubernetesNetworkConfigResponse-elasticLoadBalancing"></a>
Indicates the current configuration of the load balancing capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled.  
Type: [ElasticLoadBalancing](API_ElasticLoadBalancing.md) object  
Required: No

 ** ipFamily **   <a name="AmazonEKS-Type-KubernetesNetworkConfigResponse-ipFamily"></a>
The IP family used to assign Kubernetes `Pod` and `Service` objects IP addresses. The IP family is always `ipv4`, unless you have a `1.21` or later cluster running version `1.10.1` or later of the Amazon VPC CNI plugin for Kubernetes and specified `ipv6` when you created the cluster.   
Type: String  
Valid Values: `ipv4 | ipv6`   
Required: No

 ** serviceIpv4Cidr **   <a name="AmazonEKS-Type-KubernetesNetworkConfigResponse-serviceIpv4Cidr"></a>
The CIDR block that Kubernetes `Pod` and `Service` object IP addresses are assigned from. Kubernetes assigns addresses from an `IPv4` CIDR block assigned to a subnet that the node is in. If you didn't specify a CIDR block when you created the cluster, then Kubernetes assigns addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks. If this was specified, then it was specified when the cluster was created and it can't be changed.  
Type: String  
Required: No

 ** serviceIpv6Cidr **   <a name="AmazonEKS-Type-KubernetesNetworkConfigResponse-serviceIpv6Cidr"></a>
The CIDR block that Kubernetes pod and service IP addresses are assigned from if you created a 1.21 or later cluster with version 1.10.1 or later of the Amazon VPC CNI add-on and specified `ipv6` for **ipFamily** when you created the cluster. Kubernetes assigns service addresses from the unique local address range (`fc00::/7`) because you can't specify a custom IPv6 CIDR block when you create the cluster.  
Type: String  
Required: No

## See Also
<a name="API_KubernetesNetworkConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/KubernetesNetworkConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/KubernetesNetworkConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/KubernetesNetworkConfigResponse) 