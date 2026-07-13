---
id: "@specs/aws/ec2/describe_moving_addresses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeMovingAddresses"
---

# DescribeMovingAddresses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_moving_addresses
> **spec:implements:** @kind:operation DescribeMovingAddresses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeMovingAddresses.spec.md

This action is deprecated. Describes your Elastic IP addresses that are being moved from or being restored to the EC2-Classic platform. This request does not return information about any other Elastic IP addresses in your account.

## Input Shape: DescribeMovingAddressesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. moving-status - The status of the Elastic IP address ( MovingToVpc | RestoringToClassic ). |
| MaxResults | Any  # complex shape |  | The maximum number of results to return for the request in a single page. The remaining results of the initial request c |
| NextToken | str |  | The token for the next page of results. |
| PublicIps | list[str] |  | One or more Elastic IP addresses. |

## Output Shape: DescribeMovingAddressesResult

- **MovingAddressStatuses** (Any  # complex shape): The status for each Elastic IP address.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_moving_addresses(store, request: dict) -> dict:
    """This action is deprecated. Describes your Elastic IP addresses that are being moved from or being restored to the EC2-Classic platform. This request does not return information about any other Elastic"""


    record = {
        "DryRun": dry_run,
        "PublicIps": public_ips,
        "NextToken": next_token,
        "Filters": filters,
        "MaxResults": max_results,
    }

    store.moving_addressess(record)

    return {
        "MovingAddressStatuses": record.get("MovingAddressStatuses", {}),
        "NextToken": record.get("NextToken", {}),
    }
```
