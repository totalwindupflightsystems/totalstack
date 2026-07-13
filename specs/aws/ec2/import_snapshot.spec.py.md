---
id: "@specs/aws/ec2/import_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ImportSnapshot"
---

# ImportSnapshot

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/import_snapshot
> **spec:implements:** @kind:operation ImportSnapshot
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ImportSnapshot.spec.md

Imports a disk into an EBS snapshot. For more information, see Importing a disk as a snapshot using VM Import/Export in the VM Import/Export User Guide .

## Input Shape: ImportSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientData | Any  # complex shape |  | The client-specific data. |
| ClientToken | str |  | Token to enable idempotency for VM import requests. |
| Description | str |  | The description string for the import snapshot task. |
| DiskContainer | Any  # complex shape |  | Information about the disk container. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Encrypted | bool |  | Specifies whether the destination snapshot of the imported image should be encrypted. The default KMS key for EBS is use |
| KmsKeyId | str |  | An identifier for the symmetric KMS key to use when creating the encrypted snapshot. This parameter is only required if  |
| RoleName | str |  | The name of the role to use when not using the default role, 'vmimport'. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the import snapshot task during creation. |

## Output Shape: ImportSnapshotResult

- **Description** (str): A description of the import snapshot task.
- **ImportTaskId** (str): The ID of the import snapshot task.
- **SnapshotTaskDetail** (Any  # complex shape): Information about the import snapshot task.
- **Tags** (list[Any  # complex shape]): Any tags assigned to the import snapshot task.

## Implementation

```speclang
def import_snapshot(store, request: dict) -> dict:
    """Imports a disk into an EBS snapshot. For more information, see Importing a disk as a snapshot using VM Import/Export in the VM Import/Export User Guide ."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ImportSnapshot", request)
```
