---
id: "@specs/aws/network-firewall/docs/API_VpcEndpointAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VpcEndpointAssociation"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# VpcEndpointAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_VpcEndpointAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VpcEndpointAssociation
<a name="API_VpcEndpointAssociation"></a>

A VPC endpoint association defines a single subnet to use for a firewall endpoint for a `Firewall`. You can define VPC endpoint associations only in the Availability Zones that already have a subnet mapping defined in the `Firewall` resource. 

**Note**  
You can retrieve the list of Availability Zones that are available for use by calling `DescribeFirewallMetadata`.

To manage firewall endpoints, first, in the `Firewall` specification, you specify a single VPC and one subnet for each of the Availability Zones where you want to use the firewall. Then you can define additional endpoints as VPC endpoint associations. 

You can use VPC endpoint associations to expand the protections of the firewall as follows: 
+  **Protect multiple VPCs with a single firewall** - You can use the firewall to protect other VPCs, either in your account or in accounts where the firewall is shared. You can only specify Availability Zones that already have a firewall endpoint defined in the `Firewall` subnet mappings.
+  **Define multiple firewall endpoints for a VPC in an Availability Zone** - You can create additional firewall endpoints for the VPC that you have defined in the firewall, in any Availability Zone that already has an endpoint defined in the `Firewall` subnet mappings. You can create multiple VPC endpoint associations for any other VPC where you use the firewall.

You can use AWS Resource Access Manager to share a `Firewall` that you own with other accounts, which gives them the ability to use the firewall to create VPC endpoint associations. For information about sharing a firewall, see `PutResourcePolicy` in this guide and see [Sharing Network Firewall resources](https://docs.aws.amazon.com/network-firewall/latest/developerguide/sharing.html) in the * AWS Network Firewall Developer Guide*.

The status of the VPC endpoint association, which indicates whether it's ready to filter network traffic, is provided in the corresponding [VpcEndpointAssociationStatus](API_VpcEndpointAssociationStatus.md). You can retrieve both the association and its status by calling [DescribeVpcEndpointAssociation](API_DescribeVpcEndpointAssociation.md).

## Contents
<a name="API_VpcEndpointAssociation_Contents"></a>

 ** FirewallArn **   <a name="networkfirewall-Type-VpcEndpointAssociation-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** SubnetMapping **   <a name="networkfirewall-Type-VpcEndpointAssociation-SubnetMapping"></a>
The ID for a subnet that's used in an association with a firewall. This is used in [CreateFirewall](API_CreateFirewall.md), [AssociateSubnets](API_AssociateSubnets.md), and [CreateVpcEndpointAssociation](API_CreateVpcEndpointAssociation.md). AWS Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnet's Availability Zone.  
Type: [SubnetMapping](API_SubnetMapping.md) object  
Required: Yes

 ** VpcEndpointAssociationArn **   <a name="networkfirewall-Type-VpcEndpointAssociation-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** VpcId **   <a name="networkfirewall-Type-VpcEndpointAssociation-VpcId"></a>
The unique identifier of the VPC for the endpoint association.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^vpc-[0-9a-f]+$`   
Required: Yes

 ** Description **   <a name="networkfirewall-Type-VpcEndpointAssociation-Description"></a>
A description of the VPC endpoint association.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** Tags **   <a name="networkfirewall-Type-VpcEndpointAssociation-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** VpcEndpointAssociationId **   <a name="networkfirewall-Type-VpcEndpointAssociation-VpcEndpointAssociationId"></a>
The unique identifier of the VPC endpoint association.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: No

## See Also
<a name="API_VpcEndpointAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/VpcEndpointAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/VpcEndpointAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/VpcEndpointAssociation) 