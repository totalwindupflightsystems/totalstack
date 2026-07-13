---
id: "@specs/aws/iam/get_ssh_public_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetSSHPublicKey"
---

# GetSSHPublicKey

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_ssh_public_key
> **spec:implements:** @kind:operation GetSSHPublicKey
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetSSHPublicKey.spec.md

Retrieves the specified SSH public key, including metadata about the key. The SSH public key retrieved by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see Set up CodeCommit for SSH connections in the CodeCommit User Guide .

## Input Shape: GetSSHPublicKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Encoding | Any  # complex shape | ✓ | Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use SSH . |
| SSHPublicKeyId | Any  # complex shape | ✓ | The unique identifier for the SSH public key. This parameter allows (through its regex pattern ) a string of characters  |
| UserName | Any  # complex shape | ✓ | The name of the IAM user associated with the SSH public key. This parameter allows (through its regex pattern ) a string |

## Output Shape: GetSSHPublicKeyResponse

- **SSHPublicKey** (Any  # complex shape): A structure containing details about the SSH public key.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **UnrecognizedPublicKeyEncodingException**: The request was rejected because the public key encoding format is unsupported or unrecognized.

## Implementation

```speclang
def get_ssh_public_key(store, request: dict) -> dict:
    """Retrieves the specified SSH public key, including metadata about the key. The SSH public key retrieved by this operation is used only for authenticating the associated IAM user to an CodeCommit reposi"""
    encoding = request.get("Encoding", "").strip() if isinstance(request.get("Encoding"), str) else request.get("Encoding")
    if not encoding:
        raise ValidationException("Encoding is required")
    ssh_public_key_id = request.get("SSHPublicKeyId", "").strip() if isinstance(request.get("SSHPublicKeyId"), str) else request.get("SSHPublicKeyId")
    if not ssh_public_key_id:
        raise ValidationException("SSHPublicKeyId is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    resource = store.ssh_public_keys(user_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource user_name not found")
    return {"UserName": user_name, **resource}
```
