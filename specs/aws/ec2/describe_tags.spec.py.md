---
id: "@specs/aws/ec2/describe_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTags"
---

# DescribeTags

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_tags
> **spec:implements:** @kind:operation DescribeTags
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTags.spec.md

Describes the specified tags for your EC2 resources. For more information about tags, see Tag your Amazon EC2 resources in the Amazon Elastic Compute Cloud User Guide . We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. key - The tag key. resource-id - The ID of the resource. resource-type - The resource type. For a list of p |
| MaxResults | int |  | The maximum number of items to return for this request. This value can be between 5 and 1000. To get the next page of it |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeTagsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Tags** (list[Any  # complex shape]): The tags.

## Implementation

```speclang
def describe_tags(store, request: dict) -> dict:
    """Describes the specified tags for your EC2 resources. For more information about tags, see Tag your Amazon EC2 resources in the Amazon Elastic Compute Cloud User Guide . We strongly recommend using onl"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
