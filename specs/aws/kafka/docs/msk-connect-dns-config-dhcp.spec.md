---
id: "@specs/aws/kafka/docs/msk-connect-dns-config-dhcp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configure a VPC DHCP option"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Configure a VPC DHCP option

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-connect-dns-config-dhcp
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configure a VPC DHCP option set for your connector
<a name="msk-connect-dns-config-dhcp"></a>

Connectors automatically use the DNS servers defined in their VPC DHCP option set when the connector is created. Before you create a connector, make sure that you configure the VPC DHCP option set for your connector's DNS hostname resolution requirements.

Connectors that you created before the Private DNS hostname feature was available in MSK Connect continue to use the previous DNS resolution configuration with no modification required.

If you need only publicly resolvable DNS hostname resolution in your connector, for easier setup we recommend using the default VPC of your account when you create the connector. See [Amazon DNS Server](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#AmazonDNS) in the *Amazon VPC User Guide* for more information on the Amazon-provided DNS server or Amazon Route 53 Resolver.

If you need to resolve private DNS hostnames, make sure the VPC that is passed during connector creation has its DHCP options set correctly configured. For more information, see [Work with DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html) in the *Amazon VPC User Guide*.

When you configure a DHCP option set for private DNS hostname resolution, ensure that the connector can reach the custom DNS servers that you configure in the DHCP option set. Otherwise, your connector creation will fail.

After you customize the VPC DHCP option set, connectors subsequently created in that VPC use the DNS servers that you specified in the option set. If you change the option set after you create a connector, the connector adopts the settings in the new option set within a couple of minutes.