---
id: "@specs/aws/ec2/describe_iam_instance_profile_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIamInstanceProfileAssociations"
---

# DescribeIamInstanceProfileAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_iam_instance_profile_associations
> **spec:implements:** @kind:operation DescribeIamInstanceProfileAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIamInstanceProfileAssociations.spec.md

Describes your IAM instance profile associations.

## Input Shape: DescribeIamInstanceProfileAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationIds | list[Any  # complex shape] |  | The IAM instance profile associations. |
| Filters | list[Any  # complex shape] |  | The filters. instance-id - The ID of the instance. state - The state of the association ( associating | associated | dis |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeIamInstanceProfileAssociationsResult

- **IamInstanceProfileAssociations** (Any  # complex shape): Information about the IAM instance profile associations.
- **NextToken** (Any  # complex shape): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_iam_instance_profile_associations(store, request: dict) -> dict:
    """Describes your IAM instance profile associations."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
