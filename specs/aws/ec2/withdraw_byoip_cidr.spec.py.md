---
id: "@specs/aws/ec2/withdraw_byoip_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_WithdrawByoipCidr"
---

# WithdrawByoipCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/withdraw_byoip_cidr
> **spec:implements:** @kind:operation WithdrawByoipCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_WithdrawByoipCidr.spec.md

Stops advertising an address range that is provisioned as an address pool. You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time. It can take a few minutes before traffic to the specified addresses stops routing to Amazon Web Services because of BGP propagation delays.

## Input Shape: WithdrawByoipCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The address range, in CIDR notation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: WithdrawByoipCidrResult

- **ByoipCidr** (Any  # complex shape): Information about the address pool.

## Implementation

```speclang
def withdraw_byoip_cidr(store, request: dict) -> dict:
    """Stops advertising an address range that is provisioned as an address pool. You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time. It can """
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("WithdrawByoipCidr", request)
```
