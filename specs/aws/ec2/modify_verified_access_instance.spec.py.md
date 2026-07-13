---
id: "@specs/aws/ec2/modify_verified_access_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVerifiedAccessInstance"
---

# ModifyVerifiedAccessInstance

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_verified_access_instance
> **spec:implements:** @kind:operation ModifyVerifiedAccessInstance
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVerifiedAccessInstance.spec.md

Modifies the configuration of the specified Amazon Web Services Verified Access instance.

## Input Shape: ModifyVerifiedAccessInstanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrEndpointsCustomSubDomain | str |  | The custom subdomain. |
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access instance. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessInstanceId | Any  # complex shape | ✓ | The ID of the Verified Access instance. |

## Output Shape: ModifyVerifiedAccessInstanceResult

- **VerifiedAccessInstance** (Any  # complex shape): Details about the Verified Access instance.

## Implementation

```speclang
def modify_verified_access_instance(store, request: dict) -> dict:
    """Modifies the configuration of the specified Amazon Web Services Verified Access instance."""
    verified_access_instance_id = request.get("VerifiedAccessInstanceId", "").strip() if isinstance(request.get("VerifiedAccessInstanceId"), str) else request.get("VerifiedAccessInstanceId")
    if not verified_access_instance_id:
        raise ValidationException("VerifiedAccessInstanceId is required")

    resource = store.verified_access_instances(verified_access_instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_instance_id not found")

    # Update mutable fields
    if "Description" in request:
        resource["Description"] = description
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ClientToken" in request:
        resource["ClientToken"] = client_token
    if "CidrEndpointsCustomSubDomain" in request:
        resource["CidrEndpointsCustomSubDomain"] = cidr_endpoints_custom_sub_domain

    store.verified_access_instances(verified_access_instance_id, resource)
    return resource
```
