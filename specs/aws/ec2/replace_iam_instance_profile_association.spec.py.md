---
id: "@specs/aws/ec2/replace_iam_instance_profile_association"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceIamInstanceProfileAssociation"
---

# ReplaceIamInstanceProfileAssociation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_iam_instance_profile_association
> **spec:implements:** @kind:operation ReplaceIamInstanceProfileAssociation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceIamInstanceProfileAssociation.spec.md

Replaces an IAM instance profile for the specified running instance. You can use this action to change the IAM instance profile that's associated with an instance without having to disassociate the existing IAM instance profile first. Use DescribeIamInstanceProfileAssociations to get the association ID.

## Input Shape: ReplaceIamInstanceProfileAssociationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape | ✓ | The ID of the existing IAM instance profile association. |
| IamInstanceProfile | Any  # complex shape | ✓ | The IAM instance profile. |

## Output Shape: ReplaceIamInstanceProfileAssociationResult

- **IamInstanceProfileAssociation** (Any  # complex shape): Information about the IAM instance profile association.

## Implementation

```speclang
def replace_iam_instance_profile_association(store, request: dict) -> dict:
    """Replaces an IAM instance profile for the specified running instance. You can use this action to change the IAM instance profile that's associated with an instance without having to disassociate the ex"""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")
    iam_instance_profile = request.get("IamInstanceProfile", "").strip() if isinstance(request.get("IamInstanceProfile"), str) else request.get("IamInstanceProfile")
    if not iam_instance_profile:
        raise ValidationException("IamInstanceProfile is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReplaceIamInstanceProfileAssociation", request)
```
