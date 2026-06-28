---
id: "@specs/aws/network-firewall/docs/API_FirewallStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FirewallStatus"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FirewallStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FirewallStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FirewallStatus
<a name="API_FirewallStatus"></a>

Detailed information about the current status of a [Firewall](API_Firewall.md). You can retrieve this for a firewall by calling [DescribeFirewall](API_DescribeFirewall.md) and providing the firewall name and ARN.

The firewall status indicates a combined status. It indicates whether all subnets are up-to-date with the latest firewall configurations, which is based on the sync states config values, and also whether all subnets have their endpoints fully enabled, based on their sync states attachment values. 

## Contents
<a name="API_FirewallStatus_Contents"></a>

 ** ConfigurationSyncStateSummary **   <a name="networkfirewall-Type-FirewallStatus-ConfigurationSyncStateSummary"></a>
The configuration sync state for the firewall. This summarizes the `Config` settings in the `SyncStates` for this firewall status object.   
When you create a firewall or update its configuration, for example by adding a rule group to its firewall policy, Network Firewall distributes the configuration changes to all Availability Zones that have subnets defined for the firewall. This summary indicates whether the configuration changes have been applied everywhere.   
This status must be `IN_SYNC` for the firewall to be ready for use, but it doesn't indicate that the firewall is ready. The `Status` setting indicates firewall readiness. It's based on this setting and the readiness of the firewall endpoints to take traffic.   
Type: String  
Valid Values: `PENDING | IN_SYNC | CAPACITY_CONSTRAINED`   
Required: Yes

 ** Status **   <a name="networkfirewall-Type-FirewallStatus-Status"></a>
The readiness of the configured firewall to handle network traffic across all of the Availability Zones where you have it configured. This setting is `READY` only when the `ConfigurationSyncStateSummary` value is `IN_SYNC` and the `Attachment` `Status` values for all of the configured subnets are `READY`.   
Type: String  
Valid Values: `PROVISIONING | DELETING | READY`   
Required: Yes

 ** CapacityUsageSummary **   <a name="networkfirewall-Type-FirewallStatus-CapacityUsageSummary"></a>
Describes the capacity usage of the resources contained in a firewall's reference sets. Network Firewall calculates the capacity usage by taking an aggregated count of all of the resources used by all of the reference sets in a firewall.  
Type: [CapacityUsageSummary](API_CapacityUsageSummary.md) object  
Required: No

 ** SyncStates **   <a name="networkfirewall-Type-FirewallStatus-SyncStates"></a>
Status for the subnets that you've configured in the firewall. This contains one array element per Availability Zone where you've configured a subnet in the firewall.   
These objects provide detailed information for the settings `ConfigurationSyncStateSummary` and `Status`.   
Type: String to [SyncState](API_SyncState.md) object map  
Required: No

 ** TransitGatewayAttachmentSyncState **   <a name="networkfirewall-Type-FirewallStatus-TransitGatewayAttachmentSyncState"></a>
The synchronization state of the transit gateway attachment. This indicates whether the firewall's transit gateway configuration is properly synchronized and operational. Use this to verify that your transit gateway configuration changes have been applied.  
Type: [TransitGatewayAttachmentSyncState](API_TransitGatewayAttachmentSyncState.md) object  
Required: No

## See Also
<a name="API_FirewallStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallStatus) 