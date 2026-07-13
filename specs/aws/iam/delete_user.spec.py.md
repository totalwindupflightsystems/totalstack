---
id: "@specs/aws/iam/delete_user"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteUser"
---

# DeleteUser

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_user
> **spec:implements:** @kind:operation DeleteUser
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteUser.spec.md

Deletes the specified IAM user. Unlike the Amazon Web Services Management Console, when you delete a user programmatically, you must delete the items attached to the user manually, or the deletion fails. For more information, see Deleting an IAM user . Before attempting to delete a user, remove the following items: Password ( DeleteLoginProfile ) Access keys ( DeleteAccessKey ) Signing certificate ( DeleteSigningCertificate ) SSH public key ( DeleteSSHPublicKey ) Git credentials ( DeleteServiceSpecificCredential ) Multi-factor authentication (MFA) device ( DeactivateMFADevice , DeleteVirtualMFADevice ) Inline policies ( DeleteUserPolicy ) Attached managed policies ( DetachUserPolicy ) Group memberships ( RemoveUserFromGroup )

## Input Shape: DeleteUserRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| UserName | Any  # complex shape | ✓ | The name of the user to delete. This parameter allows (through its regex pattern ) a string of characters consisting of  |

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_user(store, request: dict) -> dict:
    """Deletes the specified IAM user. Unlike the Amazon Web Services Management Console, when you delete a user programmatically, you must delete the items attached to the user manually, or the deletion fai"""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")

    if not store.users(user_name):
        raise ResourceNotFoundException(f"Resource user_name not found")
    store.delete_users(user_name)
    return {}
```
