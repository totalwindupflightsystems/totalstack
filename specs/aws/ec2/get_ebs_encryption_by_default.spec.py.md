---
id: "@specs/aws/ec2/get_ebs_encryption_by_default"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetEbsEncryptionByDefault"
---

# GetEbsEncryptionByDefault

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ebs_encryption_by_default
> **spec:implements:** @kind:operation GetEbsEncryptionByDefault
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetEbsEncryptionByDefault.spec.md

Describes whether EBS encryption by default is enabled for your account in the current Region. For more information, see Amazon EBS encryption in the Amazon EBS User Guide .

## Input Shape: GetEbsEncryptionByDefaultRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetEbsEncryptionByDefaultResult

- **EbsEncryptionByDefault** (bool): Indicates whether encryption by default is enabled.
- **SseType** (Any  # complex shape): Reserved for future use.

## Implementation

```speclang
def get_ebs_encryption_by_default(store, request: dict) -> dict:
    """Describes whether EBS encryption by default is enabled for your account in the current Region. For more information, see Amazon EBS encryption in the Amazon EBS User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
