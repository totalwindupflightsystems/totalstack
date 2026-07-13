---
id: "@specs/aws/iam/delete_ssh_public_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteSSHPublicKey"
---

# DeleteSSHPublicKey

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_ssh_public_key
> **spec:implements:** @kind:operation DeleteSSHPublicKey
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteSSHPublicKey.spec.md

Deletes the specified SSH public key. The SSH public key deleted by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see Set up CodeCommit for SSH connections in the CodeCommit User Guide .

## Input Shape: DeleteSSHPublicKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SSHPublicKeyId | Any  # complex shape | ✓ | The unique identifier for the SSH public key. This parameter allows (through its regex pattern ) a string of characters  |
| UserName | Any  # complex shape | ✓ | The name of the IAM user associated with the SSH public key. This parameter allows (through its regex pattern ) a string |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.

## Implementation

```speclang
def delete_ssh_public_key(store, request: dict) -> dict:
    """Deletes the specified SSH public key. The SSH public key deleted by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using"""
    ssh_public_key_id = request.get("SSHPublicKeyId", "").strip() if isinstance(request.get("SSHPublicKeyId"), str) else request.get("SSHPublicKeyId")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")

    if not store.ssh_public_keys(user_name):
        raise ResourceNotFoundException(f"Resource user_name not found")
    store.delete_ssh_public_keys(user_name)
    return {}
```
