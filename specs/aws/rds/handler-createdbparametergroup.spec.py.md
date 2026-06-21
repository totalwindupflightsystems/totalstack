---
id: "@specs/aws/rds/handler-createdbparametergroup"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# CreateDBParameterGroup

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-createdbparametergroup
> **spec:implements:** @kind:operation CreateDBParameterGroup
> **@ref:** specs/aws/rds/docs/API_CreateDBParameterGroup.spec.md

AWS RDS CreateDBParameterGroup operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """CreateDBParameterGroup handler for RDS."""
    return {}
```
