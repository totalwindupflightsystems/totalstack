---
id: "@specs/aws/rds/handler-listtagsforresource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# ListTagsForResource

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-listtagsforresource
> **spec:implements:** @kind:operation ListTagsForResource
> **@ref:** specs/aws/rds/docs/API_ListTagsForResource.spec.md

AWS RDS ListTagsForResource operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """ListTagsForResource handler for RDS."""
    return {}
```
