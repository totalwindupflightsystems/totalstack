---
id: "@specs/aws/ec2/associate_dhcp_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateDhcpOptions"
---

# AssociateDhcpOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_dhcp_options
> **spec:implements:** @kind:operation AssociateDhcpOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateDhcpOptions.spec.md

Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC. After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don't need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance. For more information, see DHCP option sets in the Amazon VPC User Guide .

## Input Shape: AssociateDhcpOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DhcpOptionsId | Any  # complex shape | ✓ | The ID of the DHCP options set, or default to associate no DHCP options with the VPC. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Implementation

```speclang
def associate_dhcp_options(store, request: dict) -> dict:
    """Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC. After you associate the options with the VPC, any existing instanc"""
    dhcp_options_id = request.get("DhcpOptionsId", "").strip() if isinstance(request.get("DhcpOptionsId"), str) else request.get("DhcpOptionsId")
    if not dhcp_options_id:
        raise ValidationException("DhcpOptionsId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateDhcpOptions", request)
```
