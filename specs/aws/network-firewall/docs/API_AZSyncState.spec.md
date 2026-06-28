---
id: "@specs/aws/network-firewall/docs/API_AZSyncState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AZSyncState"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# AZSyncState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_AZSyncState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AZSyncState
<a name="API_AZSyncState"></a>

The status of the firewall endpoint defined by a `VpcEndpointAssociation`. 

## Contents
<a name="API_AZSyncState_Contents"></a>

 ** Attachment **   <a name="networkfirewall-Type-AZSyncState-Attachment"></a>
The definition and status of the firewall endpoint for a single subnet. In each configured subnet, Network Firewall instantiates a firewall endpoint to handle network traffic.   
This data type is used for any firewall endpoint type:   
+ For `Firewall.SubnetMappings`, this `Attachment` is part of the `FirewallStatus` sync states information. You define firewall subnets using `CreateFirewall` and `AssociateSubnets`. 
+ For `VpcEndpointAssociation`, this `Attachment` is part of the `VpcEndpointAssociationStatus` sync states information. You define these subnets using `CreateVpcEndpointAssociation`. 
Type: [Attachment](API_Attachment.md) object  
Required: No

## See Also
<a name="API_AZSyncState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AZSyncState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AZSyncState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AZSyncState) 