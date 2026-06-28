---
id: "@specs/aws/network-firewall/docs/API_PerObjectStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PerObjectStatus"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# PerObjectStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_PerObjectStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PerObjectStatus
<a name="API_PerObjectStatus"></a>

Provides configuration status for a single policy or rule group that is used for a firewall endpoint. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic. This is part of a [SyncState](API_SyncState.md) for a firewall.

## Contents
<a name="API_PerObjectStatus_Contents"></a>

 ** SyncStatus **   <a name="networkfirewall-Type-PerObjectStatus-SyncStatus"></a>
Indicates whether this object is in sync with the version indicated in the update token.  
Type: String  
Valid Values: `PENDING | IN_SYNC | CAPACITY_CONSTRAINED | NOT_SUBSCRIBED | DEPRECATED`   
Required: No

 ** UpdateToken **   <a name="networkfirewall-Type-PerObjectStatus-UpdateToken"></a>
The current version of the object that is either in sync or pending synchronization.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: No

## See Also
<a name="API_PerObjectStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/PerObjectStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/PerObjectStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/PerObjectStatus) 