---
id: "@specs/aws/ec2/delete_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTags"
---

# DeleteTags

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_tags
> **spec:implements:** @kind:operation DeleteTags
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTags.spec.md

Deletes the specified set of tags from the specified set of resources. To list the current tags, use DescribeTags . For more information about tags, see Tag your Amazon EC2 resources in the Amazon Elastic Compute Cloud User Guide .

## Input Shape: DeleteTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Resources | list[Any  # complex shape] | ✓ | The IDs of the resources, separated by spaces. Constraints: Up to 1000 resource IDs. We recommend breaking up this reque |
| Tags | list[Any  # complex shape] |  | The tags to delete. Specify a tag key and an optional tag value to delete specific tags. If you specify a tag key withou |

## Implementation

```speclang
def delete_tags(store, request: dict) -> dict:
    """Deletes the specified set of tags from the specified set of resources. To list the current tags, use DescribeTags . For more information about tags, see Tag your Amazon EC2 resources in the Amazon Ela"""
    resources = request.get("Resources", "").strip() if isinstance(request.get("Resources"), str) else request.get("Resources")

    if not store.tagss(resources):
        raise ResourceNotFoundException(f"Resource resources not found")
    store.delete_tagss(resources)
    return {}
```
