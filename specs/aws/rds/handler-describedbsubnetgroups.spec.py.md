---
id: "@specs/aws/rds/handler-describedbsubnetgroups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# DescribeDBSubnetGroups

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-describedbsubnetgroups
> **spec:implements:** @kind:operation DescribeDBSubnetGroups
> **@ref:** specs/aws/rds/docs/API_DescribeDBSubnetGroups.spec.md

AWS RDS DescribeDBSubnetGroups operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """DescribeDBSubnetGroups handler for RDS."""
    return {}
```
