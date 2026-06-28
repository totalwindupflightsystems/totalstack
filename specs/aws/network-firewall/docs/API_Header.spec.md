---
id: "@specs/aws/network-firewall/docs/API_Header"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Header"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# Header

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_Header
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Header
<a name="API_Header"></a>

The basic rule criteria for AWS Network Firewall to use to inspect packet headers in stateful traffic flow inspection. Traffic flows that match the criteria are a match for the corresponding [StatefulRule](API_StatefulRule.md). 

## Contents
<a name="API_Header_Contents"></a>

 ** Destination **   <a name="networkfirewall-Type-Header-Destination"></a>
The destination IP address or address range to inspect for, in CIDR notation. To match with any address, specify `ANY`.   
Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.   
Examples:   
+ To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32`.
+ To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24`.
+ To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128`.
+ To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64`.
For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: Yes

 ** DestinationPort **   <a name="networkfirewall-Type-Header-DestinationPort"></a>
The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: Yes

 ** Direction **   <a name="networkfirewall-Type-Header-Direction"></a>
The direction of traffic flow to inspect. If set to `ANY`, the inspection matches bidirectional traffic, both from the source to the destination and from the destination to the source. If set to `FORWARD`, the inspection only matches traffic going from the source to the destination.   
Type: String  
Valid Values: `FORWARD | ANY`   
Required: Yes

 ** Protocol **   <a name="networkfirewall-Type-Header-Protocol"></a>
The protocol to inspect for. To specify all, you can use `IP`, because all traffic on AWS and on the internet is IP.  
Type: String  
Valid Values: `IP | TCP | UDP | ICMP | HTTP | FTP | TLS | SMB | DNS | DCERPC | SSH | SMTP | IMAP | MSN | KRB5 | IKEV2 | TFTP | NTP | DHCP | HTTP2 | QUIC`   
Required: Yes

 ** Source **   <a name="networkfirewall-Type-Header-Source"></a>
The source IP address or address range to inspect for, in CIDR notation. To match with any address, specify `ANY`.   
Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.   
Examples:   
+ To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32`.
+ To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24`.
+ To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128`.
+ To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64`.
For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: Yes

 ** SourcePort **   <a name="networkfirewall-Type-Header-SourcePort"></a>
The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^.*$`   
Required: Yes

## See Also
<a name="API_Header_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Header) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Header) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Header) 