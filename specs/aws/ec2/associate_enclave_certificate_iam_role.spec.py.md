---
id: "@specs/aws/ec2/associate_enclave_certificate_iam_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateEnclaveCertificateIamRole"
---

# AssociateEnclaveCertificateIamRole

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_enclave_certificate_iam_role
> **spec:implements:** @kind:operation AssociateEnclaveCertificateIamRole
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateEnclaveCertificateIamRole.spec.md

Associates an Identity and Access Management (IAM) role with an Certificate Manager (ACM) certificate. This enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave. For more information, see Certificate Manager for Nitro Enclaves in the Amazon Web Services Nitro Enclaves User Guide . When the IAM role is associated with the ACM certificate, the certificate, certificate chain, and encrypted private key are placed in an Amazon S3 location that only the associated IAM role can access. The private key of the certificate is encrypted with an Amazon Web Services managed key that has an attached attestation-based key policy. To enable the IAM role to access the Amazon S3 object, you must grant it permission to call s3:GetObject on the Amazon S3 bucket returned by the command. To enable the IAM role to access the KMS key, you must grant it permission to call kms:Decrypt on the KMS key returned by the command. For more information, see Grant the role permission to access the certificate and encryption key in the Amazon Web Services Nitro Enclaves User Guide .

## Input Shape: AssociateEnclaveCertificateIamRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateArn | Any  # complex shape | ✓ | The ARN of the ACM certificate with which to associate the IAM role. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RoleArn | Any  # complex shape | ✓ | The ARN of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certific |

## Output Shape: AssociateEnclaveCertificateIamRoleResult

- **CertificateS3BucketName** (str): The name of the Amazon S3 bucket to which the certificate was uploaded.
- **CertificateS3ObjectKey** (str): The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored. The obje
- **EncryptionKmsKeyId** (str): The ID of the KMS key used to encrypt the private key of the certificate.

## Implementation

```speclang
def associate_enclave_certificate_iam_role(store, request: dict) -> dict:
    """Associates an Identity and Access Management (IAM) role with an Certificate Manager (ACM) certificate. This enables the certificate to be used by the ACM for Nitro Enclaves application inside an encla"""
    certificate_arn = request.get("CertificateArn", "").strip() if isinstance(request.get("CertificateArn"), str) else request.get("CertificateArn")
    if not certificate_arn:
        raise ValidationException("CertificateArn is required")
    role_arn = request.get("RoleArn", "").strip() if isinstance(request.get("RoleArn"), str) else request.get("RoleArn")
    if not role_arn:
        raise ValidationException("RoleArn is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateEnclaveCertificateIamRole", request)
```
