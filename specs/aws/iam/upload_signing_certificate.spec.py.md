---
id: "@specs/aws/iam/upload_signing_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UploadSigningCertificate"
---

# UploadSigningCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/upload_signing_certificate
> **spec:implements:** @kind:operation UploadSigningCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UploadSigningCertificate.spec.md

Uploads an X.509 signing certificate and associates it with the specified IAM user. Some Amazon Web Services services require you to use certificates to validate requests that are signed with a corresponding private key. When you upload the certificate, its default status is Active . For information about when you would use an X.509 signing certificate, see Managing server certificates in IAM in the IAM User Guide . If the UserName is not specified, the IAM user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users. Because the body of an X.509 certificate can be large, you should use POST rather than GET when calling UploadSigningCertificate . For information about setting up signatures and authorization through the API, see Signing Amazon Web Services API requests in the Amazon Web Services General Reference . For general information about using the Query API with IAM, see Making query requests in the IAM User Guide .

## Input Shape: UploadSigningCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateBody | Any  # complex shape | ✓ | The contents of the signing certificate. The regex pattern used to validate this parameter is a string of characters con |
| UserName | Any  # complex shape |  | The name of the user the signing certificate is for. This parameter allows (through its regex pattern ) a string of char |

## Output Shape: UploadSigningCertificateResponse

- **Certificate** (Any  # complex shape): Information about the certificate.

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **MalformedCertificateException**: The request was rejected because the certificate was malformed or expired. The error message describes the specific error.
- **InvalidCertificateException**: The request was rejected because the certificate is invalid.
- **DuplicateCertificateException**: The request was rejected because the same certificate is associated with an IAM user in the account.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def upload_signing_certificate(store, request: dict) -> dict:
    """Uploads an X.509 signing certificate and associates it with the specified IAM user. Some Amazon Web Services services require you to use certificates to validate requests that are signed with a corres"""
    certificate_body = request.get("CertificateBody", "").strip() if isinstance(request.get("CertificateBody"), str) else request.get("CertificateBody")
    if not certificate_body:
        raise ValidationException("CertificateBody is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("UploadSigningCertificate", request)
```
