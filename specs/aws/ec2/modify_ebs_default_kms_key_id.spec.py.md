---
id: "@specs/aws/ec2/modify_ebs_default_kms_key_id"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyEbsDefaultKmsKeyId"
---

# ModifyEbsDefaultKmsKeyId

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ebs_default_kms_key_id
> **spec:implements:** @kind:operation ModifyEbsDefaultKmsKeyId
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyEbsDefaultKmsKeyId.spec.md

Changes the default KMS key for EBS encryption by default for your account in this Region. Amazon Web Services creates a unique Amazon Web Services managed KMS key in each Region for use with encryption by default. If you change the default KMS key to a symmetric customer managed KMS key, it is used instead of the Amazon Web Services managed KMS key. Amazon EBS does not support asymmetric KMS keys. If you delete or disable the customer managed KMS key that you specified for use with encryption by default, your instances will fail to launch. For more information, see Amazon EBS encryption in the Amazon EBS User Guide .

## Input Shape: ModifyEbsDefaultKmsKeyIdRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| KmsKeyId | str | ✓ | The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Ama |

## Output Shape: ModifyEbsDefaultKmsKeyIdResult

- **KmsKeyId** (str): The Amazon Resource Name (ARN) of the default KMS key for encryption by default.

## Implementation

```speclang
def modify_ebs_default_kms_key_id(store, request: dict) -> dict:
    """Changes the default KMS key for EBS encryption by default for your account in this Region. Amazon Web Services creates a unique Amazon Web Services managed KMS key in each Region for use with encrypti"""
    kms_key_id = request.get("KmsKeyId", "").strip() if isinstance(request.get("KmsKeyId"), str) else request.get("KmsKeyId")
    if not kms_key_id:
        raise ValidationException("KmsKeyId is required")

    resource = store.ebs_default_kms_key_ids(kms_key_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource kms_key_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.ebs_default_kms_key_ids(kms_key_id, resource)
    return resource
```
