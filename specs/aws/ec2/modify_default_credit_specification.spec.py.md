---
id: "@specs/aws/ec2/modify_default_credit_specification"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyDefaultCreditSpecification"
---

# ModifyDefaultCreditSpecification

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_default_credit_specification
> **spec:implements:** @kind:operation ModifyDefaultCreditSpecification
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyDefaultCreditSpecification.spec.md

Modifies the default credit option for CPU usage of burstable performance instances. The default credit option is set at the account level per Amazon Web Services Region, and is specified per instance family. All new burstable performance instances in the account launch using the default credit option. ModifyDefaultCreditSpecification is an asynchronous operation, which works at an Amazon Web Services Region level and modifies the credit option for each Availability Zone. All zones in a Region are updated within five minutes. But if instances are launched during this operation, they might not get the new credit option until the zone is updated. To verify whether the update has occurred, you can call GetDefaultCreditSpecification and check DefaultCreditSpecification for updates. For more information, see Burstable performance instances in the Amazon EC2 User Guide .

## Input Shape: ModifyDefaultCreditSpecificationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CpuCredits | str | ✓ | The credit option for CPU usage of the instance family. Valid Values: standard | unlimited |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceFamily | Any  # complex shape | ✓ | The instance family. |

## Output Shape: ModifyDefaultCreditSpecificationResult

- **InstanceFamilyCreditSpecification** (Any  # complex shape): The default credit option for CPU usage of the instance family.

## Implementation

```speclang
def modify_default_credit_specification(store, request: dict) -> dict:
    """Modifies the default credit option for CPU usage of burstable performance instances. The default credit option is set at the account level per Amazon Web Services Region, and is specified per instance"""
    cpu_credits = request.get("CpuCredits", "").strip() if isinstance(request.get("CpuCredits"), str) else request.get("CpuCredits")
    if not cpu_credits:
        raise ValidationException("CpuCredits is required")
    instance_family = request.get("InstanceFamily", "").strip() if isinstance(request.get("InstanceFamily"), str) else request.get("InstanceFamily")
    if not instance_family:
        raise ValidationException("InstanceFamily is required")

    resource = store.default_credit_specifications(cpu_credits)
    if not resource:
        raise ResourceNotFoundException(f"Resource cpu_credits not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.default_credit_specifications(cpu_credits, resource)
    return resource
```
