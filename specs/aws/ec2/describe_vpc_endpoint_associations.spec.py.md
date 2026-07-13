---
id: "@specs/aws/ec2/describe_vpc_endpoint_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEndpointAssociations"
---

# DescribeVpcEndpointAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_endpoint_associations
> **spec:implements:** @kind:operation DescribeVpcEndpointAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEndpointAssociations.spec.md

Describes the VPC resources, VPC endpoint services, Amazon Lattice services, or service networks associated with the VPC endpoint.

## Input Shape: DescribeVpcEndpointAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. vpc-endpoint-id - The ID of the VPC endpoint. associated-resource-accessibility - The association state. Wh |
| MaxResults | Any  # complex shape |  | The maximum page size. |
| NextToken | str |  | The pagination token. |
| VpcEndpointIds | list[Any  # complex shape] |  | The IDs of the VPC endpoints. |

## Output Shape: DescribeVpcEndpointAssociationsResult

- **NextToken** (str): The pagination token.
- **VpcEndpointAssociations** (Any  # complex shape): Details of the endpoint associations.

## Implementation

```speclang
def describe_vpc_endpoint_associations(store, request: dict) -> dict:
    """Describes the VPC resources, VPC endpoint services, Amazon Lattice services, or service networks associated with the VPC endpoint."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
