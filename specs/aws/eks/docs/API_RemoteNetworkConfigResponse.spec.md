---
id: "@specs/aws/eks/docs/API_RemoteNetworkConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoteNetworkConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# RemoteNetworkConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_RemoteNetworkConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoteNetworkConfigResponse
<a name="API_RemoteNetworkConfigResponse"></a>

The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.

## Contents
<a name="API_RemoteNetworkConfigResponse_Contents"></a>

 ** remoteNodeNetworks **   <a name="AmazonEKS-Type-RemoteNetworkConfigResponse-remoteNodeNetworks"></a>
The list of network CIDRs that can contain hybrid nodes.  
Type: Array of [RemoteNodeNetwork](API_RemoteNodeNetwork.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** remotePodNetworks **   <a name="AmazonEKS-Type-RemoteNetworkConfigResponse-remotePodNetworks"></a>
The list of network CIDRs that can contain pods that run Kubernetes webhooks on hybrid nodes.  
Type: Array of [RemotePodNetwork](API_RemotePodNetwork.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

## See Also
<a name="API_RemoteNetworkConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/RemoteNetworkConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/RemoteNetworkConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/RemoteNetworkConfigResponse) 