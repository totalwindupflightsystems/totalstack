---
id: "@specs/aws/ec2/create_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateKeyPair"
---

# CreateKeyPair

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_key_pair
> **spec:implements:** @kind:operation CreateKeyPair
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateKeyPair.spec.md

Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the specified format. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded PKCS#1 private key or an unencrypted PPK formatted private key for use with PuTTY. If a key with the specified name already exists, Amazon EC2 returns an error. The key pair returned to you is available only in the Amazon Web Services Region in which you create it. If you prefer, you can create your own key pair using a third-party tool and upload it to any Region using ImportKeyPair . You can have up to 5,000 key pairs per Amazon Web Services Region. For more information, see Amazon EC2 key pairs in the Amazon EC2 User Guide .

## Input Shape: CreateKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| KeyFormat | Any  # complex shape |  | The format of the key pair. Default: pem |
| KeyName | str | ✓ | A unique name for the key pair. Constraints: Up to 255 ASCII characters |
| KeyType | Any  # complex shape |  | The type of key pair. Note that ED25519 keys are not supported for Windows instances. Default: rsa |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the new key pair. |

## Output Shape: KeyPair

- **KeyFingerprint** (str): For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key. For ED25519 key pairs, the ke
- **KeyMaterial** (Any  # complex shape): An unencrypted PEM encoded RSA or ED25519 private key.
- **KeyName** (str): The name of the key pair.
- **KeyPairId** (str): The ID of the key pair.
- **Tags** (list[Any  # complex shape]): Any tags applied to the key pair.

## Implementation

```speclang
def create_key_pair(store, request: dict) -> dict:
    """Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the specified format. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private ke"""
    key_name = request.get("KeyName", "").strip() if isinstance(request.get("KeyName"), str) else request.get("KeyName")
    if not key_name:
        raise ValidationException("KeyName is required")

    if store.key_pairs(key_name):
        raise ResourceInUseException(f"Resource key_name already exists")

    record = {
        "KeyName": key_name,
        "KeyType": key_type,
        "TagSpecifications": tag_specifications,
        "KeyFormat": key_format,
        "DryRun": dry_run,
    }

    store.key_pairs(key_name, record)

    return {
        "KeyPairId": record.get("KeyPairId", {}),
        "Tags": record.get("Tags", {}),
        "KeyName": key_name,
        "KeyFingerprint": record.get("KeyFingerprint", {}),
        "KeyMaterial": record.get("KeyMaterial", {}),
    }
```
