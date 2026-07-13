---
id: "@specs/aws/ec2/describe_fleet_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFleetInstances"
---

# DescribeFleetInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_fleet_instances
> **spec:implements:** @kind:operation DescribeFleetInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFleetInstances.spec.md

Describes the running instances for the specified EC2 Fleet. Currently, DescribeFleetInstances does not support fleets of type instant . Instead, use DescribeFleets , specifying the instant fleet ID in the request. For more information, see Describe your EC2 Fleet in the Amazon EC2 User Guide .

## Input Shape: DescribeFleetInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. instance-type - The instance type. |
| FleetId | Any  # complex shape | ✓ | The ID of the EC2 Fleet. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeFleetInstancesResult

- **ActiveInstances** (Any  # complex shape): The running instances. This list is refreshed periodically and might be out of date.
- **FleetId** (Any  # complex shape): The ID of the EC2 Fleet.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_fleet_instances(store, request: dict) -> dict:
    """Describes the running instances for the specified EC2 Fleet. Currently, DescribeFleetInstances does not support fleets of type instant . Instead, use DescribeFleets , specifying the instant fleet ID i"""
    fleet_id = request.get("FleetId", "").strip() if isinstance(request.get("FleetId"), str) else request.get("FleetId")
    if not fleet_id:
        raise ValidationException("FleetId is required")

    resource = store.fleet_instancess(fleet_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource fleet_id not found")
    return {"FleetId": fleet_id, **resource}
```
