---
id: "@specs/aws/lightsail/detach_certificate_from_distribution"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DetachCertificateFromDistribution"
---

# DetachCertificateFromDistribution

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/detach_certificate_from_distribution
> **spec:implements:** @kind:operation DetachCertificateFromDistribution
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DetachCertificateFromDistribution.spec.md

Detaches an SSL/TLS certificate from your Amazon Lightsail content delivery network (CDN) distribution. After the certificate is detached, your distribution stops accepting traffic for all of the domains that are associated with the certificate.

## Input Shape: DetachCertificateFromDistributionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| distributionName | Any  # complex shape | ✓ | The name of the distribution from which to detach the certificate. Use the GetDistributions action to get a list of dist |

## Output Shape: DetachCertificateFromDistributionResult

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
def detach_certificate_from_distribution(store, request: dict) -> dict:
    """Detaches an SSL/TLS certificate from your Amazon Lightsail content delivery network (CDN) distribution. After the certificate is detached, your distribution stops accepting traffic for all of the doma"""
    distribution_name = request.get("distributionName", "").strip() if isinstance(request.get("distributionName"), str) else request.get("distributionName")
    if not distribution_name:
        raise ValidationException("distributionName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachCertificateFromDistribution", request)
```
