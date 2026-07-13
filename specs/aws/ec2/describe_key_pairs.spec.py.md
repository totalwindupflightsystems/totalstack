---
id: "@specs/aws/ec2/describe_key_pairs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeKeyPairs"
---

# DescribeKeyPairs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_key_pairs
> **spec:implements:** @kind:operation DescribeKeyPairs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeKeyPairs.spec.md

Describes the specified key pairs or all of your key pairs. For more information about key pairs, see Amazon EC2 key pairs in the Amazon EC2 User Guide .

## Input Shape: DescribeKeyPairsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. key-pair-id - The ID of the key pair. fingerprint - The fingerprint of the key pair. key-name - The name of |
| IncludePublicKey | bool |  | If true , the public key material is included in the response. Default: false |
| KeyNames | list[Any  # complex shape] |  | The key pair names. Default: Describes all of your key pairs. |
| KeyPairIds | list[Any  # complex shape] |  | The IDs of the key pairs. |

## Output Shape: DescribeKeyPairsResult

- **KeyPairs** (list[Any  # complex shape]): Information about the key pairs.

## Implementation

```speclang
def describe_key_pairs(store, request: dict) -> dict:
    """Describes the specified key pairs or all of your key pairs. For more information about key pairs, see Amazon EC2 key pairs in the Amazon EC2 User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
