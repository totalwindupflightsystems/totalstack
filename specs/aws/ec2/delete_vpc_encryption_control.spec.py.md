---
id: "@specs/aws/ec2/delete_vpc_encryption_control"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpcEncryptionControl"
---

# DeleteVpcEncryptionControl

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpc_encryption_control
> **spec:implements:** @kind:operation DeleteVpcEncryptionControl
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpcEncryptionControl.spec.md

Deletes a VPC Encryption Control configuration. This removes the encryption policy enforcement from the specified VPC. For more information, see Enforce VPC encryption in transit in the Amazon VPC User Guide .

## Input Shape: DeleteVpcEncryptionControlRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcEncryptionControlId | Any  # complex shape | ✓ | The ID of the VPC Encryption Control resource to delete. |

## Output Shape: DeleteVpcEncryptionControlResult

- **VpcEncryptionControl** (Any  # complex shape): Information about the deleted VPC Encryption Control configuration.

## Implementation

```speclang
def delete_vpc_encryption_control(store, request: dict) -> dict:
    """Deletes a VPC Encryption Control configuration. This removes the encryption policy enforcement from the specified VPC. For more information, see Enforce VPC encryption in transit in the Amazon VPC Use"""
    vpc_encryption_control_id = request.get("VpcEncryptionControlId", "").strip() if isinstance(request.get("VpcEncryptionControlId"), str) else request.get("VpcEncryptionControlId")

    if not store.vpc_encryption_controls(vpc_encryption_control_id):
        raise ResourceNotFoundException(f"Resource vpc_encryption_control_id not found")
    store.delete_vpc_encryption_controls(vpc_encryption_control_id)
    return {}
```
