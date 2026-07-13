---
id: "@specs/aws/cloudformation/get_generated_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_GetGeneratedTemplate"
---

# GetGeneratedTemplate

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/get_generated_template
> **spec:implements:** @kind:operation GetGeneratedTemplate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_GetGeneratedTemplate.spec.md

Retrieves a generated template. If the template is in an InProgress or Pending status then the template returned will be the template when the template was last in a Complete status. If the template has not yet been in a Complete status then an empty template will be returned.

## Input Shape: GetGeneratedTemplateInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Format | Any  # complex shape |  | The language to use to retrieve for the generated template. Supported values are: JSON YAML |
| GeneratedTemplateName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the generated template. The format is arn:${Partition}:cloudformation:${Region |

## Output Shape: GetGeneratedTemplateOutput

- **Status** (Any  # complex shape): The status of the template generation. Supported values are: CreatePending - the creation of the template is pending. Cr
- **TemplateBody** (Any  # complex shape): The template body of the generated template, in the language specified by the Language parameter.

## Errors
- **GeneratedTemplateNotFoundException**: The generated template was not found.

## Implementation

```speclang
def get_generated_template(store, request: dict) -> dict:
    """Retrieves a generated template. If the template is in an InProgress or Pending status then the template returned will be the template when the template was last in a Complete status. If the template h"""
    generated_template_name = request.get("GeneratedTemplateName", "").strip() if isinstance(request.get("GeneratedTemplateName"), str) else request.get("GeneratedTemplateName")
    if not generated_template_name:
        raise ValidationException("GeneratedTemplateName is required")

    resource = store.generated_templates(generated_template_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource generated_template_name not found")
    return {"GeneratedTemplateName": generated_template_name, **resource}
```
