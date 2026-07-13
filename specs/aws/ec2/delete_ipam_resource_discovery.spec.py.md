---
id: "@specs/aws/ec2/delete_ipam_resource_discovery"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteIpamResourceDiscovery"
---

# DeleteIpamResourceDiscovery

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_ipam_resource_discovery
> **spec:implements:** @kind:operation DeleteIpamResourceDiscovery
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteIpamResourceDiscovery.spec.md

Deletes an IPAM resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Input Shape: DeleteIpamResourceDiscoveryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamResourceDiscoveryId | Any  # complex shape | ✓ | The IPAM resource discovery ID. |

## Output Shape: DeleteIpamResourceDiscoveryResult

- **IpamResourceDiscovery** (Any  # complex shape): The IPAM resource discovery.

## Implementation

```speclang
def delete_ipam_resource_discovery(store, request: dict) -> dict:
    """Deletes an IPAM resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account."""
    ipam_resource_discovery_id = request.get("IpamResourceDiscoveryId", "").strip() if isinstance(request.get("IpamResourceDiscoveryId"), str) else request.get("IpamResourceDiscoveryId")

    if not store.ipam_resource_discoverys(ipam_resource_discovery_id):
        raise ResourceNotFoundException(f"Resource ipam_resource_discovery_id not found")
    store.delete_ipam_resource_discoverys(ipam_resource_discovery_id)
    return {}
```
