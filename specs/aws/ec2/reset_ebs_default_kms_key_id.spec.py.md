---
id: "@specs/aws/ec2/reset_ebs_default_kms_key_id"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ResetEbsDefaultKmsKeyId"
---

# ResetEbsDefaultKmsKeyId

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reset_ebs_default_kms_key_id
> **spec:implements:** @kind:operation ResetEbsDefaultKmsKeyId
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ResetEbsDefaultKmsKeyId.spec.md

Resets the default KMS key for EBS encryption for your account in this Region to the Amazon Web Services managed KMS key for EBS. After resetting the default KMS key to the Amazon Web Services managed KMS key, you can continue to encrypt by a customer managed KMS key by specifying it when you create the volume. For more information, see Amazon EBS encryption in the Amazon EBS User Guide .

## Input Shape: ResetEbsDefaultKmsKeyIdRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: ResetEbsDefaultKmsKeyIdResult

- **KmsKeyId** (str): The Amazon Resource Name (ARN) of the default KMS key for EBS encryption by default.

## Implementation

```speclang
def reset_ebs_default_kms_key_id(store, request: dict) -> dict:
    """Resets the default KMS key for EBS encryption for your account in this Region to the Amazon Web Services managed KMS key for EBS. After resetting the default KMS key to the Amazon Web Services managed"""

```
