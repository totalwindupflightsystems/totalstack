---
id: "@specs/aws/ec2/create_launch_template"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLaunchTemplate"
---

# CreateLaunchTemplate

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_launch_template
> **spec:implements:** @kind:operation CreateLaunchTemplate
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLaunchTemplate.spec.md

Creates a launch template. A launch template contains the parameters to launch an instance. When you launch an instance using RunInstances , you can specify a launch template instead of providing the launch parameters in the request. For more information, see Store instance launch parameters in Amazon EC2 launch templates in the Amazon EC2 User Guide . To clone an existing launch template as the basis for a new launch template, use the Amazon EC2 console. The API, SDKs, and CLI do not support cloning a template. For more information, see Create a launch template from an existing launch template in the Amazon EC2 User Guide .

## Input Shape: CreateLaunchTemplateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specifie |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LaunchTemplateData | Any  # complex shape | ✓ | The information for the launch template. |
| LaunchTemplateName | Any  # complex shape | ✓ | A name for the launch template. |
| Operator | Any  # complex shape |  | Reserved for internal use. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the launch template on creation. To tag the launch template, the resource type must be launch-templ |
| VersionDescription | Any  # complex shape |  | A description for the first version of the launch template. |

## Output Shape: CreateLaunchTemplateResult

- **LaunchTemplate** (Any  # complex shape): Information about the launch template.
- **Warning** (Any  # complex shape): If the launch template contains parameters or parameter combinations that are not valid, an error code and an error mess

## Implementation

```speclang
def create_launch_template(store, request: dict) -> dict:
    """Creates a launch template. A launch template contains the parameters to launch an instance. When you launch an instance using RunInstances , you can specify a launch template instead of providing the """
    launch_template_data = request.get("LaunchTemplateData", "").strip() if isinstance(request.get("LaunchTemplateData"), str) else request.get("LaunchTemplateData")
    if not launch_template_data:
        raise ValidationException("LaunchTemplateData is required")
    launch_template_name = request.get("LaunchTemplateName", "").strip() if isinstance(request.get("LaunchTemplateName"), str) else request.get("LaunchTemplateName")
    if not launch_template_name:
        raise ValidationException("LaunchTemplateName is required")

    if store.launch_templates(launch_template_name):
        raise ResourceInUseException(f"Resource launch_template_name already exists")

    record = {
        "DryRun": dry_run,
        "ClientToken": client_token,
        "LaunchTemplateName": launch_template_name,
        "VersionDescription": version_description,
        "LaunchTemplateData": launch_template_data,
        "Operator": operator,
        "TagSpecifications": tag_specifications,
    }

    store.launch_templates(launch_template_name, record)

    return {
        "LaunchTemplate": record.get("LaunchTemplate", {}),
        "Warning": record.get("Warning", {}),
    }
```
