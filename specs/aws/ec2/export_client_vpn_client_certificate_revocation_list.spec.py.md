---
id: "@specs/aws/ec2/export_client_vpn_client_certificate_revocation_list"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ExportClientVpnClientCertificateRevocationList"
---

# ExportClientVpnClientCertificateRevocationList

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/export_client_vpn_client_certificate_revocation_list
> **spec:implements:** @kind:operation ExportClientVpnClientCertificateRevocationList
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ExportClientVpnClientCertificateRevocationList.spec.md

Downloads the client certificate revocation list for the specified Client VPN endpoint.

## Input Shape: ExportClientVpnClientCertificateRevocationListRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: ExportClientVpnClientCertificateRevocationListResult

- **CertificateRevocationList** (str): Information about the client certificate revocation list.
- **Status** (Any  # complex shape): The current state of the client certificate revocation list.

## Implementation

```speclang
def export_client_vpn_client_certificate_revocation_list(store, request: dict) -> dict:
    """Downloads the client certificate revocation list for the specified Client VPN endpoint."""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")

    items = store.list_export_client_vpn_client_certificate_revocation_lists()
    return {"CertificateRevocationList": list(items.values())}
```
