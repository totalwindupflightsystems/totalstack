---
id: "@specs/aws/ec2/create_public_ipv4_pool"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreatePublicIpv4Pool"
---

# CreatePublicIpv4Pool

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_public_ipv4_pool
> **spec:implements:** @kind:operation CreatePublicIpv4Pool
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreatePublicIpv4Pool.spec.md

Creates a public IPv4 address pool. A public IPv4 pool is an EC2 IP address pool required for the public IPv4 CIDRs that you own and bring to Amazon Web Services to manage with IPAM. IPv6 addresses you bring to Amazon Web Services, however, use IPAM pools only. To monitor the status of pool creation, use DescribePublicIpv4Pools .

## Input Shape: CreatePublicIpv4PoolRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| NetworkBorderGroup | str |  | The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to  |
| TagSpecifications | list[Any  # complex shape] |  | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the |

## Output Shape: CreatePublicIpv4PoolResult

- **PoolId** (Any  # complex shape): The ID of the public IPv4 pool.

## Implementation

```speclang
def create_public_ipv4_pool(store, request: dict) -> dict:
    """Creates a public IPv4 address pool. A public IPv4 pool is an EC2 IP address pool required for the public IPv4 CIDRs that you own and bring to Amazon Web Services to manage with IPAM. IPv6 addresses yo"""


    record = {
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
        "NetworkBorderGroup": network_border_group,
    }

    store.public_ipv4_pools(record)

    return {
        "PoolId": record.get("PoolId", {}),
    }
```
