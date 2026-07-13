---
id: "@specs/aws/ec2/get_associated_enclave_certificate_iam_roles"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetAssociatedEnclaveCertificateIamRoles"
---

# GetAssociatedEnclaveCertificateIamRoles

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_associated_enclave_certificate_iam_roles
> **spec:implements:** @kind:operation GetAssociatedEnclaveCertificateIamRoles
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetAssociatedEnclaveCertificateIamRoles.spec.md

Returns the IAM roles that are associated with the specified ACM (ACM) certificate. It also returns the name of the Amazon S3 bucket and the Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored, and the ARN of the KMS key that's used to encrypt the private key.

## Input Shape: GetAssociatedEnclaveCertificateIamRolesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateArn | Any  # complex shape | ✓ | The ARN of the ACM certificate for which to view the associated IAM roles, encryption keys, and Amazon S3 object informa |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: GetAssociatedEnclaveCertificateIamRolesResult

- **AssociatedRoles** (list[Any  # complex shape]): Information about the associated IAM roles.

## Implementation

```speclang
def get_associated_enclave_certificate_iam_roles(store, request: dict) -> dict:
    """Returns the IAM roles that are associated with the specified ACM (ACM) certificate. It also returns the name of the Amazon S3 bucket and the Amazon S3 object key where the certificate, certificate cha"""
    certificate_arn = request.get("CertificateArn", "").strip() if isinstance(request.get("CertificateArn"), str) else request.get("CertificateArn")
    if not certificate_arn:
        raise ValidationException("CertificateArn is required")

    resource = store.associated_enclave_certificate_iam_roless(certificate_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource certificate_arn not found")
    return {"CertificateArn": certificate_arn, **resource}
```
