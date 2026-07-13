---
id: "@specs/aws/ec2/modify_vpc_endpoint_service_permissions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcEndpointServicePermissions"
---

# ModifyVpcEndpointServicePermissions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_endpoint_service_permissions
> **spec:implements:** @kind:operation ModifyVpcEndpointServicePermissions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcEndpointServicePermissions.spec.md

Modifies the permissions for your VPC endpoint service. You can add or remove permissions for service consumers (Amazon Web Services accounts, users, and IAM roles) to connect to your endpoint service. Principal ARNs with path components aren't supported. If you grant permissions to all principals, the service is public. Any users who know the name of a public service can send a request to attach an endpoint. If the service does not require manual approval, attachments are automatically approved.

## Input Shape: ModifyVpcEndpointServicePermissionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddAllowedPrincipals | list[str] |  | The Amazon Resource Names (ARN) of the principals. Permissions are granted to the principals in this list. To grant perm |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RemoveAllowedPrincipals | list[str] |  | The Amazon Resource Names (ARN) of the principals. Permissions are revoked for principals in this list. |
| ServiceId | Any  # complex shape | ✓ | The ID of the service. |

## Output Shape: ModifyVpcEndpointServicePermissionsResult

- **AddedPrincipals** (Any  # complex shape): Information about the added principals.
- **ReturnValue** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_vpc_endpoint_service_permissions(store, request: dict) -> dict:
    """Modifies the permissions for your VPC endpoint service. You can add or remove permissions for service consumers (Amazon Web Services accounts, users, and IAM roles) to connect to your endpoint service"""
    service_id = request.get("ServiceId", "").strip() if isinstance(request.get("ServiceId"), str) else request.get("ServiceId")
    if not service_id:
        raise ValidationException("ServiceId is required")

    resource = store.vpc_endpoint_service_permissionss(service_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "AddAllowedPrincipals" in request:
        resource["AddAllowedPrincipals"] = add_allowed_principals
    if "RemoveAllowedPrincipals" in request:
        resource["RemoveAllowedPrincipals"] = remove_allowed_principals

    store.vpc_endpoint_service_permissionss(service_id, resource)
    return resource
```
