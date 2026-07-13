---
id: "@specs/aws/ec2/modify_network_interface_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyNetworkInterfaceAttribute"
---

# ModifyNetworkInterfaceAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_network_interface_attribute
> **spec:implements:** @kind:operation ModifyNetworkInterfaceAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyNetworkInterfaceAttribute.spec.md

Modifies the specified network interface attribute. You can specify only one attribute at a time. You can use this action to attach and detach security groups from an existing EC2 instance.

## Input Shape: ModifyNetworkInterfaceAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociatePublicIpAddress | bool |  | Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network int |
| AssociatedSubnetIds | list[Any  # complex shape] |  | A list of subnet IDs to associate with the network interface. |
| Attachment | Any  # complex shape |  | Information about the interface attachment. If modifying the delete on termination attribute, you must specify the ID of |
| ConnectionTrackingSpecification | Any  # complex shape |  | A connection tracking specification. |
| Description | Any  # complex shape |  | A description for the network interface. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EnaSrdSpecification | Any  # complex shape |  | Updates the ENA Express configuration for the network interface that’s attached to the instance. |
| EnablePrimaryIpv6 | bool |  | If you’re modifying a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv |
| Groups | list[Any  # complex shape] |  | Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You m |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |
| SourceDestCheck | Any  # complex shape |  | Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of a |

## Implementation

```speclang
def modify_network_interface_attribute(store, request: dict) -> dict:
    """Modifies the specified network interface attribute. You can specify only one attribute at a time. You can use this action to attach and detach security groups from an existing EC2 instance."""
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    resource = store.network_interface_attributes(network_interface_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource network_interface_id not found")

    # Update mutable fields
    if "EnaSrdSpecification" in request:
        resource["EnaSrdSpecification"] = ena_srd_specification
    if "EnablePrimaryIpv6" in request:
        resource["EnablePrimaryIpv6"] = enable_primary_ipv6
    if "ConnectionTrackingSpecification" in request:
        resource["ConnectionTrackingSpecification"] = connection_tracking_specification
    if "AssociatePublicIpAddress" in request:
        resource["AssociatePublicIpAddress"] = associate_public_ip_address
    if "AssociatedSubnetIds" in request:
        resource["AssociatedSubnetIds"] = associated_subnet_ids
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Description" in request:
        resource["Description"] = description
    if "SourceDestCheck" in request:
        resource["SourceDestCheck"] = source_dest_check
    if "Groups" in request:
        resource["Groups"] = groups
    if "Attachment" in request:
        resource["Attachment"] = attachment

    store.network_interface_attributes(network_interface_id, resource)
    return resource
```
