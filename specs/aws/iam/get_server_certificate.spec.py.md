---
id: "@specs/aws/iam/get_server_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetServerCertificate"
---

# GetServerCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_server_certificate
> **spec:implements:** @kind:operation GetServerCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetServerCertificate.spec.md

Retrieves information about the specified server certificate stored in IAM. For more information about working with server certificates, see Working with server certificates in the IAM User Guide . This topic includes a list of Amazon Web Services services that can use the server certificates that you manage with IAM.

## Input Shape: GetServerCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ServerCertificateName | Any  # complex shape | ✓ | The name of the server certificate you want to retrieve information about. This parameter allows (through its regex patt |

## Output Shape: GetServerCertificateResponse

- **ServerCertificate** (Any  # complex shape): A structure containing details about the server certificate.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_server_certificate(store, request: dict) -> dict:
    """Retrieves information about the specified server certificate stored in IAM. For more information about working with server certificates, see Working with server certificates in the IAM User Guide . Th"""
    server_certificate_name = request.get("ServerCertificateName", "").strip() if isinstance(request.get("ServerCertificateName"), str) else request.get("ServerCertificateName")
    if not server_certificate_name:
        raise ValidationException("ServerCertificateName is required")

    resource = store.server_certificates(server_certificate_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource server_certificate_name not found")
    return {"ServerCertificateName": server_certificate_name, **resource}
```
