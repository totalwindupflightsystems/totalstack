---
id: "@specs/aws/ec2/get_snapshot_block_public_access_state"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetSnapshotBlockPublicAccessState"
---

# GetSnapshotBlockPublicAccessState

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_snapshot_block_public_access_state
> **spec:implements:** @kind:operation GetSnapshotBlockPublicAccessState
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetSnapshotBlockPublicAccessState.spec.md

Gets the current state of block public access for snapshots setting for the account and Region. For more information, see Block public access for snapshots in the Amazon EBS User Guide .

## Input Shape: GetSnapshotBlockPublicAccessStateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetSnapshotBlockPublicAccessStateResult

- **ManagedBy** (Any  # complex shape): The entity that manages the state for block public access for snapshots. Possible values include: account - The state is
- **State** (Any  # complex shape): The current state of block public access for snapshots. Possible values include: block-all-sharing - All public sharing 

## Implementation

```speclang
def get_snapshot_block_public_access_state(store, request: dict) -> dict:
    """Gets the current state of block public access for snapshots setting for the account and Region. For more information, see Block public access for snapshots in the Amazon EBS User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
