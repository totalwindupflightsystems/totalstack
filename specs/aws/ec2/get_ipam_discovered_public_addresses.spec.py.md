---
id: "@specs/aws/ec2/get_ipam_discovered_public_addresses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamDiscoveredPublicAddresses"
---

# GetIpamDiscoveredPublicAddresses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_discovered_public_addresses
> **spec:implements:** @kind:operation GetIpamDiscoveredPublicAddresses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamDiscoveredPublicAddresses.spec.md

Gets the public IP addresses that have been discovered by IPAM.

## Input Shape: GetIpamDiscoveredPublicAddressesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddressRegion | str | ✓ | The Amazon Web Services Region for the IP address. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | Filters. |
| IpamResourceDiscoveryId | Any  # complex shape | ✓ | An IPAM resource discovery ID. |
| MaxResults | Any  # complex shape |  | The maximum number of IPAM discovered public addresses to return in one page of results. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetIpamDiscoveredPublicAddressesResult

- **IpamDiscoveredPublicAddresses** (Any  # complex shape): IPAM discovered public addresses.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **OldestSampleTime** (Any  # complex shape): The oldest successful resource discovery time.

## Implementation

```speclang
def get_ipam_discovered_public_addresses(store, request: dict) -> dict:
    """Gets the public IP addresses that have been discovered by IPAM."""
    address_region = request.get("AddressRegion", "").strip() if isinstance(request.get("AddressRegion"), str) else request.get("AddressRegion")
    if not address_region:
        raise ValidationException("AddressRegion is required")
    ipam_resource_discovery_id = request.get("IpamResourceDiscoveryId", "").strip() if isinstance(request.get("IpamResourceDiscoveryId"), str) else request.get("IpamResourceDiscoveryId")
    if not ipam_resource_discovery_id:
        raise ValidationException("IpamResourceDiscoveryId is required")

    if store.ipam_discovered_public_addressess(ipam_resource_discovery_id):
        raise ResourceInUseException(f"Resource ipam_resource_discovery_id already exists")

    record = {
        "DryRun": dry_run,
        "IpamResourceDiscoveryId": ipam_resource_discovery_id,
        "AddressRegion": address_region,
        "Filters": filters,
        "NextToken": next_token,
        "MaxResults": max_results,
    }

    store.ipam_discovered_public_addressess(ipam_resource_discovery_id, record)

    return {
        "IpamDiscoveredPublicAddresses": record.get("IpamDiscoveredPublicAddresses", {}),
        "OldestSampleTime": record.get("OldestSampleTime", {}),
        "NextToken": record.get("NextToken", {}),
    }
```
