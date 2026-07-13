---
id: "@specs/aws/ec2/describe_addresses_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeAddressesAttribute"
---

# DescribeAddressesAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_addresses_attribute
> **spec:implements:** @kind:operation DescribeAddressesAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeAddressesAttribute.spec.md

Describes the attributes of the specified Elastic IP addresses. For requirements, see Using reverse DNS for email applications .

## Input Shape: DescribeAddressesAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationIds | Any  # complex shape |  | [EC2-VPC] The allocation IDs. |
| Attribute | Any  # complex shape |  | The attribute of the IP address. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeAddressesAttributeResult

- **Addresses** (Any  # complex shape): Information about the IP addresses.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_addresses_attribute(store, request: dict) -> dict:
    """Describes the attributes of the specified Elastic IP addresses. For requirements, see Using reverse DNS for email applications ."""


    record = {
        "AllocationIds": allocation_ids,
        "Attribute": attribute,
        "NextToken": next_token,
        "MaxResults": max_results,
        "DryRun": dry_run,
    }

    store.addresses_attributes(record)

    return {
        "Addresses": record.get("Addresses", {}),
        "NextToken": record.get("NextToken", {}),
    }
```
