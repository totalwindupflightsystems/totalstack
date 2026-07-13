---
id: "@specs/aws/ec2/get_image_ancestry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetImageAncestry"
---

# GetImageAncestry

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_image_ancestry
> **spec:implements:** @kind:operation GetImageAncestry
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetImageAncestry.spec.md

Retrieves the ancestry chain of the specified AMI, tracing its lineage back to the root AMI. For more information, see AMI ancestry in Amazon EC2 User Guide .

## Input Shape: GetImageAncestryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI whose ancestry you want to trace. |

## Output Shape: GetImageAncestryResult

- **ImageAncestryEntries** (list[Any  # complex shape]): A list of entries in the AMI ancestry chain, from the specified AMI to the root AMI.

## Implementation

```speclang
def get_image_ancestry(store, request: dict) -> dict:
    """Retrieves the ancestry chain of the specified AMI, tracing its lineage back to the root AMI. For more information, see AMI ancestry in Amazon EC2 User Guide ."""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.image_ancestrys(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")
    return {"ImageId": image_id, **resource}
```
