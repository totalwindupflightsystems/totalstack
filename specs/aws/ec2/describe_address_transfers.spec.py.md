---
id: "@specs/aws/ec2/describe_address_transfers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeAddressTransfers"
---

# DescribeAddressTransfers

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_address_transfers
> **spec:implements:** @kind:operation DescribeAddressTransfers
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeAddressTransfers.spec.md

Describes an Elastic IP address transfer. For more information, see Transfer Elastic IP addresses in the Amazon VPC User Guide . When you transfer an Elastic IP address, there is a two-step handshake between the source and transfer Amazon Web Services accounts. When the source account starts the transfer, the transfer account has seven days to accept the Elastic IP address transfer. During those seven days, the source account can view the pending transfer by using this action. After seven days, the transfer expires and ownership of the Elastic IP address returns to the source account. Accepted transfers are visible to the source account for 14 days after the transfers have been accepted.

## Input Shape: DescribeAddressTransfersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationIds | list[Any  # complex shape] |  | The allocation IDs of Elastic IP addresses. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of address transfers to return in one page of results. |
| NextToken | str |  | Specify the pagination token from a previous request to retrieve the next page of results. |

## Output Shape: DescribeAddressTransfersResult

- **AddressTransfers** (list[Any  # complex shape]): The Elastic IP address transfer.
- **NextToken** (str): Specify the pagination token from a previous request to retrieve the next page of results.

## Implementation

```speclang
def describe_address_transfers(store, request: dict) -> dict:
    """Describes an Elastic IP address transfer. For more information, see Transfer Elastic IP addresses in the Amazon VPC User Guide . When you transfer an Elastic IP address, there is a two-step handshake """


    record = {
        "AllocationIds": allocation_ids,
        "NextToken": next_token,
        "MaxResults": max_results,
        "DryRun": dry_run,
    }

    store.address_transferss(record)

    return {
        "AddressTransfers": record.get("AddressTransfers", {}),
        "NextToken": record.get("NextToken", {}),
    }
```
