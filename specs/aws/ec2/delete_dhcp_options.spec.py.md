---
id: "@specs/aws/ec2/delete_dhcp_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteDhcpOptions"
---

# DeleteDhcpOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_dhcp_options
> **spec:implements:** @kind:operation DeleteDhcpOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteDhcpOptions.spec.md

Deletes the specified set of DHCP options. You must disassociate the set of DHCP options before you can delete it. You can disassociate the set of DHCP options by associating either a new set of options or the default set of options with the VPC.

## Input Shape: DeleteDhcpOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DhcpOptionsId | Any  # complex shape | ✓ | The ID of the DHCP options set. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Implementation

```speclang
def delete_dhcp_options(store, request: dict) -> dict:
    """Deletes the specified set of DHCP options. You must disassociate the set of DHCP options before you can delete it. You can disassociate the set of DHCP options by associating either a new set of optio"""
    dhcp_options_id = request.get("DhcpOptionsId", "").strip() if isinstance(request.get("DhcpOptionsId"), str) else request.get("DhcpOptionsId")

    if not store.dhcp_optionss(dhcp_options_id):
        raise ResourceNotFoundException(f"Resource dhcp_options_id not found")
    store.delete_dhcp_optionss(dhcp_options_id)
    return {}
```
