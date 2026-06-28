---
id: "@specs/aws/network-firewall/docs/API_Address"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Address"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Address

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Address
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Address
<a name="API_Address"></a>

A single IP address specification. This is used in the [MatchAttributes](API_MatchAttributes.md) source and destination specifications.

## Contents
<a name="API_Address_Contents"></a>

 ** AddressDefinition **   <a name="networkfirewall-Type-Address-AddressDefinition"></a>
Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.   
Examples:   
+ To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32`.
+ To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24`.
+ To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128`.
+ To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64`.
For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^([a-fA-F\d:\.]+($|/\d{1,3}))$`   
Required: Yes

## See Also
<a name="API_Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Address) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Address) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Address) 