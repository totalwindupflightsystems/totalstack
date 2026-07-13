---
id: "@specs/aws/ec2/create_ipam_resource_discovery"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpamResourceDiscovery"
---

# CreateIpamResourceDiscovery

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam_resource_discovery
> **spec:implements:** @kind:operation CreateIpamResourceDiscovery
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpamResourceDiscovery.spec.md

Creates an IPAM resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Input Shape: CreateIpamResourceDiscoveryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A client token for the IPAM resource discovery. |
| Description | str |  | A description for the IPAM resource discovery. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| OperatingRegions | Any  # complex shape |  | Operating Regions for the IPAM resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is a |
| TagSpecifications | list[Any  # complex shape] |  | Tag specifications for the IPAM resource discovery. |

## Output Shape: CreateIpamResourceDiscoveryResult

- **IpamResourceDiscovery** (Any  # complex shape): An IPAM resource discovery.

## Implementation

```speclang
def create_ipam_resource_discovery(store, request: dict) -> dict:
    """Creates an IPAM resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account."""


    record = {
        "DryRun": dry_run,
        "Description": description,
        "OperatingRegions": operating_regions,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
    }

    store.ipam_resource_discoverys(record)

    return {
        "IpamResourceDiscovery": record.get("IpamResourceDiscovery", {}),
    }
```
