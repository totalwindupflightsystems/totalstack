---
id: "@specs/aws/rds/handler-createdbclusterparametergroup"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# CreateDBClusterParameterGroup

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-createdbclusterparametergroup
> **spec:implements:** @kind:operation CreateDBClusterParameterGroup
> **@ref:** specs/aws/rds/docs/API_CreateDBClusterParameterGroup.spec.md

AWS RDS CreateDBClusterParameterGroup operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """CreateDBClusterParameterGroup handler for RDS."""
    return {}
```
