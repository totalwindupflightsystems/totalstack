---
id: "@specs/aws/rds/handler-modifydbparametergroup"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# ModifyDBParameterGroup

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-modifydbparametergroup
> **spec:implements:** @kind:operation ModifyDBParameterGroup
> **@ref:** specs/aws/rds/docs/API_ModifyDBParameterGroup.spec.md

AWS RDS ModifyDBParameterGroup operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """ModifyDBParameterGroup handler for RDS."""
    return {}
```
