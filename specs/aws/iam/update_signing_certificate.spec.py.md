---
id: "@specs/aws/iam/update_signing_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateSigningCertificate"
---

# UpdateSigningCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_signing_certificate
> **spec:implements:** @kind:operation UpdateSigningCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateSigningCertificate.spec.md

Changes the status of the specified user signing certificate from active to disabled, or vice versa. This operation can be used to disable an IAM user's signing certificate as part of a certificate rotation work flow. If the UserName field is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.

## Input Shape: UpdateSigningCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateId | Any  # complex shape | ✓ | The ID of the signing certificate you want to update. This parameter allows (through its regex pattern ) a string of cha |
| Status | Any  # complex shape | ✓ | The status you want to assign to the certificate. Active means that the certificate can be used for programmatic calls t |
| UserName | Any  # complex shape |  | The name of the IAM user the signing certificate belongs to. This parameter allows (through its regex pattern ) a string |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def update_signing_certificate(store, request: dict) -> dict:
    """Changes the status of the specified user signing certificate from active to disabled, or vice versa. This operation can be used to disable an IAM user's signing certificate as part of a certificate ro"""
    certificate_id = request.get("CertificateId", "").strip() if isinstance(request.get("CertificateId"), str) else request.get("CertificateId")
    if not certificate_id:
        raise ValidationException("CertificateId is required")
    status = request.get("Status", "").strip() if isinstance(request.get("Status"), str) else request.get("Status")
    if not status:
        raise ValidationException("Status is required")

    resource = store.signing_certificates(certificate_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource certificate_id not found")

    # Update mutable fields
    if "UserName" in request:
        resource["UserName"] = user_name

    store.signing_certificates(certificate_id, resource)
    return resource
```
