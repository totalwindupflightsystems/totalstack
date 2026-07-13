---
id: "@specs/aws/ec2/delete_capacity_manager_data_export"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteCapacityManagerDataExport"
---

# DeleteCapacityManagerDataExport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_capacity_manager_data_export
> **spec:implements:** @kind:operation DeleteCapacityManagerDataExport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteCapacityManagerDataExport.spec.md

Deletes an existing Capacity Manager data export configuration. This stops future scheduled exports but does not delete previously exported files from S3.

## Input Shape: DeleteCapacityManagerDataExportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityManagerDataExportId | Any  # complex shape | ✓ | The unique identifier of the data export configuration to delete. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DeleteCapacityManagerDataExportResult

- **CapacityManagerDataExportId** (Any  # complex shape): The unique identifier of the deleted data export configuration.

## Implementation

```speclang
def delete_capacity_manager_data_export(store, request: dict) -> dict:
    """Deletes an existing Capacity Manager data export configuration. This stops future scheduled exports but does not delete previously exported files from S3."""
    capacity_manager_data_export_id = request.get("CapacityManagerDataExportId", "").strip() if isinstance(request.get("CapacityManagerDataExportId"), str) else request.get("CapacityManagerDataExportId")

    if not store.capacity_manager_data_exports(capacity_manager_data_export_id):
        raise ResourceNotFoundException(f"Resource capacity_manager_data_export_id not found")
    store.delete_capacity_manager_data_exports(capacity_manager_data_export_id)
    return {}
```
