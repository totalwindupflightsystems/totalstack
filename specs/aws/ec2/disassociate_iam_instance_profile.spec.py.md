---
id: "@specs/aws/ec2/disassociate_iam_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateIamInstanceProfile"
---

# DisassociateIamInstanceProfile

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_iam_instance_profile
> **spec:implements:** @kind:operation DisassociateIamInstanceProfile
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateIamInstanceProfile.spec.md

Disassociates an IAM instance profile from a running or stopped instance. Use DescribeIamInstanceProfileAssociations to get the association ID.

## Input Shape: DisassociateIamInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape | ✓ | The ID of the IAM instance profile association. |

## Output Shape: DisassociateIamInstanceProfileResult

- **IamInstanceProfileAssociation** (Any  # complex shape): Information about the IAM instance profile association.

## Implementation

```speclang
def disassociate_iam_instance_profile(store, request: dict) -> dict:
    """Disassociates an IAM instance profile from a running or stopped instance. Use DescribeIamInstanceProfileAssociations to get the association ID."""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateIamInstanceProfile", request)
```
