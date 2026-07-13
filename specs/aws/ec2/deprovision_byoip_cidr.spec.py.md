---
id: "@specs/aws/ec2/deprovision_byoip_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeprovisionByoipCidr"
---

# DeprovisionByoipCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deprovision_byoip_cidr
> **spec:implements:** @kind:operation DeprovisionByoipCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeprovisionByoipCidr.spec.md

Releases the specified address range that you provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool. Before you can release an address range, you must stop advertising it and you must not have any IP addresses allocated from its address range.

## Input Shape: DeprovisionByoipCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the addr |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DeprovisionByoipCidrResult

- **ByoipCidr** (Any  # complex shape): Information about the address range.

## Implementation

```speclang
def deprovision_byoip_cidr(store, request: dict) -> dict:
    """Releases the specified address range that you provisioned for use with your Amazon Web Services resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool. Before"""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DeprovisionByoipCidr", request)
```
