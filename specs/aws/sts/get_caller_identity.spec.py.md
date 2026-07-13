---
id: "@specs/aws/sts/get_caller_identity"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_GetCallerIdentity"
---

# GetCallerIdentity

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/get_caller_identity
> **spec:implements:** @kind:operation GetCallerIdentity
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_GetCallerIdentity.spec.md

Returns details about the IAM user or role whose credentials are used to call the operation. No permissions are required to perform this operation. If an administrator attaches a policy to your identity that explicitly denies access to the sts:GetCallerIdentity action, you can still perform this operation. Permissions are not required because the same information is returned when access is denied. To view an example response, see I Am Not Authorized to Perform: iam:DeleteVirtualMFADevice in the IAM User Guide .

## Input Shape: GetCallerIdentityRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: GetCallerIdentityResponse

- **Account** (Any  # complex shape): The Amazon Web Services account ID number of the account that owns or contains the calling entity.
- **Arn** (Any  # complex shape): The Amazon Web Services ARN associated with the calling entity.
- **UserId** (Any  # complex shape): The unique identifier of the calling entity. The exact value depends on the type of entity that is making the call. The 

## Implementation

```speclang
def get_caller_identity(store, request: dict) -> dict:
    """Returns details about the IAM user or role whose credentials are used to call the operation. No permissions are required to perform this operation. If an administrator attaches a policy to your identi"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
