---
id: "@specs/aws/ec2/associate_ipam_resource_discovery"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateIpamResourceDiscovery"
---

# AssociateIpamResourceDiscovery

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_ipam_resource_discovery
> **spec:implements:** @kind:operation AssociateIpamResourceDiscovery
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateIpamResourceDiscovery.spec.md

Associates an IPAM resource discovery with an Amazon VPC IPAM. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Input Shape: AssociateIpamResourceDiscoveryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A client token. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamId | Any  # complex shape | ✓ | An IPAM ID. |
| IpamResourceDiscoveryId | Any  # complex shape | ✓ | A resource discovery ID. |
| TagSpecifications | list[Any  # complex shape] |  | Tag specifications. |

## Output Shape: AssociateIpamResourceDiscoveryResult

- **IpamResourceDiscoveryAssociation** (Any  # complex shape): A resource discovery association. An associated resource discovery is a resource discovery that has been associated with

## Implementation

```speclang
def associate_ipam_resource_discovery(store, request: dict) -> dict:
    """Associates an IPAM resource discovery with an Amazon VPC IPAM. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account."""
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")
    ipam_resource_discovery_id = request.get("IpamResourceDiscoveryId", "").strip() if isinstance(request.get("IpamResourceDiscoveryId"), str) else request.get("IpamResourceDiscoveryId")
    if not ipam_resource_discovery_id:
        raise ValidationException("IpamResourceDiscoveryId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateIpamResourceDiscovery", request)
```
