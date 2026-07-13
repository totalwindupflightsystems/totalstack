---
id: "@specs/aws/sts/get_access_key_info"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_GetAccessKeyInfo"
---

# GetAccessKeyInfo

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/get_access_key_info
> **spec:implements:** @kind:operation GetAccessKeyInfo
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_GetAccessKeyInfo.spec.md

Returns the account identifier for the specified access key ID. Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE ) and a secret access key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY ). For more information about access keys, see Managing Access Keys for IAM Users in the IAM User Guide . When you pass an access key ID to this operation, it returns the ID of the Amazon Web Services account to which the keys belong. Access key IDs beginning with AKIA are long-term credentials for an IAM user or the Amazon Web Services account root user. Access key IDs beginning with ASIA are temporary credentials that are created using STS operations. If the account in the response belongs to you, you can sign in as the root user and review your root user access keys. Then, you can pull a credentials report to learn which IAM user owns the keys. To learn who requested the temporary credentials for an ASIA access key, view the STS events in your CloudTrail logs in the IAM User Guide . This operation does not indicate the state of the access key. The key might be active, inactive, or deleted. Active keys might not have permissions to perform an operation. Providing a deleted access key might return an error that the key doesn't exist.

## Input Shape: GetAccessKeyInfoRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccessKeyId | Any  # complex shape | ✓ | The identifier of an access key. This parameter allows (through its regex pattern) a string of characters that can consi |

## Output Shape: GetAccessKeyInfoResponse

- **Account** (Any  # complex shape): The number used to identify the Amazon Web Services account.

## Implementation

```speclang
def get_access_key_info(store, request: dict) -> dict:
    """Returns the account identifier for the specified access key ID. Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE ) and a secret access key (for example, wJalrXUtnF"""
    access_key_id = request.get("AccessKeyId", "").strip() if isinstance(request.get("AccessKeyId"), str) else request.get("AccessKeyId")
    if not access_key_id:
        raise ValidationException("AccessKeyId is required")

    resource = store.access_key_infos(access_key_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource access_key_id not found")
    return {"AccessKeyId": access_key_id, **resource}
```
