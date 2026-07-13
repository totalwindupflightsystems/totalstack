---
id: "@specs/aws/ec2/describe_image_references"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeImageReferences"
---

# DescribeImageReferences

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_image_references
> **spec:implements:** @kind:operation DescribeImageReferences
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeImageReferences.spec.md

Describes your Amazon Web Services resources that are referencing the specified images. For more information, see Identify your resources referencing specified AMIs in the Amazon EC2 User Guide .

## Input Shape: DescribeImageReferencesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageIds | list[Any  # complex shape] | ✓ | The IDs of the images to check for resource references. |
| IncludeAllResourceTypes | bool |  | Specifies whether to check all supported Amazon Web Services resource types for image references. When specified, defaul |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| ResourceTypes | list[Any  # complex shape] |  | The Amazon Web Services resource types to check for image references. Either IncludeAllResourceTypes or ResourceTypes mu |

## Output Shape: DescribeImageReferencesResult

- **ImageReferences** (list[Any  # complex shape]): The resources that are referencing the specified images.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_image_references(store, request: dict) -> dict:
    """Describes your Amazon Web Services resources that are referencing the specified images. For more information, see Identify your resources referencing specified AMIs in the Amazon EC2 User Guide ."""
    image_ids = request.get("ImageIds", "").strip() if isinstance(request.get("ImageIds"), str) else request.get("ImageIds")
    if not image_ids:
        raise ValidationException("ImageIds is required")

    resource = store.image_referencess(image_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_ids not found")
    return {"ImageIds": image_ids, **resource}
```
