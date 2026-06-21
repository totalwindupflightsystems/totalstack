---
id: "@specs/aws/rds/handler-addtagstoresource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# AddTagsToResource

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-addtagstoresource
> **spec:implements:** @kind:operation AddTagsToResource
> **@ref:** specs/aws/rds/docs/API_AddTagsToResource.spec.md

AWS RDS AddTagsToResource operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """AddTagsToResource handler for RDS."""
    return {}
```
