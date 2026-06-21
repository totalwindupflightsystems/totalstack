---
id: "@specs/aws/rds/handler-removetagsfromresource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/rds/plan"
---

# RemoveTagsFromResource

> **spec:trace:** specs/aws/rds/rds.spec.plan.md
> **spec:id:** @specs/aws/rds/handler-removetagsfromresource
> **spec:implements:** @kind:operation RemoveTagsFromResource
> **@ref:** specs/aws/rds/docs/API_RemoveTagsFromResource.spec.md

AWS RDS RemoveTagsFromResource operation handler.

```speclang
def handler(store, request: dict) -> dict:
    """RemoveTagsFromResource handler for RDS."""
    return {}
```
