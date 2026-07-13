---
id: "@specs/aws/ec2/create_vpc_encryption_control"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpcEncryptionControl"
---

# CreateVpcEncryptionControl

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpc_encryption_control
> **spec:implements:** @kind:operation CreateVpcEncryptionControl
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpcEncryptionControl.spec.md

Creates a VPC Encryption Control configuration for a specified VPC. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements for standards like HIPAA, FedRAMP, and PCI DSS. For more information, see Enforce VPC encryption in transit in the Amazon VPC User Guide .

## Input Shape: CreateVpcEncryptionControlRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the VPC Encryption Control resource. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC for which to create the encryption control configuration. |

## Output Shape: CreateVpcEncryptionControlResult

- **VpcEncryptionControl** (Any  # complex shape): Information about the VPC Encryption Control configuration.

## Implementation

```speclang
def create_vpc_encryption_control(store, request: dict) -> dict:
    """Creates a VPC Encryption Control configuration for a specified VPC. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirem"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.vpc_encryption_controls(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "DryRun": dry_run,
        "VpcId": vpc_id,
        "TagSpecifications": tag_specifications,
    }

    store.vpc_encryption_controls(vpc_id, record)

    return {
        "VpcEncryptionControl": record.get("VpcEncryptionControl", {}),
    }
```
