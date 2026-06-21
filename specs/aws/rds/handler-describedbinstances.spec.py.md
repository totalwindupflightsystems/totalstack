---
id: "@specs/aws/rds/handler-describedbinstances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DescribeDBInstances

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-describedbinstances
> **spec:implements:** @kind:operation DescribeDBInstances
> **@ref:** specs/aws/rds/docs/API_DescribeDBInstances.spec.md

AWS RDS DescribeDBInstances operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DescribeDBInstances handler for RDS."""
    return {}
```
