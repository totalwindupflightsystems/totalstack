---
id: "@specs/aws/ec2/associate_iam_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateIamInstanceProfile"
---

# AssociateIamInstanceProfile

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_iam_instance_profile
> **spec:implements:** @kind:operation AssociateIamInstanceProfile
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateIamInstanceProfile.spec.md

Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance.

## Input Shape: AssociateIamInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| IamInstanceProfile | Any  # complex shape | ✓ | The IAM instance profile. |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |

## Output Shape: AssociateIamInstanceProfileResult

- **IamInstanceProfileAssociation** (Any  # complex shape): Information about the IAM instance profile association.

## Implementation

```speclang
def associate_iam_instance_profile(store, request: dict) -> dict:
    """Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance."""
    iam_instance_profile = request.get("IamInstanceProfile", "").strip() if isinstance(request.get("IamInstanceProfile"), str) else request.get("IamInstanceProfile")
    if not iam_instance_profile:
        raise ValidationException("IamInstanceProfile is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateIamInstanceProfile", request)
```
