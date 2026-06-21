---
id: "@specs/aws/rds/handler-createdbinstance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# CreateDBInstance

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-createdbinstance
> **spec:implements:** @kind:operation CreateDBInstance
> **@ref:** specs/aws/rds/docs/API_CreateDBInstance.spec.md

AWS RDS CreateDBInstance operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """CreateDBInstance handler for RDS."""
    return {}
```
