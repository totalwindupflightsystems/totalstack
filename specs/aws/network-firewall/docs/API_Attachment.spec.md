---
id: "@specs/aws/network-firewall/docs/API_Attachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Attachment"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Attachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Attachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Attachment
<a name="API_Attachment"></a>

The definition and status of the firewall endpoint for a single subnet. In each configured subnet, Network Firewall instantiates a firewall endpoint to handle network traffic. 

This data type is used for any firewall endpoint type: 
+ For `Firewall.SubnetMappings`, this `Attachment` is part of the `FirewallStatus` sync states information. You define firewall subnets using `CreateFirewall` and `AssociateSubnets`. 
+ For `VpcEndpointAssociation`, this `Attachment` is part of the `VpcEndpointAssociationStatus` sync states information. You define these subnets using `CreateVpcEndpointAssociation`. 

## Contents
<a name="API_Attachment_Contents"></a>

 ** EndpointId **   <a name="networkfirewall-Type-Attachment-EndpointId"></a>
The identifier of the firewall endpoint that Network Firewall has instantiated in the subnet. You use this to identify the firewall endpoint in the VPC route tables, when you redirect the VPC traffic through the endpoint.   
Type: String  
Required: No

 ** Status **   <a name="networkfirewall-Type-Attachment-Status"></a>
The current status of the firewall endpoint instantiation in the subnet.   
When this value is `READY`, the endpoint is available to handle network traffic. Otherwise, this value reflects its state, for example `CREATING` or `DELETING`.  
Type: String  
Valid Values: `CREATING | DELETING | FAILED | ERROR | SCALING | READY`   
Required: No

 ** StatusMessage **   <a name="networkfirewall-Type-Attachment-StatusMessage"></a>
If Network Firewall fails to create or delete the firewall endpoint in the subnet, it populates this with the reason for the error or failure and how to resolve it. A `FAILED` status indicates a non-recoverable state, and a `ERROR` status indicates an issue that you can fix. Depending on the error, it can take as many as 15 minutes to populate this field. For more information about the causes for failiure or errors and solutions available for this field, see [Troubleshooting firewall endpoint failures](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-troubleshooting-endpoint-failures.html) in the *Network Firewall Developer Guide*.  
Type: String  
Required: No

 ** SubnetId **   <a name="networkfirewall-Type-Attachment-SubnetId"></a>
The unique identifier of the subnet that you've specified to be used for a firewall endpoint.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^subnet-[0-9a-f]+$`   
Required: No

## See Also
<a name="API_Attachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Attachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Attachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Attachment) 