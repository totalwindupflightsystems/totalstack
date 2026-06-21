---
id: "@specs/aws/rds/handler-describedbclusters"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DescribeDBClusters

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-describedbclusters
> **spec:implements:** @kind:operation DescribeDBClusters
> **@ref:** specs/aws/rds/docs/API_DescribeDBClusters.spec.md

AWS RDS DescribeDBClusters operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DescribeDBClusters handler for RDS."""
    return {}
```
