---
id: "@specs/aws/iam/upload_ssh_public_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UploadSSHPublicKey"
---

# UploadSSHPublicKey

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/upload_ssh_public_key
> **spec:implements:** @kind:operation UploadSSHPublicKey
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UploadSSHPublicKey.spec.md

Uploads an SSH public key and associates it with the specified IAM user. The SSH public key uploaded by this operation can be used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see Set up CodeCommit for SSH connections in the CodeCommit User Guide .

## Input Shape: UploadSSHPublicKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| SSHPublicKeyBody | Any  # complex shape | ✓ | The SSH public key. The public key must be encoded in ssh-rsa format or PEM format. The minimum bit-length of the public |
| UserName | Any  # complex shape | ✓ | The name of the IAM user to associate the SSH public key with. This parameter allows (through its regex pattern ) a stri |

## Output Shape: UploadSSHPublicKeyResponse

- **SSHPublicKey** (Any  # complex shape): Contains information about the SSH public key.

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidPublicKeyException**: The request was rejected because the public key is malformed or otherwise invalid.
- **DuplicateSSHPublicKeyException**: The request was rejected because the SSH public key is already associated with the specified IAM user.
- **UnrecognizedPublicKeyEncodingException**: The request was rejected because the public key encoding format is unsupported or unrecognized.

## Implementation

```speclang
def upload_ssh_public_key(store, request: dict) -> dict:
    """Uploads an SSH public key and associates it with the specified IAM user. The SSH public key uploaded by this operation can be used only for authenticating the associated IAM user to an CodeCommit repo"""
    ssh_public_key_body = request.get("SSHPublicKeyBody", "").strip() if isinstance(request.get("SSHPublicKeyBody"), str) else request.get("SSHPublicKeyBody")
    if not ssh_public_key_body:
        raise ValidationException("SSHPublicKeyBody is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("UploadSSHPublicKey", request)
```
