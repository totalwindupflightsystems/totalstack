---
id: "@specs/aws/ec2/modify_launch_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyLaunchTemplate"
---

# ModifyLaunchTemplate

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_launch_template
> **spec:implements:** @kind:operation ModifyLaunchTemplate
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyLaunchTemplate.spec.md

Modifies a launch template. You can specify which version of the launch template to set as the default version. When launching an instance, the default version applies when a launch template version is not specified.

## Input Shape: ModifyLaunchTemplateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specifie |
| DefaultVersion | str |  | The version number of the launch template to set as the default version. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LaunchTemplateId | Any  # complex shape |  | The ID of the launch template. You must specify either the launch template ID or the launch template name, but not both. |
| LaunchTemplateName | Any  # complex shape |  | The name of the launch template. You must specify either the launch template ID or the launch template name, but not bot |

## Output Shape: ModifyLaunchTemplateResult

- **LaunchTemplate** (Any  # complex shape): Information about the launch template.

## Implementation

```speclang
def modify_launch_template(store, request: dict) -> dict:
    """Modifies a launch template. You can specify which version of the launch template to set as the default version. When launching an instance, the default version applies when a launch template version i"""

```
