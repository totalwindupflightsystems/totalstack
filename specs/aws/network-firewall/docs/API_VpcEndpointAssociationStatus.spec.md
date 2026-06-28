---
id: "@specs/aws/network-firewall/docs/API_VpcEndpointAssociationStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VpcEndpointAssociationStatus"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# VpcEndpointAssociationStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_VpcEndpointAssociationStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VpcEndpointAssociationStatus
<a name="API_VpcEndpointAssociationStatus"></a>

Detailed information about the current status of a [VpcEndpointAssociation](API_VpcEndpointAssociation.md). You can retrieve this by calling [DescribeVpcEndpointAssociation](API_DescribeVpcEndpointAssociation.md) and providing the VPC endpoint association ARN.

## Contents
<a name="API_VpcEndpointAssociationStatus_Contents"></a>

 ** Status **   <a name="networkfirewall-Type-VpcEndpointAssociationStatus-Status"></a>
The readiness of the configured firewall endpoint to handle network traffic.   
Type: String  
Valid Values: `PROVISIONING | DELETING | READY`   
Required: Yes

 ** AssociationSyncState **   <a name="networkfirewall-Type-VpcEndpointAssociationStatus-AssociationSyncState"></a>
The list of the Availability Zone sync states for all subnets that are defined by the firewall.   
Type: String to [AZSyncState](API_AZSyncState.md) object map  
Required: No

## See Also
<a name="API_VpcEndpointAssociationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/VpcEndpointAssociationStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/VpcEndpointAssociationStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/VpcEndpointAssociationStatus) 