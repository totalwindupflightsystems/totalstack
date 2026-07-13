---
id: "@specs/aws/ec2/delete_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteKeyPair"
---

# DeleteKeyPair

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_key_pair
> **spec:implements:** @kind:operation DeleteKeyPair
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteKeyPair.spec.md

Deletes the specified key pair, by removing the public key from Amazon EC2.

## Input Shape: DeleteKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| KeyName | Any  # complex shape |  | The name of the key pair. |
| KeyPairId | Any  # complex shape |  | The ID of the key pair. |

## Output Shape: DeleteKeyPairResult

- **KeyPairId** (str): The ID of the key pair.
- **Return** (bool): Is true if the request succeeds, and an error otherwise.

## Implementation

```speclang
def delete_key_pair(store, request: dict) -> dict:
    """Deletes the specified key pair, by removing the public key from Amazon EC2."""

    return {}
```
