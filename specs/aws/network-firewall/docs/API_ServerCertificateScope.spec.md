---
id: "@specs/aws/network-firewall/docs/API_ServerCertificateScope"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServerCertificateScope"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ServerCertificateScope

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ServerCertificateScope
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServerCertificateScope
<a name="API_ServerCertificateScope"></a>

Settings that define the Secure Sockets Layer/Transport Layer Security (SSL/TLS) traffic that Network Firewall should decrypt for inspection by the stateful rule engine.

## Contents
<a name="API_ServerCertificateScope_Contents"></a>

 ** DestinationPorts **   <a name="networkfirewall-Type-ServerCertificateScope-DestinationPorts"></a>
The destination ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any destination port.  
You can specify individual ports, for example `1994`, and you can specify port ranges, such as `1990:1994`.  
Type: Array of [PortRange](API_PortRange.md) objects  
Required: No

 ** Destinations **   <a name="networkfirewall-Type-ServerCertificateScope-Destinations"></a>
The destination IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any destination address.  
Type: Array of [Address](API_Address.md) objects  
Required: No

 ** Protocols **   <a name="networkfirewall-Type-ServerCertificateScope-Protocols"></a>
The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.  
Network Firewall currently supports only TCP.  
Type: Array of integers  
Valid Range: Minimum value of 0. Maximum value of 255.  
Required: No

 ** SourcePorts **   <a name="networkfirewall-Type-ServerCertificateScope-SourcePorts"></a>
The source ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any source port.  
You can specify individual ports, for example `1994`, and you can specify port ranges, such as `1990:1994`.  
Type: Array of [PortRange](API_PortRange.md) objects  
Required: No

 ** Sources **   <a name="networkfirewall-Type-ServerCertificateScope-Sources"></a>
The source IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any source address.  
Type: Array of [Address](API_Address.md) objects  
Required: No

## See Also
<a name="API_ServerCertificateScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ServerCertificateScope) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ServerCertificateScope) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ServerCertificateScope) 