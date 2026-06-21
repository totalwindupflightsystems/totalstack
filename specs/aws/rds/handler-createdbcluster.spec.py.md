---
id: "@specs/aws/rds/handler-createdbcluster"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# CreateDBCluster

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-createdbcluster
> **spec:implements:** @kind:operation CreateDBCluster
> **@ref:** specs/aws/rds/docs/API_CreateDBClusterParameterGroup.spec.md

AWS RDS CreateDBCluster operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """CreateDBCluster handler for RDS."""
    return {}
```
