---
id: "@specs/aws/iam/delete_account_alias"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteAccountAlias"
---

# DeleteAccountAlias

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_account_alias
> **spec:implements:** @kind:operation DeleteAccountAlias
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteAccountAlias.spec.md

Deletes the specified Amazon Web Services account alias. For information about using an Amazon Web Services account alias, see Creating, deleting, and listing an Amazon Web Services account alias in the Amazon Web Services Sign-In User Guide .

## Input Shape: DeleteAccountAliasRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccountAlias | Any  # complex shape | ✓ | The name of the account alias to delete. This parameter allows (through its regex pattern ) a string of characters consi |

## Errors
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_account_alias(store, request: dict) -> dict:
    """Deletes the specified Amazon Web Services account alias. For information about using an Amazon Web Services account alias, see Creating, deleting, and listing an Amazon Web Services account alias in t"""
    account_alias = request.get("AccountAlias", "").strip() if isinstance(request.get("AccountAlias"), str) else request.get("AccountAlias")

    if not store.account_aliass(account_alias):
        raise ResourceNotFoundException(f"Resource account_alias not found")
    store.delete_account_aliass(account_alias)
    return {}
```
