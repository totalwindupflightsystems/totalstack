---
id: "@specs/aws/cloudformation/delete_generated_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeleteGeneratedTemplate"
---

# DeleteGeneratedTemplate

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/delete_generated_template
> **spec:implements:** @kind:operation DeleteGeneratedTemplate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeleteGeneratedTemplate.spec.md

Deleted a generated template.

## Input Shape: DeleteGeneratedTemplateInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GeneratedTemplateName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of a generated template. |

## Errors
- **GeneratedTemplateNotFoundException**: The generated template was not found.
- **ConcurrentResourcesLimitExceededException**: No more than 5 generated templates can be in an InProgress or Pending status at one time. This error is also returned if a generated template that is in an InProgress or Pending status is attempted to

## Implementation

```speclang
def delete_generated_template(store, request: dict) -> dict:
    """Deleted a generated template."""
    generated_template_name = request.get("GeneratedTemplateName", "").strip() if isinstance(request.get("GeneratedTemplateName"), str) else request.get("GeneratedTemplateName")

    if not store.generated_templates(generated_template_name):
        raise ResourceNotFoundException(f"Resource generated_template_name not found")
    store.delete_generated_templates(generated_template_name)
    return {}
```
