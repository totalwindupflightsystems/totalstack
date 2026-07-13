---
id: "@specs/aws/iam/delete_server_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteServerCertificate"
---

# DeleteServerCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_server_certificate
> **spec:implements:** @kind:operation DeleteServerCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteServerCertificate.spec.md

Deletes the specified server certificate. For more information about working with server certificates, see Working with server certificates in the IAM User Guide . This topic also includes a list of Amazon Web Services services that can use the server certificates that you manage with IAM. If you are using a server certificate with Elastic Load Balancing, deleting the certificate could have implications for your application. If Elastic Load Balancing doesn't detect the deletion of bound certificates, it may continue to use the certificates. This could cause Elastic Load Balancing to stop accepting traffic. We recommend that you remove the reference to the certificate from Elastic Load Balancing before using this command to delete the certificate. For more information, see DeleteLoadBalancerListeners in the Elastic Load Balancing API Reference .

## Input Shape: DeleteServerCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ServerCertificateName | Any  # complex shape | ✓ | The name of the server certificate you want to delete. This parameter allows (through its regex pattern ) a string of ch |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_server_certificate(store, request: dict) -> dict:
    """Deletes the specified server certificate. For more information about working with server certificates, see Working with server certificates in the IAM User Guide . This topic also includes a list of A"""
    server_certificate_name = request.get("ServerCertificateName", "").strip() if isinstance(request.get("ServerCertificateName"), str) else request.get("ServerCertificateName")

    if not store.server_certificates(server_certificate_name):
        raise ResourceNotFoundException(f"Resource server_certificate_name not found")
    store.delete_server_certificates(server_certificate_name)
    return {}
```
