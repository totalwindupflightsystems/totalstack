---
id: "@specs/aws/ec2/describe_instance_type_offerings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceTypeOfferings"
---

# DescribeInstanceTypeOfferings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_type_offerings
> **spec:implements:** @kind:operation DescribeInstanceTypeOfferings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceTypeOfferings.spec.md

Lists the instance types that are offered for the specified location. If no location is specified, the default is to list the instance types that are offered in the current Region.

## Input Shape: DescribeInstanceTypeOfferingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. instance-type - The instance type. For a list of possib |
| LocationType | Any  # complex shape |  | The location type. availability-zone - The Availability Zone. When you specify a location filter, it must be an Availabi |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeInstanceTypeOfferingsResult

- **InstanceTypeOfferings** (list[Any  # complex shape]): The instance types offered in the location.
- **NextToken** (Any  # complex shape): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_instance_type_offerings(store, request: dict) -> dict:
    """Lists the instance types that are offered for the specified location. If no location is specified, the default is to list the instance types that are offered in the current Region."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
