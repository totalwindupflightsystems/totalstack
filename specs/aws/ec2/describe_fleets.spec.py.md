---
id: "@specs/aws/ec2/describe_fleets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFleets"
---

# DescribeFleets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_fleets
> **spec:implements:** @kind:operation DescribeFleets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFleets.spec.md

Describes the specified EC2 Fleet or all of your EC2 Fleets. If a fleet is of type instant , you must specify the fleet ID in the request, otherwise the fleet does not appear in the response. For more information, see Describe your EC2 Fleet in the Amazon EC2 User Guide .

## Input Shape: DescribeFleetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. activity-status - The progress of the EC2 Fleet ( error | pending-fulfillment | pending-termination | fulfi |
| FleetIds | Any  # complex shape |  | The IDs of the EC2 Fleets. If a fleet is of type instant , you must specify the fleet ID, otherwise it does not appear i |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeFleetsResult

- **Fleets** (Any  # complex shape): Information about the EC2 Fleets.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_fleets(store, request: dict) -> dict:
    """Describes the specified EC2 Fleet or all of your EC2 Fleets. If a fleet is of type instant , you must specify the fleet ID in the request, otherwise the fleet does not appear in the response. For more"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
