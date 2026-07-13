---
id: "@specs/aws/ec2/disassociate_ipam_resource_discovery"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateIpamResourceDiscovery"
---

# DisassociateIpamResourceDiscovery

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_ipam_resource_discovery
> **spec:implements:** @kind:operation DisassociateIpamResourceDiscovery
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateIpamResourceDiscovery.spec.md

Disassociates a resource discovery from an Amazon VPC IPAM. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Input Shape: DisassociateIpamResourceDiscoveryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamResourceDiscoveryAssociationId | Any  # complex shape | ✓ | A resource discovery association ID. |

## Output Shape: DisassociateIpamResourceDiscoveryResult

- **IpamResourceDiscoveryAssociation** (Any  # complex shape): A resource discovery association.

## Implementation

```speclang
def disassociate_ipam_resource_discovery(store, request: dict) -> dict:
    """Disassociates a resource discovery from an Amazon VPC IPAM. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account."""
    ipam_resource_discovery_association_id = request.get("IpamResourceDiscoveryAssociationId", "").strip() if isinstance(request.get("IpamResourceDiscoveryAssociationId"), str) else request.get("IpamResourceDiscoveryAssociationId")
    if not ipam_resource_discovery_association_id:
        raise ValidationException("IpamResourceDiscoveryAssociationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateIpamResourceDiscovery", request)
```
