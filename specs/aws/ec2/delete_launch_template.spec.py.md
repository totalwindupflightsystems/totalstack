---
id: "@specs/aws/ec2/delete_launch_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLaunchTemplate"
---

# DeleteLaunchTemplate

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_launch_template
> **spec:implements:** @kind:operation DeleteLaunchTemplate
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLaunchTemplate.spec.md

Deletes a launch template. Deleting a launch template deletes all of its versions.

## Input Shape: DeleteLaunchTemplateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LaunchTemplateId | Any  # complex shape |  | The ID of the launch template. You must specify either the launch template ID or the launch template name, but not both. |
| LaunchTemplateName | Any  # complex shape |  | The name of the launch template. You must specify either the launch template ID or the launch template name, but not bot |

## Output Shape: DeleteLaunchTemplateResult

- **LaunchTemplate** (Any  # complex shape): Information about the launch template.

## Implementation

```speclang
def delete_launch_template(store, request: dict) -> dict:
    """Deletes a launch template. Deleting a launch template deletes all of its versions."""

    return {}
```
