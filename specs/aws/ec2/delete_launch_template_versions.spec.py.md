---
id: "@specs/aws/ec2/delete_launch_template_versions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLaunchTemplateVersions"
---

# DeleteLaunchTemplateVersions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_launch_template_versions
> **spec:implements:** @kind:operation DeleteLaunchTemplateVersions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLaunchTemplateVersions.spec.md

Deletes one or more versions of a launch template. You can't delete the default version of a launch template; you must first assign a different version as the default. If the default version is the only version for the launch template, you must delete the entire launch template using DeleteLaunchTemplate . You can delete up to 200 launch template versions in a single request. To delete more than 200 versions in a single request, use DeleteLaunchTemplate , which deletes the launch template and all of its versions. For more information, see Delete a launch template version in the Amazon EC2 User Guide .

## Input Shape: DeleteLaunchTemplateVersionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LaunchTemplateId | Any  # complex shape |  | The ID of the launch template. You must specify either the launch template ID or the launch template name, but not both. |
| LaunchTemplateName | Any  # complex shape |  | The name of the launch template. You must specify either the launch template ID or the launch template name, but not bot |
| Versions | list[str] | ✓ | The version numbers of one or more launch template versions to delete. You can specify up to 200 launch template version |

## Output Shape: DeleteLaunchTemplateVersionsResult

- **SuccessfullyDeletedLaunchTemplateVersions** (Any  # complex shape): Information about the launch template versions that were successfully deleted.
- **UnsuccessfullyDeletedLaunchTemplateVersions** (Any  # complex shape): Information about the launch template versions that could not be deleted.

## Implementation

```speclang
def delete_launch_template_versions(store, request: dict) -> dict:
    """Deletes one or more versions of a launch template. You can't delete the default version of a launch template; you must first assign a different version as the default. If the default version is the on"""
    versions = request.get("Versions", "").strip() if isinstance(request.get("Versions"), str) else request.get("Versions")

    if not store.launch_template_versionss(versions):
        raise ResourceNotFoundException(f"Resource versions not found")
    store.delete_launch_template_versionss(versions)
    return {}
```
