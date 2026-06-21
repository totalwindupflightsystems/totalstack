---
id: "@specs/aws/rds/handler-createdbsubnetgroup"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# CreateDBSubnetGroup

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-createdbsubnetgroup
> **spec:implements:** @kind:operation CreateDBSubnetGroup
> **@ref:** specs/aws/rds/docs/API_CreateDBSubnetGroup.spec.md

AWS RDS CreateDBSubnetGroup operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """CreateDBSubnetGroup handler for RDS."""
    return {}
```
