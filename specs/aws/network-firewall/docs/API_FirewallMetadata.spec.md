---
id: "@specs/aws/network-firewall/docs/API_FirewallMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FirewallMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FirewallMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FirewallMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FirewallMetadata
<a name="API_FirewallMetadata"></a>

High-level information about a firewall, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a firewall.

## Contents
<a name="API_FirewallMetadata_Contents"></a>

 ** FirewallArn **   <a name="networkfirewall-Type-FirewallMetadata-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** FirewallName **   <a name="networkfirewall-Type-FirewallMetadata-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** TransitGatewayAttachmentId **   <a name="networkfirewall-Type-FirewallMetadata-TransitGatewayAttachmentId"></a>
The unique identifier of the transit gateway attachment associated with this firewall. This field is only present for transit gateway-attached firewalls.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^tgw-attach-[0-9a-z]+$`   
Required: No

## See Also
<a name="API_FirewallMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallMetadata) 