---
id: "@specs/aws/ec2/get_ipam_resource_cidrs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamResourceCidrs"
---

# GetIpamResourceCidrs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_resource_cidrs
> **spec:implements:** @kind:operation GetIpamResourceCidrs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamResourceCidrs.spec.md

Returns resource CIDRs managed by IPAM in a given scope. If an IPAM is associated with more than one resource discovery, the resource CIDRs across all of the resource discoveries is returned. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Input Shape: GetIpamResourceCidrsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters for the request. For more information about filtering, see Filtering CLI output . |
| IpamPoolId | Any  # complex shape |  | The ID of the IPAM pool that the resource is in. |
| IpamScopeId | Any  # complex shape | ✓ | The ID of the scope that the resource is in. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in the request. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| ResourceId | str |  | The ID of the resource. |
| ResourceOwner | str |  | The ID of the Amazon Web Services account that owns the resource. |
| ResourceTag | Any  # complex shape |  | The resource tag. |
| ResourceType | Any  # complex shape |  | The resource type. |

## Output Shape: GetIpamResourceCidrsResult

- **IpamResourceCidrs** (Any  # complex shape): The resource CIDRs.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_ipam_resource_cidrs(store, request: dict) -> dict:
    """Returns resource CIDRs managed by IPAM in a given scope. If an IPAM is associated with more than one resource discovery, the resource CIDRs across all of the resource discoveries is returned. A resour"""
    ipam_scope_id = request.get("IpamScopeId", "").strip() if isinstance(request.get("IpamScopeId"), str) else request.get("IpamScopeId")
    if not ipam_scope_id:
        raise ValidationException("IpamScopeId is required")

    resource = store.ipam_resource_cidrss(ipam_scope_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_scope_id not found")
    return {"IpamScopeId": ipam_scope_id, **resource}
```
