---
id: "@specs/aws/ec2/disable_allowed_images_settings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableAllowedImagesSettings"
---

# DisableAllowedImagesSettings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_allowed_images_settings
> **spec:implements:** @kind:operation DisableAllowedImagesSettings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableAllowedImagesSettings.spec.md

Disables Allowed AMIs for your account in the specified Amazon Web Services Region. When set to disabled , the image criteria in your Allowed AMIs settings do not apply, and no restrictions are placed on AMI discoverability or usage. Users in your account can launch instances using any public AMI or AMI shared with your account. The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will always be discoverable and usable by users in your account. For more information, see Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs in Amazon EC2 User Guide .

## Input Shape: DisableAllowedImagesSettingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisableAllowedImagesSettingsResult

- **AllowedImagesSettingsState** (Any  # complex shape): Returns disabled if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disable_allowed_images_settings(store, request: dict) -> dict:
    """Disables Allowed AMIs for your account in the specified Amazon Web Services Region. When set to disabled , the image criteria in your Allowed AMIs settings do not apply, and no restrictions are placed"""

```
