---
id: "@specs/aws/ec2/disable_ebs_encryption_by_default"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableEbsEncryptionByDefault"
---

# DisableEbsEncryptionByDefault

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_ebs_encryption_by_default
> **spec:implements:** @kind:operation DisableEbsEncryptionByDefault
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableEbsEncryptionByDefault.spec.md

Disables EBS encryption by default for your account in the current Region. After you disable encryption by default, you can still create encrypted volumes by enabling encryption when you create each volume. Disabling encryption by default does not change the encryption status of your existing volumes. For more information, see Amazon EBS encryption in the Amazon EBS User Guide .

## Input Shape: DisableEbsEncryptionByDefaultRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisableEbsEncryptionByDefaultResult

- **EbsEncryptionByDefault** (bool): The updated status of encryption by default.

## Implementation

```speclang
def disable_ebs_encryption_by_default(store, request: dict) -> dict:
    """Disables EBS encryption by default for your account in the current Region. After you disable encryption by default, you can still create encrypted volumes by enabling encryption when you create each v"""

```
