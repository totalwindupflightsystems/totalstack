---
id: "@specs/aws/rds/handler-deletedbparametergroup"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DeleteDBParameterGroup

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-deletedbparametergroup
> **spec:implements:** @kind:operation DeleteDBParameterGroup
> **@ref:** specs/aws/rds/docs/API_DeleteDBParameterGroup.spec.md

AWS RDS DeleteDBParameterGroup operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DeleteDBParameterGroup handler for RDS."""
    return {}
```
