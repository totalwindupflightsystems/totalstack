---
id: "@specs/aws/ec2/modify_ipam_scope"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpamScope"
---

# ModifyIpamScope

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam_scope
> **spec:implements:** @kind:operation ModifyIpamScope
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpamScope.spec.md

Modify an IPAM scope.

## Input Shape: ModifyIpamScopeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | The description of the scope you want to modify. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| ExternalAuthorityConfiguration | Any  # complex shape |  | The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external |
| IpamScopeId | Any  # complex shape | ✓ | The ID of the scope you want to modify. |
| RemoveExternalAuthorityConfiguration | bool |  | Remove the external authority configuration. true to remove. |

## Output Shape: ModifyIpamScopeResult

- **IpamScope** (Any  # complex shape): The results of the modification.

## Implementation

```speclang
def modify_ipam_scope(store, request: dict) -> dict:
    """Modify an IPAM scope."""
    ipam_scope_id = request.get("IpamScopeId", "").strip() if isinstance(request.get("IpamScopeId"), str) else request.get("IpamScopeId")
    if not ipam_scope_id:
        raise ValidationException("IpamScopeId is required")

    resource = store.ipam_scopes(ipam_scope_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_scope_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Description" in request:
        resource["Description"] = description
    if "ExternalAuthorityConfiguration" in request:
        resource["ExternalAuthorityConfiguration"] = external_authority_configuration
    if "RemoveExternalAuthorityConfiguration" in request:
        resource["RemoveExternalAuthorityConfiguration"] = remove_external_authority_configuration

    store.ipam_scopes(ipam_scope_id, resource)
    return resource
```
