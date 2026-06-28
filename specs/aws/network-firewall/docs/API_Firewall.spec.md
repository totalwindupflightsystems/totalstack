---
id: "@specs/aws/network-firewall/docs/API_Firewall"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Firewall"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Firewall

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Firewall
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Firewall
<a name="API_Firewall"></a>

A firewall defines the behavior of a firewall, the main VPC where the firewall is used, the Availability Zones where the firewall can be used, and one subnet to use for a firewall endpoint within each of the Availability Zones. The Availability Zones are defined implicitly in the subnet specifications.

In addition to the firewall endpoints that you define in this `Firewall` specification, you can create firewall endpoints in `VpcEndpointAssociation` resources for any VPC, in any Availability Zone where the firewall is already in use. 

The status of the firewall, for example whether it's ready to filter network traffic, is provided in the corresponding [FirewallStatus](API_FirewallStatus.md). You can retrieve both the firewall and firewall status by calling [DescribeFirewall](API_DescribeFirewall.md).

## Contents
<a name="API_Firewall_Contents"></a>

 ** FirewallId **   <a name="networkfirewall-Type-Firewall-FirewallId"></a>
The unique identifier for the firewall.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

 ** FirewallPolicyArn **   <a name="networkfirewall-Type-Firewall-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the firewall policy.  
The relationship of firewall to firewall policy is many to one. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** SubnetMappings **   <a name="networkfirewall-Type-Firewall-SubnetMappings"></a>
The primary public subnets that Network Firewall is using for the firewall. Network Firewall creates a firewall endpoint in each subnet. Create a subnet mapping for each Availability Zone where you want to use the firewall.  
These subnets are all defined for a single, primary VPC, and each must belong to a different Availability Zone. Each of these subnets establishes the availability of the firewall in its Availability Zone.   
In addition to these subnets, you can define other endpoints for the firewall in `VpcEndpointAssociation` resources. You can define these additional endpoints for any VPC, and for any of the Availability Zones where the firewall resource already has a subnet mapping. VPC endpoint associations give you the ability to protect multiple VPCs using a single firewall, and to define multiple firewall endpoints for a VPC in a single Availability Zone.   
Type: Array of [SubnetMapping](API_SubnetMapping.md) objects  
Required: Yes

 ** VpcId **   <a name="networkfirewall-Type-Firewall-VpcId"></a>
The unique identifier of the VPC where the firewall is in use.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^vpc-[0-9a-f]+$`   
Required: Yes

 ** AvailabilityZoneChangeProtection **   <a name="networkfirewall-Type-Firewall-AvailabilityZoneChangeProtection"></a>
A setting indicating whether the firewall is protected against changes to its Availability Zone configuration. When set to `TRUE`, you must first disable this protection before adding or removing Availability Zones.  
Type: Boolean  
Required: No

 ** AvailabilityZoneMappings **   <a name="networkfirewall-Type-Firewall-AvailabilityZoneMappings"></a>
The Availability Zones where the firewall endpoints are created for a transit gateway-attached firewall. Each mapping specifies an Availability Zone where the firewall processes traffic.  
Type: Array of [AvailabilityZoneMapping](API_AvailabilityZoneMapping.md) objects  
Required: No

 ** DeleteProtection **   <a name="networkfirewall-Type-Firewall-DeleteProtection"></a>
A flag indicating whether it is possible to delete the firewall. A setting of `TRUE` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to `TRUE`.  
Type: Boolean  
Required: No

 ** Description **   <a name="networkfirewall-Type-Firewall-Description"></a>
A description of the firewall.  
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** EnabledAnalysisTypes **   <a name="networkfirewall-Type-Firewall-EnabledAnalysisTypes"></a>
An optional setting indicating the specific traffic analysis types to enable on the firewall.   
Type: Array of strings  
Valid Values: `TLS_SNI | HTTP_HOST`   
Required: No

 ** EncryptionConfiguration **   <a name="networkfirewall-Type-Firewall-EncryptionConfiguration"></a>
A complex type that contains the AWS KMS encryption configuration settings for your firewall.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** FirewallArn **   <a name="networkfirewall-Type-Firewall-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** FirewallName **   <a name="networkfirewall-Type-Firewall-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** FirewallPolicyChangeProtection **   <a name="networkfirewall-Type-Firewall-FirewallPolicyChangeProtection"></a>
A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.  
Type: Boolean  
Required: No

 ** NumberOfAssociations **   <a name="networkfirewall-Type-Firewall-NumberOfAssociations"></a>
The number of `VpcEndpointAssociation` resources that use this firewall.   
Type: Integer  
Required: No

 ** SubnetChangeProtection **   <a name="networkfirewall-Type-Firewall-SubnetChangeProtection"></a>
A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.  
Type: Boolean  
Required: No

 ** Tags **   <a name="networkfirewall-Type-Firewall-Tags"></a>
  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** TransitGatewayId **   <a name="networkfirewall-Type-Firewall-TransitGatewayId"></a>
The unique identifier of the transit gateway associated with this firewall. This field is only present for transit gateway-attached firewalls.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^tgw-[0-9a-z]+$`   
Required: No

 ** TransitGatewayOwnerAccountId **   <a name="networkfirewall-Type-Firewall-TransitGatewayOwnerAccountId"></a>
The AWS account ID that owns the transit gateway. This may be different from the firewall owner's account ID when using a shared transit gateway.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^\d{12}$`   
Required: No

## See Also
<a name="API_Firewall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Firewall) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Firewall) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Firewall) 