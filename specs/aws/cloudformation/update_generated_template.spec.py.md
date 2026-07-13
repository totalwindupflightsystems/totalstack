---
id: "@specs/aws/cloudformation/update_generated_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_UpdateGeneratedTemplate"
---

# UpdateGeneratedTemplate

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/update_generated_template
> **spec:implements:** @kind:operation UpdateGeneratedTemplate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_UpdateGeneratedTemplate.spec.md

Updates a generated template. This can be used to change the name, add and remove resources, refresh resources, and change the DeletionPolicy and UpdateReplacePolicy settings. You can check the status of the update to the generated template using the DescribeGeneratedTemplate API action.

## Input Shape: UpdateGeneratedTemplateInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddResources | Any  # complex shape |  | An optional list of resources to be added to the generated template. |
| GeneratedTemplateName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of a generated template. |
| NewGeneratedTemplateName | Any  # complex shape |  | An optional new name to assign to the generated template. |
| RefreshAllResources | Any  # complex shape |  | If true , update the resource properties in the generated template with their current live state. This feature is useful |
| RemoveResources | Any  # complex shape |  | A list of logical ids for resources to remove from the generated template. |
| TemplateConfiguration | Any  # complex shape |  | The configuration details of the generated template, including the DeletionPolicy and UpdateReplacePolicy . |

## Output Shape: UpdateGeneratedTemplateOutput

- **GeneratedTemplateId** (Any  # complex shape): The Amazon Resource Name (ARN) of the generated template. The format is arn:${Partition}:cloudformation:${Region}:${Acco

## Errors
- **AlreadyExistsException**: The resource with the name requested already exists.
- **GeneratedTemplateNotFoundException**: The generated template was not found.
- **LimitExceededException**: The quota for the resource has already been reached. For information about resource and stack limitations, see CloudFormation quotas in the CloudFormation User Guide .

## Implementation

```speclang
def update_generated_template(store, request: dict) -> dict:
    """Updates a generated template. This can be used to change the name, add and remove resources, refresh resources, and change the DeletionPolicy and UpdateReplacePolicy settings. You can check the status"""
    generated_template_name = request.get("GeneratedTemplateName", "").strip() if isinstance(request.get("GeneratedTemplateName"), str) else request.get("GeneratedTemplateName")
    if not generated_template_name:
        raise ValidationException("GeneratedTemplateName is required")

    resource = store.generated_templates(generated_template_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource generated_template_name not found")

    # Update mutable fields
    if "NewGeneratedTemplateName" in request:
        resource["NewGeneratedTemplateName"] = new_generated_template_name
    if "AddResources" in request:
        resource["AddResources"] = add_resources
    if "RemoveResources" in request:
        resource["RemoveResources"] = remove_resources
    if "RefreshAllResources" in request:
        resource["RefreshAllResources"] = refresh_all_resources
    if "TemplateConfiguration" in request:
        resource["TemplateConfiguration"] = template_configuration

    store.generated_templates(generated_template_name, resource)
    return resource
```
