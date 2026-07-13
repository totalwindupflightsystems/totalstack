---
id: "@specs/aws/iam/delete_signing_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteSigningCertificate"
---

# DeleteSigningCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_signing_certificate
> **spec:implements:** @kind:operation DeleteSigningCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteSigningCertificate.spec.md

Deletes a signing certificate associated with the specified IAM user. If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated IAM users.

## Input Shape: DeleteSigningCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateId | Any  # complex shape | ✓ | The ID of the signing certificate to delete. The format of this parameter, as described by its regex pattern, is a strin |
| UserName | Any  # complex shape |  | The name of the user the signing certificate belongs to. This parameter allows (through its regex pattern ) a string of  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_signing_certificate(store, request: dict) -> dict:
    """Deletes a signing certificate associated with the specified IAM user. If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing """
    certificate_id = request.get("CertificateId", "").strip() if isinstance(request.get("CertificateId"), str) else request.get("CertificateId")

    if not store.signing_certificates(certificate_id):
        raise ResourceNotFoundException(f"Resource certificate_id not found")
    store.delete_signing_certificates(certificate_id)
    return {}
```
