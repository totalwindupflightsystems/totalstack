---
id: "@specs/aws/ec2/import_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ImportKeyPair"
---

# ImportKeyPair

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/import_key_pair
> **spec:implements:** @kind:operation ImportKeyPair
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ImportKeyPair.spec.md

Imports the public key from an RSA or ED25519 key pair that you created using a third-party tool. You give Amazon Web Services only the public key. The private key is never transferred between you and Amazon Web Services. For more information about the requirements for importing a key pair, see Create a key pair and import the public key to Amazon EC2 in the Amazon EC2 User Guide .

## Input Shape: ImportKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| KeyName | str | ✓ | A unique name for the key pair. |
| PublicKeyMaterial | bytes | ✓ | The public key. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the imported key pair. |

## Output Shape: ImportKeyPairResult

- **KeyFingerprint** (str): For RSA key pairs, the key fingerprint is the MD5 public key fingerprint as specified in section 4 of RFC 4716. For ED25
- **KeyName** (str): The key pair name that you provided.
- **KeyPairId** (str): The ID of the resulting key pair.
- **Tags** (list[Any  # complex shape]): The tags applied to the imported key pair.

## Implementation

```speclang
def import_key_pair(store, request: dict) -> dict:
    """Imports the public key from an RSA or ED25519 key pair that you created using a third-party tool. You give Amazon Web Services only the public key. The private key is never transferred between you and"""
    key_name = request.get("KeyName", "").strip() if isinstance(request.get("KeyName"), str) else request.get("KeyName")
    if not key_name:
        raise ValidationException("KeyName is required")
    public_key_material = request.get("PublicKeyMaterial", "").strip() if isinstance(request.get("PublicKeyMaterial"), str) else request.get("PublicKeyMaterial")
    if not public_key_material:
        raise ValidationException("PublicKeyMaterial is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ImportKeyPair", request)
```
