---
id: "@specs/aws/ec2/get_managed_prefix_list_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetManagedPrefixListAssociations"
---

# GetManagedPrefixListAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_managed_prefix_list_associations
> **spec:implements:** @kind:operation GetManagedPrefixListAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetManagedPrefixListAssociations.spec.md

Gets information about the resources that are associated with the specified managed prefix list.

## Input Shape: GetManagedPrefixListAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| PrefixListId | Any  # complex shape | ✓ | The ID of the prefix list. |

## Output Shape: GetManagedPrefixListAssociationsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **PrefixListAssociations** (Any  # complex shape): Information about the associations.

## Implementation

```speclang
def get_managed_prefix_list_associations(store, request: dict) -> dict:
    """Gets information about the resources that are associated with the specified managed prefix list."""
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")
    if not prefix_list_id:
        raise ValidationException("PrefixListId is required")

    resource = store.managed_prefix_list_associationss(prefix_list_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource prefix_list_id not found")
    return {"PrefixListId": prefix_list_id, **resource}
```
