---
id: "@specs/aws/eks/docs/API_RemoteNetworkConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoteNetworkConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# RemoteNetworkConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_RemoteNetworkConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoteNetworkConfigRequest
<a name="API_RemoteNetworkConfigRequest"></a>

The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.

## Contents
<a name="API_RemoteNetworkConfigRequest_Contents"></a>

 ** remoteNodeNetworks **   <a name="AmazonEKS-Type-RemoteNetworkConfigRequest-remoteNodeNetworks"></a>
The list of network CIDRs that can contain hybrid nodes.  
These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator.   
Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).  
It must satisfy the following requirements:  
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
+ Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including AWS Transit Gateway, AWS Site-to-Site VPN, or AWS Direct Connect.
+ Each host must allow outbound connection to the EKS cluster control plane on TCP ports `443` and `10250`.
+ Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.
+  Each host must allow TCP and UDP network connectivity to and from other hosts that are running `CoreDNS` on UDP port `53` for service and pod DNS names.
Type: Array of [RemoteNodeNetwork](API_RemoteNodeNetwork.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** remotePodNetworks **   <a name="AmazonEKS-Type-RemoteNetworkConfigRequest-remotePodNetworks"></a>
The list of network CIDRs that can contain pods that run Kubernetes webhooks on hybrid nodes.  
These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isn't available for on-premises and edge locations.  
Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).  
It must satisfy the following requirements:  
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
Type: Array of [RemotePodNetwork](API_RemotePodNetwork.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

## See Also
<a name="API_RemoteNetworkConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/RemoteNetworkConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/RemoteNetworkConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/RemoteNetworkConfigRequest) 