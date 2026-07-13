---
id: "@specs/aws/ec2/describe_addresses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeAddresses"
---

# DescribeAddresses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_addresses
> **spec:implements:** @kind:operation DescribeAddresses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeAddresses.spec.md

Describes the specified Elastic IP addresses or all of your Elastic IP addresses.

## Input Shape: DescribeAddressesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationIds | list[Any  # complex shape] |  | Information about the allocation IDs. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. allocation-id - The allocation ID for the address. asso |
| PublicIps | list[str] |  | One or more Elastic IP addresses. Default: Describes all your Elastic IP addresses. |

## Output Shape: DescribeAddressesResult

- **Addresses** (list[Any  # complex shape]): Information about the Elastic IP addresses.

## Implementation

```speclang
def describe_addresses(store, request: dict) -> dict:
    """Describes the specified Elastic IP addresses or all of your Elastic IP addresses."""


    record = {
        "PublicIps": public_ips,
        "DryRun": dry_run,
        "Filters": filters,
        "AllocationIds": allocation_ids,
    }

    store.addressess(record)

    return {
        "Addresses": record.get("Addresses", {}),
    }
```
