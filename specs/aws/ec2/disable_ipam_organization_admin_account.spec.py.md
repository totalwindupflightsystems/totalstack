---
id: "@specs/aws/ec2/disable_ipam_organization_admin_account"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableIpamOrganizationAdminAccount"
---

# DisableIpamOrganizationAdminAccount

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_ipam_organization_admin_account
> **spec:implements:** @kind:operation DisableIpamOrganizationAdminAccount
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableIpamOrganizationAdminAccount.spec.md

Disable the IPAM account. For more information, see Enable integration with Organizations in the Amazon VPC IPAM User Guide .

## Input Shape: DisableIpamOrganizationAdminAccountRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegatedAdminAccountId | str | ✓ | The Organizations member account ID that you want to disable as IPAM account. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |

## Output Shape: DisableIpamOrganizationAdminAccountResult

- **Success** (bool): The result of disabling the IPAM account.

## Implementation

```speclang
def disable_ipam_organization_admin_account(store, request: dict) -> dict:
    """Disable the IPAM account. For more information, see Enable integration with Organizations in the Amazon VPC IPAM User Guide ."""
    delegated_admin_account_id = request.get("DelegatedAdminAccountId", "").strip() if isinstance(request.get("DelegatedAdminAccountId"), str) else request.get("DelegatedAdminAccountId")
    if not delegated_admin_account_id:
        raise ValidationException("DelegatedAdminAccountId is required")

    resource = store.disable_ipam_organization_admin_accounts(delegated_admin_account_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource delegated_admin_account_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.disable_ipam_organization_admin_accounts(delegated_admin_account_id, resource)
    return resource
```
