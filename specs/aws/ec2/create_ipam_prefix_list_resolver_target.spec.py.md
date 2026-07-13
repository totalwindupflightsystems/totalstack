---
id: "@specs/aws/ec2/create_ipam_prefix_list_resolver_target"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpamPrefixListResolverTarget"
---

# CreateIpamPrefixListResolverTarget

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam_prefix_list_resolver_target
> **spec:implements:** @kind:operation CreateIpamPrefixListResolverTarget
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpamPrefixListResolverTarget.spec.md

Creates an IPAM prefix list resolver target. An IPAM prefix list resolver target is an association between a specific customer-managed prefix list and an IPAM prefix list resolver. The target enables the resolver to synchronize CIDRs selected by its rules into the specified prefix list, which can then be referenced in Amazon Web Services resources. For more information about IPAM prefix list resolver, see Automate prefix list updates with IPAM in the Amazon VPC IPAM User Guide .

## Input Shape: CreateIpamPrefixListResolverTargetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| DesiredVersion | Any  # complex shape |  | The specific version of the prefix list to target. If not specified, the resolver will target the latest version. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPrefixListResolverId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver that will manage the synchronization of CIDRs to the target prefix list. |
| PrefixListId | str | ✓ | The ID of the managed prefix list that will be synchronized with CIDRs selected by the IPAM prefix list resolver. This p |
| PrefixListRegion | str | ✓ | The Amazon Web Services Region where the prefix list is located. This is required when referencing a prefix list in a di |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the IPAM prefix list resolver target during creation. Tags help you organize and manage your Amazon |
| TrackLatestVersion | bool | ✓ | Indicates whether the resolver target should automatically track the latest version of the prefix list. When enabled, th |

## Output Shape: CreateIpamPrefixListResolverTargetResult

- **IpamPrefixListResolverTarget** (Any  # complex shape): Information about the IPAM prefix list resolver target that was created.

## Implementation

```speclang
def create_ipam_prefix_list_resolver_target(store, request: dict) -> dict:
    """Creates an IPAM prefix list resolver target. An IPAM prefix list resolver target is an association between a specific customer-managed prefix list and an IPAM prefix list resolver. The target enables """
    ipam_prefix_list_resolver_id = request.get("IpamPrefixListResolverId", "").strip() if isinstance(request.get("IpamPrefixListResolverId"), str) else request.get("IpamPrefixListResolverId")
    if not ipam_prefix_list_resolver_id:
        raise ValidationException("IpamPrefixListResolverId is required")
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")
    if not prefix_list_id:
        raise ValidationException("PrefixListId is required")
    prefix_list_region = request.get("PrefixListRegion", "").strip() if isinstance(request.get("PrefixListRegion"), str) else request.get("PrefixListRegion")
    if not prefix_list_region:
        raise ValidationException("PrefixListRegion is required")
    track_latest_version = request.get("TrackLatestVersion", "").strip() if isinstance(request.get("TrackLatestVersion"), str) else request.get("TrackLatestVersion")
    if not track_latest_version:
        raise ValidationException("TrackLatestVersion is required")

    if store.ipam_prefix_list_resolver_targets(prefix_list_id):
        raise ResourceInUseException(f"Resource prefix_list_id already exists")

    record = {
        "DryRun": dry_run,
        "IpamPrefixListResolverId": ipam_prefix_list_resolver_id,
        "PrefixListId": prefix_list_id,
        "PrefixListRegion": prefix_list_region,
        "DesiredVersion": desired_version,
        "TrackLatestVersion": track_latest_version,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
    }

    store.ipam_prefix_list_resolver_targets(prefix_list_id, record)

    return {
        "IpamPrefixListResolverTarget": record.get("IpamPrefixListResolverTarget", {}),
    }
```
