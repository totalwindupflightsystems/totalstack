---
id: "@specs/aws/network-firewall/docs/API_AvailabilityZoneMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AvailabilityZoneMapping"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# AvailabilityZoneMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_AvailabilityZoneMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AvailabilityZoneMapping
<a name="API_AvailabilityZoneMapping"></a>

Defines the mapping between an Availability Zone and a firewall endpoint for a transit gateway-attached firewall. Each mapping represents where the firewall can process traffic. You use these mappings when calling [CreateFirewall](API_CreateFirewall.md), [AssociateAvailabilityZones](API_AssociateAvailabilityZones.md), and [DisassociateAvailabilityZones](API_DisassociateAvailabilityZones.md).

To retrieve the current Availability Zone mappings for a firewall, use [DescribeFirewall](API_DescribeFirewall.md).

## Contents
<a name="API_AvailabilityZoneMapping_Contents"></a>

 ** AvailabilityZone **   <a name="networkfirewall-Type-AvailabilityZoneMapping-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall endpoint is located. For example, `us-east-2a`. The Availability Zone must be in the same Region as the transit gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `\S+`   
Required: Yes

## See Also
<a name="API_AvailabilityZoneMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AvailabilityZoneMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AvailabilityZoneMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AvailabilityZoneMapping) 