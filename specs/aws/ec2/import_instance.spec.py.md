---
id: "@specs/aws/ec2/import_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ImportInstance"
---

# ImportInstance

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/import_instance
> **spec:implements:** @kind:operation ImportInstance
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ImportInstance.spec.md

We recommend that you use the ImportImage API instead. For more information, see Importing a VM as an image using VM Import/Export in the VM Import/Export User Guide . Creates an import instance task using metadata from the specified disk image. This API action supports only single-volume VMs. To import multi-volume VMs, use ImportImage instead. For information about the import manifest referenced by this API action, see VM Import Manifest . This API action is not supported by the Command Line Interface (CLI).

## Input Shape: ImportInstanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | A description for the instance being imported. |
| DiskImages | list[Any  # complex shape] |  | The disk image. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LaunchSpecification | Any  # complex shape |  | The launch specification. |
| Platform | Any  # complex shape | ✓ | The instance operating system. |

## Output Shape: ImportInstanceResult

- **ConversionTask** (Any  # complex shape): Information about the conversion task.

## Implementation

```speclang
def import_instance(store, request: dict) -> dict:
    """We recommend that you use the ImportImage API instead. For more information, see Importing a VM as an image using VM Import/Export in the VM Import/Export User Guide . Creates an import instance task """
    platform = request.get("Platform", "").strip() if isinstance(request.get("Platform"), str) else request.get("Platform")
    if not platform:
        raise ValidationException("Platform is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ImportInstance", request)
```
