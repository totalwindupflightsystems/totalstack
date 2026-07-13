---
id: "@specs/aws/ec2/enable_snapshot_block_public_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableSnapshotBlockPublicAccess"
---

# EnableSnapshotBlockPublicAccess

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_snapshot_block_public_access
> **spec:implements:** @kind:operation EnableSnapshotBlockPublicAccess
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableSnapshotBlockPublicAccess.spec.md

Enables or modifies the block public access for snapshots setting at the account level for the specified Amazon Web Services Region. After you enable block public access for snapshots in a Region, users can no longer request public sharing for snapshots in that Region. Snapshots that are already publicly shared are either treated as private or they remain publicly shared, depending on the State that you specify. Enabling block public access for snapshots in block all sharing mode does not change the permissions for snapshots that are already publicly shared. Instead, it prevents these snapshots from be publicly visible and publicly accessible. Therefore, the attributes for these snapshots still indicate that they are publicly shared, even though they are not publicly available. If you later disable block public access or change the mode to block new sharing , these snapshots will become publicly available again. For more information, see Block public access for snapshots in the Amazon EBS User Guide .

## Input Shape: EnableSnapshotBlockPublicAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| State | Any  # complex shape | ✓ | The mode in which to enable block public access for snapshots for the Region. Specify one of the following values: block |

## Output Shape: EnableSnapshotBlockPublicAccessResult

- **State** (Any  # complex shape): The state of block public access for snapshots for the account and Region. Returns either block-all-sharing or block-new

## Implementation

```speclang
def enable_snapshot_block_public_access(store, request: dict) -> dict:
    """Enables or modifies the block public access for snapshots setting at the account level for the specified Amazon Web Services Region. After you enable block public access for snapshots in a Region, use"""
    state = request.get("State", "").strip() if isinstance(request.get("State"), str) else request.get("State")
    if not state:
        raise ValidationException("State is required")

    resource = store.enable_snapshot_block_public_accesss(state)
    if not resource:
        raise ResourceNotFoundException(f"Resource state not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_snapshot_block_public_accesss(state, resource)
    return resource
```
