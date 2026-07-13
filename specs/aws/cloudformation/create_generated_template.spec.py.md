---
id: "@specs/aws/cloudformation/create_generated_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_CreateGeneratedTemplate"
---

# CreateGeneratedTemplate

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/create_generated_template
> **spec:implements:** @kind:operation CreateGeneratedTemplate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_CreateGeneratedTemplate.spec.md

Creates a template from existing resources that are not already managed with CloudFormation. You can check the status of the template generation using the DescribeGeneratedTemplate API action.

## Input Shape: CreateGeneratedTemplateInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GeneratedTemplateName | Any  # complex shape | ✓ | The name assigned to the generated template. |
| Resources | Any  # complex shape |  | An optional list of resources to be included in the generated template. If no resources are specified,the template will  |
| StackName | Any  # complex shape |  | An optional name or ARN of a stack to use as the base stack for the generated template. |
| TemplateConfiguration | Any  # complex shape |  | The configuration details of the generated template, including the DeletionPolicy and UpdateReplacePolicy . |

## Output Shape: CreateGeneratedTemplateOutput

- **GeneratedTemplateId** (Any  # complex shape): The ID of the generated template.

## Errors
- **AlreadyExistsException**: The resource with the name requested already exists.
- **LimitExceededException**: The quota for the resource has already been reached. For information about resource and stack limitations, see CloudFormation quotas in the CloudFormation User Guide .
- **ConcurrentResourcesLimitExceededException**: No more than 5 generated templates can be in an InProgress or Pending status at one time. This error is also returned if a generated template that is in an InProgress or Pending status is attempted to

## Implementation

```speclang
def create_generated_template(store, request: dict) -> dict:
    """Creates a template from existing resources that are not already managed with CloudFormation. You can check the status of the template generation using the DescribeGeneratedTemplate API action."""
    generated_template_name = request.get("GeneratedTemplateName", "").strip() if isinstance(request.get("GeneratedTemplateName"), str) else request.get("GeneratedTemplateName")
    if not generated_template_name:
        raise ValidationException("GeneratedTemplateName is required")

    if store.generated_templates(generated_template_name):
        raise ResourceInUseException(f"Resource generated_template_name already exists")

    record = {
        "Resources": resources,
        "GeneratedTemplateName": generated_template_name,
        "StackName": stack_name,
        "TemplateConfiguration": template_configuration,
    }

    store.generated_templates(generated_template_name, record)

    return {
        "GeneratedTemplateId": record.get("GeneratedTemplateId", {}),
    }
```
