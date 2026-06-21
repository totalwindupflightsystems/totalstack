---
id: "@specs/aws/rds/handler-describedbsnapshots"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DescribeDBSnapshots

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-describedbsnapshots
> **spec:implements:** @kind:operation DescribeDBSnapshots
> **@ref:** specs/aws/rds/docs/API_DescribeDBSnapshots.spec.md

AWS RDS DescribeDBSnapshots operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DescribeDBSnapshots handler for RDS."""
    return {}
```
