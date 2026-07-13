---
id: "@specs/aws/ec2/disable_capacity_manager"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableCapacityManager"
---

# DisableCapacityManager

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_capacity_manager
> **spec:implements:** @kind:operation DisableCapacityManager
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableCapacityManager.spec.md

Disables EC2 Capacity Manager for your account. This stops data ingestion and removes access to capacity analytics and optimization recommendations. Previously collected data is retained but no new data will be processed.

## Input Shape: DisableCapacityManagerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisableCapacityManagerResult

- **CapacityManagerStatus** (Any  # complex shape): The current status of Capacity Manager after the disable operation.
- **OrganizationsAccess** (bool): Indicates whether Organizations access is enabled. This will be false after disabling Capacity Manager.

## Implementation

```speclang
def disable_capacity_manager(store, request: dict) -> dict:
    """Disables EC2 Capacity Manager for your account. This stops data ingestion and removes access to capacity analytics and optimization recommendations. Previously collected data is retained but no new da"""

```
