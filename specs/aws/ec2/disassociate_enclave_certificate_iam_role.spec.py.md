---
id: "@specs/aws/ec2/disassociate_enclave_certificate_iam_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateEnclaveCertificateIamRole"
---

# DisassociateEnclaveCertificateIamRole

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_enclave_certificate_iam_role
> **spec:implements:** @kind:operation DisassociateEnclaveCertificateIamRole
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateEnclaveCertificateIamRole.spec.md

Disassociates an IAM role from an Certificate Manager (ACM) certificate. Disassociating an IAM role from an ACM certificate removes the Amazon S3 object that contains the certificate, certificate chain, and encrypted private key from the Amazon S3 bucket. It also revokes the IAM role's permission to use the KMS key used to encrypt the private key. This effectively revokes the role's permission to use the certificate.

## Input Shape: DisassociateEnclaveCertificateIamRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CertificateArn | Any  # complex shape | ✓ | The ARN of the ACM certificate from which to disassociate the IAM role. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RoleArn | Any  # complex shape | ✓ | The ARN of the IAM role to disassociate. |

## Output Shape: DisassociateEnclaveCertificateIamRoleResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disassociate_enclave_certificate_iam_role(store, request: dict) -> dict:
    """Disassociates an IAM role from an Certificate Manager (ACM) certificate. Disassociating an IAM role from an ACM certificate removes the Amazon S3 object that contains the certificate, certificate chai"""
    certificate_arn = request.get("CertificateArn", "").strip() if isinstance(request.get("CertificateArn"), str) else request.get("CertificateArn")
    if not certificate_arn:
        raise ValidationException("CertificateArn is required")
    role_arn = request.get("RoleArn", "").strip() if isinstance(request.get("RoleArn"), str) else request.get("RoleArn")
    if not role_arn:
        raise ValidationException("RoleArn is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateEnclaveCertificateIamRole", request)
```
