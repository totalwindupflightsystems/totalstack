---
id: "@specs/aws/ec2/enable_ebs_encryption_by_default"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableEbsEncryptionByDefault"
---

# EnableEbsEncryptionByDefault

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_ebs_encryption_by_default
> **spec:implements:** @kind:operation EnableEbsEncryptionByDefault
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableEbsEncryptionByDefault.spec.md

Enables EBS encryption by default for your account in the current Region. After you enable encryption by default, the EBS volumes that you create are always encrypted, either using the default KMS key or the KMS key that you specified when you created each volume. For more information, see Amazon EBS encryption in the Amazon EBS User Guide . Enabling encryption by default has no effect on the encryption status of your existing volumes. After you enable encryption by default, you can no longer launch instances using instance types that do not support encryption. For more information, see Supported instance types .

## Input Shape: EnableEbsEncryptionByDefaultRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: EnableEbsEncryptionByDefaultResult

- **EbsEncryptionByDefault** (bool): The updated status of encryption by default.

## Implementation

```speclang
def enable_ebs_encryption_by_default(store, request: dict) -> dict:
    """Enables EBS encryption by default for your account in the current Region. After you enable encryption by default, the EBS volumes that you create are always encrypted, either using the default KMS key"""

```
