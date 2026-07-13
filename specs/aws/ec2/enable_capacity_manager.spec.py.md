---
id: "@specs/aws/ec2/enable_capacity_manager"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableCapacityManager"
---

# EnableCapacityManager

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_capacity_manager
> **spec:implements:** @kind:operation EnableCapacityManager
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableCapacityManager.spec.md

Enables EC2 Capacity Manager for your account. This starts data ingestion for your EC2 capacity usage across On-Demand, Spot, and Capacity Reservations. Initial data processing may take several hours to complete.

## Input Shape: EnableCapacityManagerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| OrganizationsAccess | bool |  | Specifies whether to enable cross-account access for Amazon Web Services Organizations. When enabled, Capacity Manager c |

## Output Shape: EnableCapacityManagerResult

- **CapacityManagerStatus** (Any  # complex shape): The current status of Capacity Manager after the enable operation.
- **OrganizationsAccess** (bool): Indicates whether Organizations access is enabled for cross-account data aggregation.

## Implementation

```speclang
def enable_capacity_manager(store, request: dict) -> dict:
    """Enables EC2 Capacity Manager for your account. This starts data ingestion for your EC2 capacity usage across On-Demand, Spot, and Capacity Reservations. Initial data processing may take several hours """

```
