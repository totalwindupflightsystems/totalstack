---
id: "@specs/aws/ec2/create_coip_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCoipCidr"
---

# CreateCoipCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_coip_cidr
> **spec:implements:** @kind:operation CreateCoipCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCoipCidr.spec.md

Creates a range of customer-owned IP addresses.

## Input Shape: CreateCoipCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | A customer-owned IP address range to create. |
| CoipPoolId | Any  # complex shape | ✓ | The ID of the address pool. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: CreateCoipCidrResult

- **CoipCidr** (Any  # complex shape): Information about a range of customer-owned IP addresses.

## Implementation

```speclang
def create_coip_cidr(store, request: dict) -> dict:
    """Creates a range of customer-owned IP addresses."""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")
    coip_pool_id = request.get("CoipPoolId", "").strip() if isinstance(request.get("CoipPoolId"), str) else request.get("CoipPoolId")
    if not coip_pool_id:
        raise ValidationException("CoipPoolId is required")

    if store.coip_cidrs(coip_pool_id):
        raise ResourceInUseException(f"Resource coip_pool_id already exists")

    record = {
        "Cidr": cidr,
        "CoipPoolId": coip_pool_id,
        "DryRun": dry_run,
    }

    store.coip_cidrs(coip_pool_id, record)

    return {
        "CoipCidr": record.get("CoipCidr", {}),
    }
```
