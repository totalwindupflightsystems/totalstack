---
id: "@specs/aws/ec2/modify_instance_credit_specification"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceCreditSpecification"
---

# ModifyInstanceCreditSpecification

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_credit_specification
> **spec:implements:** @kind:operation ModifyInstanceCreditSpecification
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceCreditSpecification.spec.md

Modifies the credit option for CPU usage on a running or stopped burstable performance instance. The credit options are standard and unlimited . For more information, see Burstable performance instances in the Amazon EC2 User Guide .

## Input Shape: ModifyInstanceCreditSpecificationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceCreditSpecifications | Any  # complex shape | ✓ | Information about the credit option for CPU usage. |

## Output Shape: ModifyInstanceCreditSpecificationResult

- **SuccessfulInstanceCreditSpecifications** (Any  # complex shape): Information about the instances whose credit option for CPU usage was successfully modified.
- **UnsuccessfulInstanceCreditSpecifications** (Any  # complex shape): Information about the instances whose credit option for CPU usage was not modified.

## Implementation

```speclang
def modify_instance_credit_specification(store, request: dict) -> dict:
    """Modifies the credit option for CPU usage on a running or stopped burstable performance instance. The credit options are standard and unlimited . For more information, see Burstable performance instanc"""
    instance_credit_specifications = request.get("InstanceCreditSpecifications", "").strip() if isinstance(request.get("InstanceCreditSpecifications"), str) else request.get("InstanceCreditSpecifications")
    if not instance_credit_specifications:
        raise ValidationException("InstanceCreditSpecifications is required")

    resource = store.instance_credit_specifications(instance_credit_specifications)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_credit_specifications not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ClientToken" in request:
        resource["ClientToken"] = client_token

    store.instance_credit_specifications(instance_credit_specifications, resource)
    return resource
```
