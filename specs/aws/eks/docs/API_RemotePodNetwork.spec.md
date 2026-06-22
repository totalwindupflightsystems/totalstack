---
id: "@specs/aws/eks/docs/API_RemotePodNetwork"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemotePodNetwork"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# RemotePodNetwork

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_RemotePodNetwork
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemotePodNetwork
<a name="API_RemotePodNetwork"></a>

A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.

These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isn't available for on-premises and edge locations.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).

It must satisfy the following requirements:
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.

## Contents
<a name="API_RemotePodNetwork_Contents"></a>

 ** cidrs **   <a name="AmazonEKS-Type-RemotePodNetwork-cidrs"></a>
A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.  
These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isn't available for on-premises and edge locations.  
Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).  
It must satisfy the following requirements:  
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
Type: Array of strings  
Required: No

## See Also
<a name="API_RemotePodNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/RemotePodNetwork) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/RemotePodNetwork) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/RemotePodNetwork) 