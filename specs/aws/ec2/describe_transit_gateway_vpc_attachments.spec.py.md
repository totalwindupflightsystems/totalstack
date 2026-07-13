---
id: "@specs/aws/ec2/describe_transit_gateway_vpc_attachments"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTransitGatewayVpcAttachments"
---

# DescribeTransitGatewayVpcAttachments

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_transit_gateway_vpc_attachments
> **spec:implements:** @kind:operation DescribeTransitGatewayVpcAttachments
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTransitGatewayVpcAttachments.spec.md

Describes one or more VPC attachments. By default, all VPC attachments are described. Alternatively, you can filter the results.

## Input Shape: DescribeTransitGatewayVpcAttachmentsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: state - The state of the attachment. Valid values are available | deleted  |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayAttachmentIds | list[Any  # complex shape] |  | The IDs of the attachments. |

## Output Shape: DescribeTransitGatewayVpcAttachmentsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayVpcAttachments** (list[Any  # complex shape]): Information about the VPC attachments.

## Implementation

```speclang
def describe_transit_gateway_vpc_attachments(store, request: dict) -> dict:
    """Describes one or more VPC attachments. By default, all VPC attachments are described. Alternatively, you can filter the results."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
