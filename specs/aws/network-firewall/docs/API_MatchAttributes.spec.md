---
id: "@specs/aws/network-firewall/docs/API_MatchAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MatchAttributes"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# MatchAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_MatchAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MatchAttributes
<a name="API_MatchAttributes"></a>

Criteria for Network Firewall to use to inspect an individual packet in stateless rule inspection. Each match attributes set can include one or more items such as IP address, CIDR range, port number, protocol, and TCP flags. 

## Contents
<a name="API_MatchAttributes_Contents"></a>

 ** DestinationPorts **   <a name="networkfirewall-Type-MatchAttributes-DestinationPorts"></a>
The destination port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
This setting is only used for protocols 6 (TCP) and 17 (UDP).   
Type: Array of [PortRange](API_PortRange.md) objects  
Required: No

 ** Destinations **   <a name="networkfirewall-Type-MatchAttributes-Destinations"></a>
The destination IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any destination address.   
Type: Array of [Address](API_Address.md) objects  
Required: No

 ** Protocols **   <a name="networkfirewall-Type-MatchAttributes-Protocols"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.  
Type: Array of integers  
Valid Range: Minimum value of 0. Maximum value of 255.  
Required: No

 ** SourcePorts **   <a name="networkfirewall-Type-MatchAttributes-SourcePorts"></a>
The source port to inspect for. You can specify an individual port, for example `1994` and you can specify a port range, for example `1990:1994`. To match with any port, specify `ANY`.  
 If not specified, this matches with any source port.  
This setting is only used for protocols 6 (TCP) and 17 (UDP).  
Type: Array of [PortRange](API_PortRange.md) objects  
Required: No

 ** Sources **   <a name="networkfirewall-Type-MatchAttributes-Sources"></a>
The source IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any source address.   
Type: Array of [Address](API_Address.md) objects  
Required: No

 ** TCPFlags **   <a name="networkfirewall-Type-MatchAttributes-TCPFlags"></a>
The TCP flags and masks to inspect for. If not specified, this matches with any settings. This setting is only used for protocol 6 (TCP).  
Type: Array of [TCPFlagField](API_TCPFlagField.md) objects  
Required: No

## See Also
<a name="API_MatchAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/MatchAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/MatchAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/MatchAttributes) 