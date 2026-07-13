---
id: "@specs/aws/iam/update_ssh_public_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateSSHPublicKey"
---

# UpdateSSHPublicKey

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_ssh_public_key
> **spec:implements:** @kind:operation UpdateSSHPublicKey
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateSSHPublicKey.spec.md

Sets the status of an IAM user's SSH public key to active or inactive. SSH public keys that are inactive cannot be used for authentication. This operation can be used to disable a user's SSH public key as part of a key rotation work flow. The SSH public key affected by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see Set up CodeCommit for SSH connections in the CodeCommit User Guide .

## Input Shape: UpdateSSHPublicKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SSHPublicKeyId | Any  # complex shape | ✓ | The unique identifier for the SSH public key. This parameter allows (through its regex pattern ) a string of characters  |
| Status | Any  # complex shape | ✓ | The status to assign to the SSH public key. Active means that the key can be used for authentication with an CodeCommit  |
| UserName | Any  # complex shape | ✓ | The name of the IAM user associated with the SSH public key. This parameter allows (through its regex pattern ) a string |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def update_ssh_public_key(store, request: dict) -> dict:
    """Sets the status of an IAM user's SSH public key to active or inactive. SSH public keys that are inactive cannot be used for authentication. This operation can be used to disable a user's SSH public ke"""
    ssh_public_key_id = request.get("SSHPublicKeyId", "").strip() if isinstance(request.get("SSHPublicKeyId"), str) else request.get("SSHPublicKeyId")
    if not ssh_public_key_id:
        raise ValidationException("SSHPublicKeyId is required")
    status = request.get("Status", "").strip() if isinstance(request.get("Status"), str) else request.get("Status")
    if not status:
        raise ValidationException("Status is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    resource = store.ssh_public_keys(user_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource user_name not found")

    # Update mutable fields

    store.ssh_public_keys(user_name, resource)
    return resource
```
