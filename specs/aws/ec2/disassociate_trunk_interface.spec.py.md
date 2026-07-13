---
id: "@specs/aws/ec2/disassociate_trunk_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateTrunkInterface"
---

# DisassociateTrunkInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_trunk_interface
> **spec:implements:** @kind:operation DisassociateTrunkInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateTrunkInterface.spec.md

Removes an association between a branch network interface with a trunk network interface.

## Input Shape: DisassociateTrunkInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape | ✓ | The ID of the association |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisassociateTrunkInterfaceResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E
- **Return** (bool): Is true if the request succeeds and an error otherwise.

## Implementation

```speclang
def disassociate_trunk_interface(store, request: dict) -> dict:
    """Removes an association between a branch network interface with a trunk network interface."""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateTrunkInterface", request)
```
