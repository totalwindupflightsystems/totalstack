---
id: "@specs/aws/lightsail/create_certificate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateCertificate"
---

# CreateCertificate

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_certificate
> **spec:implements:** @kind:operation CreateCertificate
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateCertificate.spec.md

Creates an SSL/TLS certificate for an Amazon Lightsail content delivery network (CDN) distribution and a container service. After the certificate is valid, use the AttachCertificateToDistribution action to use the certificate and its domains with your distribution. Or use the UpdateContainerService action to use the certificate and its domains with your container service. Only certificates created in the us-east-1 Amazon Web Services Region can be attached to Lightsail distributions. Lightsail distributions are global resources that can reference an origin in any Amazon Web Services Region, and distribute its content globally. However, all distributions are located in the us-east-1 Region.

## Input Shape: CreateCertificateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| certificateName | Any  # complex shape | ✓ | The name for the certificate. |
| domainName | str | ✓ | The domain name ( example.com ) for the certificate. |
| subjectAlternativeNames | list[str] |  | An array of strings that specify the alternate domains ( example2.com ) and subdomains ( blog.example.com ) for the cert |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the certificate during create. Use the TagResource action to tag a resource a |

## Output Shape: CreateCertificateResult

- **certificate** (Any  # complex shape): An object that describes the certificate created.
- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def create_certificate(store, request: dict) -> dict:
    """Creates an SSL/TLS certificate for an Amazon Lightsail content delivery network (CDN) distribution and a container service. After the certificate is valid, use the AttachCertificateToDistribution acti"""
    certificate_name = request.get("certificateName", "").strip() if isinstance(request.get("certificateName"), str) else request.get("certificateName")
    if not certificate_name:
        raise ValidationException("certificateName is required")
    domain_name = request.get("domainName", "").strip() if isinstance(request.get("domainName"), str) else request.get("domainName")
    if not domain_name:
        raise ValidationException("domainName is required")

    if store.certificates(domain_name):
        raise ResourceInUseException(f"Resource domain_name already exists")

    record = {
        "certificateName": certificate_name,
        "domainName": domain_name,
        "subjectAlternativeNames": subject_alternative_names,
        "tags": tags,
    }

    store.certificates(domain_name, record)

    return {
        "certificate": record.get("certificate", {}),
        "operations": record.get("operations", {}),
    }
```
