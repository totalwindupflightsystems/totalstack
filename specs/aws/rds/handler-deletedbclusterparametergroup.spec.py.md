---
id: "@specs/aws/rds/handler-deletedbclusterparametergroup"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DeleteDBClusterParameterGroup

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-deletedbclusterparametergroup
> **spec:implements:** @kind:operation DeleteDBClusterParameterGroup
> **@ref:** specs/aws/rds/docs/API_DeleteDBClusterParameterGroup.spec.md

AWS RDS DeleteDBClusterParameterGroup operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DeleteDBClusterParameterGroup handler for RDS."""
    return {}
```
