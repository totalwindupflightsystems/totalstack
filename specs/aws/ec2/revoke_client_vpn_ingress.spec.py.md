---
id: "@specs/aws/ec2/revoke_client_vpn_ingress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RevokeClientVpnIngress"
---

# RevokeClientVpnIngress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/revoke_client_vpn_ingress
> **spec:implements:** @kind:operation RevokeClientVpnIngress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RevokeClientVpnIngress.spec.md

Removes an ingress authorization rule from a Client VPN endpoint.

## Input Shape: RevokeClientVpnIngressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccessGroupId | str |  | The ID of the Active Directory group for which to revoke access. |
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint with which the authorization rule is associated. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RevokeAllGroups | bool |  | Indicates whether access should be revoked for all groups for a single TargetNetworkCidr that earlier authorized ingress |
| TargetNetworkCidr | str | ✓ | The IPv4 address range, in CIDR notation, of the network for which access is being removed. |

## Output Shape: RevokeClientVpnIngressResult

- **Status** (Any  # complex shape): The current state of the authorization rule.

## Implementation

```speclang
def revoke_client_vpn_ingress(store, request: dict) -> dict:
    """Removes an ingress authorization rule from a Client VPN endpoint."""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")
    target_network_cidr = request.get("TargetNetworkCidr", "").strip() if isinstance(request.get("TargetNetworkCidr"), str) else request.get("TargetNetworkCidr")
    if not target_network_cidr:
        raise ValidationException("TargetNetworkCidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RevokeClientVpnIngress", request)
```
