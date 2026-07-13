---
id: "@specs/aws/ec2/disable_snapshot_block_public_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableSnapshotBlockPublicAccess"
---

# DisableSnapshotBlockPublicAccess

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_snapshot_block_public_access
> **spec:implements:** @kind:operation DisableSnapshotBlockPublicAccess
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableSnapshotBlockPublicAccess.spec.md

Disables the block public access for snapshots setting at the account level for the specified Amazon Web Services Region. After you disable block public access for snapshots in a Region, users can publicly share snapshots in that Region. Enabling block public access for snapshots in block-all-sharing mode does not change the permissions for snapshots that are already publicly shared. Instead, it prevents these snapshots from be publicly visible and publicly accessible. Therefore, the attributes for these snapshots still indicate that they are publicly shared, even though they are not publicly available. If you disable block public access , these snapshots will become publicly available again. For more information, see Block public access for snapshots in the Amazon EBS User Guide .

## Input Shape: DisableSnapshotBlockPublicAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisableSnapshotBlockPublicAccessResult

- **State** (Any  # complex shape): Returns unblocked if the request succeeds.

## Implementation

```speclang
def disable_snapshot_block_public_access(store, request: dict) -> dict:
    """Disables the block public access for snapshots setting at the account level for the specified Amazon Web Services Region. After you disable block public access for snapshots in a Region, users can pub"""

```
