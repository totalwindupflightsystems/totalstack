---
id: "@specs/aws/iam/create_account_alias"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateAccountAlias"
---

# CreateAccountAlias

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_account_alias
> **spec:implements:** @kind:operation CreateAccountAlias
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateAccountAlias.spec.md

Creates an alias for your Amazon Web Services account. For information about using an Amazon Web Services account alias, see Creating, deleting, and listing an Amazon Web Services account alias in the Amazon Web Services Sign-In User Guide .

## Input Shape: CreateAccountAliasRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccountAlias | Any  # complex shape | ✓ | The account alias to create. This parameter allows (through its regex pattern ) a string of characters consisting of low |

## Errors
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_account_alias(store, request: dict) -> dict:
    """Creates an alias for your Amazon Web Services account. For information about using an Amazon Web Services account alias, see Creating, deleting, and listing an Amazon Web Services account alias in the"""
    account_alias = request.get("AccountAlias", "").strip() if isinstance(request.get("AccountAlias"), str) else request.get("AccountAlias")
    if not account_alias:
        raise ValidationException("AccountAlias is required")

    if store.account_aliass(account_alias):
        raise ResourceInUseException(f"Resource account_alias already exists")

    record = {
        "AccountAlias": account_alias,
    }

    store.account_aliass(account_alias, record)

    return {
    }
```
