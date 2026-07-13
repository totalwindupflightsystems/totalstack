---
id: "@specs/aws/ec2/list_images_in_recycle_bin"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ListImagesInRecycleBin"
---

# ListImagesInRecycleBin

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/list_images_in_recycle_bin
> **spec:implements:** @kind:operation ListImagesInRecycleBin
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ListImagesInRecycleBin.spec.md

Lists one or more AMIs that are currently in the Recycle Bin. For more information, see Recycle Bin in the Amazon EC2 User Guide .

## Input Shape: ListImagesInRecycleBinRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageIds | list[Any  # complex shape] |  | The IDs of the AMIs to list. Omit this parameter to list all of the AMIs that are in the Recycle Bin. You can specify up |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: ListImagesInRecycleBinResult

- **Images** (list[Any  # complex shape]): Information about the AMIs.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def list_images_in_recycle_bin(store, request: dict) -> dict:
    """Lists one or more AMIs that are currently in the Recycle Bin. For more information, see Recycle Bin in the Amazon EC2 User Guide ."""

    items = store.list_images_in_recycle_bins()
    return {"Images": list(items.values())}
```
