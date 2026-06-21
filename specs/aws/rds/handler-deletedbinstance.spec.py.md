---
id: "@specs/aws/rds/handler-deletedbinstance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DeleteDBInstance

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-deletedbinstance
> **spec:implements:** @kind:operation DeleteDBInstance
> **@ref:** specs/aws/rds/docs/API_DeleteDBInstance.spec.md

AWS RDS DeleteDBInstance operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DeleteDBInstance handler for RDS."""
    return {}
```
