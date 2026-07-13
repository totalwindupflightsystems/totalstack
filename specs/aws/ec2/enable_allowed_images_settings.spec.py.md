---
id: "@specs/aws/ec2/enable_allowed_images_settings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableAllowedImagesSettings"
---

# EnableAllowedImagesSettings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_allowed_images_settings
> **spec:implements:** @kind:operation EnableAllowedImagesSettings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableAllowedImagesSettings.spec.md

Enables Allowed AMIs for your account in the specified Amazon Web Services Region. Two values are accepted: enabled : The image criteria in your Allowed AMIs settings are applied. As a result, only AMIs matching these criteria are discoverable and can be used by your account to launch instances. audit-mode : The image criteria in your Allowed AMIs settings are not applied. No restrictions are placed on AMI discoverability or usage. Users in your account can launch instances using any public AMI or AMI shared with your account. The purpose of audit-mode is to indicate which AMIs will be affected when Allowed AMIs is enabled . In audit-mode , each AMI displays either "ImageAllowed": true or "ImageAllowed": false to indicate whether the AMI will be discoverable and available to users in the account when Allowed AMIs is enabled. The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will always be discoverable and usable by users in your account. For more information, see Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs in Amazon EC2 User Guide .

## Input Shape: EnableAllowedImagesSettingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllowedImagesSettingsState | Any  # complex shape | ✓ | Specify enabled to apply the image criteria specified by the Allowed AMIs settings. Specify audit-mode so that you can c |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: EnableAllowedImagesSettingsResult

- **AllowedImagesSettingsState** (Any  # complex shape): Returns enabled or audit-mode if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def enable_allowed_images_settings(store, request: dict) -> dict:
    """Enables Allowed AMIs for your account in the specified Amazon Web Services Region. Two values are accepted: enabled : The image criteria in your Allowed AMIs settings are applied. As a result, only AM"""
    allowed_images_settings_state = request.get("AllowedImagesSettingsState", "").strip() if isinstance(request.get("AllowedImagesSettingsState"), str) else request.get("AllowedImagesSettingsState")
    if not allowed_images_settings_state:
        raise ValidationException("AllowedImagesSettingsState is required")

    resource = store.enable_allowed_images_settingss(allowed_images_settings_state)
    if not resource:
        raise ResourceNotFoundException(f"Resource allowed_images_settings_state not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_allowed_images_settingss(allowed_images_settings_state, resource)
    return resource
```
