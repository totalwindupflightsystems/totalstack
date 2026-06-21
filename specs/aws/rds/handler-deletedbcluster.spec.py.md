---
id: "@specs/aws/rds/handler-deletedbcluster"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DeleteDBCluster

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-deletedbcluster
> **spec:implements:** @kind:operation DeleteDBCluster
> **@ref:** specs/aws/rds/docs/API_DeleteDBClusterAutomatedBackup.spec.md

AWS RDS DeleteDBCluster operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DeleteDBCluster handler for RDS."""
    return {}
```
