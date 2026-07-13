---
id: "@specs/aws/cloudformation/get_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_GetTemplate"
---

# GetTemplate

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/get_template
> **spec:implements:** @kind:operation GetTemplate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_GetTemplate.spec.md

Returns the template body for a specified stack. You can get the template for running or deleted stacks. For deleted stacks, GetTemplate returns the template for up to 90 days after the stack has been deleted. If the template doesn't exist, a ValidationError is returned.

## Input Shape: GetTemplateInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ChangeSetName | Any  # complex shape |  | The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you  |
| StackName | Any  # complex shape |  | The name or the unique stack ID that's associated with the stack, which aren't always interchangeable: Running stacks: Y |
| TemplateStage | Any  # complex shape |  | For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted  |

## Output Shape: GetTemplateOutput

- **StagesAvailable** (list[Any  # complex shape]): The stage of the template that you can retrieve. For stacks, the Original and Processed templates are always available. 
- **TemplateBody** (Any  # complex shape): Structure that contains the template body. CloudFormation returns the same template that was used when the stack was cre

## Errors
- **ChangeSetNotFoundException**: The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the ListChangeSets operation.

## Implementation

```speclang
def get_template(store, request: dict) -> dict:
    """Returns the template body for a specified stack. You can get the template for running or deleted stacks. For deleted stacks, GetTemplate returns the template for up to 90 days after the stack has been"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
