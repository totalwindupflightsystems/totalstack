---
id: "@specs/aws/ec2/enable_ipam_organization_admin_account"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableIpamOrganizationAdminAccount"
---

# EnableIpamOrganizationAdminAccount

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_ipam_organization_admin_account
> **spec:implements:** @kind:operation EnableIpamOrganizationAdminAccount
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableIpamOrganizationAdminAccount.spec.md

Enable an Organizations member account as the IPAM admin account. You cannot select the Organizations management account as the IPAM admin account. For more information, see Enable integration with Organizations in the Amazon VPC IPAM User Guide .

## Input Shape: EnableIpamOrganizationAdminAccountRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DelegatedAdminAccountId | str | ✓ | The Organizations member account ID that you want to enable as the IPAM account. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |

## Output Shape: EnableIpamOrganizationAdminAccountResult

- **Success** (bool): The result of enabling the IPAM account.

## Implementation

```speclang
def enable_ipam_organization_admin_account(store, request: dict) -> dict:
    """Enable an Organizations member account as the IPAM admin account. You cannot select the Organizations management account as the IPAM admin account. For more information, see Enable integration with Or"""
    delegated_admin_account_id = request.get("DelegatedAdminAccountId", "").strip() if isinstance(request.get("DelegatedAdminAccountId"), str) else request.get("DelegatedAdminAccountId")
    if not delegated_admin_account_id:
        raise ValidationException("DelegatedAdminAccountId is required")

    resource = store.enable_ipam_organization_admin_accounts(delegated_admin_account_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource delegated_admin_account_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_ipam_organization_admin_accounts(delegated_admin_account_id, resource)
    return resource
```
