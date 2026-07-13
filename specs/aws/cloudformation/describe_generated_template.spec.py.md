---
id: "@specs/aws/cloudformation/describe_generated_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeGeneratedTemplate"
---

# DescribeGeneratedTemplate

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_generated_template
> **spec:implements:** @kind:operation DescribeGeneratedTemplate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeGeneratedTemplate.spec.md

Describes a generated template. The output includes details about the progress of the creation of a generated template started by a CreateGeneratedTemplate API action or the update of a generated template started with an UpdateGeneratedTemplate API action.

## Input Shape: DescribeGeneratedTemplateInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GeneratedTemplateName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of a generated template. |

## Output Shape: DescribeGeneratedTemplateOutput

- **CreationTime** (Any  # complex shape): The time the generated template was created.
- **GeneratedTemplateId** (Any  # complex shape): The Amazon Resource Name (ARN) of the generated template. The format is arn:${Partition}:cloudformation:${Region}:${Acco
- **GeneratedTemplateName** (Any  # complex shape): The name of the generated template.
- **LastUpdatedTime** (Any  # complex shape): The time the generated template was last updated.
- **Progress** (Any  # complex shape): An object describing the progress of the template generation.
- **Resources** (Any  # complex shape): A list of objects describing the details of the resources in the template generation.
- **StackId** (Any  # complex shape): The stack ARN of the base stack if a base stack was provided when generating the template.
- **Status** (Any  # complex shape): The status of the template generation. Supported values are: CreatePending - the creation of the template is pending. Cr
- **StatusReason** (Any  # complex shape): The reason for the current template generation status. This will provide more details if a failure happened.
- **TemplateConfiguration** (Any  # complex shape): The configuration details of the generated template, including the DeletionPolicy and UpdateReplacePolicy .
- **TotalWarnings** (Any  # complex shape): The number of warnings generated for this template. The warnings are found in the details of each of the resources in th

## Errors
- **GeneratedTemplateNotFoundException**: The generated template was not found.

## Implementation

```speclang
def describe_generated_template(store, request: dict) -> dict:
    """Describes a generated template. The output includes details about the progress of the creation of a generated template started by a CreateGeneratedTemplate API action or the update of a generated temp"""
    generated_template_name = request.get("GeneratedTemplateName", "").strip() if isinstance(request.get("GeneratedTemplateName"), str) else request.get("GeneratedTemplateName")
    if not generated_template_name:
        raise ValidationException("GeneratedTemplateName is required")

    resource = store.generated_templates(generated_template_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource generated_template_name not found")
    return {"GeneratedTemplateName": generated_template_name, **resource}
```
