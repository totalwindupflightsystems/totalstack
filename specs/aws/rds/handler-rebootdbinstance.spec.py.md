---
id: "@specs/aws/rds/handler-rebootdbinstance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# RebootDBInstance

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-rebootdbinstance
> **spec:implements:** @kind:operation RebootDBInstance
> **@ref:** specs/aws/rds/docs/API_RebootDBInstance.spec.md

AWS RDS RebootDBInstance operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """RebootDBInstance handler for RDS."""
    return {}
```
