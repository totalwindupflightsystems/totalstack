---
id: "@specs/aws/ec2/get_default_credit_specification"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetDefaultCreditSpecification"
---

# GetDefaultCreditSpecification

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_default_credit_specification
> **spec:implements:** @kind:operation GetDefaultCreditSpecification
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetDefaultCreditSpecification.spec.md

Describes the default credit option for CPU usage of a burstable performance instance family. For more information, see Burstable performance instances in the Amazon EC2 User Guide .

## Input Shape: GetDefaultCreditSpecificationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceFamily | Any  # complex shape | ✓ | The instance family. |

## Output Shape: GetDefaultCreditSpecificationResult

- **InstanceFamilyCreditSpecification** (Any  # complex shape): The default credit option for CPU usage of the instance family.

## Implementation

```speclang
def get_default_credit_specification(store, request: dict) -> dict:
    """Describes the default credit option for CPU usage of a burstable performance instance family. For more information, see Burstable performance instances in the Amazon EC2 User Guide ."""
    instance_family = request.get("InstanceFamily", "").strip() if isinstance(request.get("InstanceFamily"), str) else request.get("InstanceFamily")
    if not instance_family:
        raise ValidationException("InstanceFamily is required")

    resource = store.default_credit_specifications(instance_family)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_family not found")
    return {"InstanceFamily": instance_family, **resource}
```
