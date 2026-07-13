---
id: "@specs/aws/ec2/delete_ipam"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteIpam"
---

# DeleteIpam

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_ipam
> **spec:implements:** @kind:operation DeleteIpam
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteIpam.spec.md

Delete an IPAM. Deleting an IPAM removes all monitored data associated with the IPAM including the historical data for CIDRs. For more information, see Delete an IPAM in the Amazon VPC IPAM User Guide .

## Input Shape: DeleteIpamRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cascade | bool |  | Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in priv |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamId | Any  # complex shape | ✓ | The ID of the IPAM to delete. |

## Output Shape: DeleteIpamResult

- **Ipam** (Any  # complex shape): Information about the results of the deletion.

## Implementation

```speclang
def delete_ipam(store, request: dict) -> dict:
    """Delete an IPAM. Deleting an IPAM removes all monitored data associated with the IPAM including the historical data for CIDRs. For more information, see Delete an IPAM in the Amazon VPC IPAM User Guide"""
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")

    if not store.ipams(ipam_id):
        raise ResourceNotFoundException(f"Resource ipam_id not found")
    store.delete_ipams(ipam_id)
    return {}
```
