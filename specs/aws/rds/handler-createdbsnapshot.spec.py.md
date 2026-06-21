---
id: "@specs/aws/rds/handler-createdbsnapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# CreateDBSnapshot

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-createdbsnapshot
> **spec:implements:** @kind:operation CreateDBSnapshot
> **@ref:** specs/aws/rds/docs/API_CreateDBSnapshot.spec.md

AWS RDS CreateDBSnapshot operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """CreateDBSnapshot handler for RDS."""
    return {}
```
