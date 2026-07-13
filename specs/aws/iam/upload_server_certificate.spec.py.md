---
id: "@specs/aws/iam/upload_server_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UploadServerCertificate"
---

# UploadServerCertificate

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/upload_server_certificate
> **spec:implements:** @kind:operation UploadServerCertificate
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UploadServerCertificate.spec.md

Uploads a server certificate entity for the Amazon Web Services account. The server certificate entity includes a public key certificate, a private key, and an optional certificate chain, which should all be PEM-encoded. We recommend that you use Certificate Manager to provision, manage, and deploy your server certificates. With ACM you can request a certificate, deploy it to Amazon Web Services resources, and let ACM handle certificate renewals for you. Certificates provided by ACM are free. For more information about using ACM, see the Certificate Manager User Guide . For more information about working with server certificates, see Working with server certificates in the IAM User Guide . This topic includes a list of Amazon Web Services services that can use the server certificates that you manage with IAM. For information about the number of server certificates you can upload, see IAM and STS quotas in the IAM User Guide . Because the body of the public key certificate, private key, and the certificate chain can be large, you should use POST rather than GET when calling UploadServerCertificate . For information about setting up signatures and authorization through the API, see Signing Amazon Web Services API requests in the Amazon Web Services General Reference . For general information about using the Query API with IAM, see Calling the API by making HTTP query requests in the IAM User Guide .

## Input Shape: UploadServerCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateBody | Any  # complex shape | ✓ | The contents of the public key certificate in PEM-encoded format. The regex pattern used to validate this parameter is a |
| CertificateChain | Any  # complex shape |  | The contents of the certificate chain. This is typically a concatenation of the PEM-encoded public key certificates of t |
| Path | Any  # complex shape |  | The path for the server certificate. For more information about paths, see IAM identifiers in the IAM User Guide . This  |
| PrivateKey | Any  # complex shape | ✓ | The contents of the private key in PEM-encoded format. The regex pattern used to validate this parameter is a string of  |
| ServerCertificateName | Any  # complex shape | ✓ | The name for the server certificate. Do not include the path in this value. The name of the certificate cannot contain a |
| Tags | Any  # complex shape |  | A list of tags that you want to attach to the new IAM server certificate resource. Each tag consists of a key name and a |

## Output Shape: UploadServerCertificateResponse

- **ServerCertificateMetadata** (Any  # complex shape): The meta information of the uploaded server certificate without its certificate body, certificate chain, and private key
- **Tags** (Any  # complex shape): A list of tags that are attached to the new IAM server certificate. The returned list of tags is sorted by tag key. For 

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **MalformedCertificateException**: The request was rejected because the certificate was malformed or expired. The error message describes the specific error.
- **KeyPairMismatchException**: The request was rejected because the public key certificate and the private key do not match.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def upload_server_certificate(store, request: dict) -> dict:
    """Uploads a server certificate entity for the Amazon Web Services account. The server certificate entity includes a public key certificate, a private key, and an optional certificate chain, which should"""
    certificate_body = request.get("CertificateBody", "").strip() if isinstance(request.get("CertificateBody"), str) else request.get("CertificateBody")
    if not certificate_body:
        raise ValidationException("CertificateBody is required")
    private_key = request.get("PrivateKey", "").strip() if isinstance(request.get("PrivateKey"), str) else request.get("PrivateKey")
    if not private_key:
        raise ValidationException("PrivateKey is required")
    server_certificate_name = request.get("ServerCertificateName", "").strip() if isinstance(request.get("ServerCertificateName"), str) else request.get("ServerCertificateName")
    if not server_certificate_name:
        raise ValidationException("ServerCertificateName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("UploadServerCertificate", request)
```
