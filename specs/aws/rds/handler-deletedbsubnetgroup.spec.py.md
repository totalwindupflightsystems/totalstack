---
id: "@specs/aws/rds/handler-deletedbsubnetgroup"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DeleteDBSubnetGroup

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-deletedbsubnetgroup
> **spec:implements:** @kind:operation DeleteDBSubnetGroup
> **@ref:** specs/aws/rds/docs/API_DeleteDBSubnetGroup.spec.md

AWS RDS DeleteDBSubnetGroup operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DeleteDBSubnetGroup handler for RDS."""
    return {}
```
