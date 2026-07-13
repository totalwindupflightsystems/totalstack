---
id: "@specs/aws/ec2/create_capacity_manager_data_export"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCapacityManagerDataExport"
---

# CreateCapacityManagerDataExport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_capacity_manager_data_export
> **spec:implements:** @kind:operation CreateCapacityManagerDataExport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCapacityManagerDataExport.spec.md

Creates a new data export configuration for EC2 Capacity Manager. This allows you to automatically export capacity usage data to an S3 bucket on a scheduled basis. The exported data includes metrics for On-Demand, Spot, and Capacity Reservations usage across your organization.

## Input Shape: CreateCapacityManagerDataExportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| OutputFormat | Any  # complex shape | ✓ | The file format for the exported data. Parquet format is recommended for large datasets and better compression. |
| S3BucketName | str | ✓ | The name of the S3 bucket where the capacity data export files will be delivered. The bucket must exist and you must hav |
| S3BucketPrefix | str |  | The S3 key prefix for the exported data files. This allows you to organize exports in a specific folder structure within |
| Schedule | Any  # complex shape | ✓ | The frequency at which data exports are generated. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the data export configuration. You can tag the export for organization and cost tracking purposes. |

## Output Shape: CreateCapacityManagerDataExportResult

- **CapacityManagerDataExportId** (Any  # complex shape): The unique identifier for the created data export configuration. Use this ID to reference the export in other API calls.

## Implementation

```speclang
def create_capacity_manager_data_export(store, request: dict) -> dict:
    """Creates a new data export configuration for EC2 Capacity Manager. This allows you to automatically export capacity usage data to an S3 bucket on a scheduled basis. The exported data includes metrics f"""
    output_format = request.get("OutputFormat", "").strip() if isinstance(request.get("OutputFormat"), str) else request.get("OutputFormat")
    if not output_format:
        raise ValidationException("OutputFormat is required")
    s3_bucket_name = request.get("S3BucketName", "").strip() if isinstance(request.get("S3BucketName"), str) else request.get("S3BucketName")
    if not s3_bucket_name:
        raise ValidationException("S3BucketName is required")
    schedule = request.get("Schedule", "").strip() if isinstance(request.get("Schedule"), str) else request.get("Schedule")
    if not schedule:
        raise ValidationException("Schedule is required")

    if store.capacity_manager_data_exports(s3_bucket_name):
        raise ResourceInUseException(f"Resource s3_bucket_name already exists")

    record = {
        "S3BucketName": s3_bucket_name,
        "S3BucketPrefix": s3_bucket_prefix,
        "Schedule": schedule,
        "OutputFormat": output_format,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
    }

    store.capacity_manager_data_exports(s3_bucket_name, record)

    return {
        "CapacityManagerDataExportId": record.get("CapacityManagerDataExportId", {}),
    }
```
