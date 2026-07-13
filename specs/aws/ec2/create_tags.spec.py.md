---
id: "@specs/aws/ec2/create_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTags"
---

# CreateTags

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_tags
> **spec:implements:** @kind:operation CreateTags
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTags.spec.md

Adds or overwrites only the specified tags for the specified Amazon EC2 resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique per resource. For more information about tags, see Tag your Amazon EC2 resources in the Amazon Elastic Compute Cloud User Guide . For more information about creating IAM policies that control users' access to resources based on tags, see Supported resource-level permissions for Amazon EC2 API actions in the Amazon Elastic Compute Cloud User Guide .

## Input Shape: CreateTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Resources | list[Any  # complex shape] | ✓ | The IDs of the resources, separated by spaces. Constraints: Up to 1000 resource IDs. We recommend breaking up this reque |
| Tags | list[Any  # complex shape] | ✓ | The tags. The value parameter is required, but if you don't want the tag to have a value, specify the parameter with no  |

## Implementation

```speclang
def create_tags(store, request: dict) -> dict:
    """Adds or overwrites only the specified tags for the specified Amazon EC2 resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have"""
    resources = request.get("Resources", "").strip() if isinstance(request.get("Resources"), str) else request.get("Resources")
    if not resources:
        raise ValidationException("Resources is required")
    tags = request.get("Tags", "").strip() if isinstance(request.get("Tags"), str) else request.get("Tags")
    if not tags:
        raise ValidationException("Tags is required")

    if store.tagss(resources):
        raise ResourceInUseException(f"Resource resources already exists")

    record = {
        "DryRun": dry_run,
        "Resources": resources,
        "Tags": tags,
    }

    store.tagss(resources, record)

    return {
    }
```
