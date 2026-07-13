---
id: "@specs/aws/ec2/describe_capacity_reservation_topology"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityReservationTopology"
---

# DescribeCapacityReservationTopology

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_reservation_topology
> **spec:implements:** @kind:operation DescribeCapacityReservationTopology
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityReservationTopology.spec.md

Describes a tree-based hierarchy that represents the physical host placement of your pending or active Capacity Reservations within an Availability Zone or Local Zone. You can use this information to determine the relative proximity of your capacity within the Amazon Web Services network before it is launched and use this information to allocate capacity together to support your tightly coupled workloads. Capacity Reservation topology is supported for specific instance types only. For more information, see Prerequisites for Amazon EC2 instance topology in the Amazon EC2 User Guide . The Amazon EC2 API follows an eventual consistency model due to the distributed nature of the system supporting it. As a result, when you call the DescribeCapacityReservationTopology API command immediately after launching instances, the response might return a null value for capacityBlockId because the data might not have fully propagated across all subsystems. For more information, see Eventual consistency in the Amazon EC2 API in the Amazon EC2 Developer Guide . For more information, see Amazon EC2 topology in the Amazon EC2 User Guide .

## Input Shape: DescribeCapacityReservationTopologyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationIds | Any  # complex shape |  | The Capacity Reservation IDs. Default: Describes all your Capacity Reservations. Constraints: Maximum 100 explicitly spe |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The name of the Availability Zone (for example, us-west-2a ) or Local Zone (for example |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeCapacityReservationTopologyResult

- **CapacityReservations** (Any  # complex shape): Information about the topology of each Capacity Reservation.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_capacity_reservation_topology(store, request: dict) -> dict:
    """Describes a tree-based hierarchy that represents the physical host placement of your pending or active Capacity Reservations within an Availability Zone or Local Zone. You can use this information to """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
