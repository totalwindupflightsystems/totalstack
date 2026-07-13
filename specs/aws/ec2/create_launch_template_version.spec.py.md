---
id: "@specs/aws/ec2/create_launch_template_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLaunchTemplateVersion"
---

# CreateLaunchTemplateVersion

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_launch_template_version
> **spec:implements:** @kind:operation CreateLaunchTemplateVersion
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLaunchTemplateVersion.spec.md

Creates a new version of a launch template. You must specify an existing launch template, either by name or ID. You can determine whether the new version inherits parameters from a source version, and add or overwrite parameters as needed. Launch template versions are numbered in the order in which they are created. You can't specify, change, or replace the numbering of launch template versions. Launch templates are immutable; after you create a launch template, you can't modify it. Instead, you can create a new version of the launch template that includes the changes that you require. For more information, see Modify a launch template (manage launch template versions) in the Amazon EC2 User Guide .

## Input Shape: CreateLaunchTemplateVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specifie |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LaunchTemplateData | Any  # complex shape | ✓ | The information for the launch template. |
| LaunchTemplateId | Any  # complex shape |  | The ID of the launch template. You must specify either the launch template ID or the launch template name, but not both. |
| LaunchTemplateName | Any  # complex shape |  | The name of the launch template. You must specify either the launch template ID or the launch template name, but not bot |
| ResolveAlias | bool |  | If true , and if a Systems Manager parameter is specified for ImageId , the AMI ID is displayed in the response for imag |
| SourceVersion | str |  | The version of the launch template on which to base the new version. Snapshots applied to the block device mapping are i |
| VersionDescription | Any  # complex shape |  | A description for the version of the launch template. |

## Output Shape: CreateLaunchTemplateVersionResult

- **LaunchTemplateVersion** (Any  # complex shape): Information about the launch template version.
- **Warning** (Any  # complex shape): If the new version of the launch template contains parameters or parameter combinations that are not valid, an error cod

## Implementation

```speclang
def create_launch_template_version(store, request: dict) -> dict:
    """Creates a new version of a launch template. You must specify an existing launch template, either by name or ID. You can determine whether the new version inherits parameters from a source version, and"""
    launch_template_data = request.get("LaunchTemplateData", "").strip() if isinstance(request.get("LaunchTemplateData"), str) else request.get("LaunchTemplateData")
    if not launch_template_data:
        raise ValidationException("LaunchTemplateData is required")

    if store.launch_template_versions(launch_template_data):
        raise ResourceInUseException(f"Resource launch_template_data already exists")

    record = {
        "DryRun": dry_run,
        "ClientToken": client_token,
        "LaunchTemplateId": launch_template_id,
        "LaunchTemplateName": launch_template_name,
        "SourceVersion": source_version,
        "VersionDescription": version_description,
        "LaunchTemplateData": launch_template_data,
        "ResolveAlias": resolve_alias,
    }

    store.launch_template_versions(launch_template_data, record)

    return {
        "LaunchTemplateVersion": record.get("LaunchTemplateVersion", {}),
        "Warning": record.get("Warning", {}),
    }
```
