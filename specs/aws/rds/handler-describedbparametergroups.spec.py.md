---
id: "@specs/aws/rds/handler-describedbparametergroups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DescribeDBParameterGroups

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-describedbparametergroups
> **spec:implements:** @kind:operation DescribeDBParameterGroups
> **@ref:** specs/aws/rds/docs/API_DescribeDBParameterGroups.spec.md

AWS RDS DescribeDBParameterGroups operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DescribeDBParameterGroups handler for RDS."""
    return {}
```
