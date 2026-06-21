---
id: "@specs/aws/lightsail/attach_certificate_to_distribution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_AttachCertificateToDistribution"
---

# AttachCertificateToDistribution

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/attach_certificate_to_distribution
> **spec:implements:** @kind:operation AttachCertificateToDistribution
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_AttachCertificateToDistribution.spec.md

Attaches an SSL/TLS certificate to your Amazon Lightsail content delivery network (CDN) distribution. After the certificate is attached, your distribution accepts HTTPS traffic for all of the domains that are associated with the certificate. Use the CreateCertificate action to create a certificate that you can attach to your distribution. Only certificates created in the us-east-1 Amazon Web Services Region can be attached to Lightsail distributions. Lightsail distributions are global resources that can reference an origin in any Amazon Web Services Region, and distribute its content globally. However, all distributions are located in the us-east-1 Region.

## Input Shape: AttachCertificateToDistributionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateName | Any  # complex shape | ✓ | The name of the certificate to attach to a distribution. Only certificates with a status of ISSUED can be attached to a  |
| distributionName | Any  # complex shape | ✓ | The name of the distribution that the certificate will be attached to. Use the GetDistributions action to get a list of  |

## Output Shape: AttachCertificateToDistributionResult

- **operation** (Any  # complex shape): An object that describes the result of the action, such as the status of the request, the timestamp of the request, and 

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def attach_certificate_to_distribution(store, request: dict) -> dict:
    """Attaches an SSL/TLS certificate to your Amazon Lightsail content delivery network (CDN) distribution. After the certificate is attached, your distribution accepts HTTPS traffic for all of the domains """
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    distribution_name = request.get("distributionName", "").strip() if isinstance(request.get("distributionName"), str) else request.get("distributionName")
    if not distribution_name:
        raise ValidationException("distributionName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachCertificateToDistribution", request)
```
