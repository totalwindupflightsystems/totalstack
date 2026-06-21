---
id: "@specs/aws/rds/handler-modifydbcluster"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# ModifyDBCluster

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-modifydbcluster
> **spec:implements:** @kind:operation ModifyDBCluster
> **@ref:** specs/aws/rds/docs/API_ModifyDBClusterSnapshotAttribute.spec.md

AWS RDS ModifyDBCluster operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """ModifyDBCluster handler for RDS."""
    return {}
```
