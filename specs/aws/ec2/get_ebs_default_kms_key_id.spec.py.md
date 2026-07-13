---
id: "@specs/aws/ec2/get_ebs_default_kms_key_id"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetEbsDefaultKmsKeyId"
---

# GetEbsDefaultKmsKeyId

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ebs_default_kms_key_id
> **spec:implements:** @kind:operation GetEbsDefaultKmsKeyId
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetEbsDefaultKmsKeyId.spec.md

Describes the default KMS key for EBS encryption by default for your account in this Region. For more information, see Amazon EBS encryption in the Amazon EBS User Guide .

## Input Shape: GetEbsDefaultKmsKeyIdRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetEbsDefaultKmsKeyIdResult

- **KmsKeyId** (str): The Amazon Resource Name (ARN) of the default KMS key for encryption by default.

## Implementation

```speclang
def get_ebs_default_kms_key_id(store, request: dict) -> dict:
    """Describes the default KMS key for EBS encryption by default for your account in this Region. For more information, see Amazon EBS encryption in the Amazon EBS User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
