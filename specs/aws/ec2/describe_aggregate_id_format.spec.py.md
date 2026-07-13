---
id: "@specs/aws/ec2/describe_aggregate_id_format"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeAggregateIdFormat"
---

# DescribeAggregateIdFormat

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_aggregate_id_format
> **spec:implements:** @kind:operation DescribeAggregateIdFormat
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeAggregateIdFormat.spec.md

Describes the longer ID format settings for all resource types in a specific Region. This request is useful for performing a quick audit to determine whether a specific Region is fully opted in for longer IDs (17-character IDs). This request only returns information about resource types that support longer IDs. The following resource types support longer IDs: bundle | conversion-task | customer-gateway | dhcp-options | elastic-ip-allocation | elastic-ip-association | export-task | flow-log | image | import-task | instance | internet-gateway | network-acl | network-acl-association | network-interface | network-interface-attachment | prefix-list | reservation | route-table | route-table-association | security-group | snapshot | subnet | subnet-cidr-block-association | volume | vpc | vpc-cidr-block-association | vpc-endpoint | vpc-peering-connection | vpn-connection | vpn-gateway .

## Input Shape: DescribeAggregateIdFormatRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DescribeAggregateIdFormatResult

- **Statuses** (list[Any  # complex shape]): Information about each resource's ID format.
- **UseLongIdsAggregated** (bool): Indicates whether all resource types in the Region are configured to use longer IDs. This value is only true if all user

## Implementation

```speclang
def describe_aggregate_id_format(store, request: dict) -> dict:
    """Describes the longer ID format settings for all resource types in a specific Region. This request is useful for performing a quick audit to determine whether a specific Region is fully opted in for lo"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
