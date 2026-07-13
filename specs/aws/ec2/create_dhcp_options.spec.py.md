---
id: "@specs/aws/ec2/create_dhcp_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateDhcpOptions"
---

# CreateDhcpOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_dhcp_options
> **spec:implements:** @kind:operation CreateDhcpOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateDhcpOptions.spec.md

Creates a custom set of DHCP options. After you create a DHCP option set, you associate it with a VPC. After you associate a DHCP option set with a VPC, all existing and newly launched instances in the VPC use this set of DHCP options. The following are the individual DHCP options you can specify. For more information, see DHCP option sets in the Amazon VPC User Guide . domain-name - If you're using AmazonProvidedDNS in us-east-1 , specify ec2.internal . If you're using AmazonProvidedDNS in any other Region, specify region.compute.internal . Otherwise, specify a custom domain name. This value is used to complete unqualified DNS hostnames. Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP option set is associated with a VPC that has instances running operating systems that treat the value as a single domain, specify only one domain name. domain-name-servers - The IP addresses of up to four DNS servers, or AmazonProvidedDNS. To specify multiple domain name servers in a single parameter, separate the IP addresses using commas. To have your instances receive custom DNS hostnames as specified in domain-name , you must specify a custom DNS server. ntp-servers - The IP addresses of up to eight Network Time Protocol (NTP) servers (four IPv4 addresses and four IPv6 addresses). netbios-name-servers - The IP addresses of up to four NetBIOS name servers. netbios-node-type - The NetBIOS node type (1, 2, 4, or 8). We recommend that you specify 2. Broadcast and multicast are not supported. For more information about NetBIOS node types, see RFC 2132 . ipv6-address-preferred-lease-time - A value (in seconds, minutes, hours, or years) for how frequently a running instance with an IPv6 assigned to it goes through DHCPv6 lease renewal. Acceptable values are between 140 and 2147483647 seconds (approximately 68 years). If no value is entered, the default lease time is 140 seconds. If you use long-term addressing for EC2 instances, you can increase the lease time and avoid frequent lease renewal requests. Lease renewal typically occurs when half of the lease time has elapsed.

## Input Shape: CreateDhcpOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DhcpConfigurations | list[Any  # complex shape] | ✓ | A DHCP configuration option. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the DHCP option. |

## Output Shape: CreateDhcpOptionsResult

- **DhcpOptions** (Any  # complex shape): A set of DHCP options.

## Implementation

```speclang
def create_dhcp_options(store, request: dict) -> dict:
    """Creates a custom set of DHCP options. After you create a DHCP option set, you associate it with a VPC. After you associate a DHCP option set with a VPC, all existing and newly launched instances in th"""
    dhcp_configurations = request.get("DhcpConfigurations", "").strip() if isinstance(request.get("DhcpConfigurations"), str) else request.get("DhcpConfigurations")
    if not dhcp_configurations:
        raise ValidationException("DhcpConfigurations is required")

    if store.dhcp_optionss(dhcp_configurations):
        raise ResourceInUseException(f"Resource dhcp_configurations already exists")

    record = {
        "DhcpConfigurations": dhcp_configurations,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.dhcp_optionss(dhcp_configurations, record)

    return {
        "DhcpOptions": record.get("DhcpOptions", {}),
    }
```
