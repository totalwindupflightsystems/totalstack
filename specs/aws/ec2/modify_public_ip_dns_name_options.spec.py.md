---
id: "@specs/aws/ec2/modify_public_ip_dns_name_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyPublicIpDnsNameOptions"
---

# ModifyPublicIpDnsNameOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_public_ip_dns_name_options
> **spec:implements:** @kind:operation ModifyPublicIpDnsNameOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyPublicIpDnsNameOptions.spec.md

Modify public hostname options for a network interface. For more information, see EC2 instance hostnames, DNS names, and domains in the Amazon EC2 User Guide .

## Input Shape: ModifyPublicIpDnsNameOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| HostnameType | Any  # complex shape | ✓ | The public hostname type. For more information, see EC2 instance hostnames, DNS names, and domains in the Amazon EC2 Use |
| NetworkInterfaceId | Any  # complex shape | ✓ | A network interface ID. |

## Output Shape: ModifyPublicIpDnsNameOptionsResult

- **Successful** (bool): Whether or not the request was successful.

## Implementation

```speclang
def modify_public_ip_dns_name_options(store, request: dict) -> dict:
    """Modify public hostname options for a network interface. For more information, see EC2 instance hostnames, DNS names, and domains in the Amazon EC2 User Guide ."""
    hostname_type = request.get("HostnameType", "").strip() if isinstance(request.get("HostnameType"), str) else request.get("HostnameType")
    if not hostname_type:
        raise ValidationException("HostnameType is required")
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    resource = store.public_ip_dns_name_optionss(network_interface_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource network_interface_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.public_ip_dns_name_optionss(network_interface_id, resource)
    return resource
```
