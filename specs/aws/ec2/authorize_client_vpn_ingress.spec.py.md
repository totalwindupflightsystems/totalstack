---
id: "@specs/aws/ec2/authorize_client_vpn_ingress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AuthorizeClientVpnIngress"
---

# AuthorizeClientVpnIngress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/authorize_client_vpn_ingress
> **spec:implements:** @kind:operation AuthorizeClientVpnIngress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AuthorizeClientVpnIngress.spec.md

Adds an ingress authorization rule to a Client VPN endpoint. Ingress authorization rules act as firewall rules that grant access to networks. You must configure ingress authorization rules to enable clients to access resources in Amazon Web Services or on-premises networks.

## Input Shape: AuthorizeClientVpnIngressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccessGroupId | str |  | The ID of the group to grant access to, for example, the Active Directory group or identity provider (IdP) group. Requir |
| AuthorizeAllGroups | bool |  | Indicates whether to grant access to all clients. Specify true to grant all clients who successfully establish a VPN con |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint. |
| Description | str |  | A brief description of the authorization rule. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TargetNetworkCidr | str | ✓ | The IPv4 address range, in CIDR notation, of the network for which access is being authorized. |

## Output Shape: AuthorizeClientVpnIngressResult

- **Status** (Any  # complex shape): The current state of the authorization rule.

## Implementation

```speclang
def authorize_client_vpn_ingress(store, request: dict) -> dict:
    """Adds an ingress authorization rule to a Client VPN endpoint. Ingress authorization rules act as firewall rules that grant access to networks. You must configure ingress authorization rules to enable c"""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")
    target_network_cidr = request.get("TargetNetworkCidr", "").strip() if isinstance(request.get("TargetNetworkCidr"), str) else request.get("TargetNetworkCidr")
    if not target_network_cidr:
        raise ValidationException("TargetNetworkCidr is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AuthorizeClientVpnIngress", request)
```
