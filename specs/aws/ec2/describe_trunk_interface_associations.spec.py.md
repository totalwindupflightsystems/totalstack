---
id: "@specs/aws/ec2/describe_trunk_interface_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTrunkInterfaceAssociations"
---

# DescribeTrunkInterfaceAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_trunk_interface_associations
> **spec:implements:** @kind:operation DescribeTrunkInterfaceAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTrunkInterfaceAssociations.spec.md

Describes one or more network interface trunk associations.

## Input Shape: DescribeTrunkInterfaceAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationIds | list[Any  # complex shape] |  | The IDs of the associations. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. gre-key - The ID of a trunk interface association. interface-protocol - The interface protocol. Val |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: DescribeTrunkInterfaceAssociationsResult

- **InterfaceAssociations** (list[Any  # complex shape]): Information about the trunk associations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_trunk_interface_associations(store, request: dict) -> dict:
    """Describes one or more network interface trunk associations."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
