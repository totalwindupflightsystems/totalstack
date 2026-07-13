---
id: "@specs/aws/ec2/describe_regions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeRegions"
---

# DescribeRegions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_regions
> **spec:implements:** @kind:operation DescribeRegions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeRegions.spec.md

Describes the Regions that are enabled for your account, or all Regions. For a list of the Regions supported by Amazon EC2, see Amazon EC2 service endpoints . For information about enabling and disabling Regions for your account, see Specify which Amazon Web Services Regions your account can use in the Amazon Web Services Account Management Reference Guide . The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeRegionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllRegions | bool |  | Indicates whether to display all Regions, including Regions that are disabled for your account. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. endpoint - The endpoint of the Region (for example, ec2.us-east-1.amazonaws.com ). opt-in-status - The opt- |
| RegionNames | list[str] |  | The names of the Regions. You can specify any Regions, whether they are enabled and disabled for your account. |

## Output Shape: DescribeRegionsResult

- **Regions** (list[Any  # complex shape]): Information about the Regions.

## Implementation

```speclang
def describe_regions(store, request: dict) -> dict:
    """Describes the Regions that are enabled for your account, or all Regions. For a list of the Regions supported by Amazon EC2, see Amazon EC2 service endpoints . For information about enabling and disabl"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
