---
id: "@specs/aws/rds/handler-describedbclusterparametergroups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DescribeDBClusterParameterGroups

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-describedbclusterparametergroups
> **spec:implements:** @kind:operation DescribeDBClusterParameterGroups
> **@ref:** specs/aws/rds/docs/API_DescribeDBClusterParameterGroups.spec.md

AWS RDS DescribeDBClusterParameterGroups operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DescribeDBClusterParameterGroups handler for RDS."""
    return {}
```
