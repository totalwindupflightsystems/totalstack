---
id: "@specs/aws/ec2/describe_instance_types"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceTypes"
---

# DescribeInstanceTypes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_types
> **spec:implements:** @kind:operation DescribeInstanceTypes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceTypes.spec.md

Describes the specified instance types. By default, all instance types for the current Region are described. Alternatively, you can filter the results.

## Input Shape: DescribeInstanceTypesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. auto-recovery-supported - Indicates whether Amazon Clou |
| InstanceTypes | list[Any  # complex shape] |  | The instance types. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeInstanceTypesResult

- **InstanceTypes** (list[Any  # complex shape]): The instance type.
- **NextToken** (Any  # complex shape): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_instance_types(store, request: dict) -> dict:
    """Describes the specified instance types. By default, all instance types for the current Region are described. Alternatively, you can filter the results."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
