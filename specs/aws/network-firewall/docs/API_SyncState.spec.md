---
id: "@specs/aws/network-firewall/docs/API_SyncState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SyncState"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# SyncState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_SyncState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SyncState
<a name="API_SyncState"></a>

The status of the firewall endpoint and firewall policy configuration for a single VPC subnet. This is part of the [FirewallStatus](API_FirewallStatus.md). 

For each VPC subnet that you associate with a firewall, AWS Network Firewall does the following: 
+ Instantiates a firewall endpoint in the subnet, ready to take traffic.
+ Configures the endpoint with the current firewall policy settings, to provide the filtering behavior for the endpoint.

When you update a firewall, for example to add a subnet association or change a rule group in the firewall policy, the affected sync states reflect out-of-sync or not ready status until the changes are complete. 

## Contents
<a name="API_SyncState_Contents"></a>

 ** Attachment **   <a name="networkfirewall-Type-SyncState-Attachment"></a>
The configuration and status for a single firewall subnet. For each configured subnet, Network Firewall creates the attachment by instantiating the firewall endpoint in the subnet so that it's ready to take traffic.   
Type: [Attachment](API_Attachment.md) object  
Required: No

 ** Config **   <a name="networkfirewall-Type-SyncState-Config"></a>
The configuration status of the firewall endpoint in a single VPC subnet. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic.   
Type: String to [PerObjectStatus](API_PerObjectStatus.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## See Also
<a name="API_SyncState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/SyncState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/SyncState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/SyncState) 