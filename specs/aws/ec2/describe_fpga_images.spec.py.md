---
id: "@specs/aws/ec2/describe_fpga_images"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFpgaImages"
---

# DescribeFpgaImages

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_fpga_images
> **spec:implements:** @kind:operation DescribeFpgaImages
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFpgaImages.spec.md

Describes the Amazon FPGA Images (AFIs) available to you. These include public AFIs, private AFIs that you own, and AFIs owned by other Amazon Web Services accounts for which you have load permissions.

## Input Shape: DescribeFpgaImagesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. create-time - The creation time of the AFI. fpga-image-id - The FPGA image identifier (AFI ID). fpga-image- |
| FpgaImageIds | list[Any  # complex shape] |  | The AFI IDs. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. |
| NextToken | Any  # complex shape |  | The token to retrieve the next page of results. |
| Owners | list[str] |  | Filters the AFI by owner. Specify an Amazon Web Services account ID, self (owner is the sender of the request), or an Am |

## Output Shape: DescribeFpgaImagesResult

- **FpgaImages** (list[Any  # complex shape]): Information about the FPGA images.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_fpga_images(store, request: dict) -> dict:
    """Describes the Amazon FPGA Images (AFIs) available to you. These include public AFIs, private AFIs that you own, and AFIs owned by other Amazon Web Services accounts for which you have load permissions"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
