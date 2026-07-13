---
id: "@specs/aws/ec2/create_ipam_scope"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateIpamScope"
---

# CreateIpamScope

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_ipam_scope
> **spec:implements:** @kind:operation CreateIpamScope
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateIpamScope.spec.md

Create an IPAM scope. In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict. For more information, see Add a scope in the Amazon VPC IPAM User Guide .

## Input Shape: CreateIpamScopeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| Description | str |  | A description for the scope you're creating. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| ExternalAuthorityConfiguration | Any  # complex shape |  | The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external |
| IpamId | Any  # complex shape | ✓ | The ID of the IPAM for which you're creating this scope. |
| TagSpecifications | list[Any  # complex shape] |  | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the |

## Output Shape: CreateIpamScopeResult

- **IpamScope** (Any  # complex shape): Information about the created scope.

## Implementation

```speclang
def create_ipam_scope(store, request: dict) -> dict:
    """Create an IPAM scope. In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is in"""
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")

    if store.ipam_scopes(ipam_id):
        raise ResourceInUseException(f"Resource ipam_id already exists")

    record = {
        "DryRun": dry_run,
        "IpamId": ipam_id,
        "Description": description,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "ExternalAuthorityConfiguration": external_authority_configuration,
    }

    store.ipam_scopes(ipam_id, record)

    return {
        "IpamScope": record.get("IpamScope", {}),
    }
```
