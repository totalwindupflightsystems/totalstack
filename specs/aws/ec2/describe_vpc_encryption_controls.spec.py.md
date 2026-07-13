---
id: "@specs/aws/ec2/describe_vpc_encryption_controls"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEncryptionControls"
---

# DescribeVpcEncryptionControls

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_encryption_controls
> **spec:implements:** @kind:operation DescribeVpcEncryptionControls
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEncryptionControls.spec.md

Describes one or more VPC Encryption Control configurations. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements You can filter the results to return information about specific encryption controls or VPCs. For more information, see Enforce VPC encryption in transit in the Amazon VPC User Guide .

## Input Shape: DescribeVpcEncryptionControlsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters to apply to the request. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VpcEncryptionControlIds | list[Any  # complex shape] |  | The IDs of the VPC Encryption Control configurations to describe. |
| VpcIds | list[Any  # complex shape] |  | The IDs of the VPCs to describe encryption control configurations for. |

## Output Shape: DescribeVpcEncryptionControlsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **VpcEncryptionControls** (list[Any  # complex shape]): Information about the VPC Encryption Control configurations.

## Implementation

```speclang
def describe_vpc_encryption_controls(store, request: dict) -> dict:
    """Describes one or more VPC Encryption Control configurations. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements Yo"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
