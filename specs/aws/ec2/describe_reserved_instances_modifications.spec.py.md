---
id: "@specs/aws/ec2/describe_reserved_instances_modifications"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeReservedInstancesModifications"
---

# DescribeReservedInstancesModifications

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_reserved_instances_modifications
> **spec:implements:** @kind:operation DescribeReservedInstancesModifications
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeReservedInstancesModifications.spec.md

Describes the modifications made to your Reserved Instances. If no parameter is specified, information about all your Reserved Instances modification requests is returned. If a modification ID is specified, only information about the specific modification is returned. For more information, see Modify Reserved Instances in the Amazon EC2 User Guide . The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeReservedInstancesModificationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filters | list[Any  # complex shape] |  | One or more filters. client-token - The idempotency token for the modification request. create-date - The time when the  |
| NextToken | str |  | The token to retrieve the next page of results. |
| ReservedInstancesModificationIds | list[Any  # complex shape] |  | IDs for the submitted modification request. |

## Output Shape: DescribeReservedInstancesModificationsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **ReservedInstancesModifications** (list[Any  # complex shape]): The Reserved Instance modification information.

## Implementation

```speclang
def describe_reserved_instances_modifications(store, request: dict) -> dict:
    """Describes the modifications made to your Reserved Instances. If no parameter is specified, information about all your Reserved Instances modification requests is returned. If a modification ID is spec"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
