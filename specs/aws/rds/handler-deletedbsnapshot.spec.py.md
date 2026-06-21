---
id: "@specs/aws/rds/handler-deletedbsnapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DeleteDBSnapshot

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-deletedbsnapshot
> **spec:implements:** @kind:operation DeleteDBSnapshot
> **@ref:** specs/aws/rds/docs/API_DeleteDBSnapshot.spec.md

AWS RDS DeleteDBSnapshot operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DeleteDBSnapshot handler for RDS."""
    return {}
```
