---
id: "@specs/aws/ec2/get_allowed_images_settings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetAllowedImagesSettings"
---

# GetAllowedImagesSettings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_allowed_images_settings
> **spec:implements:** @kind:operation GetAllowedImagesSettings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetAllowedImagesSettings.spec.md

Gets the current state of the Allowed AMIs setting and the list of Allowed AMIs criteria at the account level in the specified Region. The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will always be discoverable and usable by users in your account. For more information, see Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs in Amazon EC2 User Guide .

## Input Shape: GetAllowedImagesSettingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetAllowedImagesSettingsResult

- **ImageCriteria** (list[Any  # complex shape]): The list of criteria for images that are discoverable and usable in the account in the specified Amazon Web Services Reg
- **ManagedBy** (Any  # complex shape): The entity that manages the Allowed AMIs settings. Possible values include: account - The Allowed AMIs settings is manag
- **State** (str): The current state of the Allowed AMIs setting at the account level in the specified Amazon Web Services Region. Possible

## Implementation

```speclang
def get_allowed_images_settings(store, request: dict) -> dict:
    """Gets the current state of the Allowed AMIs setting and the list of Allowed AMIs criteria at the account level in the specified Region. The Allowed AMIs feature does not restrict the AMIs owned by your"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
