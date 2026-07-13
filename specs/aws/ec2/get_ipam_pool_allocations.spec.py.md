---
id: "@specs/aws/ec2/get_ipam_pool_allocations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamPoolAllocations"
---

# GetIpamPoolAllocations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_pool_allocations
> **spec:implements:** @kind:operation GetIpamPoolAllocations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamPoolAllocations.spec.md

Get a list of all the CIDR allocations in an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the Amazon Web Services Region where this IPAM pool is available for allocations. If you use this action after AllocateIpamPoolCidr or ReleaseIpamPoolAllocation , note that all EC2 API actions follow an eventual consistency model.

## Input Shape: GetIpamPoolAllocationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the request. For more information about filtering, see Filtering CLI output . |
| IpamPoolAllocationId | Any  # complex shape |  | The ID of the allocation. |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the IPAM pool you want to see the allocations for. |
| MaxResults | Any  # complex shape |  | The maximum number of results you would like returned per page. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetIpamPoolAllocationsResult

- **IpamPoolAllocations** (Any  # complex shape): The IPAM pool allocations you want information on.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_ipam_pool_allocations(store, request: dict) -> dict:
    """Get a list of all the CIDR allocations in an IPAM pool. The Region you use should be the IPAM pool locale. The locale is the Amazon Web Services Region where this IPAM pool is available for allocation"""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")

    resource = store.ipam_pool_allocationss(ipam_pool_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_pool_id not found")
    return {"IpamPoolId": ipam_pool_id, **resource}
```
