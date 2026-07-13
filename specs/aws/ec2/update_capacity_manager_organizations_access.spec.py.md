---
id: "@specs/aws/ec2/update_capacity_manager_organizations_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UpdateCapacityManagerOrganizationsAccess"
---

# UpdateCapacityManagerOrganizationsAccess

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/update_capacity_manager_organizations_access
> **spec:implements:** @kind:operation UpdateCapacityManagerOrganizationsAccess
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UpdateCapacityManagerOrganizationsAccess.spec.md

Updates the Organizations access setting for EC2 Capacity Manager. This controls whether Capacity Manager can aggregate data from all accounts in your Amazon Web Services Organization or only from the current account.

## Input Shape: UpdateCapacityManagerOrganizationsAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| OrganizationsAccess | bool | ✓ | Specifies whether to enable or disable cross-account access for Amazon Web Services Organizations. When enabled, Capacit |

## Output Shape: UpdateCapacityManagerOrganizationsAccessResult

- **CapacityManagerStatus** (Any  # complex shape): The current status of Capacity Manager after the update operation.
- **OrganizationsAccess** (bool): The updated Organizations access setting indicating whether cross-account data aggregation is enabled.

## Implementation

```speclang
def update_capacity_manager_organizations_access(store, request: dict) -> dict:
    """Updates the Organizations access setting for EC2 Capacity Manager. This controls whether Capacity Manager can aggregate data from all accounts in your Amazon Web Services Organization or only from the"""
    organizations_access = request.get("OrganizationsAccess", "").strip() if isinstance(request.get("OrganizationsAccess"), str) else request.get("OrganizationsAccess")
    if not organizations_access:
        raise ValidationException("OrganizationsAccess is required")

    resource = store.capacity_manager_organizations_accesss(organizations_access)
    if not resource:
        raise ResourceNotFoundException(f"Resource organizations_access not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ClientToken" in request:
        resource["ClientToken"] = client_token

    store.capacity_manager_organizations_accesss(organizations_access, resource)
    return resource
```
