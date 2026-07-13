---
id: "@specs/aws/iam/update_server_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateServerCertificate"
---

# UpdateServerCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_server_certificate
> **spec:implements:** @kind:operation UpdateServerCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateServerCertificate.spec.md

Updates the name and/or the path of the specified server certificate stored in IAM. For more information about working with server certificates, see Working with server certificates in the IAM User Guide . This topic also includes a list of Amazon Web Services services that can use the server certificates that you manage with IAM. You should understand the implications of changing a server certificate's path or name. For more information, see Renaming a server certificate in the IAM User Guide . The person making the request (the principal), must have permission to change the server certificate with the old name and the new name. For example, to change the certificate named ProductionCert to ProdCert , the principal must have a policy that allows them to update both certificates. If the principal has permission to update the ProductionCert group, but not the ProdCert certificate, then the update fails. For more information about permissions, see Access management in the IAM User Guide .

## Input Shape: UpdateServerCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NewPath | Any  # complex shape |  | The new path for the server certificate. Include this only if you are updating the server certificate's path. This param |
| NewServerCertificateName | Any  # complex shape |  | The new name for the server certificate. Include this only if you are updating the server certificate's name. The name o |
| ServerCertificateName | Any  # complex shape | ✓ | The name of the server certificate that you want to update. This parameter allows (through its regex pattern ) a string  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_server_certificate(store, request: dict) -> dict:
    """Updates the name and/or the path of the specified server certificate stored in IAM. For more information about working with server certificates, see Working with server certificates in the IAM User Gu"""
    server_certificate_name = request.get("ServerCertificateName", "").strip() if isinstance(request.get("ServerCertificateName"), str) else request.get("ServerCertificateName")
    if not server_certificate_name:
        raise ValidationException("ServerCertificateName is required")

    resource = store.server_certificates(server_certificate_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource server_certificate_name not found")

    # Update mutable fields
    if "NewPath" in request:
        resource["NewPath"] = new_path
    if "NewServerCertificateName" in request:
        resource["NewServerCertificateName"] = new_server_certificate_name

    store.server_certificates(server_certificate_name, resource)
    return resource
```
