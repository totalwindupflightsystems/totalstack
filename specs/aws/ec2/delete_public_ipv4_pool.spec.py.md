---
id: "@specs/aws/ec2/delete_public_ipv4_pool"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeletePublicIpv4Pool"
---

# DeletePublicIpv4Pool

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_public_ipv4_pool
> **spec:implements:** @kind:operation DeletePublicIpv4Pool
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeletePublicIpv4Pool.spec.md

Delete a public IPv4 pool. A public IPv4 pool is an EC2 IP address pool required for the public IPv4 CIDRs that you own and bring to Amazon Web Services to manage with IPAM. IPv6 addresses you bring to Amazon Web Services, however, use IPAM pools only.

## Input Shape: DeletePublicIpv4PoolRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| NetworkBorderGroup | str |  | The Availability Zone (AZ) or Local Zone (LZ) network border group that the resource that the IP address is assigned to  |
| PoolId | Any  # complex shape | ✓ | The ID of the public IPv4 pool you want to delete. |

## Output Shape: DeletePublicIpv4PoolResult

- **ReturnValue** (bool): Information about the result of deleting the public IPv4 pool.

## Implementation

```speclang
def delete_public_ipv4_pool(store, request: dict) -> dict:
    """Delete a public IPv4 pool. A public IPv4 pool is an EC2 IP address pool required for the public IPv4 CIDRs that you own and bring to Amazon Web Services to manage with IPAM. IPv6 addresses you bring t"""
    pool_id = request.get("PoolId", "").strip() if isinstance(request.get("PoolId"), str) else request.get("PoolId")

    if not store.public_ipv4_pools(pool_id):
        raise ResourceNotFoundException(f"Resource pool_id not found")
    store.delete_public_ipv4_pools(pool_id)
    return {}
```
