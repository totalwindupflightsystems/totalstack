---
id: "@specs/aws/ec2/delete_vpn_concentrator"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpnConcentrator"
---

# DeleteVpnConcentrator

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpn_concentrator
> **spec:implements:** @kind:operation DeleteVpnConcentrator
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpnConcentrator.spec.md

Deletes the specified VPN concentrator.

## Input Shape: DeleteVpnConcentratorRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpnConcentratorId | Any  # complex shape | ✓ | The ID of the VPN concentrator to delete. |

## Output Shape: DeleteVpnConcentratorResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def delete_vpn_concentrator(store, request: dict) -> dict:
    """Deletes the specified VPN concentrator."""
    vpn_concentrator_id = request.get("VpnConcentratorId", "").strip() if isinstance(request.get("VpnConcentratorId"), str) else request.get("VpnConcentratorId")

    if not store.vpn_concentrators(vpn_concentrator_id):
        raise ResourceNotFoundException(f"Resource vpn_concentrator_id not found")
    store.delete_vpn_concentrators(vpn_concentrator_id)
    return {}
```
