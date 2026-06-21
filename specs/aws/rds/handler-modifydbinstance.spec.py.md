---
id: "@specs/aws/rds/handler-modifydbinstance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# ModifyDBInstance

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-modifydbinstance
> **spec:implements:** @kind:operation ModifyDBInstance
> **@ref:** specs/aws/rds/docs/API_ModifyDBInstance.spec.md

AWS RDS ModifyDBInstance operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """ModifyDBInstance handler for RDS."""
    return {}
```
