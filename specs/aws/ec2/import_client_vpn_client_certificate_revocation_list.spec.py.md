---
id: "@specs/aws/ec2/import_client_vpn_client_certificate_revocation_list"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ImportClientVpnClientCertificateRevocationList"
---

# ImportClientVpnClientCertificateRevocationList

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/import_client_vpn_client_certificate_revocation_list
> **spec:implements:** @kind:operation ImportClientVpnClientCertificateRevocationList
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ImportClientVpnClientCertificateRevocationList.spec.md

Uploads a client certificate revocation list to the specified Client VPN endpoint. Uploading a client certificate revocation list overwrites the existing client certificate revocation list. Uploading a client certificate revocation list resets existing client connections.

## Input Shape: ImportClientVpnClientCertificateRevocationListRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateRevocationList | str | ✓ | The client certificate revocation list file. For more information, see Generate a Client Certificate Revocation List in  |
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint to which the client certificate revocation list applies. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: ImportClientVpnClientCertificateRevocationListResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def import_client_vpn_client_certificate_revocation_list(store, request: dict) -> dict:
    """Uploads a client certificate revocation list to the specified Client VPN endpoint. Uploading a client certificate revocation list overwrites the existing client certificate revocation list. Uploading """
    certificate_revocation_list = request.get("CertificateRevocationList", "").strip() if isinstance(request.get("CertificateRevocationList"), str) else request.get("CertificateRevocationList")
    if not certificate_revocation_list:
        raise ValidationException("CertificateRevocationList is required")
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")

    items = store.list_import_client_vpn_client_certificate_revocation_lists()
    return {"Return": list(items.values())}
```
