---
id: "@specs/aws/ec2/modify_subnet_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifySubnetAttribute"
---

# ModifySubnetAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_subnet_attribute
> **spec:implements:** @kind:operation ModifySubnetAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifySubnetAttribute.spec.md

Modifies a subnet attribute. You can only modify one attribute at a time. Use this action to modify subnets on Amazon Web Services Outposts. To modify a subnet on an Outpost rack, set both MapCustomerOwnedIpOnLaunch and CustomerOwnedIpv4Pool . These two parameters act as a single attribute. To modify a subnet on an Outpost server, set either EnableLniAtDeviceIndex or DisableLniAtDeviceIndex . For more information about Amazon Web Services Outposts, see the following: Outpost servers Outpost racks

## Input Shape: ModifySubnetAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssignIpv6AddressOnCreation | Any  # complex shape |  | Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Thi |
| CustomerOwnedIpv4Pool | Any  # complex shape |  | The customer-owned IPv4 address pool associated with the subnet. You must set this value when you specify true for MapCu |
| DisableLniAtDeviceIndex | Any  # complex shape |  | Specify true to indicate that local network interfaces at the current position should be disabled. |
| EnableDns64 | Any  # complex shape |  | Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addre |
| EnableLniAtDeviceIndex | int |  | Indicates the device position for local network interfaces in this subnet. For example, 1 indicates local network interf |
| EnableResourceNameDnsAAAARecordOnLaunch | Any  # complex shape |  | Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. |
| EnableResourceNameDnsARecordOnLaunch | Any  # complex shape |  | Indicates whether to respond to DNS queries for instance hostnames with DNS A records. |
| MapCustomerOwnedIpOnLaunch | Any  # complex shape |  | Specify true to indicate that network interfaces attached to instances created in the specified subnet should be assigne |
| MapPublicIpOnLaunch | Any  # complex shape |  | Specify true to indicate that network interfaces attached to instances created in the specified subnet should be assigne |
| PrivateDnsHostnameTypeOnLaunch | Any  # complex shape |  | The type of hostname to assign to instances in the subnet at launch. For IPv4-only and dual-stack (IPv4 and IPv6) subnet |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet. |

## Implementation

```speclang
def modify_subnet_attribute(store, request: dict) -> dict:
    """Modifies a subnet attribute. You can only modify one attribute at a time. Use this action to modify subnets on Amazon Web Services Outposts. To modify a subnet on an Outpost rack, set both MapCustomer"""
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    resource = store.subnet_attributes(subnet_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource subnet_id not found")

    # Update mutable fields
    if "AssignIpv6AddressOnCreation" in request:
        resource["AssignIpv6AddressOnCreation"] = assign_ipv6_address_on_creation
    if "MapPublicIpOnLaunch" in request:
        resource["MapPublicIpOnLaunch"] = map_public_ip_on_launch
    if "MapCustomerOwnedIpOnLaunch" in request:
        resource["MapCustomerOwnedIpOnLaunch"] = map_customer_owned_ip_on_launch
    if "CustomerOwnedIpv4Pool" in request:
        resource["CustomerOwnedIpv4Pool"] = customer_owned_ipv4_pool
    if "EnableDns64" in request:
        resource["EnableDns64"] = enable_dns64
    if "PrivateDnsHostnameTypeOnLaunch" in request:
        resource["PrivateDnsHostnameTypeOnLaunch"] = private_dns_hostname_type_on_launch
    if "EnableResourceNameDnsARecordOnLaunch" in request:
        resource["EnableResourceNameDnsARecordOnLaunch"] = enable_resource_name_dns_a_record_on_launch
    if "EnableResourceNameDnsAAAARecordOnLaunch" in request:
        resource["EnableResourceNameDnsAAAARecordOnLaunch"] = enable_resource_name_dns_aaaa_record_on_launch
    if "EnableLniAtDeviceIndex" in request:
        resource["EnableLniAtDeviceIndex"] = enable_lni_at_device_index
    if "DisableLniAtDeviceIndex" in request:
        resource["DisableLniAtDeviceIndex"] = disable_lni_at_device_index

    store.subnet_attributes(subnet_id, resource)
    return resource
```
