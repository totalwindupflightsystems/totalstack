---
id: "@specs/aws/ec2/get_capacity_manager_attributes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetCapacityManagerAttributes"
---

# GetCapacityManagerAttributes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_capacity_manager_attributes
> **spec:implements:** @kind:operation GetCapacityManagerAttributes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetCapacityManagerAttributes.spec.md

Retrieves the current configuration and status of EC2 Capacity Manager for your account, including enablement status, Organizations access settings, and data ingestion status.

## Input Shape: GetCapacityManagerAttributesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetCapacityManagerAttributesResult

- **CapacityManagerStatus** (Any  # complex shape): The current status of Capacity Manager.
- **DataExportCount** (int): The number of active data export configurations for this account. This count includes all data exports regardless of the
- **EarliestDatapointTimestamp** (Any  # complex shape): The timestamp of the earliest data point available in Capacity Manager, in milliseconds since epoch. This indicates how 
- **IngestionStatus** (Any  # complex shape): The current data ingestion status. Initial ingestion may take several hours after enabling Capacity Manager.
- **IngestionStatusMessage** (str): A descriptive message providing additional details about the current ingestion status. This may include error informatio
- **LatestDatapointTimestamp** (Any  # complex shape): The timestamp of the most recent data point ingested by Capacity Manager, in milliseconds since epoch. This indicates ho
- **OrganizationsAccess** (bool): Indicates whether Organizations access is enabled for cross-account data aggregation.

## Implementation

```speclang
def get_capacity_manager_attributes(store, request: dict) -> dict:
    """Retrieves the current configuration and status of EC2 Capacity Manager for your account, including enablement status, Organizations access settings, and data ingestion status."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
