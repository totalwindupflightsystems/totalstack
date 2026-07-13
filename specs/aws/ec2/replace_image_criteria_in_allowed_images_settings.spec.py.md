---
id: "@specs/aws/ec2/replace_image_criteria_in_allowed_images_settings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceImageCriteriaInAllowedImagesSettings"
---

# ReplaceImageCriteriaInAllowedImagesSettings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_image_criteria_in_allowed_images_settings
> **spec:implements:** @kind:operation ReplaceImageCriteriaInAllowedImagesSettings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceImageCriteriaInAllowedImagesSettings.spec.md

Sets or replaces the criteria for Allowed AMIs. The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will always be discoverable and usable by users in your account. For more information, see Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs in Amazon EC2 User Guide .

## Input Shape: ReplaceImageCriteriaInAllowedImagesSettingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageCriteria | list[Any  # complex shape] |  | The list of criteria that are evaluated to determine whether AMIs are discoverable and usable in the account in the spec |

## Output Shape: ReplaceImageCriteriaInAllowedImagesSettingsResult

- **ReturnValue** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def replace_image_criteria_in_allowed_images_settings(store, request: dict) -> dict:
    """Sets or replaces the criteria for Allowed AMIs. The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will alw"""

```
