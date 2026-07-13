---
id: "@specs/aws/ec2/get_ipam_discovered_accounts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamDiscoveredAccounts"
---

# GetIpamDiscoveredAccounts

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_discovered_accounts
> **spec:implements:** @kind:operation GetIpamDiscoveredAccounts
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamDiscoveredAccounts.spec.md

Gets IPAM discovered accounts. A discovered account is an Amazon Web Services account that is monitored under a resource discovery. If you have integrated IPAM with Amazon Web Services Organizations, all accounts in the organization are discovered accounts. Only the IPAM account can get all discovered accounts in the organization.

## Input Shape: GetIpamDiscoveredAccountsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DiscoveryRegion | str | ✓ | The Amazon Web Services Region that the account information is returned from. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | Discovered account filters. |
| IpamResourceDiscoveryId | Any  # complex shape | ✓ | A resource discovery ID. |
| MaxResults | Any  # complex shape |  | The maximum number of discovered accounts to return in one page of results. |
| NextToken | Any  # complex shape |  | Specify the pagination token from a previous request to retrieve the next page of results. |

## Output Shape: GetIpamDiscoveredAccountsResult

- **IpamDiscoveredAccounts** (Any  # complex shape): Discovered accounts.
- **NextToken** (Any  # complex shape): Specify the pagination token from a previous request to retrieve the next page of results.

## Implementation

```speclang
def get_ipam_discovered_accounts(store, request: dict) -> dict:
    """Gets IPAM discovered accounts. A discovered account is an Amazon Web Services account that is monitored under a resource discovery. If you have integrated IPAM with Amazon Web Services Organizations, """
    discovery_region = request.get("DiscoveryRegion", "").strip() if isinstance(request.get("DiscoveryRegion"), str) else request.get("DiscoveryRegion")
    if not discovery_region:
        raise ValidationException("DiscoveryRegion is required")
    ipam_resource_discovery_id = request.get("IpamResourceDiscoveryId", "").strip() if isinstance(request.get("IpamResourceDiscoveryId"), str) else request.get("IpamResourceDiscoveryId")
    if not ipam_resource_discovery_id:
        raise ValidationException("IpamResourceDiscoveryId is required")

    resource = store.ipam_discovered_accountss(ipam_resource_discovery_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_resource_discovery_id not found")
    return {"IpamResourceDiscoveryId": ipam_resource_discovery_id, **resource}
```
