---
id: "@specs/aws/eks/docs/API_RemoteNodeNetwork"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoteNodeNetwork"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# RemoteNodeNetwork

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_RemoteNodeNetwork
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoteNodeNetwork
<a name="API_RemoteNodeNetwork"></a>

A network CIDR that can contain hybrid nodes.

These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator. 

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).

It must satisfy the following requirements:
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
+ Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including AWS Transit Gateway, AWS Site-to-Site VPN, or AWS Direct Connect.
+ Each host must allow outbound connection to the EKS cluster control plane on TCP ports `443` and `10250`.
+ Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.
+  Each host must allow TCP and UDP network connectivity to and from other hosts that are running `CoreDNS` on UDP port `53` for service and pod DNS names.

## Contents
<a name="API_RemoteNodeNetwork_Contents"></a>

 ** cidrs **   <a name="AmazonEKS-Type-RemoteNodeNetwork-cidrs"></a>
A network CIDR that can contain hybrid nodes.  
These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator.   
Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).  
It must satisfy the following requirements:  
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
+ Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including AWS Transit Gateway, AWS Site-to-Site VPN, or AWS Direct Connect.
+ Each host must allow outbound connection to the EKS cluster control plane on TCP ports `443` and `10250`.
+ Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.
+  Each host must allow TCP and UDP network connectivity to and from other hosts that are running `CoreDNS` on UDP port `53` for service and pod DNS names.
Type: Array of strings  
Required: No

## See Also
<a name="API_RemoteNodeNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/RemoteNodeNetwork) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/RemoteNodeNetwork) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/RemoteNodeNetwork) 