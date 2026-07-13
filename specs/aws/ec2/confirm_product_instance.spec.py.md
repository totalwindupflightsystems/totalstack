---
id: "@specs/aws/ec2/confirm_product_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ConfirmProductInstance"
---

# ConfirmProductInstance

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/confirm_product_instance
> **spec:implements:** @kind:operation ConfirmProductInstance
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ConfirmProductInstance.spec.md

Determines whether a product code is associated with an instance. This action can only be used by the owner of the product code. It is useful when a product code owner must verify whether another user's instance is eligible for support.

## Input Shape: ConfirmProductInstanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| ProductCode | str | ✓ | The product code. This must be a product code that you own. |

## Output Shape: ConfirmProductInstanceResult

- **OwnerId** (str): The Amazon Web Services account ID of the instance owner. This is only present if the product code is attached to the in
- **Return** (bool): The return value of the request. Returns true if the specified product code is owned by the requester and associated wit

## Implementation

```speclang
def confirm_product_instance(store, request: dict) -> dict:
    """Determines whether a product code is associated with an instance. This action can only be used by the owner of the product code. It is useful when a product code owner must verify whether another user"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    product_code = request.get("ProductCode", "").strip() if isinstance(request.get("ProductCode"), str) else request.get("ProductCode")
    if not product_code:
        raise ValidationException("ProductCode is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ConfirmProductInstance", request)
```
