---
id: "@specs/aws/iam/get_access_key_last_used"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetAccessKeyLastUsed"
---

# GetAccessKeyLastUsed

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_access_key_last_used
> **spec:implements:** @kind:operation GetAccessKeyLastUsed
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetAccessKeyLastUsed.spec.md

Retrieves information about when the specified access key was last used. The information includes the date and time of last use, along with the Amazon Web Services service and Region that were specified in the last request made with that key.

## Input Shape: GetAccessKeyLastUsedRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccessKeyId | Any  # complex shape | ✓ | The identifier of an access key. This parameter allows (through its regex pattern ) a string of characters that can cons |

## Output Shape: GetAccessKeyLastUsedResponse

- **AccessKeyLastUsed** (Any  # complex shape): Contains information about the last time the access key was used.
- **UserName** (Any  # complex shape): The name of the IAM user that owns this access key.

## Implementation

```speclang
def get_access_key_last_used(store, request: dict) -> dict:
    """Retrieves information about when the specified access key was last used. The information includes the date and time of last use, along with the Amazon Web Services service and Region that were specifi"""
    access_key_id = request.get("AccessKeyId", "").strip() if isinstance(request.get("AccessKeyId"), str) else request.get("AccessKeyId")
    if not access_key_id:
        raise ValidationException("AccessKeyId is required")

    resource = store.access_key_last_useds(access_key_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource access_key_id not found")
    return {"AccessKeyId": access_key_id, **resource}
```
