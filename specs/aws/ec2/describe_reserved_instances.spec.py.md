---
id: "@specs/aws/ec2/describe_reserved_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeReservedInstances"
---

# DescribeReservedInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_reserved_instances
> **spec:implements:** @kind:operation DescribeReservedInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeReservedInstances.spec.md

Describes one or more of the Reserved Instances that you purchased. For more information about Reserved Instances, see Reserved Instances in the Amazon EC2 User Guide . The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeReservedInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. availability-zone - The Availability Zone where the Reserved Instance can be used. availability-zon |
| OfferingClass | Any  # complex shape |  | Describes whether the Reserved Instance is Standard or Convertible. |
| OfferingType | Any  # complex shape |  | The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have acces |
| ReservedInstancesIds | list[Any  # complex shape] |  | One or more Reserved Instance IDs. Default: Describes all your Reserved Instances, or only those otherwise specified. |

## Output Shape: DescribeReservedInstancesResult

- **ReservedInstances** (list[Any  # complex shape]): A list of Reserved Instances.

## Implementation

```speclang
def describe_reserved_instances(store, request: dict) -> dict:
    """Describes one or more of the Reserved Instances that you purchased. For more information about Reserved Instances, see Reserved Instances in the Amazon EC2 User Guide . The order of the elements in th"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
