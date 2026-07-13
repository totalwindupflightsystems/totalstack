---
id: "@specs/aws/ec2/describe_fast_launch_images"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFastLaunchImages"
---

# DescribeFastLaunchImages

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_fast_launch_images
> **spec:implements:** @kind:operation DescribeFastLaunchImages
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFastLaunchImages.spec.md

Describe details for Windows AMIs that are configured for Windows fast launch.

## Input Shape: DescribeFastLaunchImagesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | Use the following filters to streamline results. resource-type - The resource type for pre-provisioning. owner-id - The  |
| ImageIds | list[Any  # complex shape] |  | Specify one or more Windows AMI image IDs for the request. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeFastLaunchImagesResult

- **FastLaunchImages** (Any  # complex shape): A collection of details about the fast-launch enabled Windows images that meet the requested criteria.
- **NextToken** (Any  # complex shape): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_fast_launch_images(store, request: dict) -> dict:
    """Describe details for Windows AMIs that are configured for Windows fast launch."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
